# import pyautogui 
# import random
# import time
# import string


# # while True:
# #     x = random.randint(600, 700)
# #     y = random.randint(200, 700)
# #     pyautogui.moveTo(x, y, 3)
# #     time.sleep(1)

# string_new = string.ascii_lowercase
# # string_new = ''.join(set(string_new))
# string_new = ''.join(random.sample(string_new, 10))
# number = int(input('Введите число: '))
# time.sleep(4)
# for i in range(number):
#     pyautogui.typewrite(string_new)
#     pyautogui.press('Enter')



import pyautogui
import random
import time
x = random.randint(600, 700)
y = random.randint(200, 700)
pyautogui.moveTo(x,y, 0.5)