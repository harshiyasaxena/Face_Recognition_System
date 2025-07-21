from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1200+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=40)


        img_top=Image.open(r"collegeimages\helpdesk.jpg")
        img_top=img_top.resize((1350,600),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1350,height=600)

        dev_label=Label(f_lbl,text="Email: hs9268@srmist.edu.in",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_label.place(x=500,y=150)


if __name__=='__main__':
   root=Tk()
   obj=Help(root)
   root.mainloop()

