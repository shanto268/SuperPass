"""
=====================================
Program : SuperPass/SuperPass.py
=====================================
Summary:
"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "04/27/2023"
__email__ = "shanto@usc.edu"

import os
import json
import keyboard
import pyperclip
import time
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(".env")

# Read the shortcuts and corresponding strings from an environment variable named 'SHORTCUTS'
shortcuts_json = os.getenv('SHORTCUTS')

if not shortcuts_json:
    raise ValueError("Environment variable 'SHORTCUTS' is not set")

# Try to parse the JSON string into a dictionary
try:
    shortcuts = json.loads(shortcuts_json)
except json.JSONDecodeError as e:
    raise ValueError(f"Failed to parse 'SHORTCUTS' as JSON: {e}")

# Check that the dictionary is not empty
if not shortcuts:
    raise ValueError("'SHORTCUTS' is an empty dictionary")

print(f"Loaded shortcuts: {shortcuts}")

def modify_clipboard(defined_string):
    print(f"Shortcut for string '{defined_string}' activated")
    current_clipboard = pyperclip.paste()
    new_clipboard = defined_string + "\n" + current_clipboard
    pyperclip.copy(new_clipboard)
    keyboard.write(defined_string)

# Bind the keyboard shortcuts to the modify_clipboard function
for shortcut, defined_string in shortcuts.items():
    print(f"Binding shortcut '{shortcut}' to string '{defined_string}'")

    try:
        keyboard.add_hotkey(shortcut, modify_clipboard, args=[defined_string])
    except keyboard.InvalidCharacterException as e:
        print(f"Failed to bind shortcut '{shortcut}': {e}")

# Keep the script running
while True:
    time.sleep(1)