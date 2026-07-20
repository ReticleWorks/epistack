#!/usr/bin/env python3
"""Run the public Crux extractor over the preserved, sanitized COVID panel."""
# © 2026 Reticle Works. MIT License. See ../LICENSE.

from __future__ import annotations

import json
from pathlib import Path
import sys

from crux_extractor import extract_crux_map


HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "covid-panel.json"


def main() -> None:
    if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] not in {"--json", "--summary"}):
        raise SystemExit("usage: python3 run_demo.py [--json|--summary]")

    panel = json.loads(FIXTURE.read_text(encoding="utf-8"))
    output = extract_crux_map(panel["query"], panel, stance_seed=panel.get("stance_seed"))

    if len(sys.argv) == 2 and sys.argv[1] == "--json":
        print(json.dumps(output, indent=2, ensure_ascii=False))
        return

    primary = output["cruxes"][0]
    print("Epistack public Crux demonstration")
    print(f"Question: {output['query']}")
    print(f"Candidate claim: {primary['claim']}")
    print(f"Disagreement type: {primary['disagreement_type']}")
    print("Positions:")
    for position in primary["positions"]:
        files = ", ".join(ref["file"] for ref in position["source_refs"] if ref["file"])
        print(f"  - {position['reviewer_id']}: {position['position']} ({files})")
    print(f"Change-evidence records: {len(primary['would_change_judgment_if'])}")
    print(f"Failures: {len(output['failures'])}")


if __name__ == "__main__":
    main()
