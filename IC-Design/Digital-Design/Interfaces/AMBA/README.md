# AMBA on-chip buses (APB, AHB, AXI)

Arm's AMBA family is the standard way blocks talk to each other inside an SoC. Audience: **bachelor students** with SystemVerilog and the *Memory Fundamentals* training (topic 9 gives the high-level overview of AMBA and memory controllers).

## Scope
- AMBA family overview: APB, AHB / AHB-Lite, AXI4, AXI4-Lite, AXI4-Stream; ACE and CHI in brief
- Handshakes, transfers, bursts, wait states, errors, byte strobes, protection signals
- Interconnects: decoders, multiplexers, arbiters, bridges (AXI→APB, AHB→APB)
- Designing slaves (register banks, memory controllers) and masters (DMA); bus functional models and protocol assertions

## Trainings (planned)

| # | Id | Title | Topics | Status |
|---|---|---|---|---|
| 1 | `amba-apb` | APB: the Peripheral Bus | why APB; signals (PSEL, PENABLE, PWRITE, PADDR, PWDATA, PRDATA, PREADY, PSLVERR, PSTRB, PPROT); setup and access phases with waveforms; wait states and errors; APB3 vs APB4 vs APB5 in brief; register-bank slave design; address decoding for several slaves; SystemVerilog slave and a simple master/BFM | planned — first |
| 2 | `amba-ahb` | AHB-Lite: the High-Performance Bus | pipelined address and data phases; HTRANS (IDLE, BUSY, NONSEQ, SEQ); HSIZE, HBURST (INCR, WRAP); HREADY and wait states; HRESP; decoder and multiplexor; AHB-Lite SRAM controller; AHB→APB bridge; SystemVerilog examples | planned |
| 3 | `amba-axi` | AXI4: the Advanced eXtensible Interface | five channels (AW, W, B, AR, R); VALID/READY handshake rules; bursts FIXED / INCR / WRAP, AxLEN / AxSIZE; WSTRB; IDs, outstanding and out-of-order transactions; responses; AXI4-Lite; AXI4-Stream (TVALID/TREADY/TLAST/TKEEP); interconnects and QoS; SystemVerilog AXI4-Lite slave and AXI4 burst memory slave | planned |
| 4 | `amba-verification` | Verifying AMBA Interfaces (optional) | bus functional models in cocotb / SystemVerilog, protocol assertions (SVA), scoreboards, coverage of bursts and wait states | planned |

## Labs (planned)

| Id | Lab | Students build | After training |
|---|---|---|---|
| `amba-lab-apb-regs` | A1 APB register bank | APB4 slave with control/status registers, PSTRB, PSLVERR on bad address; cocotb tests | `amba-apb` |
| `amba-lab-apb-decoder` | A2 APB subsystem | APB decoder with three slaves (registers, SRAM, UART stub) | `amba-apb` |
| `amba-lab-ahb-sram` | A3 AHB-Lite SRAM controller | pipelined AHB-Lite slave in front of `sp_ram`, wait states, bursts | `amba-ahb` |
| `amba-lab-axil-slave` | A4 AXI4-Lite slave | register bank with independent read/write channels, handshake assertions | `amba-axi` |
| `amba-lab-axi-mem` | A5 AXI4 burst memory | AXI4 slave with INCR/WRAP bursts over an SRAM, IDs | `amba-axi` |
| `amba-lab-axis-fifo` | A6 AXI-Stream FIFO | stream FIFO with back-pressure, TLAST, measured throughput | `amba-axi` |

## Projects (planned)

| Id | Project | Content |
|---|---|---|
| `amba-proj-ahb2apb` | AHB-to-APB bridge | full bridge with wait states and error mapping, verified with assertions |
| `amba-proj-axi-dma` | AXI DMA engine (D) | memory-to-memory DMA with AXI4 bursts, AXI4-Lite control registers, interrupts |
| `amba-proj-mini-soc` | Mini SoC interconnect (D) | small RISC-V core + AXI interconnect + SRAM + APB peripherals |

Links: [Memories](../../Memories/README.md) (memory controllers, ECC memories), [BIST-MBIST](../../BIST-MBIST/README.md) (test access to bus-attached memories).

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
_No materials yet._
<!-- inventory:end -->
