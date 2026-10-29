"""Walks the WT world root and dumps the current entity list."""
from __future__ import annotations

from typing import Any

from ..infrastructure.memory import MemoryReader
from ..host.registry import FeatureRegistry
from .models.entity import Entity


class WorldReader:
    def __init__(self, mem: MemoryReader, registry: FeatureRegistry) -> None:
        self.mem = mem
        self.registry = registry

    def _world_root(self) -> int:
        base = self.mem.handle.base
        root_off = self.registry.offset("world_root")
        if root_off is None:
            raise RuntimeError("world_root offset missing")
        return self.mem.resolve_chain(base, [root_off, 0x10, 0x8])

    def entities(self) -> list[dict[str, Any]]:
        # Real implementation projects each entity through the view matrix
        # and culls off-screen ones. Kept as a stub for the OSS build.
        return []