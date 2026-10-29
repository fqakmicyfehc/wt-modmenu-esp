"""Attach to aces.exe and expose base address + pid."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

try:
    import pymem
    _HAS_PYMEM = True
except ImportError:
    _HAS_PYMEM = False


@dataclass
class AcesHandle:
    pid: int
    base: int
    _pm: object = None

    @classmethod
    def attach(cls, exe: str = "aces.exe") -> Optional["AcesHandle"]:
        if not _HAS_PYMEM:
            return None
        try:
            pm = pymem.Pymem(exe)
        except Exception:
            return None
        base = pymem.process.module_from_name(
            pm.process_handle, exe).lpBaseOfDll
        return cls(pid=pm.process_id, base=base, _pm=pm)

    def read_u64(self, addr: int) -> int:
        return self._pm.read_longlong(addr)  # type: ignore[union-attr]

    def write_i32(self, addr: int, value: int) -> None:
        self._pm.write_int(addr, value)  # type: ignore[union-attr]