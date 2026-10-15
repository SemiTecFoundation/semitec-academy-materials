# March Tests — Table of contents

Status: **draft for review** — all topics built together, to be reviewed one by one.
Audience: bachelor students who finished *BIST Foundations* and *Memories and Their Faults*. About 4 hours, 2 weeks. Each topic ends with a quiz.

| # | Topic (id) | Subsections | Interactive blocks | Status |
|---|---|---|---|---|
| 1 | March notation (`notation`) | 1.1 From fault models to an algorithm · 1.2 Reading March notation · 1.3 How one element runs · 1.4 Test length kN | stepper (notation anatomy), stepper (one element on 4 cells), sort | **in review** |
| 2 | First March tests (`first-tests`) | 2.1 MATS, MATS+, MATS++ · 2.2 Watch a test miss — and catch — a fault · 2.3 March X and inversion coupling | tabs, stepper (TF↓ escapes MATS+, caught by MATS++), table, categorize | **in review** |
| 3 | March C− and proving coverage (`march-c`) | 3.1 The six elements · 3.2 Proving coverage: idempotent coupling · 3.3 Why every element is needed | stepper (elements), table (8 CFid cases), accordion, sort | **in review** |
| 4 | Tests for newer fault models (`new-faults`) | 4.1 What March C− misses · 4.2 March SS · 4.3 Linked and dynamic faults · 4.4 The ladder of March tests | table, stepper (one March SS element), tabs, svg (ladder), sort | **in review** |
| 5 | Words, backgrounds and other tests (`words-other`) | 5.1 Word-oriented memories and data backgrounds · 5.2 Checkerboard · 5.3 Retention tests · 5.4 GALPAT and walking patterns | svg (backgrounds), stepper (checkerboard), table | **in review** |
| 6 | Choosing a test (`choosing`) | 6.1 Test time versus coverage · 6.2 Production, power-on and diagnosis · 6.3 From algorithm to hardware | table, categorize, flip-cards | **in review** |

Coverage claims in the tables were checked with a small fault simulator (single faults, memory of 6 cells, all aggressor/victim positions).

Follow-up material: training *MBIST Architecture* (next), Lab L4 (March tests on a faulty-memory model, future).
