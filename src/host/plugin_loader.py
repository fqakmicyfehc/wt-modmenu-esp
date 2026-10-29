"""Discovers and loads extension plugins from src/extensions."""
from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Iterable

from .registry import FeatureRegistry
from .logging_util import get_logger

log = get_logger(__name__)


class PluginLoader:
    def __init__(self, registry: FeatureRegistry, plugins_dir: Path) -> None:
        self.registry = registry
        self.plugins_dir = plugins_dir

    def _iter_plugin_files(self) -> Iterable[Path]:
        if not self.plugins_dir.exists():
            log.warning("plugin dir %s missing", self.plugins_dir)
            return
        yield from sorted(self.plugins_dir.glob("*.py"))

    def _load_module(self, path: Path) -> ModuleType | None:
        spec = importlib.util.spec_from_file_location(
            f"wt_ext_{path.stem}", path)
        if not spec or not spec.loader:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def discover_and_load(self) -> None:
        for path in self._iter_plugin_files():
            if path.name.startswith("_"):
                continue
            mod = self._load_module(path)
            if not mod:
                continue
            register = getattr(mod, "register", None)
            if callable(register):
                register(self.registry)
                log.info("loaded plugin %s", path.stem)
            else:
                log.warning("plugin %s has no register()", path.stem)