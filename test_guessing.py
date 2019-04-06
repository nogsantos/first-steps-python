import unittest

from guessing import Guessing


class TestGuessing(unittest.TestCase):

    def test_if_is_bigger_when_the_number_is_bigger(self):
        self.assertTrue(Guessing.is_biggest(11, 10))

    def test_if_is_smaller_when_the_number_is_small(self):
        self.assertFalse(Guessing.is_smaller(11, 10))

    def test_if_raise_an_exception_when_no_number_are_passed(self):
        with self.assertRaises(ValueError):
            g = Guessing()
            g.secret()
