from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog as fd
from PIL import Image, ImageFilter

tk = Tk()
tk.geometry('600x600')

def choose_file():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"), ('все', '*'))
    filename = fd.askopenfile(title = "Открыть файл", filetypes = filetypes)
    if filename:
        print(filename)
        

btn_file = Button(text = "Выбрать файл", command = choose_file)
btn_file.grid(column = 1, row = 0)

greeting = Label(text = "Здравствуйте! Выбирете нужное изображение:")
greeting.grid(column = 0, row = 0)

choose_style = Combobox(tk)
choose_style['values'] = ('обесцветить', "размытие", "теснение", "сглаживание")
choose_style.grid(column = 0, row = 30)

choose_styletx = Label(tk, text = 'Выберите стиль обработки:')
choose_styletx.grid(column = 0, row = 20)

btn_begin = Button(tk, text = "OK")
btn_begin.grid(column = 1, row = 200)


tk.mainloop()