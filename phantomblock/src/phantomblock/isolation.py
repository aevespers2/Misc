from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Protocol


@dataclass
class IsolationResult:
    device: str
    port: str
    action: str
    applied: bool
    timestamp: str
    detail: str

    def to_dict(self) -> dict:
        return asdict(self)


class SwitchAdapter(Protocol):
    def isolate(self, device: str, port: str) -> IsolationResult: ...


class DryRunSwitchAdapter:
    """Default adapter: records intent and never changes network state."""

    def isolate(self, device: str, port: str) -> IsolationResult:
        return IsolationResult(
            device=device,
            port=port,
            action="disable-port",
            applied=False,
            timestamp=datetime.now(timezone.utc).isoformat(),
            detail="Dry run only. Configure a reviewed vendor adapter to apply changes.",
        )


class GuardedCommandAdapter:
    """Minimal integration seam for an operator-supplied switch command.

    The command is intentionally not executed in the MVP. Production adapters should use
    vendor APIs, pinned TLS identities, least-privilege credentials, allowlists, approvals,
    idempotency, and rollback verification.
    """

    def isolate(self, device: str, port: str) -> IsolationResult:
        return IsolationResult(
            device=device,
            port=port,
            action="disable-port",
            applied=False,
            timestamp=datetime.now(timezone.utc).isoformat(),
            detail="Blocked: no production switch adapter is configured.",
        )
