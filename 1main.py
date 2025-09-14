import pyautogui
import time
import pyperclip  
import google.generativeai as genai

# Step 1: Gemini API Config
genai.configure(api_key="AIzaSyB5cfOTSD1qE-JZBahSGvTmzpqiZxsGiU8")
model = genai.GenerativeModel("gemini-2.5-flash")

# Step 2: Wait to ensure window is ready
time.sleep(3)

# Step 3: Click on WhatsApp chat window
pyautogui.click(1068, 1044)  # Adjust if needed
time.sleep(1)

# Step 4: Select and copy recent message
pyautogui.moveTo(951 , 228)
pyautogui.mouseDown()
pyautogui.moveTo(1827, 892, duration=0.5)
pyautogui.mouseUp(1151, 1045)
time.sleep(0.5)

pyautogui.hotkey('ctrl', 'c')
pyautogui.click()
time.sleep(0.5)

# Step 5: Get copied chat text
text = pyperclip.paste()
print(text)

# Step 6: Send chat to Gemini and get reply
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": [
            "You are Faizan, a Pakistani person who speaks in Urdu-English mix like a friend. Reply casually based on this WhatsApp chat:\n\n" + text
        ]
    }
])

response = chat.send_message("What would Faizan reply now?")
reply = response.text
print(reply)

# Step 7: Paste the reply and send it
time.sleep(1)
pyautogui.click(1139, 1053)  # Click on message box
pyperclip.copy(reply)        # Copy AI reply
pyautogui.hotkey('ctrl', 'v')  # Paste
pyautogui.press('enter')       # Send
