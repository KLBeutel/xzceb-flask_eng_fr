import os

from ibm_watson import LanguageTranslatorV3
from deep_translator import MyMemoryTranslator
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french(english_text):
    '''
        uses IBM Watson to convert text from English to French
    '''
    if english_text == "":
        return ""
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    french_text=translation["translations"][0]["translation"]
    return french_text

@app.route("/french_to_english")
def french_to_english(french_text):
    '''
       uses IBM Watson to convert text from French to English
    '''
    if french_text == "":
        return ""
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    english_text=translation["translations"][0]["translation"]
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
