# Memories and Their Faults — Table of contents

Status: **draft for review**. Topics are built and reviewed one at a time.
Audience: bachelor students who finished *BIST Foundations*. About 4 hours, 2 weeks. Each topic ends with a quiz.

| # | Topic (id) | Subsections | Interactive blocks | Status |
|---|---|---|---|---|
| 1 | Why memories need their own test (`why-memories`) | 1.1 Memories everywhere: share of area and of defects · 1.2 Memory types: SRAM, register file, ROM, DRAM, flash · 1.3 Why logic tests (scan, LBIST) do not fit memories | reveal (SoC), tabs (types), categorize | approved |
| 2 | Inside an SRAM (`sram`) | 2.1 The 6-transistor cell · 2.2 Reading and writing a cell · 2.3 The array: word lines, bit lines, row / column decoders, sense amplifiers · 2.4 Word-oriented memories and column multiplexing | reveal (cell), stepper (read, write), scrolly (array access) | approved |
| 3 | Memory variants (`variants`) | 3.1 Multi-port memories and register files · 3.2 ROM · 3.3 FPGA memories: block RAM and LUT RAM, synchronous vs asynchronous read · 3.4 DRAM (1T1C cell) and flash in brief | tabs, table, timing picture | approved |
| 4 | The functional model and cell faults (`cell-faults`) | 4.1 The reduced functional model: address decoder, cell array, read / write logic · 4.2 Stuck-at faults · 4.3 Transition faults · 4.4 Stuck-open and data-retention faults | stepper (faulty-cell state diagrams), categorize | approved |
| 5 | Coupling faults (`coupling`) | 5.1 Aggressor and victim · 5.2 Inversion, idempotent and state coupling (CFin, CFid, CFst) · 5.3 Inter-word and intra-word coupling · 5.4 Neighbourhood pattern-sensitive faults (NPSF) | stepper (an aggressor write flips the victim), reveal (neighbourhood) | approved |
| 6 | Address-decoder and read/write faults (`decoder-rw`) | 6.1 The four address-decoder faults · 6.2 Read-disturb faults: RDF, DRDF, IRF · 6.3 Write-disturb and sense-amplifier faults | stepper (AF1–AF4), stepper (read disturb), table | approved |
| 7 | Fault primitives and what comes next (`fault-primitives`) | 7.1 Fault-primitive notation ⟨S/F/R⟩ · 7.2 Static, dynamic and linked faults · 7.3 Which operations detect which faults — the bridge to March tests | stepper (FP notation), tabs, categorize, table, flip-cards | **in review** |

Follow-up material: training *March tests* (next), Lab L3 (faulty-memory model and fault injection, future).
