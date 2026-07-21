# Epistack — Implementation

Epistack combines existing research functions around a common case record. Some collect and preserve sources. Some find relevant passages and produce separate judgments. A deterministic comparison component proposes the load-bearing claim. Other implemented facilities follow citations and organize source relationships. For relationships those facilities do not encode, the case record requires a typed relationship and its supporting passage. Each function leaves an inspectable artifact, so a later investigator can see where a result came from and where a later stage stopped.

### Source harvesting and records

The source-harvest workflow searches for material, retrieves documents, records failures and exclusions, and stores a file fingerprint. A fingerprint is calculated from a file’s contents; if the file changes, its fingerprint changes. It lets another investigator confirm that they are reading the same source used in the analysis.

This process produced the ten-source COVID corpus and its retrieval record. The LHC package similarly preserves six source files, a manifest, and file fingerprints, although the supplied materials do not establish that the same gathering process assembled it.

**Atlas** is the existing research toolkit beneath Epistack. It can represent documents, claims linked to their source passages, and named entities such as people and institutions. The two case harnesses preserved documents and passages, but their linked-claim graphs were empty. They demonstrate traceable source assembly and passage storage, not the fuller graph-backed path.

### Atlas retrieval

Atlas searches stored material for passages relevant to a question and supplies selected passages to a configured reviewer. Its `taste_agent` component can combine direct passage search with claim-graph and citation context when those stores are populated.

In the COVID and LHC runs, the linked-claim graph was empty, so direct passage search supplied the evidence. A local OpenAI embedding service represented each passage numerically so the software could retrieve passages similar to the question. The cases show Atlas code retrieving preserved passages for separate reviews. They do not show that every retrieval channel or graph link contributed.

### Separate judgments

Atlas’s `judgment_panel` asks several configured reviewers the same narrow question and preserves each answer independently. Each judgment can contain a position and confidence range, supporting reasons, cited sources, counter-evidence, limitations, and evidence that could change the judgment. This is the panel structure used in both cases.

The reviewers in these cases were model roles with different source allocations, not independent human experts. Their value here is structural: the record shows who relied on what before a later synthesis can smooth the differences away.

### Checks on generated text

Atlas includes checks intended to catch two common problems in generated research. Its faithfulness check breaks an answer into factual claims and asks whether the retrieved passages support each one. Its uncertainty component records caveats about the source set and retrieval result when assigning a range.

These are diagnostic controls, not measures of truth. In the supplied runs, the support check produced useful refusals and revised outputs, but also parser warnings and truncated text. A single default source label made the uncertainty ranges uninformative about differences in source quality. Those failures remain in the case record.

### Citation-graph retrieval

Atlas also includes `rag_advisor`, a citation-focused retrieval service. It records which papers cite which others, can search one citation step beyond an initial source set, and can identify influential papers and clusters of closely connected work.

These are implemented source-relationship facilities. They can show citation connections and help organize a literature. They are not a general service for detecting shared authorship, acknowledged advice, or shared datasets across arbitrary documents. For those relationships, Epistack requires a type and the passage supporting it. In the LHC case, that complete comparison came from the source-directed audit; the panel itself did not produce the authorship and advice finding.

### Load-bearing-claim comparison

The crux extractor is a deterministic reference component: the same input produces the same output. It compares preserved judgments and returns a candidate load-bearing claim, each reviewer’s position, cited sources, disagreement type, and stated change conditions. It runs over preserved panel output and is included in the reference package. On the preserved COVID panel it met all five declared structural and evidentiary checks. Four additional tests include an unrelated clinical-trial case and an abstention case.

This shows that the component emits the required inspectable fields on those tests. It does not prove semantic accuracy across domains. The supplied record does not establish that this version has been merged into the deployed Atlas service.

### Typed relationships and the case record

Atlas and `rag_advisor` already represent source, entity, and citation relationships. Epistack’s case record adds explicit types for other documented relationships, including shared authorship, advice, data, institutions, methods, and assumptions. Each accepted relationship must retain the passage supporting it. The supplied software does not contain a general automated service for detecting all of those relationship types.

The intended case record combines the source ledger, separate judgments, extracted claim, typed relationships, missing-evidence requests, objections, and revision history. The supplied package already preserves the corpora, manifests, raw judgments, COVID crux record, LHC support map, and successive corrections. It does not yet provide one consolidated interface for challenging a relationship and recording the response.

---

© 2026 Reticle Works. Released under the MIT License — see [LICENSE](LICENSE).
