from tkinter import *
from tkinter import Tk, filedialog, colorchooser, ttk
from tkinter.messagebox import showinfo

root = Tk()
root.title('Ку')
root.geometry('550x300')

notebook = ttk.Notebook()
notebook.pack()

frame = ttk.Frame(notebook)
frame.pack()
frame2 = ttk.Frame(notebook)
frame2.pack()

notebook.add(frame, text='Первая вкладка')
notebook.add(frame2, text='Вторая вкладка')


# value=IntVar(value=120)

# def start():
#     prbar.start(10)

# def stop():
#     prbar.stop()

# prbar = ttk.Progressbar(orient='vertical', length=120, variable=value, mode='determinate')
# prbar.place(x=100, y=100)
# Label(textvariable=value).place(x=125, y=100)
# Button(text='Start', command=start).place(x=120, y=120)
# Button(text='Stop', command=stop).place(x=120, y=140)
root.mainloop()

#----------------------------------------------------

# from tkinter import *
# from tkinter import Tk, filedialog, colorchooser
# from tkinter.messagebox import showinfo

# root = Tk()
# root.title('Ку')
# root.geometry('550x300')

# text_window = Text()
# text_window.place(x=0, y=0, height = 200, width= 550)

# def openFile():
#     file_open = filedialog.askopenfilename()
#     if file_open != "":
#         with open('text.txt', 'r', encoding='utf=8') as file:
#             text = file.read()
#             text_window.delete('1.0', END)
#             text_window.insert('1.0', text)

# def saveFile():
#     text_s = text_window.get('1.0', END)
#     with open('text.txt', 'w', encoding='utf=8') as file:
#         file.write(text_s)

# def chg_col():
#     color = colorchooser.askcolor(initialcolor='black')
#     text_window['foreground'] = color[1]


# open_file = Button(text = 'Открыть файл', command=openFile)
# open_file.place(x=120, y=210)
# save_file = Button(text = 'Сохранить файл', command=saveFile)
# save_file.place(x=220,y=210)
# col = Button(text='Выбрать цвет', command=chg_col)
# col.place(x=320,y=210)
# root.mainloop()

#----------------------------------------------------

# from tkinter import *

# screen = Tk()
# screen.title('Impostor is saaaaaas')
# screen.geometry('400x600')

# def btn_click():
#     def aa():
#         print(entry.get())
#     screen2 = Tk()
#     screen2.title('2 Impostor is saaaaaas')
#     screen2.geometry('400x600')
#     entry = Entry(screen2).pack()
#     label = Label(screen2, text='Ку, это первый экран').pack()
#     be = Button(screen2, text='работай, сохрани меня', command=aa).pack()
#     bb = Button(screen2, text='Изыдий фальшивка', command=lambda:screen2.destroy()).pack()


# btn = Button(text='Создать окно 1', command=btn_click)
# btn.pack()

# screen.mainloop()

#----------------------------------------------------

# from tkinter import *

# root = Tk()
# root.title('Ку')
# root.geometry('550x300')

# label = Label(text='Записаться на мастер классы без маминой карточки!', font=('Arial', 12))
# label.pack()

# button1 = Button(text='Создать курс', background='#009900')
# button1.place(x=160, y=30)

# button2 = Button(text='Удалить курс', background='#FF2400')
# button2.place(x=260, y=30)

# list = ['тут', 'типа', 'курсы', 'будут', 'да']
# list_box = Variable(value=list)
# list_lb = Listbox(listvariable=list_box)
# list_lb.place(x=120, y=70, width=280, height=100)

# entry = Entry(text='Имя')
# entry.place(x=120, y=180)

# entry2 = Entry(text='Имя')
# entry2.place(x=250, y=180)

# entry3 = Entry(text='Имя')
# entry3.place(x=380, y=180, width=37)

# root.resizable(False, False)

# # def button2_click():
# #     global clicks
# #     clicks += 1
# #     label['text'] = f'Зачем ты нажал? Целый {clicks} раз!'

# # button2 = Button(text='*промолчать*', command=button2_click, background='#FF2B2B')
# # button2.pack()


# # def example():
# #     print("Как ты мог, просто выйти):")
# #     root.destroy()

# # root.resizable(False, False)
# # root.protocol('WM_DELETE_WINDOW', example)

# root.mainloop()

#-------------------------------------------------

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title('Ку')
# root.geometry('800x600')

# label = Label(text='Привет, как дела?', font=('Arial', 12), foreground='#e6a8d7')
# label.pack()

# button1 = Button(text='Привет!', background='#009900')
# button1.pack()

# def button2_click():
#     global clicks
#     clicks += 1
#     label['text'] = f'Зачем ты нажал? Целый {clicks} раз!'

# button2 = Button(text='*промолчать*', command=button2_click, background='#FF2B2B')
# button2.pack()


# def example():
#     print("Как ты мог, просто выйти):")
#     root.destroy()

# root.resizable(False, False)
# root.protocol('WM_DELETE_WINDOW', example)

# list = ['1', '2', '3', '4', '5']
# list_box = Variable(value=list)
# list_lb = Listbox(listvariable=list_box)
# list_lb.pack(anchor=NW, fill=X)

# root.mainloop()

#-----------------------------------------------------

# def liked(name):
#     a = len(name)
#     if(a > 3):
#         return f'Этот пост лайкнули {name[0]}, {name[1]} и ещё {a-2} человек.'
#     elif(a == 2): 
#         return f'Этот пост лайкнули {name[0]}, {name[1]}.'
#     else: 
#         return f'Этот пост лайкнул {name[0]}.'
# print(liked(['Luke']))

#------------------------------------------------------

#import random
#
#
#class Person:
#    def __init__(self, color, rank, room=0):
#        self.color = color
#        self.rank = rank
#        self.room = room
#    def __del__(self):
#        print(f'До свидания мистер {self.name} {self.surname}')
#
#    def __str__(self):
#        return f'{self.color} в конате {self.room} умер. Он занял {self.rank}'
#    
#    def __lt__(self, other: 'Person'):
#        if self.room == other.room:
#            a = random.randint(1,2)
#            if a == 1:
#                print('1')
#            if a == 2:
#                print('2')
#
#
#
#
#persons = [
#    Person('Крассный',  random.randint(0, 10)),
#    Person('Синий',  random.randint(0, 10)),
#    Person('Зелёный',  random.randint(0, 10)),
#]
#persons[0].room = 1
#persons[1].room = 2
#persons[2].room = 3
#trf = 1
#while trf == 1:
#    persons[0].room = random.randint(1, 4)
#    print(persons[0].room)
#    persons[1].room.room = random.randint(1, 4)
#    print(persons[1].room)
#    persons[2].room.room = random.randint(1, 4)
#    print(persons[2].room)
#    input('Продолжить?')
#    persons.sort()
#    
#
#input()

#------------------------------------------------------

#import random
#
#class voin:
#    def __init__(self, name, hp=100):
#        self.name = name
#        self.hp = hp
#
#    def beng(self):
#        self.hp =- 20
#    
#class red(voin):
#    pass
#
#class blue(voin):
#    pass
#
#rd = red('Красный')
#bl = blue('Синий')
#
#while(rd.hp > 0 and bl.hp > 0):
#    whred = random.randint(1,2)
#    whblue = random.randint(1,2)
#    if whred == 2:
#        bl.beng()
#        print(f'{rd.name} попал в синего, теперь у него {bl.hp} HP')
#    if whblue == 2:
#        rd.beng()
#        print(f'{bl.name} попал в красного, теперь у него {rd.hp} HP')
#if rd.hp == 0:
#    print(f'{rd.name} проиграл, но оставил синему {bl.hp}')
#elif bl.hp == 0:
#    print(f'{bl.name} проиграл, но оставил красному {rd.hp}')
#else:
#    print('Ничья!')


#------------------------------------------------------

#class Car:
#    def __init__(self, collor, name, engine=False, x = 0):
#        self.collor = collor
#        self.name = name
#        self.engine = engine
#        self.x = x
#
#    def Road(self):
#            for i in range(10):
#                if i == self.x:
#                    print('# <--', self.name)
#                else:
#                    print('|')
#
#    def Engine(self):
#        if self.engine:
#            self.engine = False
#        else:
#            self.engine = True
#        
#    
#    def Move(self, movend):
#        self.movend = movend
#        if self.engine and self.movend == 'forward' or self.engine and self.movend == 'Forward':
#            self.x = self.x + 1
#        elif self.engine and self.movend == 'back' or self.engine and self.movend == 'Back':
#            self.x = self.x + 1
#        else:
#            print('Двигатель не заведён, ничего не произошло')
#            
#
#car1 = Car('Red', 'Formula')
#car1.Engine()
#print(car1.engine)
#car1.Move('forward') #вперёд forward назад back
#car1.Road()
