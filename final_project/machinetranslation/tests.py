import unittest
from translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        """
        testing the french to english translation
        """
        self.assertEqual(french_to_english(""),"")
        self.assertNotEqual(french_to_english(""), "ooooo")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "eeeee")

    def test_englishToFrench(self):
        """
        testing the english to french translation
        """
        self.assertEqual(english_to_french(""),"")
        self.assertNotEqual(english_to_french(""), "tttt")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("hello"), "rrrrr")

if __name__ == '__main__':
    unittest.main()
