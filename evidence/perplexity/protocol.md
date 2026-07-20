# Predeclared Perplexity Deep Research comparison protocol

This comparison design was fixed before the Deep Research call on 2026-07-19. The original predeclared protocol has SHA-256 `314c46d872b7f17e6ef8fcd17682f78f39f8834bda53b19d634ce54a6659b7f9`. This public copy removes internal cross-references but does not change the question, source conditions, requested output, or comparison fields.

## Purpose

Test what Perplexity Deep Research returns on the same contested COVID question and the same ten-source starting corpus used in the Epistack COVID work.

This is a single-run, instructed capability comparison. It is not a performance benchmark and cannot establish typical behavior, superiority, or reproducibility across prompts and runs.

## Fixed substantive question

> Does the spatial clustering of early COVID-19 cases around the Huanan Seafood Market represent the outbreak's true origin, or downstream amplification of prior human-to-human transmission?

## Fixed source conditions

Perplexity receives the ten stable source URLs in the harvested Epistack corpus as its required starting set. It may add sources to check or update the record, but must identify additions. It is asked to distinguish peer-reviewed research from commentary and debate material. The prompt does not supply Epistack's panel judgments, validation checks, or conclusions.

## Requested output

The report is asked to:

1. answer the substantive question;
2. separate what spatial clustering itself supports from the broader origin inference;
3. name the claim on which its conclusion most depends;
4. state the strongest alternative explanation and what evidence would change the conclusion;
5. identify material dependencies among sources where the record establishes them, including shared authorship, data, methods, citation ancestry, advisory relationships, or repeated analysis;
6. state unresolved matters plainly;
7. provide citations and a source table.

These requirements intentionally ask Deep Research to perform the same analytical tasks proposed for Epistack. The result tests instructed capability, not what a generic prompt would expose without being asked.

## Comparison fields fixed before the run

The audit records:

- whether the distinct Deep Research mode was used;
- whether it used the ten fixed sources and clearly marked additions;
- its answer and confidence or qualification;
- the precision of its load-bearing claim;
- its strongest alternative explanation and proposed discriminating evidence;
- whether it found source dependencies, and which ones;
- whether citations support nearby claims;
- what it handled better than the current Epistack artifacts;
- what the current Epistack artifacts expose that the Deep Research report did not; and
- gaps that prevent a firm comparison.

No score or win/loss label was predeclared. Findings are descriptive.

---

© 2026 Reticle Works. Released under the MIT License — see [LICENSE](../../LICENSE).
