# Audited comparison: Perplexity Deep Research and the current Epistack evidence

## Bottom line

The genuine Perplexity Deep Research call did something important: after an explicit instruction, it named the central dispute in concrete language—whether the geographic pattern reflects transmission or ascertainment bias. It also attempted a source-dependency analysis and named three relationship groups.

The returned product is not the requested full report. It is a 258-word summary plus fifteen search results. It provides no source table, no sentence-level citation map, no supporting spans for its dependency claims, and no method for its 65–80% confidence range. One dependency claim is materially too broad: sources 1–3 do share authors, but the supplied source texts do not use "a single case dataset." Source 1 analyzes December case locations from the WHO mission report; source 2 analyzes early viral genomes, phylodynamic models, and simulations; source 3 analyzes viral genomic features. Shared authorship is established. One shared case dataset across all three is not.

This result narrows the honest case for Epistack. Deep Research can name a hinge and can notice source relationships when directly instructed. The value of the Epistack workflow cannot rest on a claim that deep research is unable to do either. The stronger distinction is the **research process and record**: AI produces separate source-cited reviews; a person compares them to identify the load-bearing claim, checks the lineage of its support, and preserves the judgments, warrants, typed dependency edges, and revisions in a versioned case record. The supplied tools support parts of that process; they do not automate the person's analysis.

## What actually ran

The raw transcript records a call to `mcp__perplexity__pplx_deep_research`, whose local registry identifies model `perplexity/deep-research` and mode `research`. This is genuine Perplexity Deep Research through the already provisioned local MCP, not the earlier `pplx_best` call. The call ran once from `00:09:39Z` to `00:12:19Z` on 2026-07-20 UTC and returned conversation UUID `68c791f3-b53c-4e01-b741-8d6bd130629d`.

No new authentication was attempted. No fallback model or second Perplexity tool was called.

## Predeclared-field audit

| Predeclared field | Deep Research result | Evidence status |
|---|---|---|
| Genuine Deep Research mode | Yes: distinct tool call and local registry identify `perplexity/deep-research`, mode `research` | Supported by raw transcript and installed model registry |
| Ten fixed sources used | The answer discusses sources 1–7 and 10, says 4 and 8 were inaccessible, and is silent about substantive use of 9; the returned structure has no source-use table | Partial; complete use cannot be verified |
| Added sources marked | Fifteen search results were returned, but the answer marks only one as an "added preprint" and does not separate all additions | Incomplete |
| Direct answer | Market-associated zoonotic origin is described as better supported, at 65–80% confidence | Present; numerical calibration is not established by the returned record |
| Spatial evidence separated from full origin inference | Yes: unusual geographic pattern versus probable but unproven zoonotic origin | Present |
| Load-bearing claim | Whether the geographic signal is causal or an ascertainment artifact | Concrete and useful |
| Strongest alternative explanation | Ascertainment bias is named; prior human transmission is not developed as a causal account | Partial |
| Evidence that would change the conclusion | The answer mentions unresolved host identity and one-versus-two introductions, but does not state a clear decision-changing observation | Missing |
| Source dependencies | Shared authorship among 1–3; reply relationship between 5 and an added preprint; Rootclaim debate relationship among 6, 7, and 10 | Present but not source-spanned; one claim overstates shared data |
| Claim-linked citations | Fifteen URLs and snippets are returned separately | Missing |
| Requested ten-source table | Not returned | Missing |

## The dependency claims, checked

### Sources 1–3

**Supported:** The three papers share authors. The locally harvested XML lists Andersen, Rambaut, Holmes, and Garry on sources 1 and 3, and those four plus other overlapping authors on source 2. Shared authorship means three papers should not automatically be treated as three wholly independent research teams.

**Not supported:** The phrase "a single case dataset." The supplied source texts identify different central evidence:

- Source 1 uses December 2019 case locations from the WHO mission report, market environmental samples, wildlife-sale evidence, population and mobility data.
- Source 2 uses 787 early viral genomes, phylogenetic rooting, phylodynamic models, and epidemic simulations, with some epidemiological context.
- Source 3 examines genomic features of SARS-CoV-2 and related coronaviruses. It predates the two 2022 market papers.

The sources overlap in authors and broad subject matter. The supplied materials do not establish that all three rest on one case dataset.

### Source 5 and the added preprint

The returned answer identifies a direct criticism-and-response relationship between Stoyan and Chiu's statistical critique and an added Worobey-team preprint. The returned search list includes both the critique and "Confirmation of the centrality of the Huanan market." This is a meaningful lineage relationship, but the result provides no quoted or located spans showing which claims the response addresses.

### Sources 6, 7, and 10

These sources are related: Rootclaim's analysis supplied the disputed model, the Astral Codex Ten piece reviewed the Rootclaim–Miller debate, and Rootclaim's later post reported and answered the debate result. Treating them as three independent confirmations would be wrong. Calling them simply "the same debate," however, compresses distinct roles: an underlying analysis, an outside judgment, and a participant's response. Dependency is established; equivalence is not.

## Head-to-head findings

| Task | Perplexity Deep Research, this run | Current Epistack evidence |
|---|---|---|
| Names the concrete COVID hinge | Yes, after the prompt explicitly requests it | The human-authored acceptance oracle names it; the local mechanical detector missed it, passing two of five oracle checks |
| Produces a readable substantive answer | Yes, though only as a short summary | Produces separate reviewer judgments rather than one integrated answer |
| Preserves distinct judgments | No; returns one synthesis | Yes; raw source-sliced judgments are preserved, with known retrieval and role-design limits |
| Audits source independence | Attempts it and finds useful relationships; one data-sharing claim is overbroad | A person demonstrated the check on the LHC case; the supplied workflow does not automate it |
| Makes dependency claims inspectable | No claim-to-source spans or typed edges | The LHC manual record supplies source-line citations; the proposed case format preserves typed edges for challenge and revision |
| Exposes the strongest alternative and decision-changing evidence | Partial | The human-authored acceptance oracle defines this target; the local mechanical detector did not meet it |
| Documents corpus provenance | Returned answer does not provide a source-use table | Ten-source manifest has URLs, retrieval timestamps, local files, and SHA-256 hashes |
| Supports correction and extension | Conversation UUID exists, but the returned artifact is a flat summary and URL list | Versioned artifacts and raw judgments exist; full challenge/revision workflow remains proposed |

## What belongs in the proposal

The comparison supports these restrained claims:

1. A genuine Deep Research run on the same question and fixed starting corpus produced a concise, useful synthesis and named the ascertainment-bias hinge after the prompt explicitly asked for it.
2. When explicitly asked, Deep Research also identified real source relationships. Therefore Epistack should not claim that source-lineage awareness is unique to it.
3. The result also shows the problem Epistack is intended to address: a dependency claim arrived without supporting spans and collapsed shared authorship into a false claim of one shared case dataset. A person following the Epistack workflow would record the relationship type and its supporting source spans, making the claim challengeable instead of accepting it as part of a fluent synthesis.
4. Epistack's current evidence advantage is inspectability—hashed corpus provenance, separate raw judgments, an acceptance oracle, and a manually sourced LHC lineage record—not a demonstrated overall research-quality advantage.
5. This is one instructed run. It does not establish typical Perplexity behavior or comparative superiority.

The proposal should not repeat the returned 65–80% confidence figure as a scientific finding. The returned record supplies neither a calibration procedure nor claim-linked evidence for that range.

## Preserved records

- `PREDECLARED-PROTOCOL.md` — frozen comparison design
- `EXACT-PROMPT.md` — exact substantive prompt
- `RETURNED-RESULT.md` — readable returned fields and mode evidence
- `RAW-CLAUDE-MCP-TRANSCRIPT.jsonl` — complete native-Claude/MCP transcript, including exact tool input and raw tool result

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
