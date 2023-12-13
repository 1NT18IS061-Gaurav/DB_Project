from tkinter import *
from tkinter import messagebox

import pymysql


class Change_password:
    '''this class helps to change password of the account that is already created and being run ,both admin and user can change their respective password'''
    def __init__(self, myframe):

        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title("Change Password")
        self.mywindow.geometry("%dx%d+%d+%d" % (510, 350, 370, 150))
        # self.mywindow.wm_minsize(400,400)
        bgcolor = Frame(self.mywindow, bg="lavenderblush", width=1900, height=2500)
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        chg_pass = Label(self.mywindow, text="Change Password")
        chg_pass.config(bg='yellow',fg='blue',font=('times new roman',22,'bold'))
        chg_pass.place(x=130, y=50)

        uname = Label(self.mywindow, text="Username:",bg="lavenderblush")
        uname.place(x=50, y=100)
        self.unameinputbox = Entry(self.mywindow)
        self.unameinputbox.place(x=160, y=100)

        cur_pass = Label(self.mywindow, text="Current password:",bg="lavenderblush")
        cur_pass.place(x=50, y=150)
        self.cpassinputbox = Entry(self.mywindow)
        self.cpassinputbox.place(x=160, y=150)


        new_pass = Label(self.mywindow, text="New password:",bg="lavenderblush")
        new_pass.place(x=50, y=200)
        self.npassinputbox = Entry(self.mywindow)
        self.npassinputbox.place(x=160, y=200)

        cnpass = Label(self.mywindow, text="Confirm Password:",bg="lavenderblush")
        cnpass.place(x=50, y=250)
        self.cnpassinputbox = Entry(self.mywindow)
        self.cnpassinputbox.place(x=160, y=250)

        donebtn = Button(self.mywindow, text="Done",padx=20,command=self.changepassword,bg='pink',fg='red',font='bold')
        donebtn.place(x=150, y=300)

    def changepassword(self):

        if self.npassinputbox.get()==self.cnpassinputbox.get():
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
                try:
                    with mydatabaseobj.cursor() as myconn:

                        myconn.execute("update usertable set  password =%s where username=%s and password=%s ",(self.cnpassinputbox.get(),self.unameinputbox.get(),self.cpassinputbox.get()))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Password Changed",parent=self.mywindow)
                        self.mywindow.destroy()
                except Exception as ex:
                    messagebox.showerror("Error Occured", 'Error in inserting query due to' + str(ex),parent=self.mywindow)
                finally:
                    mydatabaseobj.close()
            except Exception as ex:
                  messagebox.showerror("Error Occured", "Error connecting due to" + str(ex),parent=self.mywindow)
        else:
            messagebox.showwarning("Warning","Password does not match",parent=self.mywindow)
#
# mywindow=Tk()
# obj=Change_password(mywindow)
# mywindow.mainloop()

