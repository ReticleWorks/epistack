*Epistack*

# How Many Voices Is This Really?

## Finding the claim a contested conclusion rests on—and testing whether its support is as independent as it looks

<svg role="img" viewBox="0 0 900 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;">
  <title>Epistack workflow: six stages from a narrow question to a versioned case record</title>
  <desc>A horizontal flow of six stages. Stage 1, narrow question, stands alone. Stages 2 and 3, traceable corpus and separate judgments, are grouped as Atlas, the existing toolkit. Stages 4 and 5, crux extractor and typed relationships, are grouped as what Epistack adds. Stage 6, versioned case record, is the output.</desc>
  <defs>
    <marker id="epi-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <path d="M160,90 L160,72 L440,72 L440,90" fill="none" stroke="currentColor" stroke-opacity="0.45" stroke-width="1.2"/>
  <text x="300" y="60" text-anchor="middle" font-size="12" fill="currentColor" fill-opacity="0.75">Atlas (existing toolkit)</text>
  <path d="M460,90 L460,72 L740,72 L740,90" fill="none" stroke="#08645f" stroke-width="1.2"/>
  <text x="600" y="60" text-anchor="middle" font-size="12" fill="#08645f" font-weight="600">Epistack adds</text>
  <line x1="140" y1="120" x2="157" y2="120" stroke="currentColor" stroke-width="1.4" marker-end="url(#epi-arrow)"/>
  <line x1="290" y1="120" x2="307" y2="120" stroke="currentColor" stroke-width="1.4" marker-end="url(#epi-arrow)"/>
  <line x1="440" y1="120" x2="457" y2="120" stroke="currentColor" stroke-width="1.4" marker-end="url(#epi-arrow)"/>
  <line x1="590" y1="120" x2="607" y2="120" stroke="currentColor" stroke-width="1.4" marker-end="url(#epi-arrow)"/>
  <line x1="740" y1="120" x2="757" y2="120" stroke="currentColor" stroke-width="1.4" marker-end="url(#epi-arrow)"/>
  <g>
    <rect x="10" y="90" width="130" height="60" rx="6" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.4"/>
    <circle cx="28" cy="104" r="9" fill="none" stroke="currentColor" stroke-opacity="0.6"/>
    <text x="28" y="107" text-anchor="middle" font-size="10" fill="currentColor">1</text>
    <text x="75" y="123" text-anchor="middle" font-size="11" fill="currentColor">Narrow</text>
    <text x="75" y="137" text-anchor="middle" font-size="11" fill="currentColor">question</text>
  </g>
  <g>
    <rect x="160" y="90" width="130" height="60" rx="6" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.4"/>
    <circle cx="178" cy="104" r="9" fill="none" stroke="currentColor" stroke-opacity="0.6"/>
    <text x="178" y="107" text-anchor="middle" font-size="10" fill="currentColor">2</text>
    <text x="225" y="123" text-anchor="middle" font-size="11" fill="currentColor">Traceable</text>
    <text x="225" y="137" text-anchor="middle" font-size="11" fill="currentColor">corpus</text>
  </g>
  <g>
    <rect x="310" y="90" width="130" height="60" rx="6" fill="currentColor" fill-opacity="0.06" stroke="currentColor" stroke-opacity="0.4"/>
    <circle cx="328" cy="104" r="9" fill="none" stroke="currentColor" stroke-opacity="0.6"/>
    <text x="328" y="107" text-anchor="middle" font-size="10" fill="currentColor">3</text>
    <text x="375" y="123" text-anchor="middle" font-size="11" fill="currentColor">Separate</text>
    <text x="375" y="137" text-anchor="middle" font-size="11" fill="currentColor">judgments</text>
  </g>
  <g>
    <rect x="460" y="90" width="130" height="60" rx="6" fill="#08645f" fill-opacity="0.14" stroke="#08645f" stroke-width="1.2"/>
    <circle cx="478" cy="104" r="9" fill="none" stroke="#08645f"/>
    <text x="478" y="107" text-anchor="middle" font-size="10" fill="#08645f">4</text>
    <text x="525" y="123" text-anchor="middle" font-size="11" fill="currentColor">Crux</text>
    <text x="525" y="137" text-anchor="middle" font-size="11" fill="currentColor">extractor</text>
  </g>
  <g>
    <rect x="610" y="90" width="130" height="60" rx="6" fill="#08645f" fill-opacity="0.14" stroke="#08645f" stroke-width="1.2"/>
    <circle cx="628" cy="104" r="9" fill="none" stroke="#08645f"/>
    <text x="628" y="107" text-anchor="middle" font-size="10" fill="#08645f">5</text>
    <text x="675" y="123" text-anchor="middle" font-size="11" fill="currentColor">Typed</text>
    <text x="675" y="137" text-anchor="middle" font-size="11" fill="currentColor">relationships</text>
  </g>
  <g>
    <rect x="760" y="90" width="130" height="60" rx="6" fill="#08645f" fill-opacity="0.22" stroke="#08645f" stroke-width="1.6"/>
    <circle cx="778" cy="104" r="9" fill="#08645f"/>
    <text x="778" y="107" text-anchor="middle" font-size="10" fill="#fff">6</text>
    <text x="825" y="123" text-anchor="middle" font-size="11" fill="currentColor" font-weight="600">Versioned</text>
    <text x="825" y="137" text-anchor="middle" font-size="11" fill="currentColor" font-weight="600">case record</text>
  </g>
</svg>

*The Epistack workflow: six stages producing an inspectable, versioned case record.*

## Introduction

A map of the earliest known COVID-19 cases in Wuhan shows a cluster around the Huanan Seafood Market. One reader sees strong evidence that the outbreak began at or near the market. Another asks whether clinicians were more likely to find early cases near a place already suspected. The dots are the same. The disagreement is about what those dots can bear as evidence.

Now suppose five papers support the market interpretation. That sounds like five separate confirmations. But some may share authors, draw on the same data, respond to one another, or repeat an earlier analysis. Counting citations cannot tell us whether we have five independent reasons to believe something or one family of related work wearing five covers.

Epistack is a human–AI research workflow built to answer two questions:

- What specific claim is carrying a contested conclusion?
- How independent is the support behind that claim?

Epistack begins by asking several AI reviewers to answer the same narrow question. They draw from a traceable source record, sometimes through different assigned slices. Each reviewer states its position, reasons, cited sources, counter-evidence, and the evidence that could change its judgment. Their answers remain separate rather than being blended into one summary.

Keeping those judgments separate exposes the point at which their reasoning differs. Epistack calls this the **load-bearing claim**: the assertion whose evidentiary weight changes the answer. A comparison component proposes that claim and records how each judgment bears on it. An analyst can accept, revise, or reject the proposal.

Once that claim is visible, the second question becomes concrete: what stands behind it? Sources may be connected through citations, shared authors, shared data, advice, institutions, methods, or assumptions. Epistack records each documented connection as a typed relationship tied to its supporting passage. “These papers share an author” is different from “these papers use the same data.” The workflow does not silently substitute one for the other.

The result is not another essay arguing for one answer. It is a versioned case record: the separate judgments, the proposed load-bearing claim, a map of its documented support, the evidence most likely to change the picture, and a history of corrections. Another investigator can challenge or replace one part without recreating the entire inquiry.

We exercised this workflow on two cases chosen to test different demands. COVID origins remain disputed, so it tests whether the workflow can expose a contested load-bearing claim. The safety conclusion concerning the Large Hadron Collider is largely settled, but its supporting argument is technically layered. It tests whether the workflow can preserve a conditional argument and inspect relationships among its sources without manufacturing a dispute. We also gave the COVID question and the same starting sources to Perplexity Deep Research under a predeclared protocol. The comparison concerns the records the two processes produced; one run cannot establish overall superiority.

## The LHC case: a layered argument and its documentary relationships

The LHC case was not a new safety assessment. It asked whether Epistack could preserve a technically deep, largely settled argument without turning it into a false controversy. The work had two parts: map the conditional safety argument, then examine how the six documents supporting it are related.

### The safety argument

Direct reading of the six-source record produced this conditional structure:

~~~text
Standard physics does not expect dangerous black-hole production.
│
└─ If speculative production occurs:
   ├─ Expected result: rapid Hawking evaporation.
   │
   └─ If a microscopic black hole is stable:
      ├─ If charged, cosmic-ray analogues should be trapped in Earth or the Sun.
      └─ If effectively neutral, dense stars should trap analogues;
         the continued existence of old white dwarfs and neutron stars
         constrains dangerous accretion scenarios.
~~~

The official 2008 safety report expressly considers the possibility that Hawking evaporation is wrong and points to astrophysical arguments that do not depend on it. The Giddings–Mangano paper develops those arguments through cosmic-ray collisions, accretion models, and the survival of compact stars. The supplied record contains no numerical probability for the joint failure of these defenses. Epistack therefore records a conditional argument structure, not a catastrophe estimate.

### The documentary relationships

The six documents also contain relationships worth tracing separately from the physics. Michelangelo Mangano is an author of both the official safety report and the main paper developing the alternative safety arguments. That paper thanks the other four report authors, among others, for guidance and advice. The official report cites it for detailed accretion scenarios. Its acknowledgments also identify outside specialists consulted on narrower questions about accretion and compact stars.

These facts justify closer inspection of how separate the report and its principal supporting paper are. They do not establish that the documents share data, contain invalid reasoning, reflect every adviser’s endorsement, or wholly depend on one another.

The complete relationship picture came from a source-directed audit of the six documents. The audit compared bylines, acknowledgments, citations, and roles in the argument, with every recorded relationship tied to a source location. The automated panel did not produce the complete picture.

### What the software produced

The LHC retrieval stage stored 102 passages. In the initial run, passages from the same file shared one identifier. A filtering step therefore treated passages from one document as duplicates, and each reviewer retained only two passages.

A run-specific identity correction allowed each reviewer to retain twelve passages without changing the question, source allocation, ranking, or the six baseline passages. The additional evidence included the two bylines needed to establish that Mangano appeared on both documents. The completed judgments did not connect those bylines. The adviser acknowledgment was still absent from the retrieved passages, and the evidence checker declined to return a third judgment.

The result separates retrieval from comparison. The software can place relevant facts in the evidence record without connecting them across documents. Here, the panel showed that better passage retention could expose both bylines. The full authorship, advice, citation, and outside-specialist picture came from the six-document audit. The case did not demonstrate general automated authorship or advice detection.

## How Epistack is implemented

Epistack combines existing research functions around a common case record. Some collect and preserve sources. Some find relevant passages and produce separate judgments. A deterministic comparison component proposes the load-bearing claim. Other implemented facilities follow citations and organize source relationships. For relationships those facilities do not encode, the case record requires a typed relationship and its supporting passage. Each function leaves an inspectable artifact, so a later investigator can see where a result came from and where a later stage stopped.

### Source harvesting and records

The source-harvest workflow searches for material, retrieves documents, records failures and exclusions, and stores a file fingerprint. A fingerprint is calculated from a file’s contents; if the file changes, its fingerprint changes. It lets another investigator confirm that they are reading the same source used in the analysis.

This process produced the ten-source COVID corpus and its retrieval record. The LHC package similarly preserves six source files, a manifest, and file fingerprints, although the supplied materials do not establish that the same gathering process assembled it.

**Atlas** is the existing research toolkit beneath Epistack. It can represent documents, claims linked to their source passages, and named entities such as people and institutions. The two case harnesses preserved documents and passages, but their linked-claim graphs were empty. They demonstrate traceable source assembly and passage storage, not the fuller graph-backed path.

### Atlas retrieval

Atlas searches stored material for passages relevant to a question and supplies selected passages to a configured reviewer. Its \`taste_agent\` component can combine direct passage search with claim-graph and citation context when those stores are populated.

In the COVID and LHC runs, the linked-claim graph was empty, so direct passage search supplied the evidence. A local OpenAI embedding service represented each passage numerically so the software could retrieve passages similar to the question. The cases show Atlas code retrieving preserved passages for separate reviews. They do not show that every retrieval channel or graph link contributed.

### Separate judgments

Atlas’s \`judgment_panel\` asks several configured reviewers the same narrow question and preserves each answer independently. Each judgment can contain a position and confidence range, supporting reasons, cited sources, counter-evidence, limitations, and evidence that could change the judgment. This is the panel structure used in both cases.

The reviewers in these cases were model roles with different source allocations, not independent human experts. Their value here is structural: the record shows who relied on what before a later synthesis can smooth the differences away.

### Checks on generated text

Atlas includes checks intended to catch two common problems in generated research. Its faithfulness check breaks an answer into factual claims and asks whether the retrieved passages support each one. Its uncertainty component records caveats about the source set and retrieval result when assigning a range.

These are diagnostic controls, not measures of truth. In the supplied runs, the support check produced useful refusals and revised outputs, but also parser warnings and truncated text. A single default source label made the uncertainty ranges uninformative about differences in source quality. Those failures remain in the case record.

### Citation-graph retrieval

Atlas also includes \`rag_advisor\`, a citation-focused retrieval service. It records which papers cite which others, can search one citation step beyond an initial source set, and can identify influential papers and clusters of closely connected work.

These are implemented source-relationship facilities. They can show citation connections and help organize a literature. They are not a general service for detecting shared authorship, acknowledged advice, or shared datasets across arbitrary documents. For those relationships, Epistack requires a type and the passage supporting it. In the LHC case, that complete comparison came from the source-directed audit; the panel itself did not produce the authorship and advice finding.

### Load-bearing-claim comparison

The crux extractor is a deterministic reference component: the same input produces the same output. It compares preserved judgments and returns a candidate load-bearing claim, each reviewer’s position, cited sources, disagreement type, and stated change conditions. It runs over preserved panel output and is included in the reference package. On the preserved COVID panel it met all five declared structural and evidentiary checks. Four additional tests include an unrelated clinical-trial case and an abstention case.

This shows that the component emits the required inspectable fields on those tests. It does not prove semantic accuracy across domains. The supplied record does not establish that this version has been merged into the deployed Atlas service.

### Typed relationships and the case record

Atlas and \`rag_advisor\` already represent source, entity, and citation relationships. Epistack’s case record adds explicit types for other documented relationships, including shared authorship, advice, data, institutions, methods, and assumptions. Each accepted relationship must retain the passage supporting it. The supplied software does not contain a general automated service for detecting all of those relationship types.

The intended case record combines the source ledger, separate judgments, extracted claim, typed relationships, missing-evidence requests, objections, and revision history. The supplied package already preserves the corpora, manifests, raw judgments, COVID crux record, LHC support map, and successive corrections. It does not yet provide one consolidated interface for challenging a relationship and recording the response.

### One case proceeds through six stages

1. Narrow a broad topic to a question whose central claim can be supported, challenged, or left unresolved.
2. Build a traceable corpus with stable identifiers, retrieval records, exclusions, and hashes.
3. Use Atlas retrieval to supply evidence to separate reviewers, preserving reasons, citations, counter-evidence, uncertainty, and change conditions.
4. Run the crux extractor to propose the load-bearing claim and record how each judgment bears on it. The proposal remains open to acceptance, revision, or rejection.
5. Trace that claim through citations, data, authors, advice, institutions, methods, and assumptions. Keep the type and exact passage for every accepted relationship.
6. Publish the artifacts as a versioned case record so later sources, objections, corrected relationships, or replacement judgments do not erase the earlier state.

The two case harnesses exercised direct passage search, separate judgments, evidence checking, and the reference claim-comparison component. They did not exercise the linked-claim graph or the citation-following, influence, and clustering facilities inside their panel runs. Those are implemented supporting capabilities, not evidence channels shown to have contributed to these two results.

## What happened on COVID

We harvested ten source documents and preserved their URLs, retrieval records, local files, and SHA-256 fingerprints. Their canonical text totals 69,774 words. The set is deliberately plural, but it is not balanced by source quality: five sources are peer reviewed, and four of those support or synthesize the market or zoonotic account. The remaining material includes statistical criticism, Bayesian analysis, debate commentary, and advocacy. That asymmetry is part of the record.

The ten complete files were divided once among three model-reviewer roles: market and natural-origin evidence, skeptical and lab-origin analysis, and methodological audit. Ingestion stored 94 searchable passages without a recorded insertion error. Each role returned a source-cited judgment.

The market-focused review called the cluster moderately strong but not conclusive evidence that the market was the outbreak’s early center. The skeptical review gave it weak-to-moderate weight because early case-finding and the spatial analysis may have favored the market. The methodological review assigned some weight but found it materially weakened by the same concerns. Across the separate judgments, the practical crux was clear: how much of the observed geographic concentration survives correction for the way early cases were found?

The reviews also named useful missing evidence. The skeptical side emphasized a complete, unbiased early-case series. The market side emphasized direct evidence of a closely related virus in a market animal or its supply chain.

This was a designed comparison, not a survey of expert belief. The three roles received different source slices, so the design helped produce their difference. They also shared model infrastructure and cannot be treated as three independent experts. In the original run, retrieval passed one fact per source into synthesis, and every source received the same default source label. The confidence bands therefore describe the pipeline state, not the standing of the evidence.

The crux extractor ran on the preserved real panel after the reviewers finished. It met all five declared structural and evidentiary checks and produced a concrete, sourced, contestable crux record. This does not establish that the selected claim will be the right one on every case. The preserved judgments and evidence make that selection reviewable.

## Comparison with Perplexity Deep Research

We gave the distinct Perplexity Deep Research tool the same COVID question and the same ten-source starting set. Before the call, we fixed a protocol asking for a direct answer, a load-bearing claim, the strongest alternative, evidence that would change the conclusion, source dependencies, uncertainty, citations, and a source-use table. The prompt did not supply Epistack’s judgments, validation criteria, or conclusions.

The single Deep Research run did something important. It identified the central hinge as whether the geographic signal reflects transmission or ascertainment bias. It also noticed shared authorship and debate ancestry among several sources. Deep Research can therefore find both a useful crux and real source relationships when asked directly. Epistack cannot honestly claim those capabilities are unique.

The output we received was a useful 258-word synthesis plus fifteen URLs, rather than the requested full report and table. It gave no exact passages linked to its claims and no clear decision-changing observation. More importantly, it said that three papers shared “a single case dataset.” Those papers do share authors, but the supplied texts do not support the one-dataset claim: one centrally analyzes December case locations, another uses early genomes and epidemic simulations, and the third analyzes viral genomic features.

That is the kind of error the workflow is designed to expose. Here, a person checked the relationship against the source record, corrected it to **shared authorship**, attached the supporting bylines, and left the distinct evidence types intact. A fluent sentence should not be allowed to collapse one relationship into another.

| Same COVID question and starting sources | Perplexity Deep Research, one instructed run | Epistack evidence supplied here |
|---|---|---|
| Readable answer | Strong, concise synthesis | Separate reviews and a structured comparison rather than one final narrative |
| Names the crux | Yes, after direct instruction | Crux extractor meets all five declared structural and evidentiary checks on the preserved panel |
| Checks source relationships | Found useful relationships; one relationship was overgeneralized | LHC evidence audit records relationship types and exact supporting passages |
| Makes the check inspectable | No exact passages linked to claims or requested source-use table in the output received | Hashed provenance and raw judgments; the LHC analyst map labels relationships and cites exact source locations. The consolidated typed case record remains the specified output |
| What remains unproved | One run does not establish typical product behavior | One case-level extractor pass does not establish general semantic accuracy or overall research superiority |

This is not an overall win for Epistack. Deep Research produced the better single narrative and found the COVID hinge when asked. Epistack produces a different research record: the separate judgments, extracted claim, lineage decisions, exact supporting passages, and corrections remain available for challenge. Whether that record helps people reason better than Deep Research requires a comparative user study that we have not run.

## What another investigator receives

The reusable unit is a versioned case record:

1. **Source ledger:** stable identifiers, source types, retrieval records, exclusions, duplicates, and hashes.
2. **Separate judgments:** each reviewer’s position, warrant, citations, counter-evidence, uncertainty, and change conditions.
3. **Crux card:** the extracted load-bearing claim, alternative candidates, position labels, disagreement type, and the evidence attached to each side.
4. **Support and relationship map:** typed relationships among claims, documents, data, authors, advisers, institutions, methods, and assumptions, each tied to an exact passage.
5. **Missing-evidence note:** the observation or record most likely to change the present judgments.
6. **Revision history:** objections, corrected edges, replacement judgments, and unresolved questions.

The open verdict contract allows a model, research system, or human analyst to contribute without using the same software. It asks for a position, warrant, citations, counter-evidence, change conditions, and provenance. Cross-system adoption has not yet been demonstrated, but the contract and example records exist.

This structure supports cumulative work without pretending that every contribution agrees. New evidence can be attached to the claim it bears on. A disputed relationship can remain disputed. A new model can rerun one judgment without overwriting the old one. Better retrieval, models, and compute can expand the scrutiny while the reasoning record stays legible.

That cumulative design is what lets a later investigator add a source, replace one judgment, or challenge one relationship without discarding the rest of the inquiry. The open verdict contract in Appendix C makes this usable outside Epistack’s own software: it asks for a position, warrant, citations, counter-evidence, change conditions, and provenance in one shared structured format, so another tool, model, or human analyst can contribute in the same format. Compute scales with the workflow: more sources, deeper retrieval, and additional independent judgments can be added without changing the workflow’s structure. The [LHC retrieval-depth experiment](evidence/lhc/retrieval-depth-REPORT.md) demonstrated deeper retrieval directly, raising passage retention from two to twelve per reviewer without changing the question, source allocation, or ranking.

## Where the method can fail

The workflow can still mislead if its sources, reviewers, or relationship labels are poor.

- **The corpus can predetermine the dispute.** Missing sources and designed partitions can make one crux appear more important than it is.
- **Model roles are not independent experts.** Different prompts and source slices do not erase shared training, model behavior, or infrastructure.
- **The extractor can select a fluent but incomplete claim.** Its proposal must remain open to analyst correction and alternate candidates.
- **Relationships can be overread.** Shared authorship, advice, or citations invite closer inspection; they do not establish common data, invalid reasoning, bias, or falsity.
- **Retrieval can hide documentary evidence.** The LHC deduplication defect hid bylines, and the deeper run still missed the adviser acknowledgment.
- **Automated evidence checks can fail noisily.** Uniform source labels, parser warnings, truncated revised text, and refused output all occurred in the supplied runs.
- **A structured record can still be unused.** The supplied materials do not establish that another team will adopt the verdict contract or maintain the cases over time.

The strongest tests are therefore behavioral:

1. Do independent analysts accept the extracted claim, or can disagreements about it be recorded and resolved?
2. Does the leading claim remain stable under changes in model, prompt, source allocation, and source labels?
3. Do readers given the case record choose a more targeted next investigation than readers given the Deep Research synthesis?
4. When a known source relationship is added or removed, does the support map change without treating correlation as falsity?
5. On a broadly settled case, does the workflow recover conditional fallback structure instead of manufacturing disagreement?
6. Can an automated relationship pass return the exact passages supporting every proposed relationship?

Two cases are not enough to establish generality. COVID and LHC exercise complementary demands on the workflow: a contested inference and a largely settled conclusion with layered support. The dietary-eggs case remains a proposed transfer test; no eggs corpus or result is claimed.

## What the evidence supports

This work does not resolve COVID origins or revise the safety assessment of the LHC. It demonstrates a workflow for preserving the structure beneath a conclusion.

The LHC case records both the safety argument’s alternative-support depth and a documentary relationship hidden by an ordinary citation count. The COVID work produced three inspectable, source-cited judgments and a crux extractor that met all five declared structural and evidentiary checks on the preserved real panel. The retrieval experiment showed that deeper context surfaced relevant bylines but did not connect them across judgments. The Deep Research comparison showed that a strong general research tool can identify the same hinge and useful relationships, while also showing how an unsupported relationship can disappear inside a fluent synthesis.

The contribution is the combination: separate reviews, a working and contestable crux extraction step, a typed relationship audit, and a versioned case-record format supported by linked artifacts. It asks not only what conclusion the literature seems to support, but what claim carries that conclusion and which documented relationships bear on the apparent independence of its support.

## Explore the package

- [Runnable Crux demonstration](demo-crux/README.md)
- [Evidence appendix](evidence/README.md)
- [Slide walkthrough (HTML)](index.html)
- [Presentation deck (PowerPoint)](epistack-deck.pptx)
- [Workflow specification](WORKFLOW-SPEC.md) — compact pseudocode form of the case-record workflow, intended for reuse by other tools and analysts.

---

© 2026 Reticle Works. Released under the MIT License — see [LICENSE](LICENSE).
