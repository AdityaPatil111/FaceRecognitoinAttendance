from tkinter import *
import os



window=Tk(className="FACE ATTENDANCE SYSTEM")
window.geometry('1000x650')
window.configure(background='skyblue')
Photo=PhotoImage(file='TakeAttendace.png')
Photo1=PhotoImage(file='new.png')

def OpenAtt():
    os.startfile(r'C:\Users\ASUS\PycharmProjects\tkinterGUI\Attndnce.csv')

btn=Button(window,text='Take Attendace',bg='black',fg='green',relief=RAISED,bd=10,image=Photo,compound='top',pady=10,padx=10,font=('Aerial',20,'bold')).place(x=20,y=30)
btn1=Button(window,text='New Student',relief=RAISED,bd=10,bg='black',fg='green',image=Photo1,compound='top',pady=10,padx=10,font=('Aerial',20,'bold')).place(x=700,y=50)
btn2=Button(window,text='Open Attendance',compound='top',command=OpenAtt).pack()
window.mainloop()