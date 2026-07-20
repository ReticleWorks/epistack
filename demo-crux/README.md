# Public Crux demonstration

This directory contains a standalone, deterministic comparison component and a sanitized fixture derived from the preserved COVID panel. It uses only Python's standard library. It makes no network, model, database, or Atlas call.

Run the demonstration:

```sh
python3 run_demo.py
```

Print the complete structured output:

```sh
python3 run_demo.py --json
```

Run the tests:

```sh
python3 test_crux_extractor.py
```

The tests cover the preserved COVID panel, an unrelated clinical-trial example, a failed reviewer, and a support-plus-abstention case. Passing tests establish that the component returns the declared structure on these examples. They do not establish that its selected claim is always semantically correct or that it generalizes across arbitrary domains.

The public fixture retains the original reviewer judgments and cited-source identifiers. It replaces internal reviewer names with descriptive roles, replaces local file URLs with public source URLs, omits retrieved source text, and records the SHA-256 of the preserved source panel. See [PROVENANCE.md](PROVENANCE.md).

---

© 2026 Reticle Works. Released under the MIT License — see [LICENSE](../LICENSE).
