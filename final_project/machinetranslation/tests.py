import unittest
import translator

class TestTranslatorFunctions(unittest.TestCase):

    def test_englishToFrench_null_input(self):
        englishText = None
        with self.assertRaises(TypeError):
            frenchText = translator.english_to_french(englishText)

    def test_frenchToEnglish_null_input(self):
        frenchText = None
        with self.assertRaises(TypeError):
            englishText = translator.french_to_english(frenchText)

    def test_englishToFrench_hello(self):
        englishText = "Hello"
        expected_output = "Bonjour"
        self.assertEqual(translator.english_to_french(englishText), expected_output)

    def test_frenchToEnglish_bonjour(self):
        frenchText = "Bonjour"
        expected_output = "Hello"
        self.assertEqual(translator.french_to_english(frenchText), expected_output)

    def test_frenchToEnglish_hello(self):
        englishText = "Hello"
        expected_output = "Bonjour"
        self.assertEqual(translator.english_to_french(englishText), expected_output)

    def test_englishToFrench_bonjour(self):
        frenchText = "Bonjour"
        expected_output = "Hello"
        self.assertEqual(translator.french_to_english(frenchText), expected_output)

if __name__ == '__main__':
    unittest.main()
