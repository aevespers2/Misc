from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .core import Finding


@dataclass(frozen=True)
class Decision:
    status: str
    score: int
    reasons: tuple[str, ...]


class DecisionPolicy:
    """Conservative classification policy separated from evidence collection."""

    severity_score = {
        "clean": 0,
        "info": 0,
        "low": 1,
        "medium": 2,
        "high": 3,
        "critical": 4,
    }

    def evaluate(self, findings: Iterable[Finding]) -> Decision:
        observed = tuple(findings)
        score = max((self.severity_score.get(item.severity, 0) for item in observed), default=0)
        # A single heuristic must never become an unsupported compromise verdict.
        critical = [item for item in observed if item.severity == "critical"]
        corroborated = len({item.check for item in critical}) >= 2
        status = "compromised" if corroborated else "investigate" if score >= 2 else "clean"
        reasons = tuple(item.summary for item in observed if self.severity_score.get(item.severity, 0) == score)
        return Decision(status=status, score=score, reasons=reasons)
