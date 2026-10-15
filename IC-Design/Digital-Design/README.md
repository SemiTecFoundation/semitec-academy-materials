# Digital Design

RTL design of digital circuits and their implementation, verification and test.

## Scope
- Combinational and sequential logic, FSMs, SystemVerilog for design
- The subtopics below (FPGA, Verification, Timing, DFT, BIST / MBIST, Interfaces, IPs, CPU)

## Topics

| Topic | About |
|---|---|
| [FPGA](FPGA/README.md) | Implementing designs on FPGAs (AMD AUP ZU3, Vivado / Vitis). |
| [Verification](Verification/README.md) | Showing that a design does what the specification says. |
| [Timing](Timing/README.md) | Static timing analysis and timing closure. |
| [Design for Test (DFT)](DFT/README.md) | Making chips testable after manufacturing. |
| [BIST / MBIST](BIST-MBIST/README.md) | Built-in self-test of logic and memories. |
| [Memories](Memories/README.md) | Memory types, SRAM, FPGA memories, FIFOs, ECC, DRAM, NVM. |
| [Interfaces](Interfaces/README.md) | On-chip and off-chip communication. |
| [IPs](IPs/README.md) | Reusable design blocks and how to package them. |
| [CPU](CPU/README.md) | Processor design. |

## Planned trainings (roadmap)

Agreed next step after the BIST / MBIST series. Each line becomes one or more trainings; the proposed home is where its folder will go.

| # | Training | Content | Proposed home |
|---|---|---|---|
| 1 | Memories in digital design — **started: [Memories](Memories/README.md)** | SRAM, register files, FPGA block / LUT RAM in depth; memory interfaces and timing; **ECC** — parity, Hamming, SECDED, interleaving, scrubbing. Takes the memory detail the BIST trainings leave out. | new subtopic `Memories/` |
| 2 | Verification | testbenches, assertions (SVA), functional coverage, then **cocotb** and UVM basics | [Verification](Verification/README.md) |
| 3 | RTL to GDS with open tools | Yosys, OpenROAD / OpenLane, SKY130 PDK; floorplan, placement, CTS, routing; static timing analysis | [Timing](Timing/README.md) + new subtopic `Physical-Design/` |
| 4 | Low-power design | clock gating, power gating, power domains, multi-voltage, UPF basics | new subtopic `Low-Power/` |
| 5 | RISC-V SoC basics | a small RISC-V core, bus, memories and peripherals — one project that ties design, memories and BIST together | [CPU](CPU/README.md) |
| 6 | Hardware security | side channels, fault attacks, hardware Trojans, secure test access (scan as an attack path) | new subtopic `Security/` |

Also needed before *Logic BIST* and *Test Access*: a **DFT basics** training (scan, ATPG, fault coverage) in [DFT](DFT/README.md).

_Hierarchy not final yet. Material folders (`lectures/`, `trainings/`, `labs/`, `projects/`, `videos/`, `materials/`) are added only at the last level, with `python3 tools/inventory.py --init <topic>`._

See [../../README.md](../../README.md) for the workflow.
