import tkinter as tk

def sums():
  sum = input_a.get() + input_b.get()
  ans = tk.Tk()

  ans.title("Your Answer BRR")
  ans.geometry('200x200')
  ans.resizable(False, False)

  ff = tk.Label(ans, text=sum)
  ff.config(font=('Arial Black',15))
  ff.place(x=20, y=20)


win = tk.Tk()
win.title("SUm ApP less gooo")
win.geometry("600x600")
win.resizable(False,False)

input_a = tk.IntVar()
input_b = tk.IntVar()


head = tk.Label(win, text="Sum App")
head.config(font=('Algerian',30,'underline','bold'))
head.place(x=205, y=0)

ask = tk.Label(win, text="Enter First Number = ")
ask.config(font=('Arial Black',14))
ask = ask.place(x=10, y=150)

ask_input = tk.Entry(win, textvariable=input_a, bd=3)
ask_input.config(width=5)
ask_input.place(x=250,y=155)

ask2 = tk.Label(win, text="Enter Second Number = ")
ask2.config(font=('Arial Black',14))
ask2 = ask2.place(x=10, y=350)

ask2_input = tk.Entry(win, textvariable=input_b, bd=3)
ask2_input.config(width=5)
ask2_input.place(x=279,y=355)

sum_but = tk.Button(win, text="SUM!!", command=sums())
sum_but.place(x=250,y=500)



win.mainloop()



#





