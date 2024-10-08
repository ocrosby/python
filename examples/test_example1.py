import pytest

from typing import Union
from examples.example1 import get_time, get_total_discount

def test_get_time():
    # Arrange
    # Nothing to arrange

    # Act
    result = get_time()

    # Assert
    assert result is not None
    assert isinstance(result, str)

@pytest.mark.parametrize("prices, percent, expected, error_message", [
    ([100, 200, 300], 0.1, 540.0, None),
    ([50, 50, 50], 0.2, 120.0, None),
    ([10, 20, 30], 0.5, 30.0, None),
    ([0, 0, 0], 0.1, 0.0, None),
    ([100], 0.0, 100.0, None),
    ([100], 1.0, 0.0, None),
    ([100], -0.1, pytest.raises(ValueError), "ValueError: Invalid discount rate: -0.1. Must be between 0 and 1 inclusive."),
    ([100], 1.1, pytest.raises(ValueError), "ValueError: Invalid discount rate: 1.1. Must be between 0 and 1 inclusive."),
    ([-100, 200], 0.1, pytest.raises(ValueError), "ValueError: All prices must be non-negative numbers."),
    ([100, '200'], 0.1, pytest.raises(ValueError), "ValueError: All prices must be non-negative numbers."),
], ids=[
    "10% discount on [100, 200, 300]",
    "20% discount on [50, 50, 50]",
    "50% discount on [10, 20, 30]",
    "10% discount on [0, 0, 0]",
    "0% discount on [100]",
    "100% discount on [100]",
    "Invalid discount rate -0.1",
    "Invalid discount rate 1.1",
    "Negative price in list",
    "Non-numeric price in list"
])
def test_get_total_discount(prices: list[any], percent: float, expected: Union[float | Exception], error_message: str):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with expected(match=error_message):
            get_total_discount(prices, percent)
    else:
        result = get_total_discount(prices, percent)
        assert result == expected