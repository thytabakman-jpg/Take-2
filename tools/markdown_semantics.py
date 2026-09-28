"""Deterministic Markdown semantic intake for Take-2.

The analyzer reads the full UTF-8 Markdown body and extracts structural/semantic signals.
It is deliberately fail-closed: weak or conflicting evidence produces role=OPEN rather
than a confident guess.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import re
from pathlib import Path

ROLE_TERMS = {
    "architecture": (
        "architecture", "architectural", "kernel", "schema", "ontology",
        "invariant", "primitive", "contract", "interface", "system design",
    ),
    "project": (
        "project", "scope", "deliverable", "milestone", "workstream",
        "project manager", "acceptance criteria",
    ),
    "tool": (
        "tool", "operator", "controller", "runtime", "wrapper", "assert",
        "improvement core", "improvecore", "icc", "hf2", "pd", "goal",
    ),
    "plan": (
        "plan", "next step", "roadmap", "todo", "to do", "phase", "sequence",
        "implementation step",
    ),
    "decision": (
        "decision", "decided", "rationale", "accepted", "rejected",
        "tradeoff", "trade-off", "option",
    ),
    "status": (
        "status", "current state", "progress", "blocked", "complete", "completed",
        "open issue", "remaining", "done",
    ),
    "research": (
        "research", "hypothesis", "method", "evidence", "experiment",
        "analysis", "results", "finding", "literature",
    ),
    "specification": (
        "specification", "spec", "requirements", "must", "shall", "input",
        "output", "precondition", "postcondition", "acceptance test",
    ),
}

SYSTEM_REF_PATTERN = re.compile(
    r"\b(?:ICC(?:[- ]?\d+)?|IC[- ]?\d+|HF[12]|PD|ASSERT|GOAL|MT|Jane|"
    r"Improvement\s*Core|ImproveCore|Take[- ]?\d+)\b",
    re.IGNORECASE,
)
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
LINK_PATTERN = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
WIKI_LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)

@dataclass(frozen=True)
class MarkdownSemantics:
    title: str | None
    headings: tuple[str, ...]
    links: tuple[str, ...]
    system_references: tuple[str, ...]
    role: str
    confidence: str
    scores: dict[str, int]
    reasons: tuple[str, ...]
    word_count: int

    def as_dict(self) -> dict:
        return asdict(self)

def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()

def _frontmatter_title(text: str) -> str | None:
    m = FRONTMATTER_PATTERN.search(text)
    if not m:
        return None
    for line in m.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and key.strip().lower() == "title":
            value = value.strip().strip("'\"")
            return value or None
    return None

def analyze_markdown_text(text: str) -> MarkdownSemantics:
    headings = tuple(m.group(2).strip() for m in HEADING_PATTERN.finditer(text))
    title = _frontmatter_title(text) or (headings[0] if headings else None)
    links = tuple(
        dict.fromkeys(
            [m.group(2).strip() for m in LINK_PATTERN.finditer(text)]
            + [m.group(1).strip() for m in WIKI_LINK_PATTERN.finditer(text)]
        )
    )
    system_refs = tuple(dict.fromkeys(m.group(0) for m in SYSTEM_REF_PATTERN.finditer(text)))

    normalized = _normalize(text)
    heading_text = _normalize(" ".join(headings))
    title_text = _normalize(title or "")
    scores: dict[str, int] = {}
    reasons: list[str] = []

    for role, terms in ROLE_TERMS.items():
        score = 0
        matched: list[str] = []
        for term in terms:
            t = term.lower()
            body_hits = len(re.findall(r"(?<!\w)" + re.escape(t) + r"(?!\w)", normalized))
            heading_hits = len(re.findall(r"(?<!\w)" + re.escape(t) + r"(?!\w)", heading_text))
            title_hits = len(re.findall(r"(?<!\w)" + re.escape(t) + r"(?!\w)", title_text))
            contribution = min(body_hits, 4) + 2 * min(heading_hits, 2) + 3 * min(title_hits, 1)
            if contribution:
                score += contribution
                matched.append(term)
        scores[role] = score
        if matched:
            reasons.append(f"{role}:{','.join(matched[:5])}")

    if system_refs:
        scores["tool"] += min(5, len(system_refs))
        reasons.append("system-references:" + ",".join(system_refs[:5]))

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    top_role, top_score = ranked[0]
    second_score = ranked[1][1] if len(ranked) > 1 else 0

    if top_score < 3:
        role, confidence = "open", "LOW"
        reasons.append("insufficient-semantic-evidence")
    elif top_score == second_score:
        role, confidence = "open", "LOW"
        reasons.append("conflicting-top-roles")
    elif top_score - second_score == 1:
        role, confidence = top_role, "MEDIUM"
        reasons.append("narrow-margin")
    else:
        role = top_role
        confidence = "HIGH" if top_score >= 6 and top_score - second_score >= 2 else "MEDIUM"

    words = re.findall(r"\b[\w'-]+\b", text)
    return MarkdownSemantics(
        title=title,
        headings=headings,
        links=links,
        system_references=system_refs,
        role=role,
        confidence=confidence,
        scores=scores,
        reasons=tuple(reasons),
        word_count=len(words),
    )

def analyze_markdown(path: Path) -> MarkdownSemantics:
    return analyze_markdown_text(path.read_text(encoding="utf-8-sig"))
