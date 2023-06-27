import unittest
from translator import english_to_french, french_to_english
class TranslationTestCase(unittest.TestCase):
    def test_english_to_french(self):
        english_text = 'hello'
        french_text = 'bonjour'
        translation = english_to_french(english_text)
        self.assertEqual((translation), french_text)
    def test_french_to_english(self):
        french_text = 'bonjour'
        english_text = 'hello'
        translation = french_to_english(french_text)
        self.assertEqual((translation), english_text)

if __name__=='__main__':
    unittest.main()