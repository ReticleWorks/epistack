# Crux component validation

The deterministic component processes preserved reviewer judgments after the panel finishes. It proposes a concrete claim, labels each review as supporting, challenging, or insufficient, resolves cited-source references, classifies the disagreement, and carries forward explicit evidence that could change a judgment.

On the preserved COVID panel, the current component met all five declared structural and evidentiary checks:

1. return a concrete claim responsive to the common question;
2. preserve each reviewer's position;
3. resolve cited files and sources;
4. classify the disagreement and preserve the original question; and
5. return stated decision-changing evidence.

Four standard-library tests also pass. They cover the preserved COVID fixture, an unrelated clinical-trial example, a failed reviewer, and a support-plus-abstention case.

These checks establish that the component emits the required inspectable structure on the tested records. They do not establish general semantic accuracy, scientific correctness, or cross-domain performance. The public component is standalone reference code; the supplied record does not establish that it has been merged into a deployed Atlas service.

Run the public evidence directly:

```sh
cd publication/demo-crux
python3 test_crux_extractor.py
python3 run_demo.py --json
```

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../../LICENSE](../../LICENSE).
