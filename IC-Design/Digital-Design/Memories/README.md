# Memories

How memories work and how to design with them: SRAM, register files, FPGA memories, DRAM and non-volatile memories, memory interfaces, FIFOs, and error-correcting codes. Audience: **bachelor students** (digital logic and an HDL assumed).

This topic holds the memory detail that the BIST / MBIST trainings deliberately leave out; *Memories and Their Faults* in [BIST-MBIST](../BIST-MBIST/README.md) links here.

## Scope
- Memory fundamentals: types, hierarchy, organisation (words, banks, ports), metrics, synchronous interfaces and timing
- SRAM in depth: 6T/8T cells, read and write margins, sense amplifiers, decoders, memory compilers, low-power modes, register files
- Memories in FPGAs: block RAM, distributed (LUT) RAM, large RAM blocks; inference from RTL; vendor-neutral
- Designing with memories in RTL: FIFOs (synchronous and asynchronous), banking, ping-pong buffers, arbitration, caches in brief
- Error-correcting codes: parity, Hamming, SECDED, interleaving, soft errors, scrubbing
- DRAM and external memory: cell and array, refresh, DDR commands and timing, memory controllers
- Non-volatile memories: ROM, OTP / eFuse, flash, emerging memories (MRAM, ReRAM) in brief


## Trainings (planned)

| # | Id | Title | Content | Status |
|---|---|---|---|---|
| 1 | `mem-fundamentals` | Memory Fundamentals | hierarchy, types, organisation and address mapping, register-level read/write, interfaces, multi-port, FIFOs, ECC memory modules, controllers and AMBA overview, metrics, timing — SystemVerilog for every structure | built — version 2, 11 topics, in review |
| 2 | `mem-sram` | SRAM in Depth | 6T/8T cells, read stability and write margin, sense amps, decoders, memory compilers, low-power modes, register files | planned |
| 3 | `mem-fpga` | Memories in FPGAs | block RAM, LUT RAM, large RAM blocks, inference templates, read-during-write, output registers, timing | planned |
| 4 | `mem-rtl-design` | Designing with Memories | asynchronous FIFOs in depth (Gray pointers, CDC), ping-pong buffers, arbitration, caches | planned |
| 5 | `mem-ecc` | Error-Correcting Codes | code theory: parity, Hamming math, SECDED construction, BCH, interleaving, soft-error rates, ECC in caches and DRAM (the ECC *module* is in mem-fundamentals) | planned |
| 6 | `mem-dram` | DRAM and External Memory | cell and array, refresh, DDR commands and timing, controllers and PHY in brief | planned |
| 7 | `mem-nvm` | Non-Volatile Memories | ROM, OTP / eFuse, NOR and NAND flash, wear and ECC, MRAM / ReRAM in brief | planned |

## Training `mem-fundamentals` — structure (version 2, built — in review)

Rule for every topic: **first the concept subsections** (pictures, interactive diagrams, waveforms, register-level view),
**then a separate subsection "In SystemVerilog"** with the synthesizable description (all code compiled and simulated with Verilator).
About 10 hours, 3 weeks, 11 topics.

| # | Topic (id) | Concept subsections | "In SystemVerilog" subsection | Visuals |
|---|---|---|---|---|
| 1 | Why memory matters (`why-memory`) | storage in a digital system · hierarchy · processor–memory gap · locality and AMAT | register array vs RAM | hierarchy, locality animations |
| 2 | Memory types (`types`) | how each memory stores a bit · volatile / non-volatile · choosing | ROM with case and $readmemh | clickable cells |
| 3 | Organisation and address mapping (`organisation`) | system address map (which address → which memory) · byte vs word addresses · depth / width / address bits · rows, columns, column mux · banks · interleaving · width and depth expansion | sp_ram, address decoder for a memory map, row/col split, bank select, ram_64x1k, ram_16x4k | **interactive memory map**, **address-field mapping**, **banking vs interleaving animation**, expansion |
| 4 | Inside a memory: register-level read and write (`register-level`) | memory = registers + write decoder + read multiplexer · the write process clock by clock · the read process (async and sync) · waveforms | structural memory (decoder + registers + mux) vs behavioural array | **write animation**, **read animation**, waveforms |
| 5 | The synchronous memory interface (`sync-interface`) | signals · read latency 1 / 2 · byte enables · read-during-write · async vs sync read | sp_ram_lat, sp_ram_be, three read-during-write variants, async read | waveform animations |
| 6 | Multi-port memories (`multi-port`) | port types · inside a dual-port memory · register files · bypass · collisions (waveforms) · dual-clock memories | sdp_ram, tdp_ram, regfile_2r1w, collision assertion | **port illustrations**, multi-port internals, collision waveform, bypass |
| 7 | FIFOs (`fifo`) | queue and ring buffer · read/write pointers · full / empty (extra pointer bit) · almost-full, FWFT vs standard read · waveforms · asynchronous FIFO overview (Gray pointers, synchronisers) | synchronous FIFO on sdp_ram with flags | **ring-buffer animation**, FIFO waveform, async FIFO diagram |
| 8 | ECC memory modules (`ecc-memory`) | why memories need ECC · ECC memory architecture: encoder on write, check bits stored, decoder on read · SECDED behaviour: correct 1, detect 2 · overhead (39,32), (72,64) · error flags, counters, scrubbing | parameterised SECDED encoder / decoder modules and an `ecc_ram` wrapper | **ECC write/read/error animation** |
| 9 | Memory controllers and AMBA (`controllers-amba`) | what a memory controller does · SRAM vs DRAM controller · arbitration and wait states · the AMBA family at high level (APB, AHB, AXI, AXI-Lite, AXI-Stream, ACE/CHI) · typical SoC bus structure · handshakes in one picture | APB slave in front of an SRAM | **SoC bus diagram**, APB and AXI handshake waveforms |
| 10 | Metrics (`metrics`) | latency / cycle time · bandwidth · area · energy · retention and endurance | — | latency chart |
| 11 | Timing and datasheets (`timing`) | setup / hold / tCQ · datasheet · asynchronous SRAM | behavioural model with timing checks; self-checking testbench | timing animations |

The deeper follow-ups stay in later trainings: `mem-rtl-design` (async FIFO in depth, caches, arbitration), `mem-ecc` (code theory: Hamming math, BCH, interleaving), and the AMBA trainings in [Interfaces/AMBA](../Interfaces/AMBA/README.md).

## How to continue in a new chat (working notes)

- Content rules: global use — **no specific boards** (no AMD AUP ZU3) and vendor-neutral FPGA wording; big pictures that never overlap text;
  diagrams and step-by-step animations in most subsections (not everywhere); stepper buttons fixed under the picture.
- SystemVerilog style: **no `for` / `while` loops** in the examples — write repeated hardware out explicitly (separate instances, one line per byte lane, constant masks or lookup tables). Synthesizable, short, commented; every example compiled and simulated with Verilator.
- Delivery: edit files **directly in the Foundation folder** on the computer; no zip / tgz.
- Start a training by copying the engine from an existing one: `cp -R ../BIST-MBIST/trainings/bist-test-access/{INTEGRATION.md,README.md,index.html,certificate.json,css,js,tools,reference}` into the new folder, then write `training.json`, `TOC.md`, `topics/*.json`, `assets/*.svg`.
- Block types: text, callout, table, code, svg, stepper (`data-step` / `data-until` in the SVG), reveal (spots in % with title/md), scrolly, tabs, accordion, categorize, sort, flipcards; quiz types single, multiple, truefalse, order, match.
- Check and build: `python3 tools/validate.py .` (0 errors) and `python3 tools/build_single_file.py` → `dist/training-preview.html`; then `python3 semitec-academy-materials/tools/inventory.py`.
- SVG style used so far: white background, Segoe UI, title 19 px bold navy (#1f4e79), text ≥ 14 px, colours navy #1f4e79, blue #1f6feb, purple #6c4fb3, green #1e8449, red #c0392b, gold #c9a227, orange #d35400.

## Labs (planned) — hands-on on an FPGA

A lab is **practice, not reading**: students write the memory in SystemVerilog, simulate it in Vivado, implement it, program the board and show it working.
The labs use the Vivado flow; the steps are the same in other vendors' tools. Any FPGA board works if it has
**switches, push-buttons, LEDs, a USB-UART and a 100 MHz clock** (a 7-segment display helps). Each lab includes a constraints template, so the labs do not depend on one board.

**Every lab follows the same six steps (and is graded on them):**

1. **Spec**: read the interface table and draw the block diagram.
2. **RTL**: SystemVerilog without `for` / `while` loops, synthesizable.
3. **Simulate**: a self-checking testbench in the Vivado simulator; hand in a waveform screenshot with the key cycles marked.
4. **Implement**: synthesis and implementation; read the **utilization** report (FF / LUT / LUTRAM / BRAM) and the **timing** report (WNS, Fmax).
5. **Program and demo**: generate the bitstream, program the board, demonstrate with switches, buttons, LEDs or UART.
6. **Debug and report**: where marked, capture signals on hardware with the **ILA**; write a 2-page report with results and answers to the lab questions.

| Id | Lab | Students build | On the board | Level · time | After topic |
|---|---|---|---|---|---|
| `mem-lab-regfile-board` | M1 A memory you can touch | 8 × 8 register-level memory: write decoder, registers, read mux (structural), plus the behavioural version | address on switches, data on switches, write button; the read word on LEDs / 7-segment; check that the two versions behave the same | basic · 3 h | 4 |
| `mem-lab-fpga-infer` | M2 Inferring FPGA memories | the same 1K × 8 RAM written four ways: async read, sync read, output register, read-first / write-first; a ROM loaded with `$readmemh` | a message from the ROM scrolls on the 7-segment display; compare the utilization report: FF vs LUTRAM vs BRAM, and the Fmax of each version | basic · 3 h | 2, 5 |
| `mem-lab-banks` | M3 Byte enables, banks and the address map | 32-bit memory with byte enables built from four 8-bit banks; address decoder for a small memory map (RAM, ROM, LED register) | byte writes from switches; an access to an unmapped address lights an error LED; ILA shows the bank select and byte enables | medium · 4 h | 3, 5 |
| `mem-lab-dual-port` | M4 Dual-port memory and collisions | true dual-port RAM; port A from the switches, port B from a counter that sweeps the memory; collision detector with assertion | port B shows the memory content on LEDs while port A writes; a collision counter on the 7-segment display; the simulation shows the read-during-write result | medium · 4 h | 6 |
| `mem-lab-uart-fifo` | M5 FIFO between UART and buttons | synchronous FIFO (wrap-bit pointers, full / empty / almost-full) between a UART receiver and a UART transmitter | type characters in a terminal; they are stored and sent back one per button press; full / empty / almost-full on LEDs; ILA captures the moment of full | medium · 5 h | 7 |
| `mem-lab-async-fifo` | M6 Two clocks, one FIFO | asynchronous FIFO with Gray pointers and 2-FF synchronisers; Clocking Wizard makes 100 MHz and 37 MHz | a producer at one clock and a consumer at the other; a checker counts lost or wrong words (must stay 0); run `report_cdc` and explain every line of the report | advanced · 6 h | 7 |
| `mem-lab-hamming` | M7 Hamming on switches | Hamming (7,4) + parity encoder and decoder exactly as in the worked example of Topic 8 | 4 data bits on switches → 8-bit code word on LEDs; 8 more switches flip code bits; corrected data, syndrome, ce and ue on LEDs / 7-segment | basic · 3 h | 8 |
| `mem-lab-ecc-ram` | M8 ECC RAM with error injection | `ecc_ram` (SECDED 39,32) with an error-injection mask on the write path, ce / ue counters, and the address of the last error | inject 1-bit and 2-bit errors at a chosen address; counters on the 7-segment display; timing report with and without a pipeline register after the decoder | medium · 5 h | 8, 11 |
| `mem-lab-apb-ram` | M9 A memory on a bus | `apb_sram` from Topic 9 plus an AXI-Lite version, in a Vivado block design with a JTAG-to-AXI master (or a soft CPU) | read and write the memory from the Vivado Tcl console; add wait states and see them in the ILA; out-of-range addresses return an error response | advanced · 6 h | 9 |
| `mem-lab-timing` | M10 How fast is my memory? | the same RAM with 0, 1 and 2 pipeline stages, and a wide (32K × 32) RAM built from many BRAMs | measure Fmax from the timing report, find the critical path in the device view, fix it; plot Fmax vs latency | advanced · 4 h | 10, 11 |

## Projects (planned) — bigger and harder than labs

Projects take **3–6 weeks** for a team of 2–3 students. Each one has a written spec, a verification plan, a self-checking testbench with coverage of the main cases, a working board demo and a final report or presentation.
Projects marked **(D)** are large enough for a diploma (bachelor thesis).

| Id | Project | What students build | Board demo | Level |
|---|---|---|---|---|
| `mem-proj-mem-tester` | Memory test station (D) | a hardware March engine (March C−, MATS+) that tests an on-chip RAM; a fault-injection wrapper (stuck-at, transition, coupling); UART commands `fill`, `dump`, `march`, `inject`; a Python script on the PC | inject a fault, run March C−, the failing address and element are printed on the PC; a coverage table for each fault type — links to [BIST-MBIST](../BIST-MBIST/README.md) | hard |
| `mem-proj-ecc-memory` | ECC memory subsystem with scrubber (D) | SECDED memory, background scrubber, error counters, error-address log, interrupt; AXI-Lite or APB control registers; error injection | a PC script injects random errors at a chosen rate; the scrubber keeps the double-error count at 0; statistics printed live | hard |
| `mem-proj-frame-buffer` | Video frame buffer | dual-port BRAM frame buffer (e.g. 160 × 120, 8-bit colour) scanned out at 640 × 480 VGA/HDMI timing; drawing commands over UART; **ping-pong** double buffering, so there is no tearing | draw shapes or show an image sent from the PC; switch between single and double buffering to see the difference (needs a board with VGA / HDMI or a VGA add-on) | medium–hard |
| `mem-proj-cache` | Cache in front of a slow memory | slow memory model in BRAM with programmable wait states; a direct-mapped cache, then a 2-way set-associative cache with LRU; hit / miss counters; a traffic generator with several access patterns | the hit rate and average latency for each pattern on the 7-segment display or over UART; compare cache sizes and associativity | hard |
| `mem-proj-flash-ctrl` | SPI / QSPI flash controller | a controller for the board's configuration flash or an add-on flash: read ID, read, page program, sector erase, status polling; a FIFO toward the UART | save a text over UART, power-cycle the board, read it back — non-volatile memory in practice | medium–hard |
| `mem-proj-ddr` | External DDR memory (D) | generate the vendor DDR controller IP (MIG) for the board's DDR; an AXI traffic generator written by the students; a bandwidth and latency monitor | measure read and write bandwidth for different burst lengths and access patterns; compare with the theoretical peak (needs a board with DDR) | hard |
| `mem-proj-mini-soc` | Memory subsystem for a mini SoC (D) | a small RISC-V soft core with instruction and data BRAM, a banked shared SRAM with an arbiter for CPU and DMA, ECC on the data memory, UART; a C program runs on it | the program copies and checks buffers; DMA and CPU contend for memory; performance counters show the stalls — ties together the Memories, AMBA and BIST material | very hard |
| `mem-proj-mem-generator` | Memory generator tool | a Python tool that writes parameterised SystemVerilog memories (ports, width, depth, banks, ECC, pipeline) plus testbenches and Vivado Tcl scripts — a mini "memory compiler" | generate 5 configurations, implement them automatically and plot area and Fmax in one table | medium–hard |

Links: `mem-ecc` ↔ `mbist-architecture` (testing ECC memories) and `bist-in-field` (ECC in operation); `mem-sram` ↔ `mbist-memories-faults` (why cells fail).

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
| Training | Memory Fundamentals | `trainings/mem-fundamentals` | 11 topics, 3-week plan | BIST and MBIST |
<!-- inventory:end -->
