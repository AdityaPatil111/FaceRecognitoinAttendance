from tkinter import *
import cv2
window=Tk()
photo=PhotoImage(file='like.png')
count=0
def click():
    global count
    count+=1
    print(count)
def camera():
    cap=cv2.VideoCapture(0)
    while True:
        succes,frame=cap.read()
        cv2.imshow("camera",frame)
        k=cv2.waitKey(1)                        #C:/Users/ASUS/PycharmProjects/pythonProjectFace/ImagesAttendance
        if k%256==27:           #for esc key
            print("close")
            break
        elif k%256==32:         #for space key

            print("image "+str(count)+ " saved")
            a=input("Enter name for image")
            file="C:/Users/ASUS/PycharmProjects/pythonProjectFace/ImagesAttendance/"+a+'.jpg'
            cv2.imwrite(file,frame)
            print("saved")
    cap.release()
    cv2.destroyAllWindows()


button=Button(window,text='Like',bg='white',font=('Aerial',30,'bold'),image=photo,compound='bottom',command=click).pack()
button1=Button(window,text='Take Images',bg='white',font=('Aerial',30,'bold'),image=photo,compound='bottom').pack()

window.mainloop()