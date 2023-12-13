import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import turtle


import pymysql


class EmployeeList:
    '''this class displays the list of all the employees depending upon the selected department'''
    def __init__(self,myframe):
        self.mywindow = Toplevel(myframe)
        self.mywindow.title("Employee List")
        self.mywindow.wm_minsize(1000,600)

        bgcolor=Frame(self.mywindow,width=1900,height=2500,bg="palegoldenrod")
        bgcolor.place(x=0,y=0)
        bgcolor.pack(side=TOP,expand=NO,fill=NONE)

        headingboxlabel = Label(self.mywindow, text="List Of Employees")
        headingboxlabel.config(font=('times new roman', '24', 'bold'), bg='yellow', fg='blue')
        headingboxlabel.place(x=450, y=70)

        dept = Label(self.mywindow, text=" Select Department:",bg="palegoldenrod")
        dept.place(x=50, y=150)

        self.fetch_department()

        self.department=StringVar()

        departmentbox = ttk.Combobox(self.mywindow, textvariable=self.department, state='readonly')
        departmentbox.config(values=self.departnames)
        departmentbox.set("Choose Department")
        departmentbox.place(x=180, y=150)

        searchbtn = Button(self.mywindow, text="Search", command=self.searchemp, padx=20 )
        searchbtn.place(x=380, y=150)

        mytablearea = Frame(self.mywindow)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("emp_id","Fname", "Lname", "Designation", "department", "status"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=LEFT, fill=Y)

        self.mytable.heading("emp_id", text="Employee ID")
        self.mytable.heading("Fname", text="First Name")
        self.mytable.heading("Lname", text="Last Name")
        self.mytable.heading("Designation", text="Designation")
        self.mytable.heading("department", text="Department")
        self.mytable.heading("status", text="Status")
        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#4', stretch=NO, minwidth=0, width=150)
        self.mytable.column('#5', stretch=NO, minwidth=0, width=150)
        self.mytable.column('#6', stretch=NO, minwidth=0, width=150)
        self.mytable.bind("<ButtonRelease-1>", self.fetchbydept)
        self.mytable.pack()
        mytablearea.place(x=170,y=220,height=250)
    def fetch_department(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as x:
                    x.execute("select department from department_table")
                    resultdata = x.fetchall()
                    self.departnames = []
                    for row in resultdata:
                        self.departnames.append(row[0])

                    if len(self.departnames) == 0:
                        messagebox.showerror("Error Occured", "No Data Available",parent=self.mywindow)

            except Exception as y:
                messagebox.showerror("Error Occured", "Error in inseting query due to" + str(y),parent=self.mywindow)
        except Exception as z:
            messagebox.showerror("Error Occured", "Error in creating database due to" + str(z),parent=self.mywindow)

    def fetchbydept(self, e):
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        self.dept = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select emp_id from addemployee where department=%s",
                                   (self.dept))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:
                        self.department.set(row[0])
                        # self.empidentry.delete(0,END)
                        # self.empidentry.insert(0,row[9])
                        # self.empidentry.delete(0, END)
                        # self.empidentry.insert(0, row[3])
                        # # self.department.insert(0,row[9])


                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.",parent=self.mywindow)

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)

    def searchemp(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select emp_id,Fname,Lname,Designation, department, status from addemployee"
                                   " where department like %s", (self.department.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.",parent=self.mywindow)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)









#
#
# myframe = Tk()
# obj=EmployeeList(myframe)
# myframe.mainloop()