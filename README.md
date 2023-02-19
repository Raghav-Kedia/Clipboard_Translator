# Clipboard Translator

The Clipboard Translator is a Python script that automates the process of translating text to different languages by listening for specific word triggers through the keyboard and typing the translated text directly into the active application. The program uses the `win32clipboard`, `keyboard`, `time`, and `translate` modules to perform these actions.

## How to use

1. Clone the repository or download the `clipboard_translator.py` file.
2. Install the necessary Python modules by running `pip install win32clipboard keyboard translate`.
3. Run the `clipboard_translator.py` script by executing `python clipboard_translator.py`.
4. Start using the Clipboard Translator by copying some text to the clipboard.
5. To trigger a translation, type one of the supported language codes followed by the `Enter` key. The program currently supports the following languages:
    - English (`@eng`)
    - Hindi (`@hin`)
    - Bengali (`@ben`)
    - Russian (`@rus`)
    - German (`@ger`)
    - French (`@fre`)
    - Japanese (`@jap`)
    - Spanish (`@spa`)
6. The translated text will be automatically typed into the active application.

## How it works

The program works by listening for specific word triggers through the keyboard using the `keyboard` module. When a trigger is detected, the program retrieves the text currently in the clipboard using the `win32clipboard` module, and passes it to the `Translator` class from the `translate` module for translation to the language specified by the trigger. The program then uses the `keyboard` module to simulate backspace key presses to clear the original text and type the translated text directly into the active application. The program introduces a delay of 1 second before returning.

The program is ideal for individuals who frequently work with text in multiple languages, and can be used to quickly translate text without having to switch between different applications or manually perform translations.
