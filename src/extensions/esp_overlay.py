"""ESP / wallhack box renderer — draws players, tanks, and air targets
through geometry using the projected entity list from the host."""
from __future__ import annotations

from typing import Any

from ..host.registry import Feature, FeatureRegistry


def _draw(ctx: Any) -> None:
    cfg = ctx.registry.get("esp").config
    if not cfg.get("enabled"):
        return
    draw = ctx.renderer
    for ent in ctx.world.entities():
        if not ent.get("visible"):
            continue
        color = (255, 40, 40) if ent.get("team") != "self" else (40, 200, 255)
        draw.box(ent["box"], color=color, thickness=2)
        if cfg.get("show_names"):
            draw.text(ent["box"][:2], ent.get("name", "unknown"), color=color)
        if cfg.get("show_distance"):
            draw.text((ent["box"][0], ent["box"][1] - 14),
                      f"{ent['distance']:.0f}m", color=color)


def register(registry: FeatureRegistry) -> None:
    registry.add(Feature(
        name="esp",
        category="visual",
        draw=_draw,
        config={"enabled": False, "show_names": True,
                "show_distance": True, "max_dist": 1500},
    ))