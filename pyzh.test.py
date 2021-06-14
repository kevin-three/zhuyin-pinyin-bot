import unittest

from pyzh import split, convert

class TestSplit(unittest.TestCase):

    def test_simple(self):
        s = "hello world"
        self.assertEqual(split(s), [("hello", " "), ("world", "")])

    def test_trailing(self):
        s = "hello world  "
        self.assertEqual(split(s), [("hello", " "), ("world", "  ")])

    def test_opening(self):
        s = "  hello world"
        self.assertEqual(split(s), [("", "  "), ("hello", " "), ("world", "")])

    def test_open_trail(self):
        s = "  hello   world    "
        self.assertEqual(split(s), [("", "  "), ("hello", "   "), ("world", "    ")])

class TestConvert(unittest.TestCase):

    def test_pinyin(self):
        s = "ni hao"
        self.assertEqual(convert(s), "ㄋㄧ˙ ㄏㄠ˙")

    def test_mixed_pinyin(self):
        s = "the word that I want to say is ni hao"
        self.assertEqual(convert(s), "the word that I want to say is ㄋㄧ˙ ㄏㄠ˙")

    def test_numbered_pinyin(self):
        s = "ni3 hao3"
        self.assertEqual(convert(s), "ㄋㄧˇ ㄏㄠˇ")

    def test_spaceless_pinyin(self):
        s = "nihao"
        self.assertEqual(convert(s), "ㄋㄧ˙ ㄏㄠ˙")

    def test_spaceless_numbered_pinyin(self):
        s = "ni3hao3"
        self.assertEqual(convert(s), "ㄋㄧˇ ㄏㄠˇ")

    def test_tone_pinyin(self):
        s = "nǐ hǎo"
        self.assertEqual(convert(s), "ㄋㄧˇ ㄏㄠˇ")

    def test_zhuyin(self):
        s = "ㄋㄧˇ ㄏㄠˇ"
        self.assertEqual(convert(s), "nǐ hǎo")

    def test_spaceless_zhuyin(self):
        s = "ㄋㄧˇㄏㄠˇ"
        self.assertEqual(convert(s), "nǐhǎo")

    def test_mixed_zhuyin(self):
        s = "the word that I want to say is ㄋㄧ ㄏㄠ"
        self.assertEqual(convert(s), "the word that I want to say is nī hāo")


if __name__ == "__main__":
    unittest.main()
