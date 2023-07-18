# SuperPass

SuperPass is a simple Python utility that allows users to define custom keyboard shortcuts for quickly pasting pre-defined text strings. This can be useful for pasting repetitive text, such as commonly used passwords, code snippets, or phrases.

## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Usage](#usage)
   - [One Time](#one-time)
   - [Creating an executable that starts automatically upon startup](#creating-an-executable-that-starts-automatically-upon-startup)
4. [Notes](#notes)
5. [Running the Keyboard Shortcut Script on Windows](#running-the-keyboard-shortcut-script-on-windows)
6. [License](#license)

## Installation

1. Install Python on your Windows machine if you haven't already. You can download the installer from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone or download this repository to your local machine.

3. Open a Command Prompt or PowerShell, navigate to the project directory, and run the following commands to install the required libraries:

```bash
pip install -r requirements.txt
```


## Setup

1. Open the `.env` file in the project directory and update the `SHORTCUTS` variable with your desired keyboard shortcuts and corresponding strings. Use a JSON-like format with key-value pairs, where the key represents the keyboard shortcut and the value is the associated string.

Example:

```json
SHORTCUTS={"ctrl+shift+a": "String1","ctrl+shift+b": "String2","ctrl+shift+c": "String3"}
```

2. Save the `.env` file.

## Usage

### One Time:

Run the `SuperPass.py` script by double-clicking on the Python file, or run the script from the Command Prompt or PowerShell with the following command (Admin Mode):

```
python SuperPass.py
```


The script will now run in the background, and the pre-defined strings will be pasted whenever the corresponding keyboard shortcuts are pressed.

To stop the script, either close the Command Prompt or PowerShell window or use the Task Manager to end the Python process.

### Creating an executable that starts automatically upon startup:

1. Install pyinstaller if you haven't already. Open a Command Prompt or PowerShell and run the following command:

```
pip install pyinstaller
```


2. Navigate to the directory containing your `SuperPass.py` script, and run the following command to create a single .exe file:

```
pyinstaller --onefile SuperPass.py
```


3. This command will generate a standalone `.exe` file in the dist folder within the same directory as your script.

4. Copy the generated .exe file (e.g., `SuperPass.exe`) from the dist folder.

5. Press `Win+R` to open the Run dialog, type shell:startup, and press Enter. This will open the `Startup` folder.

6. Paste the copied `.exe` file into the `Startup` folder.

Now, whenever you restart your Windows machine, the `SuperPass.exe` file will be executed automatically on startup, and the app will run in the background.

## Notes

Running scripts that capture keyboard input may trigger anti-virus or security software warnings. Be cautious when using such scripts, and only use them on your own computer or with proper authorization.

Be careful when defining shortcuts to avoid conflicts with existing system or application shortcuts.

---

## Running the Keyboard Shortcut Script on Windows

This application uses AutoHotkey, a powerful and flexible open-source tool for Windows, to bind specific strings to keyboard shortcuts. Here's how you can set it up:

1. **Download and Install AutoHotkey**

Download AutoHotkey from the official website at [https://www.autohotkey.com/](https://www.autohotkey.com/). Run the installer and follow the instructions to install AutoHotkey on your system.

2. **Create a New AutoHotkey Script**

Create a new script by right-clicking anywhere on your desktop or inside a folder, then select "New" -> "AutoHotkey Script". You can name this script as per your preference.

3. **Edit the AutoHotkey Script**

Right-click on the script file and select "Edit Script". This will open the script in your default text editor. In this file, you can define your keyboard shortcuts and the strings they should output.

Here's a template for your AutoHotkey code:

```autohotkey
; This is a comment. Replace 'YourHotkey' and 'YourString' with your hotkey and string.
YourHotkey::
  SendInput, YourString
return
```

For example, if you want to bind the string "example" to Ctrl+Shift+E, you would write:

```autohotkey
^+e::
  SendInput, example
return
```

1. **Save and Run the AutoHotkey Script**

After you've defined your keyboard shortcuts, save the script and close your text editor. You can then run the script by right-clicking on the script file and selecting "Run Script". The script will now be running, and you can use the keyboard shortcuts you've defined.

2. **Running the Script with Elevated Privileges**

If you're trying to send input to a process that's running with elevated privileges (such as a software installer), you might need to run your AutoHotkey script as an administrator. To do this, right-click on the script file and select "Run as administrator".

Note: Be cautious while running scripts with administrator privileges, as they have full access to your system.

---

You can customize this guide as per your needs. Remember to replace `YourHotkey` and `YourString` with your actual hotkeys and strings.
