from tkinter import *
from tkinter import ttk, messagebox

import pymysql as pymysql


class AddDepartment:
    '''this class is used to add department'''

    def __init__(self, myframe):
        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title("Add Department")
        self.mywindow.geometry("%dx%d+%d+%d" % (550, 350, 350, 150))


        bgcolor=Frame(self.mywindow,width=1900,height=2500,bg="palegoldenrod")
        bgcolor.place(x=0,y=0)
        bgcolor.pack(side=TOP,expand=NO,fill=NONE)

        departmentbox = Label(self.mywindow, text="Department Name",font='bold',bg="palegoldenrod")
        departmentbox.place(x=100, y=100)

        self.departmententry = Entry(self.mywindow)
        self.departmententry.place(x=300, y=108)
        savebtn = Button(self.mywindow, text="Save", command=self.saveinfo,bg='pink',fg='red',padx=20)
        savebtn.place(x=300, y=150)

    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into department_table(department)""values(%s)",(self.departmententry.get()))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Department Added Successfully",parent=self.mywindow)
                    self.departmententry.delete(0,END)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)


# self.mywindow= Tk()
# obj=AddDepartment(mywindow)
# mywindow.mainloop()