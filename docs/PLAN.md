# Plan — SemiTec Academy Materials

What this repository is for, what goes in it, how material is classified, and in what order it gets
built. This is the planning document; [`README.md`](../README.md) is the index of what exists today.

Status: **published reference repository.** It serves standalone learning materials and a signed Academy catalog through GitHub Pages.

## 1. Why a separate repository

The Foundation's work splits into three products with different audiences and release rhythms. Keeping
them apart means a student downloading the app never pulls course content, and a company contributing
one lab never touches the application code.

| Repository | What it holds | Who uses it | Releases |
|---|---|---|---|
| [`semitec-academy`](https://github.com/SemiTecFoundation/semitec-academy) | the desktop app, the packer, the pack format | students (installers), developers | versioned installers |
| [`semitec-academy-skills`](https://github.com/SemiTecFoundation/semitec-academy-skills) | the AI skills and templates that *create* material | lecturers, course authors | plugin versions |
| **`semitec-academy-materials`** (this one) | the material itself: lectures, trainings, labs, projects, videos, files — and the packages built from them | lecturers, partners, students (through the app's Catalog) | package versions |

Planned fourth repository: **hackathon projects** (§7).

### Boundaries

- **No application code here.** Building a package calls the packer from a `semitec-academy` checkout
  or the copy bundled in the `package` skill.
- **No templates here.** Trainings and labs are *made with* the skills; the templates stay in
  `semitec-academy-skills`.
- **No course content in the other two.** The app repository carries only test fixtures; the skills
  repository only template examples.

## 2. What we publish

| Type | Form | Made with |
|---|---|---|
| Lecture / reading | Markdown with images, or PDF | by hand, or a PDF template |
| Interactive training | a folder of JSON + assets, runs offline in the app or as one HTML file | Academy Templates — training skill |
| Lab | LaTeX manual (PDF) + app lab (`lab.json`, steps, quiz, source files) | Academy Templates — lab-manual skill |
| Project | brief (PDF) + app project (`project.json`, weekly plan, milestones, rubric) | Academy Templates — project-brief skill |
| Video | `.mp4` (H.264 + AAC) / `.webm`, or a list of links | — |
| Files | starter projects, constraints, datasheets, report templates | — |
| **Package** | a signed `.stlp` combining any of the above, with a study plan | Academy Templates — package skill |

A material lives in exactly one topic and may appear in many packages.

## 3. Taxonomy

Three levels: **sphere → topic → material**, with material folders only at the last level (a topic that
still has sub-topics holds only its README).

```
<sphere>/[<sub-topic>/]<topic>/{lectures,trainings,labs,projects,videos,materials}/<material>/
```

Spheres now: **IC-Design** (Analog-Design, Digital-Design), **EDA**. Spheres are added when there is
real material to put in them, not in advance.

Naming is identity: a material folder is `<topic>-<short-name>` in lowercase with dashes, unique across
the repository, and **never renamed after release** — student progress is stored per id.

## 4. Classification

Beyond the folder it sits in, every material carries a small `meta.json`. It is optional — a material
without one is treated as Foundation-made, released, English — and `tools/inventory.py` reads it so
[`INVENTORY.md`](INVENTORY.md) and each topic's *Inventory* can group and filter.

```json
{
  "audience": "bachelor",
  "language": "en",
  "status": "released",
  "origin": "partner",
  "partner": "example-semiconductor",
  "license": "CC-BY-4.0",
  "contributors": ["Name, role"]
}
```

| Field | Values | Why |
|---|---|---|
| `audience` | `bachelor` · `master` · `professional` · `school` | who the material is pitched at; a package usually keeps one audience |
| `language` | `en` · `hy` · `ru` … | one material per language, suffixed folder (`…-hy`) |
| `status` | `draft` · `review` · `released` | drafts are packaged `--unsigned` for review; only released material is signed |
| `origin` | `foundation` · `partner` · `community` | who made it: us, a company, or students / individual researchers |
| `partner` | key into [`PARTNERS.md`](PARTNERS.md) | credit, logo, and the permission under which we publish |
| `license` | SPDX id, or `proprietary` | what a reader may do with it |
| `contributors` | names and roles | credit on the material and the certificate |

**Why `origin` matters.** Partner material arrives under a specific permission and must carry the right
credit and licence; community material needs review before it is signed. Mixing them silently would
make both impossible to audit — so the field is required for anything that is not Foundation-made.

## 5. How material reaches students

1. **Create** a material in its topic folder with the matching skill.
2. **Package** it: `Packages/<name>/pack-spec.json` lists materials from any topic, adds the study plan.
3. **Sign** with the production key (`semitec-academy/docs/KEYS.md`) — the app trusts only that key.
4. **Publish** the `.stlp` in the package's `dist/` folder, then regenerate [`catalog/catalog.json`](../catalog/catalog.json) with `python3 tools/build_catalog.py`. The catalog only indexes the canonical package files, and GitHub Pages serves its direct URL. Sources and the
   released package are committed here so the catalog has a stable, reviewable history.

## 6. Roadmap

**Phase 0 — bootstrap (complete).** Naming is aligned with the other repositories; this plan, the README
index, `meta.json` convention, `PARTNERS.md`, the first package and the GitHub Pages catalog are present.

**Phase 1 — first complete topic.** BIST-MBIST is the furthest along (5 trainings, 1 package). Finish it
as the reference example of what "done" looks like: lectures, a lab, a project, a study plan, released
and signed. Everything after copies its shape.

**Phase 2 — first public catalog (complete).** The first package is available through GitHub Pages and
its direct catalog URL can be added to Academy. The next contribution will prove the author workflow.

**Phase 3 — breadth.** Fill the empty topics that have demand: FPGA, Verification, Memories, DFT.
Prefer one finished topic over five half-built ones.

**Phase 4 — partners.** First company collaboration end to end: agreement, `origin: partner` material,
credit and licence, published package. `PARTNERS.md` becomes real.

**Phase 5 — community.** Accept student and individual-researcher material under `origin: community`,
with review before signing.

## 7. Planned: hackathon projects

A separate repository for hackathon and competition projects, organised by sphere — FPGA, Verification,
ASIC, Backend/Physical design, EDA algorithms — contributed by companies, students and individual
researchers.

It is kept apart from this repository on purpose: the material here is **taught** (curriculum, reviewed,
signed into packages), while a hackathon project is an **event artefact** (submitted, judged, archived
with its results). Mixing them would blur both the review rules and the licensing.

Open questions before it starts: per-sphere folders or per-event folders; what a submission must contain
to be publishable; how results and prizes are recorded; whether winning projects graduate into a project
brief here.

## 8. Open decisions

- Licence for Foundation-made material (one default, declared in `PARTNERS.md` terms).
- Whether `docs/INVENTORY.md` stays generated-and-committed, or becomes a build artefact.
- Video hosting: committed files grow the repository quickly — size limit before moving to links.
