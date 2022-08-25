import tkinter as tk
import random

def yess():
	root.destroy()
	win = tk.Tk();
	win.title("")
	win.geometry("300x290")
	win.resizable(False, False)

	Exit = tk.Label(win, text="I knew it! :3")
	Exit.config(font=('Arial', 30))
	Exit.place(x=48,y=95)

def noo():
	no.place(x=random.choice(range(120,240)),y=random.choice(range(110,240)))
	#xidk = random.choice(range(70,250))
	#yidk = random.choice(range(90,250))
	#root.update()
	#print(xidk," ",yidk)

root = tk.Tk();
root.title("")	
root.geometry("300x290")
root.resizable(False, False)

Heading = tk.Label(root, text="Are u dumb?")
Heading.config(font=('Arial', 20))
Heading.place(x=70,y=55)

yes = tk.Button(root, text="Yes",bd=2, command=yess)
yes.config(font=('Arial', 15))
yes.place(x=50,y=190)

no = tk.Button(root, text="No",bd=2, command=noo)
no.config(font=('Arial', 15))
no.place(x=200,y=190)

root.mainloop()