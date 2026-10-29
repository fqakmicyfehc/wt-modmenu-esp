from src.extensions.aimbot import _pick_target


def test_picks_closest_visible():
    ents = [
        {"screen_x": 100, "screen_y": 100, "visible": True, "team": "enemy"},
        {"screen_x": 960, "screen_y": 540, "visible": True, "team": "enemy"},
        {"screen_x": 960, "screen_y": 540, "visible": True, "team": "self"},
    ]
    t = _pick_target(ents)
    assert t is not None
    assert t["team"] == "enemy"


def test_none_when_all_hidden():
    assert _pick_target([{"screen_x": 0, "screen_y": 0,
                          "visible": False, "team": "enemy"}]) is None