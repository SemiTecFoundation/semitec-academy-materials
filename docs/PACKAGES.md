# Packages

One folder per SemiTec Learning Package:

```
Packages/<package-name>/
├── pack-spec.json        what goes in: materials from any topic (paths like ../../IC-Design/Digital-Design/FPGA/labs/fpga-lab01-leds/lab)
├── cover.svg             600 × 340 cover, publisher-logo.svg, certificate.json (optional)
└── dist/                 canonical releases: <id>-<version>.stlp (made by `stlp create`)
```

The archive and its display assets stay here. `catalog/catalog.json` links to them; do not copy them
to a separate catalog-assets folder.

Make or update a package with the skill `academy-templates:package`, or by hand with the packer from
an [Academy](https://github.com/SemiTecFoundation/semitec-academy) checkout: `node <academy>/packer/stlp.js check|create <pack-spec.json>`.
Spec format: [`docs/PACK-SPEC.md`](https://github.com/SemiTecFoundation/semitec-academy/blob/main/docs/PACK-SPEC.md). Package ids are
`org.semitec.<name>`; raise `version` for every update you share, and sign a release with the
production key ([`docs/KEYS.md`](https://github.com/SemiTecFoundation/semitec-academy/blob/main/docs/KEYS.md)).

| Package | Id | For | Status |
|---|---|---|---|
| [BIST and MBIST](../Packages/bist-mbist/pack-spec.json) | `org.semitec.bist-mbist` | bachelor students; 5 BIST trainings over 10 weeks, *Memory Fundamentals* as prerequisite | 1.0.0 — signed with the production key; kept in `bist-mbist/dist/` in this materials repository |
