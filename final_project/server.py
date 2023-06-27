from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
def english_to_french(english_text):
    """
    English--->French
    """
    french_text=MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    """
    English<---French
    """
    english_text=MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template(index.html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
