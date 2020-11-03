from sample.zad3 import Song_lyrics
import unittest


class RomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song_lyrics()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def test_print_first_line_only(self):
        self.assertEqual(self.temp.byLine(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
