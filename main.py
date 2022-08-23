from tkinter import *
from tkinter import messagebox
import emoji


def btn_click():
    height = heightInput.get()
    if height.isdigit():
        messagebox.showinfo(message=f'Ваш рост: {height} см {emoji.emojize(":blush:", language="alias")}')
    else:
        messagebox.showinfo(message=f'Введите ваш рост! {emoji.emojize(":angry:", language="alias")}')


def click_enter(event):
    btn_click()


root = Tk()

root['bg'] = '#fafafa'
root.title('Калькулятор роста')
root.geometry('350x100')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=100, width=350)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Введите ваш рост:', bg='white')
title.place(x=10)

heightInput = Entry(frame, bg='white', width=40)
heightInput.place(x=10, y=25, height=25)
heightInput.bind('<Return>', click_enter)

btn = Button(frame, text='Отправить', command=btn_click)
btn.place(x=260, y=25, height=25)


root.mainloop()
