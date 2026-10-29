"""Host bootstrap: opens the process handle, loads offsets, spins up
the plugin loader and overlay thread."""
from __future__ import annotations

import logging
import threading
from pathlib import Path
from typing import Optional

from ..infrastructure.process_handle import AcesHandle
from ..infrastructure.overlay import OverlayWindow
from .registry import FeatureRegistry
from .plugin_loader import PluginLoader
from .logging_util import get_logger

log = get_logger(__name__)


class HostBootstrap:
    def __init__(self, offsets_dir: Path, plugins_dir: Path) -> None:
        self.offsets_dir = offsets_dir
        self.plugins_dir = plugins_dir
        self.handle: Optional[AcesHandle] = None
        self.registry = FeatureRegistry()
        self.loader = PluginLoader(self.registry, plugins_dir)
        self._overlay_thread: Optional[threading.Thread] = None

    def attach(self) -> bool:
        self.handle = AcesHandle.attach("aces.exe")
        if not self.handle:
            log.error("aces.exe not found — is War Thunder running?")
            return False
        log.info("attached to aces.exe pid=%d base=0x%x",
                 self.handle.pid, self.handle.base)
        return True

    def load_offsets(self) -> None:
        self.registry.load_offsets(self.offsets_dir / "aces_offsets.json")

    def start_overlay(self) -> None:
        overlay = OverlayWindow(self.registry, title="WT ModMenu | ESP")
        self._overlay_thread = threading.Thread(
            target=overlay.run, name="modmenu-overlay", daemon=True)
        self._overlay_thread.start()

    def run(self) -> int:
        if not self.attach():
            return 1
        self.load_offsets()
        self.loader.discover_and_load()
        self.start_overlay()
        log.info("ModMenu host running — press F8 to toggle ESP")
        self._overlay_thread.join()
        return 0