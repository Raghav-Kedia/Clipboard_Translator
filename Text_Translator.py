import win32clipboard
import keyboard
import time
from translate import Translator


def get_clip_text():
    win32clipboard.OpenClipboard()
    clip = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return clip


def translate_to_language(language):
    original_text = get_clip_text()
    translated_text = Translator(to_lang=language).translate(original_text)
    for i in range(5):
        keyboard.press_and_release("backspace")
    keyboard.write(translated_text)
    time.sleep(1)


keyboard.add_word_listener('@eng', callback=lambda: translate_to_language('en'))  # English
keyboard.add_word_listener('@hin', callback=lambda: translate_to_language('hi'))  # Hindi
keyboard.add_word_listener('@ben', callback=lambda: translate_to_language('bn'))  # Bengali
keyboard.add_word_listener('@rus', callback=lambda: translate_to_language('ru'))  # Russian
keyboard.add_word_listener('@ger', callback=lambda: translate_to_language('de'))  # German
keyboard.add_word_listener('@fre', callback=lambda: translate_to_language('fr'))  # French
keyboard.add_word_listener('@jap', callback=lambda: translate_to_language('ja'))  # Japanese
keyboard.add_word_listener('@spa', callback=lambda: translate_to_language('es'))  # Spanish

print("Running...")
while True:
    time.sleep(3600*24)