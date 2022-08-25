import tkinter as tk

root = tk.Tk()
root.title("My first tkinter application")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width, " ", height)

root.geometry(f'{width}x{height}')

root.resizable(False,False)
root.geometry('500x500')
root.attributes('-alpha',1)
#root.iconbitmap('./brr2.ico') #ONLY .ICO FILE SUPPORTED

root.mainloop()
