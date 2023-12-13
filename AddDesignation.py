from tkinter import *
from tkinter import messagebox

import pymysql as pymysql
from pymysql.connections import Connection


class AddDesignation:
    '''this class is used to add designtion'''
    def __init__(self, myframe):
        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title("Add designation")
        self.mywindow.geometry("%dx%d+%d+%d" % (550, 350,350, 150))
        bgcolor = Frame(self.mywindow,bg="peachpuff", width=1900, height=2500,)
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)


        designationbox = Label(self.mywindow, bg="peachpuff",text="Enter the name of Designation:",font='bold')
        designationbox.place(x=50, y=100)

        self.designationentrybox = Entry(self.mywindow)
        self.designationentrybox.place(x=330, y=110)

        savebtn = Button(self.mywindow, text="Save", command=self.saveinfo, padx=20)
        savebtn.config(bg='pink',fg='red',font='23')
        savebtn.place(x=200, y=170)

    def saveinfo(self):

        try:
            mydatabaseobj= pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into designation_table(Designation) ""values(%s)",(self.designationentrybox.get()))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.mywindow)
                    self.designationentrybox.delete(0,END)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)


# self.mywindow = Tk()
# obj = AddDesignation(self.mywindow)
# self.mywindow.mainloop()
