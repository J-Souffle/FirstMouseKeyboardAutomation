'Mouse and Keyboard Automation in Python'
import pyautogui
import time
# ctrl + k + c (to comment code)
# ctrl + alt + n (to run code)
# Ctrl + alt + m (stop the code)
# print(pyautogui.size())
# # moveTo() function - moving the mouse from point a to pont b on the x and y axis
# pyautogui.moveTo(300, 300, duration=3)
# # moveRel function - moves the mouse relative to its previous position
# pyautogui.moveRel(0, 50, duration=2)
print(pyautogui.position())

# pyautogui.click(70, 20, duration=1)

# dragTo / dragRel
# pyautogui.dragTo()
# pyautogui.dragRel()

'''
time.sleep(10)
pyautogui.moveTo(500, 500, duration=1)
pyautogui.dragRel(100, 0, duration=1)
pyautogui.dragRel(0, 100, duration=1)
pyautogui.dragRel(-100, 0, duration=1)
pyautogui.dragRel(0, -100, duration=1)
'''

pyautogui.moveTo(1100, 300, duration=10)
pyautogui.scroll(-500)
pyautogui.scroll(500)

# keyboard functions
'''pyautogui.click(400, 700, duration=1)
pyautogui.typewrite('Subscribe to Bek Brace channel!')'''

pyautogui.click(300, 300, duration=3)
pyautogui.hotkey('ctrlleft', 'a')