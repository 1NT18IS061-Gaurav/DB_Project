import traceback
from tkinter import *
from tkinter import ttk, messagebox

import pymysql

class payment_list:
    def __init__(self,myframe):
        self.mywindow = Toplevel(myframe)
        bgcolor = Frame(self.mywindow, bg="#c98a71", width=1900, height=2500)
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)
        self.mywindow.wm_title("Payment List")
        self.mywindow.geometry("%dx%d+%d+%d" % (1000, 600, 50, 50))

        month = Label(self.mywindow, text="Month:", bg="#c98a71")
        month.place(x=100, y=100)

        self.monthbox = StringVar(self.mywindow)
        self.monthinputbox = ttk.Combobox(self.mywindow, textvariable=self.monthbox, state='readonly')
        self.monthinputbox.set("Choose Month")
        self.monthinputbox.config(values=('January', 'February', 'March',
                                             'April', 'May', 'June', 'July',
                                              'August', 'September', 'October', 
                                              'November','December'))
        self.monthinputbox.bind("<<ComboboxSelected>>", self.showrecords)
        self.monthinputbox.place(x=200, y=100)

        mytablearea = Frame(self.mywindow)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=(
        "emp_id", "Fname", "Lname", "department", "Designation", "basic_pay",
        "convance_allowance", "medical_allowance", "houserent_allowance",
        "absence", "month", "income_tax", "overtime_hours", "deducted_amount","added_allowance","net_salary"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)
        self.mytable.heading("emp_id", text="Employee ID")
        self.mytable.heading("Fname", text="First Name")
        self.mytable.heading("Lname", text="Last Name")
        self.mytable.heading("department", text="Department")
        self.mytable.heading("Designation", text="Designation")
        self.mytable.heading("basic_pay", text="Basic Salary")
        self.mytable.heading("convance_allowance", text="Convance Allowance")
        self.mytable.heading("medical_allowance", text="Medical Allowance")
        self.mytable.heading("houserent_allowance", text="Houserent Allowance")
        self.mytable.heading("absence", text="Absence")
        self.mytable.heading("month", text="Month")
        self.mytable.heading("income_tax", text="Income Tax")
        self.mytable.heading("overtime_hours", text="Overtime Hours")
        self.mytable.heading("deducted_amount", text="Deducted Amount")
        self.mytable.heading("added_allowance", text="Added Allowance")
        self.mytable.heading("net_salary", text="Net Salary")


        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#4', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#5', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#6', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#7', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#8', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#9', stretch=NO, minwidth=0, width=80)
        self.mytable.column('#10', stretch=NO, minwidth=0, width=80)

        self.mytable.pack()
        mytablearea.place(x=100, y=150, height=200,width=700)

    def showrecords(self, e):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select emp_id, Fname,Lname,department,Designation,"
                                   "basic_pay,convance_allowance,medical_allowance,houserent_allowance,"
                                   "absence,month,income_tax,overtime_hours,deducted_amount,"
                                   "added_allowance,net_salary from payment_table "
                                   " where month like %s", (self.monthbox.get()))
                    myresultdata = myconn.fetchall()

                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No employees added yet.",parent=self.mywindow)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)
#
# myframe = Tk()
# obj=payment_list(myframe)
# myframe.mainloop()