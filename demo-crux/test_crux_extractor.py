#!/usr/bin/env python3
"""Standard-library tests for the public deterministic Crux extractor."""
# © 2026 Reticle Works. MIT License. See ../LICENSE.

from __future__ import annotations

import json
from pathlib import Path
import unittest

from crux_extractor import extract_crux_map


HERE = Path(__file__).resolve().parent
COVID_PANEL = HERE / "fixtures" / "covid-panel.json"


class CruxExtractorTests(unittest.TestCase):
    def test_preserved_covid_panel_meets_structural_contract(self) -> None:
        panel = json.loads(COVID_PANEL.read_text(encoding="utf-8"))
        output = extract_crux_map(panel["query"], panel, stance_seed=panel.get("stance_seed"))
        primary = output["cruxes"][0]
        self.assertEqual(output["schema"], "epistack.crux_map.v1")
        self.assertEqual(output["query"], panel["query"])
        self.assertIn("stance_seed", output)
        self.assertGreater(len(primary["claim"]), 40)
        self.assertNotEqual(primary["claim"].lower(), "different citations")
        self.assertEqual(primary["disagreement_type"], "different weighting / likelihood ratio")
        self.assertEqual(primary["disagreement_type_confidence"], "MEDIUM")
        self.assertEqual(
            {position["position"] for position in primary["positions"]},
            {"supports", "challenges"},
        )
        self.assertTrue(primary["would_change_judgment_if"])
        for position in primary["positions"]:
            self.assertTrue(any(ref["file"] for ref in position["source_refs"]))
            self.assertTrue(all(not ref["url"].startswith("file:") for ref in position["source_refs"]))

    def test_unrelated_panel_is_extracted_without_topic_constants(self) -> None:
        query = "How strongly does the trial support compound Q over usual care?"
        panel = {
            "query": query,
            "stance_seed": "audit the treatment claim",
            "results": [
                {
                    "reviewer_id": "trial_reader",
                    "ok": True,
                    "result": {
                        "judgment": "## Position The randomized trial strongly supports compound Q over usual care for six-month symptom relief. ## Counterpoint A larger independent trial would strengthen this judgment.",
                        "cited_sources": ["trial-a"],
                        "facts": [{"uuid": "trial-a", "title": "trial-a.txt", "url": "https://example.org/trial-a"}],
                        "uncertainty": {"band": "MODERATE"},
                    },
                },
                {
                    "reviewer_id": "methods_reader",
                    "ok": True,
                    "result": {
                        "judgment": "## Position The trial does not reliably support compound Q because attrition undermines the estimated effect. ## Counterpoint Complete follow-up data would change the judgment.",
                        "cited_sources": ["methods-b"],
                        "facts": [{"uuid": "methods-b", "title": "methods-b.txt", "url": "https://example.org/methods-b"}],
                        "uncertainty": {"band": "MODERATE"},
                    },
                },
            ],
        }
        output = extract_crux_map(query, panel, stance_seed=panel["stance_seed"])
        primary = output["cruxes"][0]
        self.assertIn("compound Q", primary["claim"])
        self.assertNotIn("Huanan", primary["claim"])
        self.assertEqual(primary["disagreement_type"], "different weighting / likelihood ratio")
        self.assertEqual(output["stance_seed"], "audit the treatment claim")
        self.assertTrue(primary["would_change_judgment_if"])

    def test_failure_is_preserved(self) -> None:
        output = extract_crux_map(
            "Any claim?",
            {"results": [{"reviewer_id": "broken", "ok": False, "error": "timeout"}]},
        )
        self.assertEqual(output["failures"], [{"reviewer_id": "broken", "error": "timeout"}])

    def test_support_plus_abstention_is_not_called_contested(self) -> None:
        panel = {
            "results": [
                {
                    "reviewer_id": "supporter",
                    "ok": True,
                    "result": {
                        "judgment": "## Position The available record strongly supports the stated claim.",
                        "cited_sources": ["a.txt"],
                        "facts": [],
                    },
                },
                {
                    "reviewer_id": "abstainer",
                    "ok": True,
                    "result": {
                        "judgment": "## Position The available record is insufficient to determine the claim.",
                        "cited_sources": ["b.txt"],
                        "facts": [],
                    },
                },
            ]
        }
        output = extract_crux_map("Does the available record support the stated claim?", panel)
        self.assertEqual(output["cruxes"][0]["divergence_signal"], "mixed_with_abstention")
        self.assertEqual(output["cruxes"][0]["disagreement_type_confidence"], "LOW")


if __name__ == "__main__":
    unittest.main()
