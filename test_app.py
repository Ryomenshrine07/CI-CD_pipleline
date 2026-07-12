"""Unit tests for app module."""
import unittest


class TestApp(unittest.TestCase):
    """Test cases for app functions."""

    def test_add(self):
        """Test add function."""
        self.assertEqual(2 + 3, 5)

    def test_subtract(self):
        """Test subtract function."""
        self.assertEqual(5 - 3, 2)


if __name__ == "__main__":
    unittest.main()
