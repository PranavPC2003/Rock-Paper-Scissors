import tkinter as tk

root = tk.Tk()
root.title("Quick Cat")
root.geometry("550x650")
root.resizable(False, False)

def Screen1func():
	inpScreen1 = Screen1.get()

	if inpScreen1 == 1:
		Screen11func()

	elif inpScreen1 == 2:
		Screen12func()

	elif inpScreen1 == 3:
		Screen13func()

	elif inpScreen1 == 4:
		Screen14func()

	elif inpScreen1 == 5:
		exit = tk.Tk()
		exit.title("GOOD BYE")
		exit.geometry("250x100")
		exit.resizable(False, False)

		root.destroy()

		exitMsg = tk.Label(exit, text="Thank you for visting us")
		exitMsg.config(font=('Arial Black', 10))
		exitMsg.place(x=35, y=12)

		exitMsg = tk.Label(exit, text="Come back later :)")
		exitMsg.config(font=('Arial Black', 10))
		exitMsg.place(x=50, y=50)


def Screen11RadioFunc():
	inpScreen11 = Screen11.get()

	if inpScreen11 == 1:
		Screen11Afunc()

	elif inpScreen11 == 2:
		Screen11Bfunc()

	elif inpScreen11 == 3:
		Screen11Cfunc()

	

def Screen11Cfunc():
	Screen11.destroy
	

def Screen11func():
	Screen11 = tk.Tk()
	Screen11.title("List of pros")

	Screen11.geometry("400x450")
	Screen11.resizable(False, False)

	Heading = tk.Label(Screen11, text="List of Pros")
	Heading.config(font=('Roboto Mono', 23, 'bold', 'underline'))
	Heading.place(x=90, y=5)

	file = open('pros.txt', 'r')
	
	ycounter = 100

	for line in file:
		x = line.split(" ")
		tk.Label(Screen11, text=x[0]).place(x=95, y=ycounter)
		ycounter += 22

	Screen11 = tk.IntVar()

	option1 = tk.Radiobutton(Screen11, text="Would you like to know the prices?", variable=Screen11, value=1, command = Screen11RadioFunc)
	option1.config(font=('Roboto Mono', 10))
	option1.place(x=50, y=300)

	option2 = tk.Radiobutton(Screen11, text="Would you like to know the rating?", variable=Screen11, value=2, command = Screen11RadioFunc)
	option2.config(font=('Roboto Mono', 10))
	option2.place(x=50, y=330)

	option3 = tk.Radiobutton(Screen11, text="Return to previous menu", variable=Screen11, value=3, command = Screen11RadioFunc)
	option3.config(font=('Roboto Mono', 10))
	option3.place(x=50, y=300)


def Screen12func():
	Screen12 = tk.Tk()
	Screen12.title("Choose a pros")
	Screen12.geometry("400x450")
	Screen12.resizable(False, False)

def Screen13func():
	Screen13 = tk.Tk()
	Screen13.title("Rate us")
	Screen13.geometry("400x450")
	Screen13.resizable(False, False)

def Screen14func():
	Screen14 = tk.Tk()
	Screen14.title("Client List")
	Screen14.geometry("400x450")
	Screen14.resizable(False, False)

def Screen11Afunc():
	Screen11A = tk.Tk()
	Screen11A.title("Prices")
	Screen11A.geometry("400x450")
	Screen11A.resizable(False, False)

	Heading = tk.Label(Screen11A, text="Our Prices are listed as 'PER HOUR'")
	Heading.config(font=('Roboto Mono', 20, 'bold'))
	Heading.place(x=50, y=0)


heading1 = tk.Label(root, text="----------------------")
heading1.config(font=('Roboto Mono', 25, 'bold'))
heading1.place(x=58, y=0)


heading2 = tk.Label(root, text=" WELCOME TO QUICK CAT ")
heading2.config(font=('Roboto Mono', 25, 'bold'))
heading2.place(x=58, y=36)

heading3 = tk.Label(root, text="----------------------")
heading3.config(font=('Roboto Mono', 25, 'bold'))
heading3.place(x=58, y=76)

Screen1 = tk.IntVar()

opt1 = tk.Radiobutton(root, text="List of pros", variable=Screen1, value=1, command = Screen1func)
opt1.config(font=('Roboto Mono', 15))
opt1.place(x=170, y=200)

opt2 = tk.Radiobutton(root, text="Choose a pros", variable=Screen1, value=2, command = Screen1func)
opt2.config(font=('Roboto Mono', 15))
opt2.place(x=170, y=250)

opt3 = tk.Radiobutton(root, text="Rate us", variable=Screen1, value=3, command = Screen1func)
opt3.config(font=('Roboto Mono', 15))
opt3.place(x=170, y=300)

opt4 = tk.Radiobutton(root, text="Client List", variable=Screen1, value=4, command = Screen1func)
opt4.config(font=('Roboto Mono', 15))
opt4.place(x=170, y=350)

opt5 = tk.Radiobutton(root, text="Exit", variable=Screen1, value=5, command = Screen1func)
opt5.config(font=('Roboto Mono', 15))
opt5.place(x=170, y=400)

root.mainloop() 