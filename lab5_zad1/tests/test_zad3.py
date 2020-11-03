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

    def test_byLines_interval_from_1_to_3(self):
        self.assertEqual(self.temp.byLineInterval(1, 3),
                         'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.' +
                         'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.' +
                         'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_byLines_dont_accept_lower_first_value(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLineInterval(0, 3)

    def test_byLines_dont_accept_higher_second_value(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLineInterval(12, 14)

    def test_byLines_dont_accept_lower_second_value(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLineInterval(2, 1)

    def test_byLines_dont_accept_higher_first_value(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLineInterval(14, 8)

    def test_byLines_dont_accept_nothing_bout_integers(self):
        with self.assertRaisesWithMessage(ValueError):
            self.temp.byLineInterval('1', '3')

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
