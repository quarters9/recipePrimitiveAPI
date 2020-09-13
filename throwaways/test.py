from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test add function"""
        self.assertEqual(add(3,8), 11)

    def test_subtract_numbers(self):
        """Test sub function"""
        self.assertEqual(subtract(5, 11), 6)

