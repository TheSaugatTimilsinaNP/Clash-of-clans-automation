import pyautogui

while True:
    # Get the current mouse position
    x, y = pyautogui.position()
    # Print the coordinates
    print(f"Mouse pointer is at X: {x}, Y: {y}")