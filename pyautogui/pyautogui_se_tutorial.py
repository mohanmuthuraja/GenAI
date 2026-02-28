# This script uses PyAutoGUI to open a web browser, navigate to a specific website, and perform some actions on the page.
import webbrowser
import time
import pyautogui as a

# Open website directly
webbrowser.open("https://socialeagle.ai")

# Wait for page to load
time.sleep(6)

# Scroll to bottom
a.hotkey('ctrl', 'end')
a.sleep(2)
a.click(2766, 322)