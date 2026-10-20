# Packages

One folder per SemiTec Learning Package:

```
Packages/<package-name>/
├── pack-spec.json        what goes in: materials from any topic (paths like ../../IC-Design/Digital-Design/FPGA/labs/fpga-lab01-leds/lab)
├── cover.svg             600 × 340 cover and publisher-logo.svg
├── certificate/          optional HTML/CSS/JavaScript design and author preview
└── dist/                 canonical releases: <id>-<version>.stlp (made by `stlp create`)
```

The archive and its display assets stay here. `catalog/catalog.json` links to them; do not copy them
to a separate catalog-assets folder.

Make or update a package with the skill `academy-templates:package`, or by hand with the packer from
an [Academy](https://github.com/SemiTecFoundation/semitec-academy) checkout: `node <academy>/packer/stlp.js check|create <pack-spec.json>`.
Spec format: [`docs/PACK-SPEC.md`](https://github.com/SemiTecFoundation/semitec-academy/blob/main/docs/PACK-SPEC.md). Package ids are
`org.semitec.<name>`; raise `version` for every update you share.

Each `.stlp` archive has a `manifest.json` plus `content/trainings/`, `content/labs/`,
`content/readings/`, `content/videos/`, `content/materials/` and `content/projects/` folders as needed.
It retains complete runnable training source (JSON, HTML, CSS, JavaScript, assets, themes and certificates)
and complete lab/project folders. The exact fictional reference archive and manifest are maintained with the
authoring product: [Academy Templates package archive layout](https://github.com/SemiTecFoundation/semitec-academy-skills/blob/main/skills/package/reference/archive-layout.md).

| Package | Id | For | Status |
|---|---|---|---|
| [BIST and MBIST](../Packages/bist-mbist/pack-spec.json) | `org.semitec.bist-mbist` | bachelor students; five BIST and MBIST trainings plus *Memory Fundamentals* over 10 weeks | 1.1.1 — kept in `bist-mbist/dist/` in this materials repository |

## Current release

**BIST and MBIST 1.1.1 / Academy 2.2.0+** has an explicit course order, a ten-week study plan, six
author previews, portable standalone training entries and optional HTML certificates at package and
training levels. The publisher has chosen to offer those certificates, and `catalog/catalog.json` points to this canonical
release archive.

The 1.0.0 and 1.1.0 archives are retained for historical compatibility. Never overwrite a published version
with changed bytes: create and catalog a new version instead.

Private feature-check and other local review packages are not catalog content and must not be committed
or published. Generated review archives are stored outside this repository.
