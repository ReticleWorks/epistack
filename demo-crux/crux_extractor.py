#!/usr/bin/env python3
"""Deterministic, standard-library Crux extraction for preserved panel records."""
# © 2026 Reticle Works. MIT License. See ../LICENSE.

from __future__ import annotations

import re
from typing import Any


ALLOWED_DISAGREEMENT_TYPES = (
    "different weighting / likelihood ratio",
    "competing causal model",
    "source quality / method dispute",
    "missing evidence",
    "persistent inference dispute",
)

STOPWORDS = {
    "about", "after", "again", "against", "also", "among", "around", "because",
    "been", "before", "being", "between", "both", "could", "does", "from", "have",
    "into", "most", "other", "over", "provided", "question", "should", "strongest",
    "their", "there", "these", "they", "this", "through", "under", "what", "when",
    "where", "which", "while", "with", "would",
}


def _plain_text(value: Any) -> str:
    text = str(value or "")
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -:\n\t")


def _position_text(judgment: str) -> str:
    match = re.search(
        r"(?:#{1,6}\s*|\*\*)Position(?:\*\*)?\s*[:\-]*\s*(.*?)(?=\s*---\s*(?:#{1,6}\s*)?(?:Why|Counterpoint|Caveats|Confidence)|\n\s*#{1,6}\s|\Z)",
        judgment,
        flags=re.IGNORECASE | re.DOTALL,
    )
    candidate = match.group(1) if match else judgment
    clean = _plain_text(candidate)
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", clean)
    return (sentences[0] if sentences else clean)[:1200]


def _tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower())
        if token not in STOPWORDS
    }


def _claim(query: str, positions: list[dict[str, Any]]) -> str:
    query_tokens = _tokens(query)
    candidates = [position["position_statement"] for position in positions if position["position_statement"]]
    if not candidates:
        return _plain_text(query).rstrip("?")

    def score(candidate: str) -> tuple[float, int]:
        overlap = len(_tokens(candidate) & query_tokens) / max(1, len(query_tokens))
        return (overlap - max(0, len(candidate) - 420) / 4000, -len(candidate))

    return max(candidates, key=score)


def _claim_id(claim: str) -> str:
    tokens = [
        token
        for token in re.findall(r"[a-z0-9]+", claim.lower())
        if len(token) > 2 and token not in STOPWORDS
    ]
    return "crux:" + "-".join(tokens[:10])


def _position_label(statement: str) -> str:
    lowered = statement.lower()
    if "insufficient" in lowered or "cannot adjudicate" in lowered or "cannot determine" in lowered:
        return "insufficient_evidence"
    if (
        "does not" in lowered
        or "not reliably" in lowered
        or "unreliable" in lowered
        or "only weak" in lowered
        or "undermined" in lowered
    ):
        return "challenges"
    if "support" in lowered or "strong" in lowered or "consistent with" in lowered or "provides some" in lowered:
        return "supports"
    return "insufficient_evidence"


def _disagreement_type(positions: list[dict[str, Any]]) -> str:
    text = " ".join(position["position_statement"] for position in positions).lower()
    labels = {position["position"] for position in positions}
    if "ascertainment" in text or "source quality" in text or "sampling bias" in text:
        if len(labels & {"supports", "challenges"}) > 1 or "likelihood" in text:
            return ALLOWED_DISAGREEMENT_TYPES[0]
        return ALLOWED_DISAGREEMENT_TYPES[2]
    if "missing" in text or "data gap" in text or "absence of" in text:
        return ALLOWED_DISAGREEMENT_TYPES[3]
    if re.search(r"\b(?:causal|cause|pathway|mechanism|model)\b", text):
        return ALLOWED_DISAGREEMENT_TYPES[1]
    if len(labels & {"supports", "challenges"}) > 1:
        return ALLOWED_DISAGREEMENT_TYPES[0]
    return ALLOWED_DISAGREEMENT_TYPES[4]


def _source_refs(result: dict[str, Any], cited_sources: list[Any]) -> list[dict[str, str]]:
    cited = {str(source) for source in cited_sources}
    refs: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    facts = result.get("facts") if isinstance(result.get("facts"), list) else []
    for fact in facts:
        if not isinstance(fact, dict) or str(fact.get("uuid") or "") not in cited:
            continue
        source_id = str(fact.get("uuid") or "")
        title = str(fact.get("title") or "")
        url = str(fact.get("url") or "")
        key = (source_id, title, url)
        if key in seen:
            continue
        seen.add(key)
        refs.append({"source_id": source_id, "file": title, "url": url})
    if not refs:
        refs = [
            {
                "source_id": source_id,
                "file": source_id if ("-" in source_id or "." in source_id) else "",
                "url": "",
            }
            for source_id in sorted(cited)
        ]
    return refs


def _change_evidence(judgment: str, facts: list[Any]) -> list[str]:
    candidates: list[str] = []
    patterns = (
        re.compile(r"\bwould\b.{0,100}\b(?:change|strengthen|weaken|alter|reverse)\b", re.I),
        re.compile(r"\b(?:lack|lacks|lacking|absence|missing|no)\b.{0,60}\b(?:evidence|data|record|records)\b", re.I),
        re.compile(r"\b(?:evidence|data|record|records|study|trial|dataset|series)\b.{0,100}\b(?:needed|required|missing|absent|unavailable|unbiased|complete|decisive|definitive)\b", re.I),
    )

    def collect(body: str) -> None:
        clean = _plain_text(body)
        for sentence in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", clean):
            if 25 <= len(sentence) <= 700 and any(pattern.search(sentence) for pattern in patterns):
                candidates.append(sentence)

    collect(judgment)
    if not candidates:
        for fact in facts:
            if isinstance(fact, dict):
                collect(str(fact.get("fact") or fact.get("text") or ""))

    unique: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = re.sub(r"\W+", " ", candidate.lower()).strip()
        if key not in seen:
            seen.add(key)
            unique.append(candidate)
    return unique[:3]


def extract_crux_map(
    query: str,
    panel_result: dict[str, Any],
    *,
    stance_seed: str | None = None,
) -> dict[str, Any]:
    """Extract an inspectable candidate claim from preserved reviewer judgments."""

    results = panel_result.get("results", [])
    positions: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for item in results if isinstance(results, list) else []:
        reviewer_id = str(item.get("reviewer_id") or "")
        if not item.get("ok"):
            failures.append({"reviewer_id": reviewer_id, "error": str(item.get("error") or "")})
            continue
        result = item.get("result") or {}
        if not isinstance(result, dict):
            failures.append({"reviewer_id": reviewer_id, "error": "panel result was not a mapping"})
            continue
        uncertainty = result.get("uncertainty") or {}
        if not isinstance(uncertainty, dict):
            uncertainty = {}
        cited_sources = result.get("cited_sources") or []
        if not isinstance(cited_sources, list):
            cited_sources = []
        judgment = str(result.get("judgment") or "")
        statement = _position_text(judgment)
        facts = result.get("facts") if isinstance(result.get("facts"), list) else []
        positions.append(
            {
                "reviewer_id": reviewer_id,
                "position": _position_label(statement),
                "position_statement": statement,
                "judgment_excerpt": judgment[:1200],
                "uncertainty_band": uncertainty.get("band"),
                "cited_sources": [str(source) for source in cited_sources],
                "source_refs": _source_refs(result, cited_sources),
                "would_change_judgment_if": _change_evidence(judgment, facts),
                "stance_seed": result.get("stance_seed") or stance_seed,
            }
        )

    source_sets = {tuple(position["cited_sources"]) for position in positions}
    claim = _claim(query, positions)
    disagreement_type = _disagreement_type(positions)
    combined = " ".join(position["position_statement"] for position in positions).lower()
    explicit_terms = (
        "ascertainment", "sampling bias", "source quality", "missing", "data gap",
        "causal", "pathway", "mechanism", "model",
    )
    classification_basis = (
        "explicit_method_or_evidence_language"
        if any(term in combined for term in explicit_terms)
        else "contrasting_position_labels_only"
    )
    change_evidence = [
        {"reviewer_id": position["reviewer_id"], "evidence": position["would_change_judgment_if"]}
        for position in positions
        if position["would_change_judgment_if"]
    ]
    labels = {position["position"] for position in positions}

    return {
        "schema": "epistack.crux_map.v1",
        "query": query,
        "stance_seed": stance_seed or None,
        "reviewers": [position["reviewer_id"] for position in positions],
        "source_support": {
            "positions": [
                {
                    "reviewer_id": position["reviewer_id"],
                    "position": position["position"],
                    "cited_sources": position["cited_sources"],
                    "source_refs": position["source_refs"],
                    "uncertainty_band": position["uncertainty_band"],
                }
                for position in positions
            ],
            "divergence_signal": "different_citations" if len(source_sets) > 1 else "same_citations",
        },
        "cruxes": [
            {
                "crux_id": _claim_id(claim),
                "claim": claim,
                "question": query,
                "disagreement_type": disagreement_type,
                "disagreement_type_basis": classification_basis,
                "disagreement_type_confidence": (
                    "MEDIUM" if classification_basis == "explicit_method_or_evidence_language" else "LOW"
                ),
                "positions": positions,
                "would_change_judgment_if": change_evidence,
                "divergence_signal": (
                    "contested_claim"
                    if {"supports", "challenges"}.issubset(labels)
                    else "mixed_with_abstention"
                    if "insufficient_evidence" in labels and len(labels) > 1
                    else "aligned_claim"
                ),
            }
        ],
        "failures": failures,
    }
