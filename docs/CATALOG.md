# SemiTec Foundation Academy Catalog

`catalog/catalog.json` is the public index for **SemiTec Academy**. It contains no package archive and no
copied display asset. Each entry points to the canonical `.stlp`, cover and publisher logo in its
`Packages/<package-name>/` folder.

When this repository's GitHub Pages site is enabled, add this exact URL in **SemiTec Academy → Catalog → Add
a catalog link**:

```text
https://semitecfoundation.github.io/semitec-academy-materials/catalog/catalog.json
```

Do not use the repository home page or a GitHub file-view page. The Academy app needs the direct HTTPS URL to
`catalog.json`.

The current package is signed by SemiTec Foundation. Foundation public keys are already included in Academy;
other publishers distribute their `.pub.pem` public key separately and recipients decide whether to trust it.

## Update procedure

1. Build and sign a new `.stlp` from a package specification. Keep it in that package's `dist/` folder.
2. Regenerate the catalog from this repository root:

   ```bash
   python3 tools/build_catalog.py
   ```

   It scans `Packages/*/dist/*.stlp`, selects the newest version of each package id, calculates the
   download checksum, and writes the relative URLs. Use `python3 tools/build_catalog.py --check` in a
   review or CI check.

3. Check the direct GitHub Pages `catalog.json` URL in Academy before announcing the update.
