# Mocking

Mocking allows you to simulate objects, functions, and behaviors, making your tests more isolated and predictable. 
It also allows you to focus on the specific function you want to test by isolating it from dependencies that could 
introduce complexity or unexpected behavior.

pytest-mock is a plugin for pytest that provides easy access to mocking capabilities. It builds on top of Python's
built-in unittest, simplifying the process of mocking during testing.

## Basics of Mocking with pytest-mock

Mocking can be thought of as creating a "dummy" version of a component that mimics real behavior.  It is especially
helpful when you need to test how functions or classes interact with external components like databases or external
APIs.

### Introduction to mocking

mock object
: simulates the behavior of a real object

mock objects are often used in unit tests to isolate components and test their 
behavior without executing dependent code.

Mocking is useful when the real object:

- is difficult to create or configure
- is time-consuming to use (e.g., accessing a remote database)
- has side effects that should be avoided during testing (e.g., sending emails, incurring costs)

### Using the mocker fixture

pytest-mock provides a `mocker` fixture, making creating and controlling mock objects easy.
The `mocker` fixture is powerful and integrates into your pytest tests.

### Mocking functions or class methods

```python
# production code
def calculate_discount(price, discount_provider):
    discount = discount_provider.get_discount()
    return price - (price * discount / 100)

# test code
def test_calculate_discount(mocker):
    # Mock the get_discount method
    mock_discount_provider = mocker.Mock()
    mock_discount_provider.get_discount.return_value = 10  # Mocked discount value
    # Call the function with the mocked dependency
    result = calculate_discount(100, mock_discount_provider)
    # Assert the calculated discount is correct
    assert result == 90
    mock_discount_provider.get_discount.assert_called_once()
```

### Mocking time-dependent code

```python
# production code
import time
def long_running_task():
    time.sleep(5)  # Simulate a long delay
    return "Task Complete"

# test code
def test_long_running_task(mocker):
    # Mock the sleep function in the time module
    mocker.patch("time.sleep", return_value=None)
    # Call the function
    result = long_running_task()
    # Assert the result is correct
    assert result == "Task Complete"
```

### Mocking object attributes

```python
# production code
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def is_adult(self):
        return self.age >= 18

# test code
def test_user_is_adult(mocker):
    # Create a User object
    user = User(name="Alice", age=17)
    # Mock the is_adult property
    mocker.patch.object(User, "is_adult", new_callable=mocker.PropertyMock, return_value=True)
    # Assert the mocked property value
    assert user.is_adult is True
```

### Mock side effects

```python
import pytest

# production code
def process_payment(payment_gateway, amount):
    response = payment_gateway.charge(amount)
    if response == "Success":
        return "Payment processed successfully"
    else:
        raise ValueError("Payment failed")

# test code
def test_process_payment_with_side_effects(mocker):
    # Mock the charge method of the payment gateway
    mock_payment_gateway = mocker.Mock()
    # Add side effects: Success on first call, raise exception on second call
    mock_payment_gateway.charge.side_effect = ["Success", ValueError("Insufficient funds")]
    # Test successful payment
    assert process_payment(mock_payment_gateway, 100) == "Payment processed successfully"
    # Test payment failure
    with pytest.raises(ValueError, match="Insufficient funds"):
        process_payment(mock_payment_gateway, 200)
    # Verify the mock's behavior
    assert mock_payment_gateway.charge.call_count == 2
```

### Spying on functions

```python
# production code
def log_message(logger, message):
    logger.info(message)
    return f"Logged: {message}"

# test code
def test_log_message_with_spy(mocker):
    # Spy on the info method of the logger
    mock_logger = mocker.Mock()
    spy_info = mocker.spy(mock_logger, "info")
    # Call the function
    result = log_message(mock_logger, "Test message")
    # Assert the returned value
    assert result == "Logged: Test message"
    # Verify the spy behavior
    spy_info.assert_called_once_with("Test message")
    assert spy_info.call_count == 1
```

## References

- [Python Mocking 101: Fake It Before You Make It](https://realpython.com/python-mock-library/)
- [pytest-mock Tutorial: A Beginner's Guide to Mocking in Python](https://www.datacamp.com/tutorial/pytest-mock)
- 