from tkinter import*
from tkinter import messagebox, ttk
import pymysql
from PIL import ImageTk


class CreateAdmin:
    '''this class is used for creating a new account,if the user is not registered'''
    def __init__(self):
        self.mywindow=Tk()
        # self.mywindow=Toplevel(myframe)
        self.mywindow.wm_minsize(500, 500)
        self.mywindow.wm_title("Create Account")
        # self.mywindow.geometry('500x500')


        # self.mywindow.wm_title("Create ")
        self.mywindow.geometry("%dx%d+%d+%d" % (560, 350, 350, 150))
        # self.mywindow.wm_minsize(400,400)
        bgcolor = Frame(self.mywindow, bg="moccasin", width=1900, height=2500)
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        # self.image = ImageTk.PhotoImage(file="image\\signup.png")
        # self.signuplabel = Label(self.mywindow)
        # # , image="signup.png")
        # self.signuplabel.place(x=300, y=250)
        # self.signuplabel.configure(image=self.image)
        #
        # # self.mywindow = Tk()
        # self.mywindow.title("Login")
        # self.mywindow.geometry('500x500')

        login=Label(self.mywindow,bg="moccasin",text="Create New Account",width=20,font=('bold',20))
        login.place(x=90,y=53)

        username=Label(self.mywindow,bg="moccasin",text="Username:",width=20,font=('bold',10))
        username.place(x=68,y=130)

        self.usernamebox=Entry(self.mywindow)
        self.usernamebox.place(x=240,y=130)

        password=Label(self.mywindow,bg="moccasin",text="Password:",width=20,font=('bold',10))
        password.place(x=68,y=160)

        self.passwordbox=Entry(self.mywindow)
        self.passwordbox.place(x=240,y=160)

        self.savebutton=Button(self.mywindow,bg="pink",fg='red',text="Create Account",width=15,command=self.CreateAccount,font='bold')
        self.savebutton.place(x=240,y=280)
        account = Label(self.mywindow, bg="moccasin", text="Type Account type", width=20, font=('bold', 10))
        account.place(x=68, y=200)
        self.account_type = Entry(self.mywindow)
        self.account_type.place(x=240, y=200)
        # self.account_type = StringVar()

        #print(StringVar)
        # self.typelabel=Label(self.mywindow,bg="moccasin",text="Account Type",width=20,font=('bold',10))
        # self.typelabel.place(x=68,y=230)
        #
        # self.typebox = ttk.Combobox(self.mywindow, textvariable=self.account_type, state='readonly')
        # self.typebox.config(values=('Admin','Employee'))
        # self.typebox.set("Choose Account Type")
        # self.typebox.place(x=240, y=230)
        # self.mywindow.destroy()

        self.mywindow.mainloop()

    def CreateAccount(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                        myconn.execute("insert into usertable values(%s,%s,%s)",(self.usernamebox.get(),self.passwordbox.get(),self.account_type.get()))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Account Created Successfull",parent=self.mywindow)
                        import mainfile
                        mainfile.Mainfile()
            except Exception as ex:
                messagebox.showerror("Error Occured",'Error in inserting query due to'+str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error connecting due to"+str(ex),parent=self.mywindow)
        self.mywindow.withdraw()

    # mywindow=Tk()
    # myobj=CreateAdmin()
# CreateAdmin()