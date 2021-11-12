import pytest

from forecast.utils import calculate_stats


@pytest.mark.parametrize(
    ("forecast", "expected"),
    [
        ([], {}),
        ([20], {"average": 20, "maximum": 20, "median": 20, "minimum": 20}),
        (
            [20, 10.5, 15, 9],
            {"average": 13.625, "maximum": 20, "median": 12.75, "minimum": 9},
        ),
    ],
)
def test_calculate_stats(forecast, expected):
    stats = calculate_stats(forecast)

    assert stats == expected
