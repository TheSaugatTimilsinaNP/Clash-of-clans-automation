import time
import pyautogui
import random

#Works on LD Player
print("Zooming out...")
pyautogui.keyDown('ctrl')  # Hold Ctrl key
for _ in range(1):
    pyautogui.scroll(-500)  # Moderate downward scroll
    time.sleep(random.uniform(0.1, 0.3))