from sample.zad3 import Song_lyrics
import unittest


class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song_lyrics()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def test_print_first_Byline_only(self):
        self.assertEqual(self.temp.byLine(1),
                         'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_print_second_Byline_only(self):
        self.assertEqual(self.temp.byLine(2),
                         'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_dont_accept_value_higher_than_number_of_lines(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLine(24)

    def test_dont_accept_value_lower_than_1(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLine(0)

    def test_dont_accept_anything_bout_integers(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLine("Wiktor")

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
