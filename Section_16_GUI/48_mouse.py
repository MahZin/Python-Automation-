# GUI automation
import pyautogui

pyautogui.size() # returns monitor resolution
# Size(width=2560, height=1440)
width, height = pyautogui.size()
width
# 2560
height
# 1440

# Checking current cursor position
pyautogui.position()
# Point(x=2004, y=736)
pyautogui.position()
# Point(x=-843, y=447)

# Function to move mouse cursor
pyautogui.moveTo(10, 10)
pyautogui.moveTo(10, 10, duration=1.5)

# moving mouse cursor relative to its current position
pyautogui.moveRel(200, 0)
pyautogui.moveRel(200, 0, duration=2)
pyautogui.moveRel(0, -100, duration=1)

# Let's create a function for clicking
pyautogui.position()
# returns current position
pyautogui.click(893, 307)
pyauto.click() # clicks current position
# other click functions: doubleClick(), rightClick(), middleClick()
# drag functions: dragTo(), dragRel()


# TO STOP pyautogui, move mouse cursor to (0, 0) i.e. top left of the screen

# To find mouse cursor positions, use these functions in cmd:
# py -3.8
# import pyautogui
# pyautogui.displayMousePosition()
