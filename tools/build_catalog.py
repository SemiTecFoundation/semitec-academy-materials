#!/usr/bin/env python3
"""Build the public Academy catalog without copying package release files.

Usage:
    python3 tools/build_catalog.py          write catalog/catalog.json
    python3 tools/build_catalog.py --check  verify it matches the package releases

Each package release stays in Packages/<name>/dist/.  The catalog is only an
index: its relative URLs point to that canonical archive and its two display
assets beside the package specification.
"""
import argparse
import hashlib
import json
import os
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGES_DIR = ROOT / 'Packages'
CATALOG_PATH = ROOT / 'catalog' / 'catalog.json'
CATALOG_NAME = 'SemiTec Foundation Academy Catalog'


def read_json_from_pack(archive, name):
    try:
        with zipfile.ZipFile(archive) as package:
            return json.loads(package.read(name))
    except KeyError:
        return None
    except (OSError, zipfile.BadZipFile, json.JSONDecodeError) as exc:
        raise ValueError(f'{archive.relative_to(ROOT)}: cannot read {name}: {exc}') from exc


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def semantic_version(value):
    """Return a SemVer precedence key for choosing the newest catalog entry."""
    core_and_pre, _, _build = str(value).partition('+')
    core, separator, prerelease = core_and_pre.partition('-')
    parts = core.split('.')
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        raise ValueError(f'not a semantic version: {value!r}')
    numbers = tuple(int(part) for part in parts)
    if not separator:
        return numbers, (1, ())
    identifiers = prerelease.split('.')
    if not all(identifier and all(char.isalnum() or char == '-' for char in identifier) for identifier in identifiers):
        raise ValueError(f'not a semantic version: {value!r}')
    # SemVer orders numeric prerelease identifiers before non-numeric ones,
    # compares numeric identifiers as integers, and puts a release after any
    # prerelease of the same core version.
    pre = tuple((0, int(identifier)) if identifier.isdigit() else (1, identifier) for identifier in identifiers)
    return numbers, (0, pre)


def relative(path):
    return path.relative_to(ROOT).as_posix()


def catalog_entry(archive):
    manifest = read_json_from_pack(archive, 'manifest.json')
    if not isinstance(manifest, dict):
        raise ValueError(f'{relative(archive)}: manifest.json is missing or invalid')
    required = ('id', 'version', 'title')
    missing = [field for field in required if not manifest.get(field)]
    if missing:
        raise ValueError(f'{relative(archive)}: manifest is missing {", ".join(missing)}')

    items = manifest.get('items') or []
    if not isinstance(items, list):
        raise ValueError(f'{relative(archive)}: manifest items must be a list')
    counts = {}
    for item in items:
        item_type = item.get('type') if isinstance(item, dict) else None
        if item_type:
            counts[item_type] = counts.get(item_type, 0) + 1

    package_dir = archive.parents[1]
    signature = read_json_from_pack(archive, 'signature.json')
    entry = {
        'id': manifest['id'],
        'version': manifest['version'],
        'title': manifest['title'],
        'description': manifest.get('description', ''),
        'language': manifest.get('language', ''),
        'publisher': manifest.get('publisher', ''),
        'authors': manifest.get('authors', []),
        'minAppVersion': manifest.get('minAppVersion', '1.0.0'),
        'format': manifest.get('format', 1),
        'items': [
            {'type': item.get('type'), 'format': item.get('format', 1)}
            for item in items if isinstance(item, dict) and item.get('type')
        ],
        'counts': counts,
        'itemTitles': [item.get('title', item.get('id', '')) for item in items if isinstance(item, dict)],
        'projectCategories': sorted({
            item.get('category', 'other') for item in items
            if isinstance(item, dict) and item.get('type') == 'project'
        }),
        'hasSchedule': bool((manifest.get('schedule') or {}).get('entries')),
        'created': manifest.get('created'),
        'signed': bool(signature),
        'signedBy': manifest.get('publisher', '') if signature else '',
        'url': Path(os.path.relpath(archive, CATALOG_PATH.parent)).as_posix(),
        'size': archive.stat().st_size,
        'sha256': sha256(archive),
    }
    for manifest_field, catalog_field in (('cover', 'cover'), ('publisherLogo', 'publisherLogo')):
        name = manifest.get(manifest_field)
        if not isinstance(name, str):
            continue
        asset = (package_dir / name).resolve()
        if asset.is_file() and asset.is_relative_to(package_dir.resolve()):
            entry[catalog_field] = Path(os.path.relpath(asset, CATALOG_PATH.parent)).as_posix()
    return entry


def build():
    releases = []
    for archive in sorted(PACKAGES_DIR.glob('*/dist/*.stlp')):
        releases.append(catalog_entry(archive))
    if not releases:
        raise ValueError('No package releases found in Packages/*/dist/*.stlp')

    newest = {}
    for entry in releases:
        try:
            later = entry['id'] not in newest or semantic_version(entry['version']) > semantic_version(newest[entry['id']]['version'])
        except ValueError as exc:
            raise ValueError(f'{relative(PACKAGES_DIR)}: {exc}') from exc
        if later:
            newest[entry['id']] = entry
    return {
        'format': 1,
        'name': CATALOG_NAME,
        'updated': datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        'packages': sorted(newest.values(), key=lambda item: item['title'].lower()),
    }


def stable_json(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail if catalog/catalog.json is out of date')
    args = parser.parse_args()
    try:
        catalog = build()
    except ValueError as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1

    if args.check:
        try:
            current = json.loads(CATALOG_PATH.read_text(encoding='utf-8'))
        except (OSError, json.JSONDecodeError) as exc:
            print(f'error: cannot read {relative(CATALOG_PATH)}: {exc}', file=sys.stderr)
            return 1
        current.pop('updated', None)
        catalog.pop('updated', None)
        if stable_json(current) != stable_json(catalog):
            print('error: catalog/catalog.json is out of date; run python3 tools/build_catalog.py', file=sys.stderr)
            return 1
        print(f'catalog/catalog.json matches {len(catalog["packages"])} package release(s)')
        return 0

    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2) + '\n', encoding='utf-8')
    print(f'wrote {relative(CATALOG_PATH)} for {len(catalog["packages"])} package release(s)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
