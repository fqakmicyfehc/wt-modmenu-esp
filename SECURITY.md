# Security Policy

wt-modmenu-esp is a local-only hobbyist tool. It does not phone home,
does not ship telemetry, and does not include any remote loader.

## Reporting

Open a private issue or email the maintainers listed in `docs/maintainers.md`.
Please include: War Thunder build number, Windows version, and the
offset dump produced by `scripts/dump_offsets.py`.

## Scope

- **In scope**: memory-safety bugs in the injector, RCE in the plugin
  loader, arbitrary file write from the config parser.
- **Out of scope**: Anti-Cheat detections, account bans, or issues
  caused by third-party plugins. Use at your own risk.

## Disclaimer

This software is provided for **educational and research purposes only**.
Running it against live servers violates Gaijin's EULA and may result
in a permanent ban. The maintainers accept no responsibility for
account loss.