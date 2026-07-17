from __future__ import annotations

from dataclasses import dataclass, field
from importlib.metadata import entry_points
from typing import Any, Iterable, Protocol, runtime_checkable

from .core import Finding

API_VERSION = "1"


@dataclass(frozen=True)
class CapabilityContext:
    config: dict[str, Any] = field(default_factory=dict)
    evidence: dict[str, Any] = field(default_factory=dict)
    dry_run: bool = True


@dataclass(frozen=True)
class CapabilityResult:
    namespace: str
    evidence: dict[str, Any] = field(default_factory=dict)
    findings: tuple[Finding, ...] = ()


@runtime_checkable
class Capability(Protocol):
    """Stable extension contract for passive or explicitly authorized capabilities."""

    name: str
    api_version: str
    category: str
    description: str
    mutates_target: bool

    def run(self, context: CapabilityContext) -> CapabilityResult: ...


class ExtensionError(RuntimeError):
    pass


class Registry:
    def __init__(self) -> None:
        self._capabilities: dict[str, Capability] = {}

    def register(self, capability: Capability) -> None:
        if not isinstance(capability, Capability):
            raise ExtensionError("Extension does not satisfy the Capability protocol")
        if capability.api_version != API_VERSION:
            raise ExtensionError(
                f"Unsupported API version {capability.api_version!r}; expected {API_VERSION!r}"
            )
        if capability.name in self._capabilities:
            raise ExtensionError(f"Duplicate extension name: {capability.name}")
        if capability.mutates_target:
            raise ExtensionError(
                f"Extension {capability.name!r} declares target mutation; "
                "mutation is prohibited in the general capability registry"
            )
        self._capabilities[capability.name] = capability

    def discover(self, group: str = "phantomblock.capabilities") -> list[str]:
        loaded: list[str] = []
        for entry_point in entry_points(group=group):
            capability = entry_point.load()()
            self.register(capability)
            loaded.append(capability.name)
        return loaded

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._capabilities))

    def capabilities(self, selected: Iterable[str] | None = None) -> tuple[Capability, ...]:
        names = tuple(selected) if selected is not None else self.names()
        missing = sorted(set(names) - self._capabilities.keys())
        if missing:
            raise ExtensionError(f"Unknown extensions: {', '.join(missing)}")
        return tuple(self._capabilities[name] for name in names)

    def run(
        self,
        context: CapabilityContext,
        selected: Iterable[str] | None = None,
    ) -> tuple[CapabilityResult, ...]:
        return tuple(capability.run(context) for capability in self.capabilities(selected))
