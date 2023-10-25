from datasets import swap_dict, swap_dict_loop


def test_swap_dict():
    assert swap_dict({1: "a", 2: "b", 3: "c"}) == {"a": 1, "b": 2, "c": 3}


def test_swap_dict_loop():
    assert swap_dict_loop({1: "a", 2: "b", 3: "c"}) == {"a": 1, "b": 2, "c": 3}
