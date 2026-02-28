# This script uses PyAutoGUI to take screenshots when the user clicks the mouse. It will save up to 3 screenshots in a folder named "meeting_screenshots".
import pyautogui as a
from pynput import mouse
from datetime import datetime
import os

# Create folder
folder_name = "meeting_screenshots"
os.makedirs(folder_name, exist_ok=True)

screenshot_count = 0
max_screenshots = 3

print("Program started...")
print("Click anywhere to take screenshot (Max 3).")

def on_click(x, y, button, pressed):
    global screenshot_count
    
    if pressed:  # Only when mouse button pressed
        if screenshot_count < max_screenshots:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{folder_name}/screenshot_{timestamp}.png"
            
            a.screenshot().save(filename)
            screenshot_count += 1
            
            print(f"Screenshot {screenshot_count} saved!")

        if screenshot_count >= max_screenshots:
            print("Max screenshots reached. Stopping program.")
            return False  # Stop listener

# Start listening for mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
    
    