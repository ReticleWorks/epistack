# Crux component validation

## Outcome

The deterministic reference component extracts a concrete disputed claim from
the preserved three-reviewer COVID panel.

The baseline record met **2/5** declared checks; the current record meets
**5/5**. These are structural and evidentiary checks, not a general
semantic-accuracy score.

The extracted claim is the market specialist's own proposition that the spatial
concentration of early cases around Huanan is moderately strong, though not
conclusive, evidence that the market was the pandemic's epicenter. The other
specialists are represented as challenging that weight or assigning it some
weight subject to ascertainment bias. The extractor classifies the dispute as
`different weighting / likelihood ratio`, resolves each position's cited files,
and carries forward explicit evidence that could change the judgment.

## What the component returns

The current component:

1. reads each judgment's `Position` section;
2. selects the proposition most directly responsive to the common query;
3. labels each specialist `supports`, `challenges`, or `insufficient_evidence`;
4. resolves cited ids to source filenames and URLs carried in retrieved facts;
5. classifies the dispute and reports the basis and confidence of that label;
6. extracts explicit statements about evidence that would change the judgment;
7. distinguishes true support/challenge disagreement from support plus abstention.

The declared reference answer was unchanged (SHA-256
`04376455d6079bb590e535d8f63cbeb2663039d33f48b93a2551bd18f304164b`)
and was not passed to the extractor.

## Verification

- Four standard-library tests pass, including an unrelated clinical-trial panel
  and a support-plus-abstention case.
- The evaluator reproduces the preserved COVID output and scores all five declared
  checks as passing.
- An independent code review examined specificity, abstention behavior, and the
  basis for disagreement labels. The final test suite covers its material findings.
- The review's remaining caveat is adopted here: 5/5 shows that the extractor emits
  the required concrete and inspectable fields. It does not establish semantic
  accuracy across arbitrary domains.

## Run it

From `../../demo-crux/`:

```sh
python3 run_demo.py covid
```

No database, model call, network request, or reference-answer input is used during
extraction.

## Evidence files

- `after_crux_map.json` — current output over the preserved panel
- `before_after.json` — complete baseline and current outputs
- `oracle_score.json` — check-by-check score and evidence
- `exact_code_diff.patch` — exact baseline-to-current code diff
- `run_manifest.json` — implementation, input paths, hashes, and configuration
- `run_evaluation.py` — reproducible evaluator
- `INDEPENDENT-COMPONENT-REVIEW.md` — independent code and evidence review

## Boundary

The component is included in the demo package. The supplied record does not
establish that this version is merged into the deployed Atlas service. The
preserved panel came from a corpus-grounded run; rerunning the extractor does not
rerun ingestion or the model panel. It deterministically processes that captured
record.

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
