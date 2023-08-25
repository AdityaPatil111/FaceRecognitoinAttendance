from tkinter import *

window=Tk()
photo=PhotoImage(file='C:\\Users\\ASUS\\Downloads\\new.png')
label=Label(window,text="hello world",bg="red",foreground="black",font=("Arial",40,"bold"),
            relief=RAISED,bd=10,
            padx=100,pady=50,
            image=photo,
            compound='bottom').pack()

window.mainloop()