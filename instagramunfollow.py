'Mouse and Keyboard Automation to unfollow people on instagram'
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


# endless loop
while(True):
    # click on the following
    print(pyautogui.position())
    
    pyautogui.click(1630, 215, duration=3)
    time.sleep(5)

    # unfollow 9 people
    # pyautogui.moveTo(1525, 510, duration=1)
    for i in range(8):
        time.sleep(1)
        pyautogui.moveTo(300, 300, duration=3)
        pyautogui.click(1525, 510, duration=1)
        pyautogui.click(1395, 650, duration=1)
        pyautogui.scroll(-176)
        
      

    # unfollow last 3 people
    # 1st person
    pyautogui.click(1525, 580, duration=1)
    pyautogui.click(1395, 650, duration=1)

    # 2nd person
    pyautogui.click(1525, 650, duration=1)
    pyautogui.click(1395, 650, duration=1)

    # 3rd person
    pyautogui.click(1525, 730, duration=1)
    pyautogui.click(1395, 650, duration=1)


    # close the pop up window and repeat the process
    pyautogui.click(1630, 215, duration=1)
    