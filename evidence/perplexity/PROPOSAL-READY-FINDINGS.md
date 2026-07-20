# Proposal-ready findings from the Deep Research comparison

## Suggested core passage

We gave Perplexity Deep Research the same COVID question and the same ten-source starting corpus. We also asked it directly to name the claim carrying its conclusion and to check whether the sources behind that claim were independent. The output we received was a useful 258-word synthesis. It named ascertainment bias as the hinge and noticed shared authorship and debate ancestry among several sources.

It also showed why a structured lineage check matters. Deep Research said three papers shared "a single case dataset." They do share authors, but not one dataset: one studies December case locations, another uses early viral genomes and epidemic simulations, and the third analyzes genomic features. The returned answer supplied no source spans or source-use table with which to inspect that relationship. A person following the Epistack workflow would record **shared authorship** as the relationship, attach the supporting bylines, and leave the distinct data sources intact.

This is not an overall win for Epistack. Deep Research produced the better single narrative and found the hinge when asked. Epistack changes the form of the work: AI reviews remain separate, and a person records the hinge and the lineage of its support in a case record that another reader can challenge and revise. Our current artifacts demonstrate separate judgments, corpus provenance, an acceptance target, and a manual source-lineage correction. They do not establish that this workflow produces better answers in general.

## Compact comparison table

| Same COVID question and ten-source starting corpus | Perplexity Deep Research, one instructed run | Epistack evidence supplied with this submission |
|---|---|---|
| Readable answer | Strong, concise synthesis | Separate reviews rather than one final narrative |
| Names the hinge | Yes, after being asked directly | A person names it; the local mechanical demonstration missed the COVID target |
| Checks source lineage | Found useful relationships, but merged shared authorship into a false shared-dataset claim | A person demonstrated a source-spanned lineage correction on the LHC case |
| Makes the check inspectable | The returned answer had no claim-linked spans or source-use table | Hashed corpus and raw judgments exist; the proposed case record keeps relationship types and supporting spans |
| What remains unproved | The single run does not establish typical Deep Research behavior | The supplied work does not establish general uplift or an automated end-to-end method |

## Required caveats

- Call this a genuine `pplx_deep_research` run, not the earlier `pplx_best` baseline.
- Say "the output we received," not "Perplexity Deep Research never provides," because the local tool returned only a summary and URL list.
- State that the prompt explicitly requested hinge and dependency analysis. Do not imply that these appeared unprompted.
- Do not use Perplexity's 65–80% figure as a scientific result; the returned record did not show how it was calibrated.
- Do not claim a win, benchmark result, or typical behavior from one run.
- Describe Epistack as a human-AI workflow: AI produces separate source-cited reviews; a person identifies the load-bearing claim and checks lineage.

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
