# BIST / MBIST

Built-in self-test of memories and logic. Audience: **bachelor students** (digital design and an HDL assumed).
Prerequisites from other topics: SystemVerilog and FSMs (Digital Design); fault models, scan and ATPG basics (DFT).

## Scope
- Foundations: why self-test; LFSRs, MISRs, signature analysis; the BIST controller
- Memories for testers: SRAM cell and array, decoders, sense amps; word-oriented and multi-port memories; ROM; FPGA BRAM / LUTRAM
- Memory fault models: stuck-at, transition, stuck-open, address-decoder, coupling, read-disturb, retention, NPSF, linked faults; fault primitives
- March tests: notation; MATS+, March X, C−, A, B, SS, LR; proving detection; data backgrounds and address orders
- MBIST architecture: hard-wired and programmable controllers, collars, comparators, shared controllers, at-speed test, test power, diagnosis and bitmaps
- Test access: IEEE 1149.1 TAP, IEEE 1687 (IJTAG), IEEE 1500 in brief
- Repair: spare rows / columns, redundancy analysis (BIRA), built-in self-repair, eFuses
- Logic BIST: STUMPS, phase shifter, X-bounding, test points, at-speed LBIST, in-field test
- Industry flows: Tessent MemoryBIST / LogicBIST, Synopsys SMS / TestMAX

## Trainings

One training per subject, in `trainings/`. Each has a `TOC.md`; topics are built and reviewed one by one.

| Id | Title | Status |
|---|---|---|
| `bist-foundations` | BIST Foundations: Why Chips Test Themselves | built — 6 topics |
| `mbist-memories-faults` | Memories and Their Faults | built — 7 topics (topic 7 in review) |
| `mbist-march-tests` | March Tests | built — 6 topics, in review |
| `mbist-architecture` | MBIST Architecture | built — 7 topics, in review |
| `bist-test-access` | Test Access: JTAG and IJTAG | built — 8 topics, expert review |
| `mbist-repair` | Memory Repair | planned |
| `lbist` | Logic BIST | planned |
| `bist-in-field` | BIST in the Field and Functional Safety | planned |
| `bist-industry-flows` | Industry BIST Flows (optional) | planned |

### Where ECC is covered

- **How ECC works** (parity, Hamming, SECDED, interleaving): the memory courses in *Digital Design*, not here.
- `mbist-memories-faults` (topic 7): a short pointer — MBIST finds faults at test time, ECC corrects errors in operation.
- `mbist-architecture`: testing memories that have ECC — ECC bypass during MBIST, testing the check bits and the encoder/decoder.
- `mbist-repair`: ECC versus spare rows/columns — which faults each one handles, and how they are combined.
- `bist-in-field`: ECC in operation — soft errors, scrubbing, error counters, periodic MBIST and functional safety (ISO 26262).


### Proposed additional trainings

| Id | Title | Content | Status |
|---|---|---|---|
| `bist-diagnosis` | Fault Simulation and Diagnosis | how fault simulators work, failure bitmaps, from fail to defect location, yield learning | proposed |
| `bist-analog` | Analog and Mixed-Signal BIST | ADC/DAC histogram test, PLL and clock BIST, SerDes loopback, IEEE 1149.4 / P1687.2 in brief | proposed |
| `bist-chiplets` | Test of 3D ICs and Chiplets | known-good die, die-to-die interconnect test, IEEE 1838, test access through a stack | proposed |
| `bist-security` | Secure Test Access | scan and JTAG as attack paths, locking, challenge-response, secure IJTAG networks | proposed |
| `bist-lifecycle` | Silicon Lifecycle Monitoring | on-chip sensors (aging, voltage droop, temperature), in-system test data, predictive maintenance | proposed (may merge into `bist-in-field`) |

Prerequisite outside this topic: **DFT basics** (scan, ATPG, fault coverage) in [DFT](../DFT/README.md), needed before `lbist` and helpful for `bist-test-access`.

## Labs (planned)

Free tools only: Python, SystemVerilog with Verilator / Icarus, cocotb, any FPGA board. One folder per lab in `labs/` (manual PDF + app lab).

| Id | Lab | Students build / measure | After training |
|---|---|---|---|
| `bist-lab-lfsr` | L1 LFSR | LFSRs in SystemVerilog, primitive vs non-primitive polynomials, period | `bist-foundations` |
| `bist-lab-misr` | L2 MISR and aliasing | MISR, fault injection, measured aliasing vs 2⁻ⁿ | `bist-foundations` |
| `mbist-lab-fault-model` | L3 Faulty-memory model | Python memory model with injectable faults (SAF, TF, CF, AF, RDF …) | `mbist-memories-faults` |
| `mbist-lab-march` | L4 March tests | run MATS+ … March SS on the faulty model, measure coverage, write own test | `mbist-march-tests` |
| `mbist-lab-controller` | L5 MBIST controller | March C− controller + collar in SystemVerilog, simulation, then FPGA | `mbist-architecture` |
| `bist-lab-tap` | L6 JTAG TAP | TAP controller, IR, BYPASS, IDCODE and one TDR in SystemVerilog; cocotb driver | `bist-test-access` |
| `bist-lab-ijtag` | L7 IJTAG network | SIB-based network with two instruments; Python driver that opens paths (mini retargeting) | `bist-test-access` |
| `mbist-lab-bira` | L8 Redundancy analysis | BIRA algorithms on failure bitmaps in Python; repair rate vs spares | `mbist-repair` |
| `bist-lab-lbist` | L9 Logic BIST | STUMPS on a small circuit, fault coverage with a fault simulator, test points | `lbist` |

## Projects (planned)

Longer, open-ended work — semester projects or **diploma** topics (marked D).

| Id | Project | Content |
|---|---|---|
| `bist-proj-prog-mbist` | Programmable MBIST engine (D) | microcode controller for any March test, loaded over JTAG or UART, on FPGA, with diagnosis |
| `bist-proj-bisr` | Built-in self-repair (D) | MBIST + BIRA + spare rows/columns + fuse emulation on FPGA |
| `bist-proj-march-tool` | March test generator and verifier | Python tool: fault-primitive simulator that proves coverage and searches for short tests |
| `bist-proj-ijtag-tools` | Mini IJTAG toolkit (D) | ICL subset parser, network model and PDL retargeting to TAP vectors; verified on the L7 network |
| `bist-proj-lbist-riscv` | Logic BIST for a small RISC-V block | STUMPS, X-handling and coverage on an open-source core |
| `bist-proj-field-test` | In-field memory test | periodic, non-destructive memory test under software control with error logging |

## Materials

| Folder | What goes in | Made with |
|---|---|---|
| `lectures/` | lecture notes and readings (Markdown with images, or PDF) | by hand / any PDF template |
| `trainings/` | interactive web trainings, one folder each | `academy-templates:training` |
| `labs/` | labs: manual PDF + app lab (`lab/`), one folder each | `academy-templates:lab-manual` |
| `projects/` | project briefs + app projects (`project/`) | `academy-templates:project-brief` (+ `brief2project.py`) |
| `videos/` | `.mp4` (H.264 + AAC) / `.webm`, or `links.md` with online videos | — |
| `materials/` | starter files, constraints, datasheets, templates | — |

Name every material folder `<topic>-<short-name>` (e.g. `fpga-vivado-flow`); it becomes its id in packages.

## Inventory

<!-- inventory:start -->
| Type | Title | Path | Info | In packages |
|---|---|---|---|---|
| Training | BIST Foundations: Why Chips Test Themselves | `trainings/bist-foundations` | 6 topics, 2-week plan | BIST and MBIST |
| Training | Test Access: JTAG and IJTAG | `trainings/bist-test-access` | 8 topics, 2-week plan | BIST and MBIST |
| Training | MBIST Architecture | `trainings/mbist-architecture` | 7 topics, 2-week plan | BIST and MBIST |
| Training | March Tests | `trainings/mbist-march-tests` | 6 topics, 2-week plan | BIST and MBIST |
| Training | Memories and Their Faults | `trainings/mbist-memories-faults` | 7 topics, 2-week plan | BIST and MBIST |
<!-- inventory:end -->

See [../../../README.md](../../../README.md) for the workflow.
