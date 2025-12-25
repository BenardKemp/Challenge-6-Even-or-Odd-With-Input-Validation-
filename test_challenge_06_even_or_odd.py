import pytest

from challenge_06_even_or_odd import even_or_odd


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "Even"),
        (1, "Odd"),
        (2, "Even"),
        (7, "Odd"),
        (10, "Even"),
        (-1, "Odd"),
        (-2, "Even"),
        (-99, "Odd"),
        (100, "Even"),
    ],
)
def test_even_or_odd_valid_integers(n, expected):
    assert even_or_odd(n) == expected


@pytest.mark.parametrize(
    "bad_value",
    [
        True,
        False,
        2.0,
        -3.5,
        "4",
        "odd",
        None,
        [],
        {},
        (2,),
        object(),
    ],
)
def test_even_or_odd_rejects_non_integers_and_bools(bad_value):
    with pytest.raises(TypeError):
        even_or_odd(bad_value)