import tkinter as tk
from PIL import ImageTk, Image
import random


def rock():
	p1text.set("You chose Rock")
	p1state.config(font=('Serif',15))
	p1state.place(x=265,y=320)

	p2 = random.choice(range(1,4))
	for widget in frame1.winfo_children():
		widget.destroy()
	Rockpic = tk.Label(frame1, image = newrockpic)
	Rockpic.pack()

	if (p2 == 1):
		p2text.set("PC chose Rock")
		p2state.config(font=('Serif',15))
		p2state.place(x=492,y=325)
		wintext.set("You Tied !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Rockpic = tk.Label(frame2, image = newrockpic)
		Rockpic.pack()

	elif (p2 == 2):
		p2text.set("PC chose Paper")
		p2state.config(font=('Serif',15))
		p2state.place(x=490,y=325)
		wintext.set("You Lost !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Paperpic = tk.Label(frame2, image = newpaperpic)
		Paperpic.pack()

	else:
		p2text.set("PC chose Scissors")
		p2state.config(font=('Serif',15))
		p2state.place(x=481,y=325)
		wintext.set("You Won !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Scissorspic = tk.Label(frame2, image = newscissorspic)
		Scissorspic.pack()	


def paper():
	p1text.set("You chose Paper")
	p1state.config(font=('Serif',15))
	p1state.place(x=261,y=320)

	p2 = random.choice(range(1,4))
	for widget in frame1.winfo_children():
		widget.destroy()
	Paperpic = tk.Label(frame1, image = newpaperpic)
	Paperpic.pack()

	if (p2 == 1):
		p2text.set("PC chose Rock")
		p2state.config(font=('Serif',15))
		p2state.place(x=493,y=325)
		wintext.set("You Won !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Rockpic = tk.Label(frame2, image = newrockpic)
		Rockpic.pack()

	elif (p2 == 2):
		p2text.set("PC chose Paper")
		p2state.config(font=('Serif',15))
		p2state.place(x=490,y=325)
		wintext.set("You Tied !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Paperpic = tk.Label(frame2, image = newpaperpic)
		Paperpic.pack()

	else:
		p2text.set("PC chose Scissors")
		p2state.config(font=('Serif',15))
		p2state.place(x=480,y=325)
		wintext.set("You Lost !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Scissorspic = tk.Label(frame2, image = newscissorspic)
		Scissorspic.pack()


def scissors():
	p1text.set("You chose Scissors")
	p1state.config(font=('Serif',15))
	p1state.place(x=252,y=320)

	p2 = random.choice(range(1,4))
	for widget in frame1.winfo_children():
		widget.destroy()
	Scissorspic = tk.Label(frame1, image = newscissorspic)
	Scissorspic.pack()

	if (p2 == 1):
		p2text.set("PC chose Rock")
		p2state.config(font=('Serif',15))
		p2state.place(x=492,y=325)
		wintext.set("You Lost !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Rockpic = tk.Label(frame2, image = newrockpic)
		Rockpic.pack()

	elif (p2 == 2):
		p2text.set("PC chose Paper")
		p2state.config(font=('Serif',15))
		p2state.place(x=491,y=325)
		wintext.set("You Won !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Paperpic = tk.Label(frame2, image = newpaperpic)
		Paperpic.pack()

	else:
		p2text.set("PC chose Scissors")
		p2state.config(font=('Serif',15))
		p2state.place(x=480,y=325)
		wintext.set("You Tied !!")

		for widget in frame2.winfo_children():
			widget.destroy()
		Scissorspic = tk.Label(frame2, image = newscissorspic)
		Scissorspic.pack()


win = tk.Tk()
win.title("Rock Paper Scissors")
win.geometry("700x500")
win.resizable(False,False)
win.iconbitmap('game2.ico')

Heading = tk.Label(win, text="Rock Paper Scissors")
Heading.config(font=('Georgia', 22), bd=3, bg="light grey")
Heading.place(x=217,y=17)

Choose = tk.Label(win, text="Choose your move")
Choose.config(font=('Sans-Serif',18))
Choose.place(x=22,y=88)

Rock = tk.Button(win, text="Rock", command=rock)
Rock.config(font=('Sans-Serif',18))
Rock.place(x=55,y=137)

Paper = tk.Button(win, text="Paper", command=paper)
Paper.config(font=('Sans-Serif',18))
Paper.place(x=55,y=204)

Scissors = tk.Button(win, text="Scissors", command=scissors)
Scissors.config(font=('Sans-Serif',18))
Scissors.place(x=55,y=270)

frame1 = tk.Frame(win, width=160, height=160);
frame1.place(x=260,y=145)
frame1.config(bg="light grey")

frame2 = tk.Frame(win, width=160, height=160);
frame2.place(x=485,y=145)
frame2.config(bg="light grey")

global newrockpic, newpaperpic, newscissorspic, p1var, p2var, p1text, p1state, p2state, p2text, wintext
rockpic = Image.open("rock.png")
resizedrockpic = rockpic.resize((160,160))
newrockpic = ImageTk.PhotoImage(resizedrockpic)

paperpic = Image.open("paper.png")
resizedpaperpic = paperpic.resize((160,160))
newpaperpic = ImageTk.PhotoImage(resizedpaperpic)

scissorspic = Image.open("scissors.png")
resizedscissorspic = scissorspic.resize((160,160))
newscissorspic = ImageTk.PhotoImage(resizedscissorspic)

p1text=tk.StringVar()
p1text.set("Choosing...")
p1state = tk.Label(win, textvariable=p1text)
p1state.config(font=('Serif',15))
p1state.place(x=292,y=320)

p2text=tk.StringVar()
p2state = tk.Label(win, textvariable=p2text)
p2state.config(font=('Serif',15))
p2state.place(x=517,y=320)

wintext = tk.StringVar()
winstate = tk.Label(win, textvariable=wintext)
winstate.config(font=('Audrey',18), bd=3)
winstate.place(x=386,y=372)

win.mainloop()