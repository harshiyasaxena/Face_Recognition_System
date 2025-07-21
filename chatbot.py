from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("800x800+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=800)
        main_frame.pack()

        img_chat=Image.open(r'collegeimages\chat.jpg')
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=800,compound=LEFT,image=self.photoimg,text='CHAT WITH ME',font=('arial',30,'bold'),fg="green",bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=100,height=20,bd=3,relief=RAISED,font=('times new roman',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg="white",width=800)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=('times new roman',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=59,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('times new roman',16,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('times new roman',16,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

        #================function=======================


    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
        

    def send(self):
        send = '\t\t\tYou: ' + self.entry.get()
        self.text.insert(END, '\n' + send)
        self.text.yview(END)

        if self.entry.get() == '':
            self.msg = 'Please enter some input'
            self.label_11.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_11.config(text=self.msg, fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot : Hello')

        elif(self.entry.get()=='How are you ?'):
            self.text.insert(END,'\n\n'+'Bot : I am fine and you ?')

        elif(self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot : Nice to hear')

        elif(self.entry.get()=='Who created you ?'):
            self.text.insert(END,'\n\n'+'Bot : Harshiya, Divyam, Shruti created a Face Recognition Project using Python , with a me(chatbot) integrated into it.It was done under the giudance of their Professor Ms.Madhuri Sharma. It was a great collaborative effort in developing projects and exploring different aspects of technology. If you have any specific questions or if there is anything else you would like to share or discuss, feel free to contact the developers through Help Desk')

        elif(self.entry.get()=='What is your name ?'):
            self.text.insert(END,'\n\n'+'Bot : My name is Siri')

        elif(self.entry.get()=='Which languages you can speak ?'):
            self.text.insert(END,'\n\n'+'Bot : Currently , I can speak only english . I will soon learn the other languages !')

        elif(self.entry.get()=='What is Advaned Programming Practice ?'):
            self.text.insert(END,'\n\n'+'Bot : It is a course or study focused on honing advanced programming skills, emphasizing practical application, design patterns, code optimization, and industry best practices in software development.')

        elif(self.entry.get()=='How does Face Recognition Work ?'):
            self.text.insert(END,'\n\n'+'Bot : A face recognition project implemented in Python typically begins with the collection of facial data for the first student. This process involves capturing images or embeddings of the student face using a camera and storing this information in a database. Subsequently, a machine learning model, often based on libraries like OpenCV or dlib, is employed to train on the collected facial data. The training phase enables the model to recognize and distinguish the unique features of the student face. Once the face recognition model is trained, the system is ready for attendance tracking. During this phase, the camera captures the faces of students in real-time, and the trained model is applied to identify individuals. When the system successfully recognizes the face of the first student, it links the identified face to the corresponding data stored in the database. As a result, the system can automatically mark the attendance of the recognized student, eliminating the need for manual input.<br>This project combines elements of image processing, machine learning, and database management to create an efficient and automated attendance tracking system. It not only streamlines the attendance process but also enhances accuracy and reduces the administrative burden associated with manual attendance management in educational or organizational settings.')

        elif(self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Bot : Thank you chatting ... Have a Good Day !!')

        else:
            self.text.insert(END,"\n\n"+'Bot : Sorry I did not get you.')


        

           






if __name__=='__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()