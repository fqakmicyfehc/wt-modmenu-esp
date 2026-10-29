"""CLI entry — python -m src.host.entry"""
from pathlib import Path
import argparse

from .bootstrap import HostBootstrap


def main() -> int:
    ap = argparse.ArgumentParser(prog="wt-modmenu-esp")
    ap.add_argument("--offsets", default="offsets", type=Path)
    ap.add_argument("--plugins", default="src/extensions", type=Path)
    args = ap.parse_args()
    return HostBootstrap(args.offsets, args.plugins).run()


if __name__ == "__main__":
    raise SystemExit(main())