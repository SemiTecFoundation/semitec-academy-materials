# SemiTec Academy Materials

The SemiTec Foundation's **course content** — lectures, interactive trainings, labs, projects, videos and
files — organised by subject, and the **SemiTec Learning Packages** (`.stlp`) built from it for the
[SemiTec Academy](https://github.com/SemiTecFoundation/semitec-academy) app. One material can be used in
many packages. The published site also serves standalone browser trainings and the Academy catalog.

Material is made with the skills in
[`semitec-academy-skills`](https://github.com/SemiTecFoundation/semitec-academy-skills). Why the three
repositories are separate, how material is classified, and what gets built next:
**[`docs/PLAN.md`](docs/PLAN.md)**.

## Index

| Sphere | Topic | State |
|---|---|---|
| **IC-Design** | [Digital-Design / BIST-MBIST](IC-Design/Digital-Design/BIST-MBIST/) | 6 trainings — the furthest along |
| | [Digital-Design / Memories](IC-Design/Digital-Design/Memories/) | 1 training |
| | [Digital-Design / Interfaces / AMBA](IC-Design/Digital-Design/Interfaces/AMBA/) | ready for content |
| | [Digital-Design / FPGA](IC-Design/Digital-Design/FPGA/) · [Verification](IC-Design/Digital-Design/Verification/) · [DFT](IC-Design/Digital-Design/DFT/) · [Timing](IC-Design/Digital-Design/Timing/) · [CPU](IC-Design/Digital-Design/CPU/) · [IPs](IC-Design/Digital-Design/IPs/) | planned |
| | [Analog-Design](IC-Design/Analog-Design/) | planned |
| **EDA** | [EDA](EDA/) | planned |

**[`docs/INVENTORY.md`](docs/INVENTORY.md)** lists every material with its path and the packages it is used in.
It is generated — run `python3 tools/inventory.py` after adding anything.

## Use the published materials

- **Standalone use:** each released training has a self-contained `dist/training.html`. Open it in any
  browser, or use the links on the [GitHub Pages site](https://semitecfoundation.github.io/semitec-academy-materials/).
  A standalone training does not require Academy or a package.
- **Academy use:** install a complete course package from the catalog. In **Academy → Catalog → Add a
  catalog link**, paste:

  ```text
  https://semitecfoundation.github.io/semitec-academy-materials/catalog/catalog.json
  ```

  This is a direct catalog URL, not the repository URL. The catalog is only an index; it points to the
  single canonical package archive and display assets in `Packages/`. Its update procedure is in
  [`docs/CATALOG.md`](docs/CATALOG.md).

### Packages

| Package | Id | For | Status |
|---|---|---|---|
| [BIST and MBIST](Packages/bist-mbist/pack-spec.json) | `org.semitec.bist-mbist` | bachelor students; five BIST and MBIST trainings plus *Memory Fundamentals* over 10 weeks | 1.1.0 · Academy 2.1.0+ |

More in [`docs/PACKAGES.md`](docs/PACKAGES.md).

## Layout

```
semitec-academy-materials/
├── IC-Design/
│   ├── Analog-Design/
│   └── Digital-Design/
│       ├── FPGA/   ├── Verification/   ├── Timing/   ├── DFT/
│       ├── BIST-MBIST/   ├── Interfaces/   ├── IPs/   └── CPU/
├── EDA/
├── Packages/                    one canonical package location: sources, release archive and display assets
├── catalog/                     public catalog.json index only
├── docs/                        repository plan, catalog procedure, package guide, partners and inventory
├── index.html                   GitHub Pages entry point for standalone browser materials
└── tools/                       repository maintenance scripts
```

**Material folders only at the last level.** A topic that has sub-topics holds only its README. When a
topic is final (no more sub-topics), make it ready for content with

```
python3 tools/inventory.py --init IC-Design/Digital-Design/FPGA
```

which adds these folders and the *Materials* / *Inventory* sections to its README:

| Folder | What goes in | Made with |
|---|---|---|
| `lectures/` | lecture notes and readings (Markdown with images, or PDF) | by hand / a PDF template |
| `trainings/` | interactive web trainings, one folder each | [Academy Templates training skill](https://github.com/SemiTecFoundation/semitec-academy-skills/tree/main/skills/training) |
| `labs/` | labs: LaTeX manual + app lab (`lab/`), one folder each | [Academy Templates lab-manual skill](https://github.com/SemiTecFoundation/semitec-academy-skills/tree/main/skills/lab-manual) |
| `projects/` | project briefs + app projects (`project/`) | [Academy Templates project-brief skill](https://github.com/SemiTecFoundation/semitec-academy-skills/tree/main/skills/project-brief) |
| `videos/` | `.mp4` (H.264 + AAC) / `.webm`, or `links.md` with online videos | — |
| `materials/` | starter files, constraints, datasheets, report templates | — |

## Who made it — `meta.json`

A material may carry a `meta.json` saying who it is for and where it came from. Leave it out and the
material counts as Foundation-made, released, English. Full field list in [`docs/PLAN.md`](docs/PLAN.md#4-classification).

```json
{ "audience": "bachelor", "language": "en", "status": "released",
  "origin": "foundation", "license": "CC-BY-4.0" }
```

Material made **with a company** sets `"origin": "partner"` and a `"partner"` key registered in
[`docs/PARTNERS.md`](docs/PARTNERS.md); material from **students or individual researchers** sets
`"origin": "community"` and stays a draft until reviewed.

## Workflow

1. **Define** — what the course teaches, for whom, how many weeks: the topic README's *Scope* is the
   starting point. Write the outline (modules → lectures / trainings / labs / project) before making files.
2. **Create** each material in its (last-level) topic folder with the matching skill, e.g. *"Make a training
   `fpga-vivado-flow` in IC-Design/Digital-Design/FPGA/trainings: …"*, *"Make Lab 1 `fpga-lab01-leds` in
   …/FPGA/labs"*, *"Write a project brief in …/Verification/projects and convert it for the app"*.
   Each skill checks its own output (`validate.py`, `build.py`, `check_lab.py`, `brief2project.py`).
3. **Package** — in `Packages/<package-name>/pack-spec.json` list the materials from any topics (an FPGA
   course can take a training from Verification and an interface lab from Interfaces), add the study plan
   (`schedule`), attach files to their labs (`"for"`), then [Academy Templates package skill](https://github.com/SemiTecFoundation/semitec-academy-skills/tree/main/skills/package) checks and builds
   the `.stlp`.
4. **Share** — keep the release archive in its package's `dist/` folder, then run
   `python3 tools/build_catalog.py`; students install it from the app's Catalog.
5. **Keep track** — `python3 tools/inventory.py` updates every topic's *Inventory* (and `docs/INVENTORY.md`)
   and shows which materials are not in any package yet.

## Rules

- **Names = ids.** Material folders are named `<topic>-<short-name>` in lowercase with dashes
  (`fpga-vivado-flow`, `verif-sva-basics`, `mbist-march-c`), unique across this repository, so that
  packages combining topics never get duplicate ids. Never rename a released material — students'
  progress is stored per id; make a new version of the package instead.
- **One home per material.** A material lives in exactly one topic (where it is taught); other packages
  point to it. Shared starter files go in the `materials/` of the topic that owns them.
- **Languages.** One material per language with a suffix: `fpga-vivado-flow` (English),
  `fpga-vivado-flow-hy` (Armenian).
- **Sources stay here, builds go out.** LaTeX sources, training JSON and lab files live here; generated
  files (`.stlp`, single-file HTML trainings) go to `Packages/<name>/dist/` or the skill's `dist/`.
- **Status.** Draft packages can be tested locally. Publish only materials intended for release.
