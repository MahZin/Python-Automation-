import pyautogui
aXYb
# typewrite function needs a field to work with
pyautogui.click(300,100) ; pyautogui.typewrite('Hello world!', interval=0.2)

# typing with sequential commands
pyautogui.click(300,100) ; pyautogui.typewrite(['a', 'b', 'left', 'X', 'Y'], interval=1)

# to find operatable keys
pyautogui.KEYBOARD_KEY

# Opening documentations tab
pyautogui.press('f1')

# Opening files
pyautogui.hotkey('ctrl', 'o')
