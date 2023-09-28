"""
Sample tests
"""


from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        # Arrange
        # Act
        res = calc.add(5, 6)
        # Assert
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtract numbers"""
        # Arrange
        # Act
        res = calc.subtract(15, 10)
        # Assert
        self.assertEqual(res, 5)
