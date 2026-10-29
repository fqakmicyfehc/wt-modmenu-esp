# Offsets

Offsets are dumped per War Thunder patch. Run:

```
python -m scripts.dump_offsets
```

Known keys:

- `world_root` — root of the entity tree
- `local_player` — pointer to the local player object
- `entity_list` — vector<Entity*> inside world
- `view_matrix` — 4x4 MVP matrix used for world-to-screen

If any offset returns 0 after a patch, the signature has moved. Update
`scripts/dump_offsets.py::SIGNATURES` and open a PR.