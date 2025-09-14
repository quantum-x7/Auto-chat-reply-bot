import pyautogui
import time
import pyperclip  # For clipboard access
# STEP 1: Give time to switch to the target screen
time.sleep(3)  # Wait for 3 seconds before starting
# STEP 2: Click on the icon at (770, 748)
pyautogui.click(770, 748)
time.sleep(1)
# STEP 3: Drag from (435, 153) to (1080, 415) to select text
pyautogui.moveTo(435, 153)
pyautogui.mouseDown()
pyautogui.moveTo(430, 572, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)
# STEP 4: Copy selected content (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(430 , 572)
time.sleep(0.5)
# STEP 5: Get clipboard content into a variable
copied_text = pyperclip.paste()
# STEP 6: Print the variable
print("Copied Text:\n", copied_text)