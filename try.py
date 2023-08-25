import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime

path = 'C:\\Users\\ASUS\\PycharmProjects\\pythonProjectFace\\ImagesAttendance'
images = []
className = []
myList = os.listdir(path)
#
# print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    className.append(os.path.splitext(cl)[0])
print(className)


# def findEncoding(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encodeImg = face_recognition.face_encodings(img)[0]
#         encodeList.append(encodeImg)
#     return encodeList
def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faceEncodings = face_recognition.face_encodings(img)
        if len(faceEncodings) > 0:
            encodeImg = faceEncodings[0]
            encodeList.append(encodeImg)
    return encodeList



def attendance():
    def markAttendace(name):
        with open('Attendance2.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])

            if name not in nameList:
                now = datetime.now()
                dataStr = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dataStr},present')

    encodeListKnown = findEncoding(images)
    print("Encode Completes")

    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurrFrame = face_recognition.face_locations(imgS)
        encodeCurrImg = face_recognition.face_encodings(imgS, facesCurrFrame)

        for encodeFace, faceLoc in zip(encodeCurrImg, facesCurrFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDist = face_recognition.face_distance(encodeListKnown, encodeFace)

            #print(faceDist)

            matchIndex = np.argmin(faceDist)
            if  matches[matchIndex]:
                name = className[matchIndex].upper()
                #print(name)

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)


                markAttendace(name)
        cv2.imshow("webcam", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


#count=0
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

            #print("image "+str(count)+ " saved")
            a=input("Enter name for student")
            file="C:/Users/ASUS/PycharmProjects/pythonProjectFace/ImagesAttendance/"+a+'.png'
            cv2.imwrite(file,frame)
            print("saved")

    cap.release()
    cv2.destroyAllWindows()
#////////////////////////////////////////////////
from tkinter import *
import os
from PIL import Image,ImageTk

def OpenAtt():
    os.startfile(r'C:/Users/ASUS/PycharmProjects/tkinterGUI/Attendance2.csv')
window=Tk(className="FACE ATTENDANCE SYSTEM")
window.geometry('1800x950')
window.configure(background='black')
#///////////////////////////////////////////////////


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open('back2.png')
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = Example(window)
e.pack(fill=BOTH, expand=YES)



#////////////////////////////////////////////////////////////////////////
label=Label(window,text="FACE ATTENDACE SYSTEM",bg="white",foreground="black",font=("Arial",25,"bold"),
            relief=RAISED,
            bd=5,
            padx=100,pady=30,
            ).place(x=600,y=20)

Photo=PhotoImage(file='download (1).png')
Photo1=PhotoImage(file='new.png')
photo2=PhotoImage(file='images.png')
photo3=PhotoImage(file='images (1).png')

btn=Button(window,text='Take Attendace',bg='#cca550',fg='green',
           relief=RAISED,bd=10,image=Photo,compound='top',pady=20,
           padx=10,height=390
           ,width=360,font=('Aerial',20,'bold'),command=attendance).place(x=50,y=200)

btn1=Button(window,text='New Student',relief=RAISED,bd=10,bg='#69b389',height=370,width=360,fg='green',
            image=Photo1,compound='top',pady=30,padx=10,
            font=('Aerial',20,'bold'),command=camera).place(x=500,y=200)

btn2=Button(window,text='Open Attendance',compound='top',command=OpenAtt,bd=5,image=photo2,bg='#5498cc',pady=30,padx=10,fg='green',height=370,width=360,
            font=('Aerial',20,'bold'),relief=RAISED).place(x=960,y=200)

btn3=Button(window,text='Exit',compound='top',command=window.destroy,bd=5,image=photo3,bg='#392387',pady=30,padx=10,fg='green',height=370,width=360,
            font=('Aerial',20,'bold'),relief=RAISED).place(x=1400,y=200)
window.mainloop()

