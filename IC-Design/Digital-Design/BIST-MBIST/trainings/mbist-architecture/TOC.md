# MBIST Architecture — Table of contents

Status: **draft for review** — all topics built together, to be reviewed one by one.
Audience: bachelor students who finished *Memories and Their Faults* and *March Tests*. About 4 hours, 2 weeks. Each topic ends with a quiz.

| # | Topic (id) | Subsections | Interactive blocks | Status |
|---|---|---|---|---|
| 1 | MBIST in a chip (`overview`) | 1.1 The big picture · 1.2 What each part does · 1.3 One test run, end to end · 1.4 Design choices | reveal (SoC), table, stepper (run timeline), sort, svg (dedicated vs shared), tabs | **in review** |
| 2 | The memory collar (`collar`) | 2.1 Muxes: functional and test paths · 2.2 Where to compare · 2.3 Bypass for logic test · 2.4 At-speed timing | stepper (collar), svg (local vs central compare), accordion, categorize, stepper (pipeline) | **in review** |
| 3 | Address and data generators (`generators`) | 3.1 The address counter · 3.2 Address order and scrambling · 3.3 The data generator · 3.4 Write masks and wide words | stepper (address generator), stepper (visiting order, scrambling), svg (data patterns), table, sort, accordion | **in review** |
| 4 | The MBIST controller (`controller`) | 4.1 A March test as nested loops · 4.2 A hard-wired controller · 4.3 A programmable controller · 4.4 Hard-wired or programmable? | stepper (loops), code, stepper (MATS+ state machine), stepper (programmable controller), sort, tabs | **in review** |
| 5 | Results and diagnosis (`results`) | 5.1 Comparators and the fail flag · 5.2 Go/no-go and diagnosis modes · 5.3 Failure bitmaps · 5.4 ROM: signatures instead of compares | stepper (results path), table, svg (failure bitmaps), categorize, svg (ROM + MISR) | **in review** |
| 6 | Special memories (`special`) | 6.1 Memories with ECC · 6.2 Multi-port memories and register files · 6.3 Clocks and at-speed operation | stepper (ECC test), table, accordion, svg (clock domains), categorize | **in review** |
| 7 | Integration in a chip (`integration`) | 7.1 Sharing controllers · 7.2 Scheduling under a power budget · 7.3 The insertion flow · 7.4 Area cost and what comes next | table, svg (floorplan grouping), svg (schedule), stepper (insertion flow), sort, flip-cards | **in review** |

Follow-up material: training *Test Access: JTAG and IJTAG* (next), *Memory Repair*; Lab L5 (MBIST controller in SystemVerilog, future).
