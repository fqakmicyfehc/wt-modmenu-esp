"""Aimbot extension — smooth-lock onto the closest visible target using
the entity list walked from the world root offset."""
from __future__ import annotations

import math
from typing import Any

from ..host.registry import Feature, FeatureRegistry


def _pick_target(entities: list[dict[str, Any]]) -> dict[str, Any] | None:
    best, best_dist = None, math.inf
    for ent in entities:
        if not ent.get("visible") or ent.get("team") == "self":
            continue
        d = math.hypot(ent["screen_x"] - 960, ent["screen_y"] - 540)
        if d < best_dist:
            best, best_dist = ent, d
    return best


def _tick(ctx: Any) -> None:
    cfg = ctx.registry.get("aimbot").config
    if not cfg.get("enabled"):
        return
    target = _pick_target(ctx.world.entities())
    if target is None:
        return
    smooth = cfg.get("smooth", 6.0)
    dx = (target["screen_x"] - 960) / smooth
    dy = (target["screen_y"] - 540) / smooth
    ctx.input.move_mouse_relative(int(dx), int(dy))


def register(registry: FeatureRegistry) -> None:
    registry.add(Feature(
        name="aimbot",
        category="combat",
        tick=_tick,
        config={"enabled": False, "smooth": 6.0, "fov": 220},
    ))