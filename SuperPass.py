# -*- coding: utf-8 -*-
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
shortcuts_json = os.environ.get('SHORTCUTS')

if not shortcuts_json:
    raise ValueError("Environment variable 'SHORTCUTS' is not set")

shortcuts = json.loads(shortcuts_json)

def modify_clipboard(defined_string):
    current_clipboard = pyperclip.paste()
    new_clipboard = defined_string + "\n" + current_clipboard
    pyperclip.copy(new_clipboard)

# Bind the keyboard shortcuts to the modify_clipboard function
for shortcut, defined_string in shortcuts.items():
    keyboard.add_hotkey(shortcut, modify_clipboard, args=[defined_string])

# Keep the script running
while True:
    time.sleep(1)
