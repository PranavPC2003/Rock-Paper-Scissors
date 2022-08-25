import tkinter as tk

win = tk.Tk()
win.resizable(False,False)

brr = tk.Canvas(win, bg='pink', height=500, width=500)
#lolly = brr.create_arc(80,100,200,200,start=0,extent=180,fill='purple')
lolly2 = brr.create_arc(80,100,190,200,start=0,extent=359,fill='purple')
stick = brr.create_line(140,200,140,300,fill='black',width=10)
mouth = brr.create_oval(420,200,300,300,fill='red')


brr.pack()
win.mainloop()