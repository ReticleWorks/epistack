# Provenance and publication boundary

The extractor in `crux_extractor.py` is a clean standalone rendering of the minimal deterministic Crux logic exercised in the submission. It includes only text parsing, position labeling, source-reference resolution, disagreement classification, and change-evidence extraction.

The public version deliberately omits proprietary Atlas code, service configuration, database access, environment variables, internal imports, and unrelated routing functions. Its output schema is named `epistack.crux_map.v1`, and reviewer identifiers are generic.

The COVID fixture derives from the preserved panel whose SHA-256 is:

`087bec7ebad58c717553e9751a5367cbb6984cc5302c94e5c3054fc801a26897`

Publication transforms are limited to:

- replacing three internal reviewer identifiers with `covid_market_review`, `covid_skeptical_review`, and `covid_method_review`;
- retaining each reviewer judgment verbatim;
- retaining cited-source identifiers and source filenames;
- replacing local file URLs with the source's public URL;
- omitting retrieved passage text and unrelated run metadata; and
- recording the original panel hash and these transformations in the fixture.

The standalone output may differ from the internal component in its public schema name and reviewer identifiers. The claim-selection, labeling, dispute-classification, and change-evidence rules are otherwise the same minimal deterministic logic used for the submitted validation.

---

© 2026 Reticle Works. All rights reserved. Prose licensed under CC BY 4.0. Code in `demo-crux/` licensed under MIT. See [../LICENSE](../LICENSE).
