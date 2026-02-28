# This script uses PyAutoGUI to find the current position of the mouse pointer and move it to the center of a specific image on the screen.
import pyautogui as a
import time
time.sleep(4)
x,y = a.position()  # Get the current mouse position
print(x,y)  # Print the current mouse position

a.center(a.locateOnScreen('1.png'))  # Move the mouse to the center of the located image on the screen
