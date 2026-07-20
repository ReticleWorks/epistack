# Independent component review

The review examined the deterministic component, its tests, and its output over
the preserved COVID panel.

## Initial findings

The review confirmed that the current component replaced the baseline's generic
`different_citations` / `requires_human_review` output with a concrete claim,
position labels, source-file resolution, dispute typing, and decision-changing
evidence. It found no literal COVID, Huanan, Wuhan, zoonotic, or market-origin
constants in the extractor and independently reproduced the output.

It nevertheless found four softer problems:

1. Several change-evidence phrases duplicated wording in the COVID panel.
2. The causal classifier included `spillover` and `introduction`.
3. `supports` plus `insufficient_evidence` was labeled `contested_claim`.
4. Disagreement typing did not expose whether it used an explicit cue or a fallback.

It also cautioned that 5/5 is a structural and evidence-bearing score, not proof
of semantic equivalence to every word of the hand-authored gold claim.

## Current behavior

The final code replaces panel-specific phrase strings with generic grammatical
patterns, removes the domain-specific causal words, distinguishes
`mixed_with_abstention`, and emits a classification basis plus `MEDIUM` or `LOW`
confidence. The test suite now covers the latter two fields.

The remaining caveat is binding: report the result as a five-check structural and
evidentiary pass, not as a general semantic-accuracy result.

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
