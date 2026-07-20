# Epistack — Compact workflow specification

*Extracted verbatim from the v3.2 proposal (Appendix B). Referenced as a standalone artifact so an FLF reviewer can cite the workflow specification directly.*

## Appendix B — Compact specification

~~~text
INPUT
  narrow question
  versioned source records with provenance
  two or more reviewers using the shared verdict contract

1. preserve each raw judgment before synthesis
2. extract a concrete claim responsive to the common question
3. label each judgment supports | challenges | insufficient_evidence
4. attach the cited files and decision-changing evidence
5. allow an analyst to revise or reject the extracted claim
6. trace important support through typed documentary relationships
7. require exact passages for every recorded relationship
8. publish the crux card, lineage map, missing-evidence note, and revisions

IF JUDGMENTS ALIGN
  map conditional defenses and shared assumptions
  do not manufacture a dispute

IF THE RECORD CANNOT SUPPORT A CLAIM
  return insufficient_evidence and identify what is missing
~~~

---

For the full workflow rationale, case runs, evidence, and limitations, see [README.md](README.md).

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [LICENSE](LICENSE).
