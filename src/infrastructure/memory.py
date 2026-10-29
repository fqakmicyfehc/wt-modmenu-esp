"""Thin pattern-scanner / pointer-chain helper used by extensions."""
from __future__ import annotations

import re
from typing import Iterable

from .process_handle import AcesHandle


class MemoryReader:
    def __init__(self, handle: AcesHandle) -> None:
        self.handle = handle

    def resolve_chain(self, base: int, offsets: Iterable[int]) -> int:
        addr = base
        for off in offsets:
            addr = self.handle.read_u64(addr + off)
        return addr

    def scan_pattern(self, pattern: str, module_range: tuple[int, int]) -> int | None:
        rx = re.compile(pattern.replace("??", ".").replace(" ", ""), re.I)
        start, end = module_range
        chunk = 0x1000
        for addr in range(start, end, chunk):
            try:
                data = self.handle._pm.read_bytes(addr, chunk)  # type: ignore[union-attr]
            except Exception:
                continue
            m = rx.search(data)
            if m:
                return addr + m.start()
        return None