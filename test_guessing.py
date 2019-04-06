import unittest

from guessing import Guessing


class TestGuessing(unittest.TestCase):

    def test_if_is_bigger_when_the_number_is_bigger(self):
        guessing_game = Guessing()
        self.assertTrue(guessing_game.is_bigger())

    def test_if_is_smaller_when_the_number_is_small(self):
        guessing_game = Guessing()
        self.assertFalse(guessing_game.is_smaller())

    def test_if_raise_an_exception_when_no_number_are_passed(self):
        with self.assertRaises(ValueError):
            guessing_game = Guessing()
            guessing_game.secret()


if __name__ == '__main__':
    unittest.main()
