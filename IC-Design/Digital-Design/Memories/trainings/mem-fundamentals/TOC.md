# Memory Fundamentals — Table of contents (version 2)

Status: **draft for review**.
Audience: bachelor students with digital logic and basic SystemVerilog. About 10 hours, 3 weeks. Each topic ends with a quiz.
Rule: every topic first explains the concept with diagrams, animations and waveforms, then ends with a separate
**"In SystemVerilog"** subsection. All code was compiled and simulated with Verilator.

| # | Topic (id) | Concept subsections | In SystemVerilog | Interactive / visual |
|---|---|---|---|---|
| 1 | Why memory matters (`why-memory`) | storage in a digital system · hierarchy · processor–memory gap · locality and AMAT | register array vs RAM | stepper (hierarchy), stepper (locality), categorize |
| 2 | Memory types (`types`) | how each memory stores a bit · volatile / non-volatile · choosing | ROM with case and $readmemh | reveal (six cells), tabs, table, categorize |
| 3 | Organisation and address mapping (`organisation`) | system address map · byte address → region, bank, word, byte · depth / width / address bits · rows, columns, column mux · banks and interleaving · width and depth expansion | sp_ram, address decoder, field split, row/col, bank select, ram_64x1k, ram_16x4k | reveal (address map), stepper (address fields), stepper (address split), stepper (banking vs interleaving), stepper (expansion), categorize, sort |
| 4 | Inside a memory: register-level read and write (`register-level`) | decoder + registers + read mux · the write process · the read process (async / sync) · waveforms | structural memory and behavioural equivalent | stepper (write), stepper (read), waveform, accordion |
| 5 | The synchronous memory interface (`sync-interface`) | signals · read latency 1 / 2 · byte enables · read-during-write · async vs sync read | sp_ram_lat, sp_ram_be, three read-during-write variants, async read | stepper (waveforms), svg (byte enables), stepper (read-during-write), categorize |
| 6 | Multi-port memories (`multi-port`) | port types · inside a multi-port memory · register files and bypass · collisions · dual-clock memories | sdp_ram, tdp_ram, regfile_2r1w, collision assertion | svg (port types), svg (8T cell, register file), stepper (bypass), waveform (collisions), categorize |
| 7 | FIFOs (`fifo`) | why FIFOs · ring buffer and pointers · full / empty with a wrap bit · almost-full, FWFT · waveforms · asynchronous FIFO overview | sync_fifo | stepper (ring buffer), waveform, svg (async FIFO), categorize |
| 8 | ECC memory modules (`ecc-memory`) | why ECC · the ECC memory module (encoder, check bits, decoder, ce / ue) · worked example: Hamming check bits and syndrome by hand · overhead and organisation · counters and scrubbing | secded32_pkg, secded32_enc, secded32_dec, ecc_ram (verified on all 39 single and 741 double errors) | stepper (write / read / correct / detect), stepper (encoding 4 data bits), stepper (syndrome decoding), svg (XOR trees), tables, categorize |
| 9 | Memory controllers and AMBA (`controllers-amba`) | jobs of a memory controller · memories on an SoC bus · the AMBA family at a glance · APB and AXI handshakes | apb_sram (APB4 slave with byte strobes and error response) | svg (SoC bus), table, stepper (handshakes), sort |
| 10 | Metrics (`metrics`) | latency / cycle time · bandwidth · area · energy · retention and endurance | — | svg (latency chart), sort |
| 11 | Timing and datasheets (`timing`) | setup / hold / tCQ · datasheet · asynchronous SRAM | behavioural model with timing checks; self-checking testbench | stepper (macro timing), stepper (async cycles), flip-cards |

Notes for reviewers: datasheet numbers are illustrative; energy figures after M. Horowitz (ISSCC 2014, 45 nm).
Follow-up: *SRAM in Depth*; *Designing with Memories* (async FIFO in depth, caches); *Error-Correcting Codes* (code theory); the AMBA trainings in Interfaces/AMBA; labs M1, M3, M5.
