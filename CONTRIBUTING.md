# Contributing to wt-modmenu-esp

Thanks for hacking on the ModMenu. This project is a community research
effort around War Thunder client-side modding — aimbot, ESP, wallhack,
and the in-game ModMenu overlay — built as a plugin-host so features
stay modular.

## Ground rules

- Every new feature must ship as a plugin under `src/extensions/`.
- Do not hardcode patch offsets in core code — put them in
  `src/host/registry.py` or the offset dumper.
- Keep the overlay draw path allocation-free per frame.
- No `except: pass`. Log through `src/host/logging_util.py`.

## Workflow

1. Fork, branch from `main` as `feat/<plugin-name>`.
2. `pip install -r requirements.txt`
3. Drop new offsets into `offsets/` and run `python -m scripts.dump_offsets`.
4. Add a stub test in `tests/`.
5. Open a PR — CI runs `pytest` and `python -m host.smoke`.

## Code style

Black, 100 cols, type hints required on public functions. Rust/C++
sidecars go under `src/sidecars/`.