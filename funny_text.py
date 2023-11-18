string_new = string.ascii_lowercase
# string_new = ''.join(set(string_new))
string_new = ''.join(random.sample(string_new, 10))
number = int(input('Введите число: '))
time.sleep(4)
for i in range(number):
    pyautogui.typewrite(string_new)
    pyautogui.press('Enter')


text = 'FUNNY'
print(f'{text}')
print(f'{text:#<20}')
print(f'{text:_>20}')
print(f'{text:.^20}')