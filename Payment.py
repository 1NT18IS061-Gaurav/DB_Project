import traceback
from tkinter import *
from tkinter import ttk, messagebox

import pymysql

class Payment:
    '''this class is used to calculate and manage the payment for employee'''
    def __init__(self,myframe):

        self.mywindow = Toplevel(myframe)
        self.mywindow.title("Payment ")
        self.mywindow.geometry("%dx%d+%d+%d" % (1400, 800,0, 0))

        bgcolor = Frame(self.mywindow,bg="palegoldenrod", width=1900, height=2500)
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        empid = Label(self.mywindow, text="Employee ID:",bg="palegoldenrod")
        empid.place(x=170, y=50)
        self.empidinputbox = Entry(self.mywindow)
        self.empidinputbox.place(x=250, y=50)

        firstname = Label(self.mywindow, text="First Name:",bg="palegoldenrod")
        firstname.place(x=50, y=100)
        self.fninputbox = Entry(self.mywindow)
        self.fninputbox.place(x=180, y=100)

        searchbtn = Button(self.mywindow, text="Search", command=self.searchinfo, padx=40)
        searchbtn.place(x=400, y=100)

        lastname = Label(self.mywindow, text="last Name:",bg="palegoldenrod")
        lastname.place(x=50, y=150)
        self.lninputbox = Entry(self.mywindow)
        self.lninputbox.place(x=180, y=150)

        deptname = Label(self.mywindow, text="Department:",bg="palegoldenrod")
        deptname.place(x=50, y=200)
        self.deptinputbox = Entry(self.mywindow)
        self.deptinputbox.place(x=180, y=200)

        convance = Label(self.mywindow, text="Convance Allowance:",bg="palegoldenrod")
        convance.place(x=50, y=250)
        self.convanceinputbox = Entry(self.mywindow)
        self.convanceinputbox.place(x=180, y=250)

        house_rent = Label(self.mywindow, text="House Rent Allowance:",bg="palegoldenrod")
        house_rent.place(x=50, y=300)
        self.rentinputbox = Entry(self.mywindow)
        self.rentinputbox.place(x=180, y=300)

        month = Label(self.mywindow, text="Month:",bg="palegoldenrod")
        month.place(x=50, y=350)
        self.monthinputbox = Entry(self.mywindow)
        self.monthinputbox.place(x=180, y=350)

        overtime = Label(self.mywindow, text="Overtime Hours:",bg="palegoldenrod")
        overtime.place(x=50, y=400)
        self.overtimeinputbox = Entry(self.mywindow)
        self.overtimeinputbox.place(x=180, y=400)

        add_allowance = Label(self.mywindow, text="Added Allowance:",bg="palegoldenrod")
        add_allowance.place(x=50, y=450)
        self.add_allowanceinputbox = Entry(self.mywindow)
        self.add_allowanceinputbox.place(x=180, y=450)

        ded_amt = Label(self.mywindow, text="Deducted Amount:",bg="palegoldenrod")
        ded_amt.place(x=340, y=400)
        self.ded_amtinputbox = Entry(self.mywindow)
        self.ded_amtinputbox.place(x=450, y=400)

        designation = Label(self.mywindow, text="Designation:",bg="palegoldenrod")
        designation.place(x=340, y=150)
        self.designationinputbox = Entry(self.mywindow)
        self.designationinputbox.place(x=450, y=150)

        basicsal = Label(self.mywindow, text="Basic Salary:",bg="palegoldenrod")
        basicsal.place(x=340, y=200)
        self.basicsalinputbox = Entry(self.mywindow)
        self.basicsalinputbox.place(x=450, y=200)

        med_all = Label(self.mywindow, text="Medical Allowance:",bg="palegoldenrod")
        med_all.place(x=340, y=250)
        self.med_allinputbox = Entry(self.mywindow)
        self.med_allinputbox.place(x=450, y=250)

        # totalamt = Label(self.mywindow, text="Total Amount:")
        # totalamt.place(x=340, y=300)
        # self.totalamtinputbox = Entry(self.mywindow)
        # self.totalamtinputbox.place(x=450, y=300)

        absence = Label(self.mywindow, text="Absence:",bg="palegoldenrod")
        absence.place(x=340, y=300)
        self.absenceinputbox = Entry(self.mywindow)
        self.absenceinputbox.place(x=450, y=300)

        # late = Label(self.mywindow, text="Late:")
        # late.place(x=340, y=400)
        # self.lateinputbox = Entry(self.mywindow)
        # self.lateinputbox.place(x=450, y=400)
        #
        # half_day = Label(self.mywindow, text="Half Day:")
        # half_day.place(x=340, y=450)
        # self.half_dayinputbox = Entry(self.mywindow)
        # self.half_dayinputbox.place(x=450, y=450)

        inctax = Label(self.mywindow, text="Income Tax:",bg="palegoldenrod")
        inctax.place(x=340, y=350)
        self.inc_taxinputbox = Entry(self.mywindow)
        self.inc_taxinputbox.place(x=450, y=350)

        netsal = Label(self.mywindow, text="Net Salary:",bg="palegoldenrod")
        netsal.place(x=340, y=450)
        self.netsalinputbox = Entry(self.mywindow)
        self.netsalinputbox.place(x=450, y=450)

        payment_btn=Button(self.mywindow,text="Payment Done",command=self.paymentinfo,bg='pink')
        payment_btn.place(x=350,y=500)

        calculation_btn = Button(self.mywindow, text="Calculate net salary", command=self.calculate_income)
        calculation_btn.place(x=130, y=500)

        attendance_btn= Button(self.mywindow, text="mark absence", command=self.count_attendance)
        attendance_btn.place(x=250, y=500)

        mytablearea = Frame(self.mywindow)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=(
            "emp_id", "Fname", "Lname",
            "Designation", "department", "basic_pay"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("emp_id", text="Employee ID")
        self.mytable.heading("Fname", text="First Name")
        self.mytable.heading("Lname", text="Last Name")
        self.mytable.heading("Designation", text="Designation")
        self.mytable.heading("department", text="Department")
        self.mytable.heading("basic_pay", text="Basic Salary")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=80)
        self.mytable.bind("<ButtonRelease-1>", self.fetchbyempid)
        self.mytable.pack()
        mytablearea.place(x=600, y=100, height=200, width=700)

        calculatorlabel=Label(self.mywindow,text="Calculator")
        calculatorlabel.place(x=780,y=330)

        self.expression = ""
        self.equation = StringVar(self.mywindow)
        expression_field = Entry(self.mywindow, textvariable=self.equation,width=38)
        expression_field.place(x=700, y=370)

        self.equation.set('')
        button1 = Button(self.mywindow, text=' 1 ', fg='black', bg='blue',
                         command=lambda: self.press(1), height=1, width=7)
        button1.place(x=700, y=390)

        button2 = Button(self.mywindow, text=' 2 ', fg='black', bg='blue',
                         command=lambda: self.press(2), height=1, width=7)
        button2.place(x=758, y=390)

        button3 = Button(self.mywindow, text=' 3 ', fg='black', bg='blue',
                         command=lambda: self.press(3), height=1, width=7)
        button3.place(x=816, y=390)

        button4 = Button(self.mywindow, text=' 4 ', fg='black', bg='blue',
                         command=lambda: self.press(4), height=1, width=7)
        button4.place(x=700, y=416)

        button5 = Button(self.mywindow, text=' 5 ', fg='black', bg='blue',
                         command=lambda: self.press(5), height=1, width=7)
        button5.place(x=758, y=416)

        button6 = Button(self.mywindow, text=' 6 ', fg='black', bg='blue',
                         command=lambda: self.press(6), height=1, width=7)
        button6.place(x=816, y=416)

        button7 = Button(self.mywindow, text=' 7 ', fg='black', bg='blue',
                         command=lambda: self.press(7), height=1, width=7)
        button7.place(x=700, y=442)

        button8 = Button(self.mywindow, text=' 8 ', fg='black', bg='blue',
                         command=lambda: self.press(8), height=1, width=7)
        button8.place(x=758, y=442)

        button9 = Button(self.mywindow, text=' 9 ', fg='black', bg='blue',
                         command=lambda: self.press(9), height=1, width=7)
        button9.place(x=816, y=442)

        button0 = Button(self.mywindow, text=' 0 ', fg='black', bg='blue',
                         command=lambda: self.press(0), height=1, width=7)
        button0.place(x=700, y=468)

        plus = Button(self.mywindow, text=' + ', fg='black', bg='blue',
                      command=lambda: self.press("+"), height=1, width=7)
        plus.place(x=874, y=390)

        minus = Button(self.mywindow, text=' - ', fg='black', bg='blue',
                       command=lambda: self.press("-"), height=1, width=7)
        minus.place(x=874, y=416)

        multiply = Button(self.mywindow, text=' * ', fg='black', bg='blue',
                          command=lambda: self.press("*"), height=1, width=7)
        multiply.place(x=874, y=442)

        divide = Button(self.mywindow, text=' / ', fg='black', bg='blue',
                        command=lambda: self.press("/"), height=1, width=7)
        divide.place(x=874, y=468)

        equal = Button(self.mywindow, text=' = ', fg='black', bg='blue',
                       command=self.equalpress, height=1, width=7)
        equal.place(x=816, y=468)

        clear = Button(self.mywindow, text='Clear', fg='black', bg='blue',
                       command=self.clear, height=1, width=7)
        clear.place(x=758, y=468)

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set(" error ")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

    def calculate_income(self):
        value=int(self.basicsalinputbox.get())
        if value<=10000:
            self.rentinputbox.delete(0,END)
            self.rentinputbox.insert(0,"1850")
            self.convanceinputbox.delete(0,END)
            self.convanceinputbox.insert(0,"1000")
            self.med_allinputbox.delete(0, END)
            self.med_allinputbox.insert(0, "1000")
            self.add_allowanceinputbox.delete(0, END)
            self.add_allowanceinputbox.insert(0, "800")
            tax=(12/100)*value
            self.inc_taxinputbox.delete(0,END)
            self.inc_taxinputbox.insert(0,tax)
        elif value>10000 and value<=20000:
            self.rentinputbox.delete(0, END)
            self.rentinputbox.insert(0, "2850")
            self.convanceinputbox.delete(0, END)
            self.convanceinputbox.insert(0, "2000")
            self.med_allinputbox.delete(0, END)
            self.med_allinputbox.insert(0, "2000")
            self.add_allowanceinputbox.delete(0, END)
            self.add_allowanceinputbox.insert(0, "800")
            tax = (12 / 100) * value
            self.inc_taxinputbox.delete(0, END)
            self.inc_taxinputbox.insert(0, tax)
        elif value > 20000 and value <= 30000:
            self.rentinputbox.delete(0, END)
            self.rentinputbox.insert(0, "3850")
            self.convanceinputbox.delete(0, END)
            self.convanceinputbox.insert(0, "3000")
            self.med_allinputbox.delete(0, END)
            self.med_allinputbox.insert(0, "3000")
            self.add_allowanceinputbox.delete(0, END)
            self.add_allowanceinputbox.insert(0, "1800")
            tax = (12 / 100) * value
            self.inc_taxinputbox.delete(0, END)
            self.inc_taxinputbox.insert(0, tax)
        elif value > 30000 and value <= 40000:
            self.rentinputbox.delete(0, END)
            self.rentinputbox.insert(0, "3850")
            self.convanceinputbox.delete(0, END)
            self.convanceinputbox.insert(0, "3000")
            self.med_allinputbox.delete(0, END)
            self.med_allinputbox.insert(0, "3000")
            self.add_allowanceinputbox.delete(0, END)
            self.add_allowanceinputbox.insert(0, "2800")
            tax = (12 / 100) * value
            self.inc_taxinputbox.delete(0, END)
            self.inc_taxinputbox.insert(0, tax)
        else:
            self.rentinputbox.delete(0, END)
            self.rentinputbox.insert(0, "4850")
            self.convanceinputbox.delete(0, END)
            self.convanceinputbox.insert(0, "4000")
            self.med_allinputbox.delete(0, END)
            self.med_allinputbox.insert(0, "4000")
            self.add_allowanceinputbox.delete(0, END)
            self.add_allowanceinputbox.insert(0, "3800")
            tax = (12 / 100) * value
            self.inc_taxinputbox.delete(0, END)
            self.inc_taxinputbox.insert(0, tax)


    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select emp_id,Fname,Lname,Designation,department,basic_pay from addemployee "
                                   " where Fname like %s", (self.fninputbox.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())

                    for row in myresultdata:
                       self.mytable.insert('',END,value=(row))
                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.",parent=self.mywindow)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)

    def fetchbyempid(self, e):
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        employee_ID = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select emp_id,Fname,Lname,Designation,department,basic_pay  from addemployee where emp_id=%s",
                                   (employee_ID))
                    myresultdata = myconn.fetchall()


                    for row in myresultdata:
                        self.empidinputbox.delete(0,END)
                        self.empidinputbox.insert(0,row[0])
                        self.fninputbox.delete(0, END)
                        self.fninputbox.insert(0, row[1])
                        self.lninputbox.delete(0, END)
                        self.lninputbox.insert(0, row[2])
                        self.designationinputbox.delete(0, END)
                        self.designationinputbox.insert(0, row[3])
                        self.deptinputbox.delete(0, END)
                        self.deptinputbox.insert(0, row[4])
                        self.basicsalinputbox.delete(0, END)
                        self.basicsalinputbox.insert(0, row[5])
                        self.absenceinputbox.delete(0,END)
                        self.rentinputbox.delete(0,END)
                        self.convanceinputbox.delete(0,END)
                        self.med_allinputbox.delete(0,END)
                        self.add_allowanceinputbox.delete(0,END)
                        self.inc_taxinputbox.delete(0,END)

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No employees added yet.",parent=self.mywindow)

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching in due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)

    def count_attendance(self):
        mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="addemployeedb")
        try:

            with mydatabaseobj.cursor() as myconn:
                myconn.execute("select * from attendence_table "
                               " where emp_id like %s", (self.empidinputbox.get() + "%"))
                myresultdata = myconn.fetchall()
                # self.mytable.delete(*self.mytable.get_children())
                c = 0

                for row in myresultdata:
                    if row[3]=="absent":
                        c=int(c)+1
                self.absenceinputbox.delete(0,END)
                self.absenceinputbox.insert(0,c)

                if myresultdata == None:
                    messagebox.showerror("No Records Found", "No Students added yet.",parent=self.mywindow)

                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)
        # self.absenceinputbox.delete(0,END)

    def paymentinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into payment_table(emp_id,Fname,Lname,department,Designation,"
                                   "basic_pay,convance_allowance,medical_allowance,houserent_allowance,"
                                   "absence,month,income_tax,overtime_hours,deducted_amount,added_allowance,net_salary) "
                                   "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                   self.empidinputbox.get(),self.fninputbox.get(),self.lninputbox.get(),self.deptinputbox.get() ,
                                   self.designationinputbox.get(),self.basicsalinputbox.get(),self.convanceinputbox.get(),
                                   self.med_allinputbox.get(),self.rentinputbox.get(),self.absenceinputbox.get(),
                                   self.monthinputbox.get(),self.inc_taxinputbox.get(),self.overtimeinputbox.get(),
                                   self.ded_amtinputbox.get(),self.add_allowanceinputbox.get(),self.netsalinputbox.get()))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.mywindow)
                    self.empidinputbox.delete(0,END)
                    self.absenceinputbox.delete(0,END)
                    self.add_allowanceinputbox.delete(0,END)
                    self.basicsalinputbox.delete(0,END)
                    self.convanceinputbox.delete(0,END)
                    self.ded_amtinputbox.delete(0,END)
                    self.deptinputbox.delete(0,END)
                    self.designationinputbox.delete(0,END)
                    self.fninputbox.delete(0,END)
                    self.inc_taxinputbox.delete(0,END)
                    self.lninputbox.delete(0,END)
                    self.med_allinputbox.delete(0,END)
                    self.monthinputbox.delete(0,END)
                    self.netsalinputbox.delete(0,END)
                    self.overtimeinputbox.delete(0,END)
                    self.rentinputbox.delete(0,END)


            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)



#
# myframe=Tk()
# obj=Payment(myframe)
# myframe.mainloop()