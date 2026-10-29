"""Smoke check used by CI — verifies the host can import every plugin."""
from pathlib import Path

from .plugin_loader import PluginLoader
from .registry import FeatureRegistry


def main() -> int:
    reg = FeatureRegistry()
    loader = PluginLoader(reg, Path(__file__).resolve().parents[1] / "extensions")
    loader.discover_and_load()
    names = sorted(f.name for f in reg.all())
    print("features:", names)
    return 0 if names else 1


if __name__ == "__main__":
    raise SystemExit(main())