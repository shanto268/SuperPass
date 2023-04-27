# SuperPass

SuperPass is a simple Python utility that allows users to define custom keyboard shortcuts for quickly pasting pre-defined text strings. This can be useful for pasting repetitive text, such as commonly used passwords, code snippets, or phrases.

## Installation

1. Install Python on your Windows machine if you haven't already. You can download the installer from the official Python website: https://www.python.org/downloads/

2. Clone or download this repository to your local machine.

3. Open a Command Prompt or PowerShell, navigate to the project directory, and run the following commands to install the required libraries:

```
pip install keyboard
pip install pyperclip
pip install python-dotenv
```

## Setup

1. Open the `.env` file in the project directory and update the `SHORTCUTS` variable with your desired keyboard shortcuts and corresponding strings. Use a JSON-like format with key-value pairs, where the key represents the keyboard shortcut and the value is the associated string.

Example:

```
SHORTCUTS={
    "ctrl+shift+a": "String1",
    "ctrl+shift+b": "String2",
    "ctrl+shift+c": "String3"
}
```

2. Save the `.env` file.

## Usage

### One Time:

1. Run the `SuperPass.py` script by double-clicking on the Python file, or run the script from the Command Prompt or PowerShell with the following command:

```
python SuperPass.py
```

The script will now run in the background, and the pre-defined strings will be pasted whenever the corresponding keyboard shortcuts are pressed.

To stop the script, either close the Command Prompt or PowerShell window or use the Task Manager to end the Python process.

### Creating an executable that starts automatically upon startup:

Install pyinstaller if you haven't already. Open a Command Prompt or PowerShell and run the following command:

```
pip install pyinstaller
```

Navigate to the directory containing your `SuperPass.py` script, and run the following command to create a single .exe file:

```
pyinstaller --onefile SuperPass.py
```

This command will generate a standalone `.exe` file in the dist folder within the same directory as your script.

Copy the generated .exe file (e.g., `SuperPass.exe`) from the dist folder.

Press Win+R to open the Run dialog, type shell:startup, and press Enter. This will open the Startup folder.

Paste the copied `.exe` file into the Startup folder.

Now, whenever you restart your Windows machine, the `SuperPass.exe` file will be executed automatically on startup, and the app will run in the background.

# Notes

Running scripts that capture keyboard input may trigger anti-virus or security software warnings. Be cautious when using such scripts, and only use them on your own computer or with proper authorization.
Be careful when defining shortcuts to avoid conflicts with existing system or application shortcuts.

# License
This project is released under the MIT License. See the LICENSE file for more information.
