from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from time import strftime
from datetime import datetime
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from developer import Developer
from help import Help
from chatbot import ChatBot
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1200+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"collegeimages\BestFacialRecognition.jpg")
        img=img.resize((445,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=420,height=130)


        img1=Image.open(r"collegeimages\facialrecognition.png")
        img1=img1.resize((450,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=420,y=0,width=420,height=130)


       
        img2=Image.open(r"collegeimages\images.jpg")
        img2=img2.resize((450,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=840,y=0,width=420,height=130)

        #backgroundimage
        img3=Image.open(r"collegeimages\back.jpg")
        img3=img3.resize((1260,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1260,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=('times new roman',20,'bold'),fg='blue',bg='white')
        title_lbl.place(x=0,y=0,width=1260,height=45)

        #--------------------time--------------------
        def time():
           string=strftime('%H:%M:%S %p')
           lbl.config(text=string)
           lbl.after(1000,time)
           
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
         #student button
        img4=Image.open(r"collegeimages\students.jpg")
        img4=img4.resize((200,200),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",font=('times new roman',15,'bold'),fg='white',bg='navy blue',command=self.student_details,cursor="hand2")
        b1_1.place(x=100,y=60,width=200,height=40)
        
        #detectface
        img5=Image.open(r"collegeimages\face_detector1.jpg")
        img5=img5.resize((200,200),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.face_data)
        b1_1.place(x=400,y=60,width=200,height=40)

        #attendance
        img6=Image.open(r"collegeimages\report.jpg")
        img6=img6.resize((200,200),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x=700,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.attendance)
        b1_1.place(x=700,y=60,width=200,height=40)

        #helpdesk      
        img7=Image.open(r"collegeimages\helpdesk.jpg")
        img7=img7.resize((200,200),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.help_data)
        b1_1.place(x=1000,y=60,width=200,height=40)

        #train
        img8=Image.open(r"collegeimages\Train.jpg")
        img8=img8.resize((200,200),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.train_data)
        b1_1.place(x=100,y=300,width=200,height=40)

        #Photos
        img9=Image.open(r"collegeimages\photos.jpg")
        img9=img9.resize((200,200),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="Photos",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.open_img)
        b1_1.place(x=400,y=300,width=200,height=40)

        #developer
        img10=Image.open(r"collegeimages\chat.jpg")
        img10=img10.resize((200,200),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.chatbot)
        b1.place(x=700,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="ChatBot",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.chatbot)
        b1_1.place(x=700,y=300,width=200,height=40)

        #Exit
        img11=Image.open(r"collegeimages\exit.jpg")
        img11=img11.resize((200,200),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=300,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.iExit)
        b1_1.place(x=1000,y=300,width=200,height=40)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
       self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure , you want to EXIT !",parent=self.root)
       if self.iExit>0:
          self.root.destroy()
       else:
          return
          


 
#  -------------------------------Functions button--------------------
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)
    

    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Train(self.new_window)
    

    def face_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)

    def help_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Help(self.new_window)

    def chatbot(self):
      self.new_window=Toplevel(self.root)
      self.app=ChatBot(self.new_window)

    def attendance(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendance(self.new_window)

    
    




        
if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
        


