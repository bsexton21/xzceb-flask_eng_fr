"""
Translator
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    French To English
    """ 
    french_text=MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    English To French
    """
    english_text=MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
