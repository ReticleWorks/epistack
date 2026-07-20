# Controlled LHC retrieval-depth experiment

**Date:** 2026-07-19  
**Status:** completed, exit status 0  
**Scope:** isolated experiment only; no proposal draft, canonical corpus, existing run artifact, production registry, deployed source file, production service, or walkthrough was edited

## Result in one paragraph

The verified treatment worked at the retrieval layer. The preserved run retained two passages per specialist—one per assigned source—because Channel B gave all passages from a file the same source UUID and the fusion stage deduplicated on that UUID. The run-local treatment kept the existing top-12 ranking but assigned each passage a deterministic source-plus-text-hash identity. Each specialist then retained 12 passages, and every one of the six baseline passages remained in its corresponding deeper set. The deeper evidence included the LSAG byline naming Michelangelo Mangano and the Giddings–Mangano byline, so shared Mangano authorship became visible across the raw panel evidence. It did **not** include the fallback paper's acknowledgment of advice from the other four LSAG authors. Neither completed judgment mentioned Mangano or authorship overlap, and the auditor judgment was refused by the faithfulness gate. The test therefore establishes that the deduplication defect hid relevant bylines, but it also shows that passage depth alone is not enough to produce the dependency finding.

## What was actually changed

The deployed path was inspected before the run, not inferred from the old output shape.

1. `graph_judgment` defaults to `top_k=12` and passes that limit to `_channel_b_search`.
2. The pgvector store returns the top passages ordered by cosine distance.
3. `_channel_b_search` labels every returned passage with `"uuid": chunk.source_id`.
4. `source_loader.source_id()` hashes the file path, so all chunks from one file share that ID.
5. `_fuse_graph_facts` calls `_fact_key`, which returns `uuid` when present, and removes repeated keys.

This means the existing `top_k=12` setting already requested 12 passages. Merely increasing an environment variable would not correct the within-source collapse. The treatment in `run/retrieval_depth_patch.py` calls the deployed Channel-B search unchanged and replaces only the result identity:

```text
before: uuid = source_id
after:  uuid = source_id + ":chunk:" + sha256(passage_text)[0:16]
```

It retains the original source ID in `channel_b_source_id` for audit. Search query, embedding, similarity score, rank order, source allocation, chunking, result limit, and fact text are untouched. The synthesis helper reads only each fact's text, so the added audit metadata does not enter the model prompt. The changed UUID also means `cited_sources` now contains passage identities rather than one file identity; that is a disclosed schema consequence of the treatment.

A dependency-light unit check confirmed that two different passages with the same source ID remain distinct while order and scores stay unchanged:

```text
PASS: same-source passages remain distinct; order and scores are unchanged
```

The complete harness and registry diff from the preserved run is in `results/exact_harness_and_config_diff.patch`.

## Controls and isolation

The treatment retained the preserved run's:

- exact research question;
- official, method, and auditor focus/persona text;
- two-source allocation for each specialist;
- `chunk_size: 900`, `chunk_overlap: 120`, and `late_chunking: false`;
- native OpenAI `text-embedding-3-small` embeddings at 1,024 dimensions through the unchanged direct embedding shim;
- deployed synthesis default `claude-sonnet-4-6`, temperature 0.0, one sample, 1,000 output tokens;
- faithfulness mode `act` and verifier `gpt-4.1-mini`; and
- panel concurrency of one.

No synthesis override was present in the non-interactive Trailhead environment after the run, and the run script set none. The direct embedding shim is byte-identical to the preserved one: SHA-256 `edb7da9e9050714cb0c54c2a2e78e508fbb38ff328635aaa9d0ed4cd2771fc93`.

All six copied texts are byte-identical to the canonical corpus:

| Source | SHA-256 |
|---|---|
| LSAG 2008 | `6e4f5244885bae3d208a754477226c7b55c3796aa7111acb231ccb8397830b56` |
| Giddings–Mangano 2008 | `f6a3cf1e92df21f29ab3d8475d341a4c381b3131dc55f9d90cdc5e7d5f9b2bd8` |
| LHC Safety Study Group 2003 | `6f31a09b5eeefce082b6d41b97d62e09016939b79added6093fb6df62c7d3332` |
| CERN background page | `ec912d5671e6512cd9268a7ad868b1868f6f045ef29de5534d83f80d6fa8ba1c` |
| Ord, Hillerbrand, and Sandberg 2010 | `dc9b6e06f4f7fdf60fa6d4c92cab65caa7a2cd0d09a2853b5e7e8e2881ef4ffd` |
| Kent 2004 | `9b71b3d02320e68e8e3484c4a5d42c62ac11458a78b72d04409d9038922c7979` |

The treatment used new, private identifiers:

- specialists: `flf_sol_lhc_depth_official`, `flf_sol_lhc_depth_method`, and `flf_sol_lhc_depth_auditor`;
- Postgres table: `public.flf_sol_lhc_depth_chunks`;
- empty graph group: `flf_sol_lhc_depth_20260719`; and
- private registry: `registry/registry.yaml`.

A pre-run read-only query established that the new table was absent. Ingest then wrote 14, 64, and 24 chunks for the three new specialist IDs, respectively, with zero reported ingest errors. The 102 rows remain in that isolated table as the reproducible record. The production server was not started, stopped, reloaded, or called.

This remained a Channel-B-only test. The new graph namespace was not ingested, so this does not establish graph retrieval or graph-backed dependency detection.

## Before and after

| Specialist | Preserved facts | Treatment facts | Treatment allocation | Baseline passages retained? | Returned judgment |
|---|---:|---:|---|---|---|
| Official | 2 | 12 | 11 LSAG, 1 CERN page | Yes | Yes; faithfulness `repaired`, ratio 0.933 |
| Method | 2 | 12 | 6 Giddings–Mangano, 6 2003 report | Yes | Yes; faithfulness `repaired`, ratio 0.789 |
| Auditor | 2 | 12 | 5 Ord et al., 7 Kent | Yes | **No**; faithfulness `refused`, `gate_error`, evaluated coverage below 80%, ratio 0.688 |

The panel wrapper reports all three calls as `ok: true` because all three `graph_judgment` calls returned a result object. That count must not be described as three usable judgments: the auditor's final `judgment` is `null` after enforcement refusal.

The raw treatment output has SHA-256 `a0a38db2ad0b379cfd5b2d4528ffa3bea4bde762ad8191ac7867d2fd272df868`. The copied preserved baseline has SHA-256 `fe2dcf3667fef5ed62f33e5ac15ce4ebdfc9c22b1782aa00461d8c462319a6f1`.

## Did the target dependency evidence surface?

### Shared Mangano authorship: present in retrieval, absent from judgments

- **Preserved run:** neither relevant byline was among the six retained facts.
- **Treatment official specialist:** the LSAG byline was retained at rank 3. It names John Ellis, Gian Giudice, Michelangelo Mangano, Igor Tkachev, and Urs Wiedemann. Passage-text SHA-256: `1734ec9aa77ed8c6be97d3c586b8eafbb9a70caee1e16eb0f84f5772aa46e4f1`.
- **Treatment method specialist:** the fallback-paper byline was retained at rank 10. It names Steven B. Giddings and Michelangelo L. Mangano. Passage-text SHA-256: `dd95bf51a72bed910443ad8931c96e953b0222ead1e0246274b138dc4269d5bb`.

Comparing those two raw passages establishes shared Mangano authorship as a documentary fact. The panel did not perform that cross-specialist comparison. Neither completed judgment contains "Mangano," "shared author," "co-author," or "authorship overlap." Therefore:

- **Established:** deeper within-source retrieval exposed the two bylines needed for the shared-author finding.
- **Not established as system output:** that the judgment panel identified or reasoned over the shared authorship.

### Adviser acknowledgments: not retrieved

The top-12 method evidence did not contain the Giddings–Mangano acknowledgment thanking the other four LSAG authors for guidance and advice. No returned judgment mentioned that adviser relationship. The human-directed warrant map remains the only supplied artifact establishing it from the document text.

- **Established:** the top-12 treatment did not retrieve this acknowledgment for the unchanged research question.
- **Not established by this run:** the four adviser relationships or their effect on evidential independence.

### Argument structure: richer, but not the requested personnel dependency

The official and method judgments gave a more detailed layered/fallback account than a bare Hawking-radiation chain. They discussed the cosmic-ray and compact-object fallback, charge/neutralization conditions, accretion models, and observational constraints. This is useful qualitative output. It is not a controlled accuracy score, and model/provider nondeterminism can still affect exact prose at temperature zero.

## What this result establishes

1. The prior two-fact shape came from a verified source-ID deduplication path, not from a configured per-source cap.
2. A run-local passage identity correction raised retained depth from 2 to 12 facts per specialist while preserving all six baseline fact texts.
3. Under the unchanged question and top-12 semantic ranking, the deeper evidence exposed both bylines needed to observe shared Mangano authorship.
4. The existing judgment-panel path did not join those bylines across specialists or state the authorship finding.
5. Top-12 retrieval still missed the adviser acknowledgment.
6. More evidence increased enforcement burden enough that the auditor output was refused rather than returned as a judgment.

## What this result does not establish

- that raising retrieval depth generally improves judgment accuracy;
- that the panel automatically detects personnel, citation, advice, or institutional dependencies;
- that the fallback paper is inferentially invalid or its physics is wrong;
- that the LHC was or is dangerous;
- that the two argument layers are statistically or causally independent;
- that the four LSAG authors advised on, reviewed, or endorsed the final safety conclusion rather than supplying discussion or guidance;
- that graph retrieval ran;
- that 12 passages is an optimal depth; or
- that the same result will hold across embeddings, models, seeds, questions, or corpora.

## Practical implication for the proposal

The safe claim is narrower and more interesting than "more context solved it":

> Correcting within-source deduplication exposed the two bylines required to see shared authorship, but the panel did not connect them, and it still missed the adviser acknowledgment. Retrieval depth was one bottleneck, not the whole problem.

An Atlas-centered proposal can use this as evidence for a separate, explicit dependency pass over bylines, acknowledgments, citations, institutions, and advice relationships. It should not claim that the existing panel already performs that pass. A next test should predeclare a dependency-specific query or structured metadata extractor and require it to return the supporting source spans; that would test the missing function directly rather than asking a broad safety-case query to retrieve document furniture by semantic similarity.

## Commands and artifacts

Core commands:

```bash
# Pre-run table check on <host>
psql -h <host> -p <port> -U <user> -d taste \
  -Atc "SELECT COALESCE(to_regclass('public.flf_sol_lhc_depth_chunks')::text,'ABSENT');"

# Run-local identity unit check
python3 \
  comparisons/strategy/lhc-retrieval-depth-test/run/test_retrieval_depth_patch.py

# Full foreground run on <host>
bash ./comparisons/strategy/lhc-retrieval-depth-test/run/run_panel.sh

# Deterministic comparison/diff builder
python3 comparisons/strategy/lhc-retrieval-depth-test/run/analyze_results.py
```

Key artifacts:

- `results/panel_result_raw.json` — unedited treatment panel output;
- `results/retrieval_trace.json` — exact requested limits, source IDs, passage IDs, ranks, scores, sizes, and text hashes;
- `results/before_after_comparison.json` — deterministic baseline/treatment comparison and target checks;
- `results/ingest_reports.json` — exact ingestion results;
- `results/run.stderr.log`, `results/run.stdout.log`, and `results/run_log.json` — execution record;
- `results/exact_harness_and_config_diff.patch` — complete registry and runner diff;
- `code-snapshot/` — exact deployed files governing routing, source IDs, storage, synthesis, and enforcement;
- `run/retrieval_depth_patch.py` — sole algorithmic treatment; and
- `baseline_panel_result_raw.json` and `baseline_manifest.json` — copied preserved controls.

Native Claude Sonnet was invoked for a read-only code review before execution. Three headless processes remained active without returning review text. The two redundant processes were terminated, followed by the first after more than seven minutes without output. No review finding is claimed or relied on.

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
