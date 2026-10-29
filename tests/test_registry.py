from src.host.registry import Feature, FeatureRegistry


def test_register_and_lookup():
    reg = FeatureRegistry()
    reg.add(Feature(name="esp", category="visual"))
    assert reg.get("esp").category == "visual"


def test_duplicate_warns_but_keeps_first():
    reg = FeatureRegistry()
    reg.add(Feature(name="aimbot", category="combat", enabled=False))
    reg.add(Feature(name="aimbot", category="combat", enabled=True))
    assert reg.get("aimbot").enabled is False


def test_offsets_roundtrip(tmp_path):
    import json
    f = tmp_path / "aces_offsets.json"
    f.write_text(json.dumps({"world_root": 0xDEAD}))
    reg = FeatureRegistry()
    reg.load_offsets(f)
    assert reg.offset("world_root") == 0xDEAD