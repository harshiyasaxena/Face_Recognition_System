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
from tkinter import messagebox
import mysql.connector


def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1200+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\d251dcc27cdd25b905d3c4845b2a7f01 (1).jpg")
        img=img.resize((1260,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1260,height=710)

        frame=Frame(self.root,bg="black")
        frame.place(x=460,y=150,width=350,height=450)

        img1=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\facialrecognition (1).png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=585,y=155,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=('times new roman',20,'bold'),fg="white",bg="black")
        get_str.place(x=110,y=100)

        username=lbl=Label(frame,text="Username",font=('times new roman',15,'bold'),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=('times new roman',15,'bold'),fg="white",bg="black")
        password.place(x=70,y=225)
        

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #===============icon images===================
        img2=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=300,width=25,height=25)

        img3=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\lock-512.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=500,y=370,width=25,height=25)

        loginbtn=Button(frame,text="Login",command=self.login,font=('times new roman',15,'bold'),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New User Registration",command=self.register_window,font=('times new roman',12,'bold'),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)

        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=('times new roman',12,'bold'),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=0,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to Face Recognition")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Iamgreat123@", database="login")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s", (
                                                                                         self.txtuser.get(),
                                                                                         self.txtpass.get()
                                                                                        ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Username and Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Iamgreat123@",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer")
            else:
                query=("Update register set pass=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset . Please Login with new password")

            
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please write your email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Iamgreat123@",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s" )
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please enter valid username ")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x450+460+150")

                l=Label(self.root2,text="Forgot Password",font=('times new roman',20,'bold'),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=('times new roman',15,'bold'),bg='white',fg='black')
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=('times new roman',15,'bold'),state='readonly')
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your First School","Your Best Friend")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=('times new roman',15,'bold'),bg='white',fg='black')
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=('times new roman',15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=('times new roman',15,'bold'),bg='white',fg='black')
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=('times new roman',15,'bold'),show="*")
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=('times new roman',15,'bold'),fg='white',bg='green')
                btn.place(x=100,y=290)

           

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1200+0+0")
        self.root.title("Face Recognition System")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



        img=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\bg.jpg")
        img=img.resize((1280,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1280,height=710)

        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=40,width=700,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=('times new roman',20,'bold'),fg='darkgreen',bg='white')
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name",font=('times new roman',15,'bold'),bg='white')
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=('times new roman',15,'bold'))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=('times new roman',15,'bold'),bg='white',fg='black')
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=('times new roman',15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No",font=('times new roman',15,'bold'),bg='white',fg='black')
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=('times new roman',15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=('times new roman',15,'bold'),bg='white',fg='black')
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=('times new roman',15))
        self.txt_email.place(x=370,y=200,width=250)

        security_Q=Label(frame,text="Select Security Question",font=('times new roman',15,'bold'),bg='white',fg='black')
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=('times new roman',15,'bold'),state='readonly')
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your First School","Your Best Friend")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=('times new roman',15,'bold'),bg='white',fg='black')
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=('times new roman',15))
        self.txt_security.place(x=370,y=270,width=250)

        pswd=Label(frame,text="Password",font=('times new roman',15,'bold'),bg='white',fg='black')
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,show="*",textvariable=self.var_pass,font=('times new roman',15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=('times new roman',15,'bold'),bg='white',fg='black')
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,show="*",textvariable=self.var_confpass,font=('times new roman',15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms and Conditions",font=('times new roman',12,'bold'),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)


        img1=Image.open(r"collegeimages\register-now-button1.jpg")
        img1=img1.resize((200,55),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        self.login_btn=Button(frame,image=self.photoimg1,command=self.register_data,borderwidth=0,cursor="hand2",font=('times new roman',15,'bold'),fg="white")
        self.login_btn.place(x=100, y=420, width=200)

        img2=Image.open(r"collegeimages\loginpng.png")
        img2=img2.resize((200,45),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        self.register_btn=Button(frame,image=self.photoimg2,borderwidth=0,cursor="hand2",font=('times new roman',15,'bold'),fg="white")
        self.register_btn.place(x=400, y=425, width=200)


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get=="Select":
            messagebox.showerror("Error","All the fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirmed Password should be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions !")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Iamgreat123@",database="login")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists , please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                       ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successful")


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x1200+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\BestFacialRecognition.jpg")
        img=img.resize((445,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=420,height=130)


        img1=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\face-recognition.png")
        img1=img1.resize((450,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=420,y=0,width=420,height=130)


       
        img2=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\images.jpg")
        img2=img2.resize((450,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=840,y=0,width=420,height=130)

        #backgroundimage
        img3=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\dark-black-and-gray-blurred-gradient-background-has-a-little-abstract-light-soft-background-for-wallpaper-design-graphic-and-presentation-backdrop-wall-free-photo.jpg")
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
        img4=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\students.jpg")
        img4=img4.resize((200,200),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",font=('times new roman',15,'bold'),fg='white',bg='navy blue',command=self.student_details,cursor="hand2")
        b1_1.place(x=100,y=60,width=200,height=40)
        
        #detectface
        img5=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\face_detector1.jpg")
        img5=img5.resize((200,200),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.face_data)
        b1_1.place(x=400,y=60,width=200,height=40)

        #attendance
        img6=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\report.jpg")
        img6=img6.resize((200,200),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x=700,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.attendance)
        b1_1.place(x=700,y=60,width=200,height=40)

        #helpdesk      
        img7=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\helpdesk.jpg")
        img7=img7.resize((200,200),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=80,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",font=('times new roman',15,'bold'),fg='white',bg='navy blue',cursor="hand2",command=self.help_data)
        b1_1.place(x=1000,y=60,width=200,height=40)

        #train
        img8=Image.open(r"C:\Users\harsh\OneDrive\Desktop\face_recognition_system-master\collegeimages\Train.jpg")
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
    obj=Login(root)
    root.mainloop()
        