# Architecture

```
src/
  host/           # bootstrap, plugin loader, registry, logging
  extensions/     # aimbot, esp_overlay, modmenu, wallhack, ...
  core/           # world reader, view matrix, entity models
  infrastructure/ # process handle, memory reader, GLFW overlay
  sidecars/       # Rust espcore binary for hot-path projection
offsets/          # per-patch aces.exe offsets (JSON)
installer/        # PowerShell installer
scripts/          # offset dumper, sidecar builder
tests/            # pytest stubs
```

The host boots, attaches to `aces.exe`, loads `offsets/aces_offsets.json`,
then walks `src/extensions/*.py` looking for a `register(registry)`
function. Every plugin registers a `Feature` with optional `draw` and
`tick` callbacks. The overlay thread calls `draw` on every feature that
has one; the tick loop (in `host.bootstrap`) pumps `tick` at ~144 Hz.