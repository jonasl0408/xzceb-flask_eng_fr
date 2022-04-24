import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

def f2e(french_text):
    #write the code here
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = json.dumps(translation['translations'][0]['translation'])
    return english_text
print(f2e('Bonjour comment vas-tu?'))

def e2f(english_text):
    #write the code here
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = json.dumps(translation['translations'][0]['translation'])
    return french_text
print(e2f('Hello, how are you?'))