import pytest
from gameplay import goap_planner as mod

CASES = [
    ("key", 'm.normalize_key("HasAmmo") == "hasammo"'),
    ("cost", 'm.action_cost(1, 2, 2) == 5'),
    ("goal", "m.goal_satisfied({'a': 1}, {'a': 1}) is True"),
    ("cache", 'm.cache_key("npc1", "goal") == "npc1:goal"'),
    ("effects", 'm.effect_order([1, 2]) == [1, 2]'),
    ("fallback", 'm.fallback_state("prev", "cur") == "prev"'),
    ("lock", 'm.lock_blackboard(True) is True'),
    ("restore", "m.restore_snapshot({'a': 1}) == {'a': 1}"),
    ("depth", 'm.depth_limit(5, 3) == 3'),
    ("save", 'm.save_plan([1, 2]) == (1, 2)'),
    ("pre", "m.precondition_match({'a': 1}, {'a': 1}) is True"),
    ("total", 'm.plan_cost([1, 2, 3]) == 6'),
    ("applicable", "m.action_applicable({'a': 1}, {'a': 1}) is True"),
    ("search", 'm.search_key("s", 2) == "s:2"'),
    ("isolation", 'm.npc_isolation("npc1", {"npc1"}) is False')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
