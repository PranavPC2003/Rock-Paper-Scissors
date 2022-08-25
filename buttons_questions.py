import tkinter as tk

def addList():
	global i, list2, ys, cunter
	recommend = rec_input.get()

	list2.append(recommend)

	tk.Label(root, text=list2[cunter]).place(x=19, y=ys)
	cunter += 1
	ys += 18
	#config(font=('Arial', 10))
	#place(x=19, y=195)

	ask.delete(0,tk.END)



root = tk.Tk()
root.title("To Watch-List")
root.geometry("400x510")
root.resizable(False, False)

i=0
list2 = []
ys=195
cunter = 0

rec_input = tk.StringVar()


Heading = tk.Label(root, text="Recommendation List")
Heading.config(font=('Roboto Mono', 16, 'underline', 'bold'))
Heading.place(x=79, y=0)

recommend = tk.Label(root, text="Recommendation: ")
recommend.config(font=('Arial', 11, 'bold'))
recommend.place(x=3, y=67)

ask = tk.Entry(root, textvariable= rec_input, bd=4)
ask.config(width=34)
ask.place(x=160, y=69)


submit_button = tk.Button(root, text="SUBMIT", bd=2, command=addList)
submit_button.config(font=('Algerian', 10), bg='light grey', fg='black')
submit_button.place(x=142, y=107)

root.mainloop()