import tkinter as tk

root = tk.Tk()
root.title("My first tkinter application")

root.resizable(False,False)
root.geometry('500x500')
#root.attributes('-alpha',1)   transperancy
#root.iconbitmap('./brr2.ico') #ONLY .ICO FILE SUPPORTED


a = tk.Label(root, text="Welcome to my first application")
a.config(font=('Courier', 16, 'bold', 'underline'))
a.place(x=45, y=225)

nom = tk.Label(root, text="Pranav Chauhan")
nom.config(font=('Roboto Mono', 18), fg='navy blue')
nom.place(x=150,y=0)

age = tk.Label(root, text='18yrs')
age.config(font=('Algerian', 18, 'bold'), fg='dark grey')
age.place(x=0,y=470)

gender = tk.Label(root, text='Male')
gender.config(font=('Arial Black', 18, 'bold', 'underline'), fg='red')
gender.place(x=430, y=465)


root.mainloop()	