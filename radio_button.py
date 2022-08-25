import tkinter as tk

root = tk.Tk()
root.title("radioButton")
root.geometry("600x600")
root.resizable(False, False)

def yoruBest():
	answer = a.get()

	if answer == 69:
		print("great choice")

	elif answer == 420:
		root.destroy()	
		pc = tk.Tk()
		pc.mainloop()


title = tk.Label(root, text="Is Yoru Craked?")
title.config(font=('Algerian', 25, 'underline', 'bold'), fg= 'Black')
title.place(x=158, y=0)

a = tk.IntVar()

opt1 = tk.Radiobutton(root, text="Yah sure", variable=a, value=69, command=yoruBest)
opt1.config(font=('Roboto Mono', 10), fg='grey')
opt1.place(x=220, y=150)

opt2 = tk.Radiobutton(root, text="Why not?!?")
opt2.config(font=('Roboto Mono', 10), fg='grey', variable=a, value=420, command=yoruBest)
opt2.place(x=220, y=250)


root.mainloop()