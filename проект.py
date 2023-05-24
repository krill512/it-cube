import tkinter.filedialog
from PIL import Image,ImageTk
from torchvision import transforms as trans


win = tkinter.Tk()
win.title("picture process")
win.geometry("1280x600")

original = Image.new('RGB', (300, 400))
save_img = Image.new('RGB', (1920, 1080))
img2 = tkinter.Label(win)

def choose_file():
	select_file = tkinter.filedialog.askopenfilename(title='Выбрать изображение')
	e.set(select_file)
	load = Image.open(select_file)
	load = trans.Resize((300,400))(load)
	global original
	original = load
	render = ImageTk.PhotoImage(load)
	
	img  = tkinter.Label(win,image=render)
	img.image = render
	img.place(x=100, y=100)
	
def Horizon():
	temp = original
	new_im = trans.RandomHorizontalFlip(p = 1)(temp)
	render = ImageTk.PhotoImage(new_im)
	global img2
	img2.destroy()
	img2  = tkinter.Label(image=render)
	img2.image = render
	img2.place(x=800,y=100)
	global save_img
	save_img = new_im
	
	
def Vertical():
	temp = original
	new_im = trans.RandomVerticalFlip(p = 1)(temp)	
	render = ImageTk.PhotoImage(new_im)
	global img2
	img2.destroy()
	img2  = tkinter.Label(image=render)
	img2.image = render
	img2.place(x=800,y=100)
	global save_img
	save_img = new_im

def gray():
	temp = original
	new_im = trans.RandomGrayscale(p = 1)(temp)
	render = ImageTk.PhotoImage(new_im)
	global img2
	img2.destroy()
	img2  = tkinter.Label(win,image=render)
	img2.image = render
	img2.place(x=800,y=100)
	global save_img
	save_img = new_im

def set_bright():
	def show_bright(ev = None):
		temp = original
		new_im = trans.ColorJitter(brightness=scale.get())(temp)
		render = ImageTk.PhotoImage(new_im)
		global img2
		img2.destroy()
		img2  = tkinter.Label(win,image=render)
		img2.image = render
		img2.place(x=800, y=100)
		global save_img
		save_img = new_im
		
	top = tkinter.Tk()
	top.geometry('250x150')
	top.title('Настройки яркости')
	scale = tkinter.Scale(top, from_= 0, to= 10, orient=tkinter.HORIZONTAL, command = show_bright)
	scale.set(1)
	scale.pack()
	
def set_contrast():
	def show_contrast(ev = None):
		temp = original
		new_im = trans.ColorJitter(contrast=scale.get())(temp)
		render = ImageTk.PhotoImage(new_im)
		global img2
		img2.destroy()
		img2  = tkinter.Label(win,image=render)
		img2.image = render
		img2.place(x=800, y=100)
		global save_img
		save_img = new_im
		
	top = tkinter.Tk()
	top.geometry('250x150')
	top.title('Настройка контраста')
	scale = tkinter.Scale(top, from_=0, to=10, orient = tkinter.HORIZONTAL, command=show_contrast)
	scale.set(1)
	scale.pack()

def set_hue():
	def show_hue(ev=None):
		temp = original
		new_im = trans.ColorJitter(hue=scale.get())(temp)
		render = ImageTk.PhotoImage(new_im)
		global img2
		img2.destroy()
		img2  = tkinter.Label(win, image=render)
		img2.image = render
		img2.place(x=800, y=100)
		global save_img
		save_img = new_im
		
	top = tkinter.Tk()
	top.geometry('250x150')
	top.title('Хроматическая настройка')
	scale = tkinter.Scale(top, from_=0, to=0.5, resolution=0.1, orient=tkinter.HORIZONTAL, command=show_hue)
	scale.set(1)
	scale.pack()
	
def set_saturation():
	def show_saturation(ev=None):
		temp = original
		new_im = trans.ColorJitter(saturation=scale.get())(temp)
		render = ImageTk.PhotoImage(new_im)
		global img2
		img2.destroy()
		img2  = tkinter.Label(win, image=render)
		img2.image = render
		img2.place(x=800, y=100)
		global save_img
		save_img = new_im
		
	top = tkinter.Tk()
	top.geometry('250x150')
	top.title('Насыщенность')
	scale = tkinter.Scale(top, from_=0, to=10, resolution=1, orient=tkinter.HORIZONTAL, command=show_saturation)
	scale.set(1)
	scale.pack()

filename = 'new image.jpeg'
def save():
	save_img.save(filename)

e = tkinter.StringVar()
e_entry = tkinter.Entry(win, width=68, textvariable=e)
e_entry.pack()

button1 = tkinter.Button(win, text ="Выбрать изображение", command = choose_file)
button1.pack()

label1 = tkinter.Label(win, text="Исходное изображение")
label1.place(x=200, y=50)

label2 = tkinter.Label(win, text="Новое изображение")
label2.place(x=900, y=50)

button2 = tkinter.Button(win, text="сохранить", command = save)
button2.place(x=600, y=100)


button6 = tkinter.Button(win,text="отзеркалить горизонтально", command=Horizon)
button6.place(x=600, y=150)


button7 = tkinter.Button(win,text="отзеркалить вертикально", command=Vertical)
button7.place(x=600, y=200)

button9 = tkinter.Button(win,text="Черно-белое", command=gray)
button9.place(x=600, y=250)


button10 = tkinter.Button(win,text="Яркость", command=set_bright)
button10.place(x=600, y=300)


button11 = tkinter.Button(win,text="Контраст", command=set_contrast)
button11.place(x=600, y=350)


button12 = tkinter.Button(win,text="Цвет", command=set_hue)
button12.place(x=600, y=400)


button13 = tkinter.Button(win,text="Насыщеность", command=set_saturation)
button13.place(x=600, y=450)


button0 = tkinter.Button(win,text="Выход", command=win.quit)
button0.place(x=600, y=550)

win.mainloop()