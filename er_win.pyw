from tkinter import *
def err(error, err_code):
    def ex():
        root.destroy()
    root = Tk()
    root.title('Error: ' + str(err_code))
    root.geometry('250x70+500+300')
    root.iconbitmap('C:/program1/app_ico.ico')
    text = Label(root, text = error)
    kill = Button(root, text = 'Ok', command = ex)
    text.pack()
    kill.pack()
    root.mainloop()
