# This script uses PyAutoGUI to automate the creation of a daily report in Notepad.
import pyautogui as a
import time
from datetime import datetime

# Small delay to prepare
time.sleep(3)

# Open Start menu
a.press("win")
time.sleep(1)

# Type notepad
a.write("notepad")
time.sleep(1)

a.press("enter")
time.sleep(2)

# Get current date
today = datetime.now().strftime("%d-%m-%Y")

# Type report content
a.write("Daily Automation Report", interval=0.05)
a.press("enter")
a.write("--------------------------", interval=0.05)
a.press("enter")
a.press("enter")

a.write(f"Date: {today}", interval=0.05)
a.press("enter")
a.press("enter")

a.write("Tasks Completed:", interval=0.05)
a.press("enter")

a.write("- Learned PyAutoGUI automation", interval=0.05)
a.press("enter")
a.write("- Practiced Playwright basics", interval=0.05)
a.press("enter")
a.write("- Explored AI automation concepts", interval=0.05)

time.sleep(1)

# Save file
a.hotkey("ctrl", "s")
time.sleep(2)

# Type file name
a.write("report.txt")
time.sleep(1)

a.press("enter")
time.sleep(1)

# If replace confirmation appears
a.press("left")
a.press("enter")

print("Report created successfully!")