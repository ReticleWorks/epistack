# LHC case evidence

## Scope

The LHC case is not a new collider-safety assessment. It tests whether Epistack can preserve a layered, largely settled safety argument and distinguish documented source relationships from claims the documents do not support.

The [source manifest](source-manifest.json) records six sources totaling 78,481 words in the panel text, with retrieval URLs, fingerprints, and per-source word counts. Full source texts are not redistributed here.

## Conditional safety structure

Direct reading of the six-source record supports this structure:

```text
Standard physics does not expect dangerous black-hole production.
|
+- If speculative production occurs:
   +- Expected result: rapid Hawking evaporation.
   +- If a microscopic black hole is stable:
      +- If charged, cosmic-ray analogues should be trapped in Earth or the Sun.
      +- If effectively neutral, dense stars should trap analogues;
         old white dwarfs and neutron stars constrain dangerous accretion scenarios.
```

The 2008 official report expressly considers the possibility that Hawking evaporation is wrong and directs readers to astrophysical arguments that do not depend on it (`src-0001`, lines 151–155 and 402–406 in the preserved extraction). The Giddings–Mangano paper develops the stable-black-hole test through cosmic-ray collisions, accretion models, and the survival of compact stars (`src-0002`, lines 371 and 2437–2523).

The supplied sources do not give a numerical probability for the joint failure of these defenses. The evidence supports a conditional argument map, not a catastrophe estimate.

## Documented relationships

| Relationship | Direct documentary support | What it does not establish |
|---|---|---|
| Shared authorship | Michelangelo Mangano appears on the official report's byline (`src-0001`, line 27) and the fallback paper's byline (`src-0002`, line 34). | Shared data, invalid reasoning, bias, or falsity. |
| Acknowledged advice | The fallback paper thanks the other four official-report authors, among others, for guidance and advice (`src-0002`, lines 2538–2544). | The subject of each conversation, review of the final argument, or endorsement of the safety conclusion. |
| Citation relationship | The official report points to the fallback paper for detailed accretion scenarios (`src-0001`, lines 402–406 and reference [2] at line 1022). | That the two documents are equivalent or wholly dependent. |
| Outside specialist input | The fallback paper names outside specialists consulted about accretion, white dwarfs, and neutron-star systems (`src-0002`, lines 2547–2550). | That those specialists reviewed or endorsed the full safety conclusion. |

These relationships justify closer inspection of how separate the report and its principal supporting paper are. They do not show that the physics is wrong or that the documents use one dataset.

## Retrieval-depth experiment

The preserved panel retained two passages per reviewer because passages from the same file shared a source identifier and the filtering stage treated them as duplicates. An isolated treatment retained twelve passages per reviewer while preserving the question, source allocation, rank order, and all six baseline passages.

The additional evidence contained both Mangano bylines. The two completed judgments did not connect them. The adviser acknowledgment was still absent from the retrieved evidence, and the third judgment was refused by the evidence checker. The result establishes that retrieval had hidden relevant bylines and that deeper retrieval alone did not complete the relationship check.

The [experiment record](retrieval-depth.json) preserves the baseline and treatment hashes, counts, and claim boundaries. It does not include internal service configuration, logs, code snapshots, database details, or proprietary implementation.

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
