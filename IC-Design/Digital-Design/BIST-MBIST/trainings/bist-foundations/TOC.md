# BIST Foundations: Why Chips Test Themselves — Table of contents

Status: **draft for review**. Each topic is built and reviewed one at a time; a topic file is added to
`training.json` → `topics` when it is approved.

Audience: bachelor students (digital logic, an HDL). About 4 hours, 2 weeks. Each topic ends with a quiz
(4–6 questions, each linked back to the subsection that teaches it).

| # | Topic (id) | Subsections | Interactive blocks | Status |
|---|---|---|---|---|
| 1 | Why test chips? (`why-test`) | 1.1 Defects, faults and failures · 1.2 Yield and the cost of a test escape · 1.3 How chips are tested today (ATE, wafer sort, final test) | reveal (defects on a die), stepper (rule of ten), scrolly (test flow) | approved |
| 2 | Why external test is not enough (`why-bist`) | 2.1 The pin and tester-memory bottleneck · 2.2 At-speed defects · 2.3 Buried memories · 2.4 The BIST idea: generator, circuit under test, analyser, controller | animation (pins vs flip-flops), tabs, reveal (SoC with memories), stepper | approved |
| 3 | BIST over a chip's life (`bist-lifetime`) | 3.1 Manufacturing test and burn-in · 3.2 Power-on and periodic test, functional safety (ISO 26262) · 3.3 What BIST costs: area, power, timing, effort | scrolly (chip life), categorize (benefits / costs) | approved |
| 4 | LFSR: patterns made on chip (`lfsr`) | 4.1 Shift register with XOR feedback (Fibonacci) · 4.2 The Galois form · 4.3 Polynomials, primitive polynomials, maximal length 2ⁿ−1, the lock-up state · 4.4 Seeds and pseudo-random patterns | step animation of a 4-bit LFSR, tabs (Fibonacci / Galois), sort (state sequence) | approved |
| 5 | Compacting responses: MISR (`misr`) | 5.1 Why compact responses · 5.2 Signature analysis as polynomial division · 5.3 The MISR · 5.4 Aliasing and unknown (X) values | stepper (division), animation (MISR), accordion | approved |
| 6 | A tiny BIST, end to end (`tiny-bist`) | 6.1 The BIST controller FSM · 6.2 The golden signature · 6.3 Walk-through: LFSR → circuit → MISR, and a fault changing the signature · 6.4 What comes next: MBIST and LBIST | fsm picture, scrolly walk-through | **in review** |

Follow-up material: Lab L1 (LFSR in SystemVerilog), Lab L2 (MISR and aliasing), video "LFSR in motion".
