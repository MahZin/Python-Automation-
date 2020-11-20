import pyautogui

pyautogui.screenshot()
pyautogui.screenshot('c:\\screenshot_example.png')

# to locate an item on screen
pyautogui.locateOnScreen()

pyautogui.locateCenterOnScreen()

pyautogui.moveTo((932, 336), duration=1)
pyautogui.click((932, 336))

# need to get this code to work
