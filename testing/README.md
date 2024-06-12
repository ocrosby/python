# Testing

```python3
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

In order to skip a unittest in Python

```python3
import unittest

class TestSum(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(True, "skipping if True")
    def test_skip_if(self):
        self.fail("shouldn't happen")

    @unittest.skipUnless(False, "skipping unless False")
    def test_skip_unless(self):
        self.fail("shouldn't happen")

    def test_normal(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
```

Asserting that a function raises an exception

```python3
import unittest

def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))

class ExceptionTest(unittest.TestCase):
    def test_trap_locally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def test_assert_raises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')
```

Asserting that a function raises an exception with a specific message

```python3
import unittest

def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))

class ExceptionTest(unittest.TestCase):
    def test_message(self):
        with self.assertRaisesRegex(ValueError, 'Invalid value: a'):
            raises_error('a')
```

Asserting on the return value

```python3
import unittest

def my_function(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(my_function(1, 2), 3)
```

Asserting on the return value with a message

```python3
import unittest

def my_function(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(my_function(1, 2), 3, "Should be 3")
```

Asserting that a return value is True or False

```python3
import unittest

def is_even(n):
    return n % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(1))
```

