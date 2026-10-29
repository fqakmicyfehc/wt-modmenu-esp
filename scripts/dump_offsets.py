"""Dump current aces.exe offsets into offsets/aces_offsets.json.
Requires the game to be running. Run after each WT major patch."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.infrastructure.process_handle import AcesHandle  # noqa: E402

SIGNATURES = {
    "world_root": "48 8B 05 ?? ?? ?? ?? 48 8B 88",
    "local_player": "48 8B 0D ?? ?? ?? ?? 48 85 C9 74",
    "entity_list": "48 8B 03 48 8B 88 ?? ?? 00 00",
    "view_matrix": "F3 0F 10 05 ?? ?? ?? ?? F3 0F 11",
}


def main() -> int:
    handle = AcesHandle.attach("aces.exe")
    if not handle:
        print("[-] aces.exe not running", file=sys.stderr)
        return 1
    out = {k: handle.base for k in SIGNATURES}  # placeholder offsets
    Path("offsets/aces_offsets.json").write_text(json.dumps(out, indent=2))
    print(f"[+] wrote {len(out)} offsets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())