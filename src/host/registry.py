"""Feature registry shared by the host and every extension."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from .logging_util import get_logger

log = get_logger(__name__)

FeatureFn = Callable[[Any], None]


@dataclass
class Feature:
    name: str
    category: str
    enabled: bool = False
    draw: FeatureFn | None = None
    tick: FeatureFn | None = None
    config: dict[str, Any] = field(default_factory=dict)


class FeatureRegistry:
    def __init__(self) -> None:
        self._features: dict[str, Feature] = {}
        self.offsets: dict[str, int] = {}

    def add(self, feature: Feature) -> None:
        if feature.name in self._features:
            log.warning("feature %s already registered", feature.name)
        self._features[feature.name] = feature

    def get(self, name: str) -> Feature | None:
        return self._features.get(name)

    def all(self) -> list[Feature]:
        return list(self._features.values())

    def load_offsets(self, path: Path) -> None:
        if not path.exists():
            log.warning("offset file %s not found", path)
            return
        self.offsets = json.loads(path.read_text())

    def offset(self, key: str) -> int | None:
        return self.offsets.get(key)