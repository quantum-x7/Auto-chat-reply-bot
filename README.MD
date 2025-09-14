WhatsApp Chat Auto-Reply Bot with Gemini AI

This project automates WhatsApp chat replies using Google Gemini AI. It uses Python scripts to read messages from the WhatsApp desktop app, generate a reply using Gemini, and send it back automatically.

Files Overview

1main.py
Main automation script.

Selects and copies the latest WhatsApp message.
Sends the message to Gemini AI with a prompt for a casual Urdu-English reply.
Pastes and sends the AI-generated reply in WhatsApp.
axis.py
Utility script to print the current mouse cursor position.

Useful for finding screen coordinates for automation.
main.py
Lists available Gemini models for your API key.

Helps verify API access and model names.
program.py
Example script for automating text selection and copying from a specific screen area.

Requirements

Python 3.x
pyautogui
pyperclip
google-generativeai
Install dependencies: pip install pyautogui pyperclip google-generativeai

Usage

Set up your Google Gemini API key in the scripts.
Adjust screen coordinates in 1main.py for your WhatsApp window and message box.
Run 1main.py to automate WhatsApp replies.
Notes

Make sure WhatsApp Desktop is open and visible.
Use axis.py to find the correct coordinates for your setup.
The scripts use screen automation; do not move your mouse or keyboard during execution.
License

MIT License