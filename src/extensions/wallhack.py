"""Wallhack extension — disables geometry occlusion for enemy vehicles
by flipping the visibility bit in the render pass descriptor."""
from __future__ import annotations

from typing import Any

from ..host.registry import Feature, FeatureRegistry


def _tick(ctx: Any) -> None:
    cfg = ctx.registry.get("wallhack").config
    if not cfg.get("enabled"):
        return
    off = ctx.registry.offset("local_player")
    if off is None:
        return
    addr = ctx.memory.resolve_chain(ctx.handle.base, [off, 0x48, 0x1C])
    try:
        ctx.handle.write_i32(addr, 0)
    except Exception:
        pass


def register(registry: FeatureRegistry) -> None:
    registry.add(Feature(
        name="wallhack",
        category="visual",
        tick=_tick,
        config={"enabled": False},
    ))