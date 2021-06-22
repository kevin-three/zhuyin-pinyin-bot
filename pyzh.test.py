import unittest

from pyzh import split, convert, annotate

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

    def test_tone_spaceless_pinyin(self):
        s = "nǐhǎo"
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


class TestAnnotate(unittest.TestCase):

    def test_annotate(self):
        s = "你好 is how you say hi in chinese"
        self.assertEqual(annotate(s), "你好(nǐ hǎo / ㄋㄧˇ ㄏㄠˇ) is how you say hi in chinese")

    def test_annotate_long(self):
        s = "测试一段非常长的文本"
        self.assertEqual(annotate(s), "测试一段非常长的文本(cè shì yī duàn fēi cháng zhǎng de wén běn / ㄘㄜˋ ㄕˋ ㄧ ㄉㄨㄢˋ ㄈㄟ ㄔㄤˊ ㄓㄤˇ ㄉㄜ˙ ㄨㄣˊ ㄅㄣˇ)")

    def test_annotate_sentences(self):
        s = "测试。测试"
        self.assertEqual(annotate(s), "测试(cè shì / ㄘㄜˋ ㄕˋ)。测试(cè shì / ㄘㄜˋ ㄕˋ)")

if __name__ == "__main__":
    unittest.main()
