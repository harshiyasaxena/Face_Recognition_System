from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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



        img=Image.open(r"collegeimages\bg.jpg")
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









if __name__=='__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()