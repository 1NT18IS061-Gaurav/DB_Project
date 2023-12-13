from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askquestion
import pymysql
import login
class Logout:
    '''this class displays and perform the logout operation'''
    def __init__(self,myframe):
        self.mywindow=myframe

        bgcolor = Frame(self.mywindow, width=1900, height=2500, bg="palegoldenrod")
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)


        answer = askquestion("Are you sure", "Do you really want to Logout?", icon="warning",parent=self.mywindow)
        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
                try:
                    self.mywindow.destroy()
                    # self.mywindow.destroy()
                    with mydatabaseobj.cursor() as myconn:
                        # myconn.close()
                        # self.mywindow.destroy()
                        login.Mylogin()
                        # self.mywindow.destroy()
                    # self.mywindow.destroy()
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
                finally:
                    mydatabaseobj.close()
                    # self.mywindow.destroy()
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)
        # self.mywindow.destroy()
        self.mywindow.mainloop()