import unittest
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from translator import e2f, f2e

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(e2f('Hello'), '"Bonjour"')
        self.assertEqual(e2f(' '), '" "')
    def test_frenchToEnglish(self):
        self.assertEqual(f2e('Bonjour'), '"Hello"')
        self.assertEqual(f2e(' '), '" "')
if __name__ == '__main__':
    unittest.main()