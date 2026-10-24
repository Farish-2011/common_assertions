import unittest
from wordcounter import count_words


class TestWordCounter(unittest.TestCase):
    def test_normal_sentence(self):
        self.assertEqual(count_words("i love python"), 3)

    def test_single_word(self):
        self.assertEqual(count_words("python"), 1)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_word_exists(self):
        self.assertIn("python", "i love python")

    def test_not_equal(self):
        self.assertNotEqual(count_words("i love python"), 5)


if __name__ == "__main__":
    unittest.main()