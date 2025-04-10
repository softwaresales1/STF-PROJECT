from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Test that 1 + 1 equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_basic_subtraction(self):
        """
        Test that 2 - 1 equals 1.
        """
        self.assertEqual(2 - 1, 1)
