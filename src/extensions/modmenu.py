"""In-game ModMenu panel — the tabbed overlay that toggles every other
plugin. Rendered last so it always sits on top."""
from __future__ import annotations

from typing import Any

from ..host.registry import Feature, FeatureRegistry


def _draw(ctx: Any) -> None:
    menu = ctx.modmenu
    if not menu.visible:
        return
    menu.begin("WT ModMenu  ::  build 2026.03")
    for tab_name in ("Combat", "Visual", "Misc"):
        menu.tab(tab_name)
        for feat in ctx.registry.all():
            if feat.category.lower() != tab_name.lower():
                continue
            new_val = menu.checkbox(feat.name, feat.enabled)
            if new_val != feat.enabled:
                feat.enabled = new_val
                feat.config["enabled"] = new_val
    menu.end()


def register(registry: FeatureRegistry) -> None:
    registry.add(Feature(name="modmenu", category="ui", draw=_draw))