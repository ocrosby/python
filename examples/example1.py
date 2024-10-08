from datetime import datetime

from collections.abc import Iterable

# 1. Short and concise
# 2. Specify a return type
# 3. Makae as simple and reusable as possible
# 4. Document all your functions
# 5. Handle errors appropriately

def get_time() -> str:
    """
    Get the current time

    :return: The current time in HH:MM:SS format
    :rtype: str
    """
    now: datetime = datetime.now()

    return f'{now:%X}'

def get_total_discount(prices: Iterable[float], percent: float) -> float:
    """
    Calculate the total price after applying a discount.

    This function calculates the total sum of prices in the provided list and then applies a
    discount based on the given discount rate. If the discount rate is invalid (e.g., negative
    or grater than 1), the function raises a ValueError.

    :param prices: List of item prices
    :param percent: Discount percentage (between 0 and 1)
    :type percent: float, optional
    :return: The total price after applying the discount.
    :rtype: float
    :raises ValueError: If the discount rate is not between 0 and 1 inclusive, or if prices
                        contain non-numeric values.

    :Example:
    >>> get_total_discount([100.0, 50.0, 25.0], 0.2)
    140.0
    """
    if not (0 <= percent <= 1):
        raise ValueError(f'Invalid discount rate: {percent}. Must be between 0 and 1 inclusive.')

    if not all(isinstance(price, (int, float)) and price >= 0 for price in prices):
        raise ValueError('All prices must be non-negative numbers.')

    total: float = sum(prices)

    return total * (1 - percent)


if __name__ == "__main__":
    print(get_time())
