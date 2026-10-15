# Test Access: JTAG and IJTAG — Table of contents

Status: **draft for expert review** — all topics built together.
Audience: bachelor students who finished *BIST Foundations* and *MBIST Architecture*. About 5 hours, 2 weeks. Each topic ends with a quiz.

| # | Topic (id) | Subsections | Interactive blocks | Status |
|---|---|---|---|---|
| 1 | Why chips need test access (`why-access`) | 1.1 Many instruments, few pins · 1.2 The standards (1149.1, 1500, 1687, related) · 1.3 Serial access | svg (pins and instruments), table, sort, stepper (shift register) | **in review** |
| 2 | The JTAG test access port (`tap`) | 2.1 TAP signals · 2.2 Inside the TAP · 2.3 The 16-state controller · 2.4 Capture, shift, update · 2.5 Control signals to the registers | table, svg (TAP architecture), stepper (TAP state machine), categorize, reveal (one register bit), stepper (capture-shift-update on 3 bits), svg (control waveform) | **in review** |
| 3 | Instructions and data registers (`registers`) | 3.1 Instructions · 3.2 BYPASS and IDCODE · 3.3 TMS sequences · 3.4 Several chips in one chain | table, svg (IDCODE fields), svg (TMS waveform), sort, table (chain lengths) | **in review** |
| 4 | Boundary scan (`boundary-scan`) | 4.1 Boundary-scan cells · 4.2 Testing a board · 4.3 How many patterns · 4.4 BSDL | table, stepper (EXTEST: short and open), table, code | **in review** |
| 5 | IEEE 1500: wrapping cores (`ieee1500`) | 5.1 Why wrap cores · 5.2 The wrapper at a glance · 5.3 The wrapper serial port (WSI, WSO, WRCK, WRSTN, SelectWIR, Capture/Shift/UpdateWR) · 5.4 The wrapper boundary cell · 5.5 Instructions and test modes · 5.6 Parallel port, control from the TAP, CTL | svg (SoC with wrapped cores), svg (wrapper), table, svg (WSP waveform), categorize, reveal (wrapper cell), accordion, stepper (WIR selects the path), svg (WPP) | **in review** |
| 6 | IEEE 1687: networks of instruments (`ijtag`) | 6.1 Why a network · 6.2 The instrument's scan interface · 6.3 Segment insertion bits · 6.4 Scan muxes and hierarchy · 6.5 Connecting the network to the TAP · 6.6 Access time | accordion, svg (instrument interface), table, stepper (SIB path), svg (SIB = register + ScanMux), svg (hierarchy), sort, table | **in review** |
| 7 | ICL and PDL (`icl-pdl`) | 7.1 ICL: describing the network · 7.2 PDL: operating an instrument · 7.3 iApply: few scans for many requests · 7.4 Retargeting | table, code (SIB and TDR in ICL), table (PDL commands), code, categorize, stepper (iApply), svg (retargeting), sort | **in review** |
| 8 | Running MBIST through IJTAG (`mbist-access`) | 8.1 The controller's register · 8.2 One run step by step · 8.3 How long to wait · 8.4 Many controllers, field access, security | svg (TDR fields), stepper (JTAG run timeline), code (PDL), accordion, flip-cards | **in review** |

Notes for reviewers: ICL/PDL and BSDL snippets are simplified illustrations; MBIST register fields are generic, not from a specific tool.

Follow-up material: training *Memory Repair* (next); Lab: JTAG TAP controller in SystemVerilog (future).
