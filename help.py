from tkinter import *

def help():
    file = open('Help.txt', 'r', encoding='utf-8')
    window = Tk()
    window.title('help')
    window.geometry('500x300')
    window.iconbitmap('C:/program1/app_ico.ico')

    text = Label(window, text= file.read(), anchor='e')
    text.pack()

    window.mainloop()

def about():
    file = open('about.txt', 'r', encoding='utf-8')
    window = Tk()
    window.title('about')
    window.geometry('500x300')
    window.iconbitmap('C:/program1/app_ico.ico')

    text = Label(window, text= file.read(), anchor='e')
    text.pack()

    window.mainloop()
