import pytest

def mysum(a: int, b: int) -> int:
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (1, 1, 2),
    (1, 0, 1),
    (0, 0, 0),
    (-1, 1, 0),
    (-1, -1, -2),
    (-1, 0, -1),
    (0, -1, -1),
],
ids=[
 "positive numbers",
 "positive numbers with 1",
 "positive and zero",
 "zero",
 "negative and positive",
 "negative numbers",
 "negative and zero",
 "zero and negative",
])
def test_sum(a: int, b: int, expected: int):
    # Act
    result = mysum(a, b)

    # Assert
    assert result == expected
