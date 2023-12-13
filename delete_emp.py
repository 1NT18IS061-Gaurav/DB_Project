import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql


class DeleteEmployee:

    def __init__(self, myframe):
        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title("Delete Employee")
        self.mywindow.wm_minsize(900,900)

        headingbox=Label(self.mywindow,text="Employee Deletion Form",fg='blue',bg='yellow')
        headingbox.config(font=('times new roman',24,'bold'))
        headingbox.place(x=450,y=50)

        empidlabel=Label(self.mywindow,text="Employee ID")
        empidlabel.place(x=450,y=100)

        self.empidentry=Entry(self.mywindow)
        self.empidentry.place(x=550,y=100)

        fnamebox = Label(self.mywindow, text=" First Name")
        fnamebox.place(x=100, y=150)

        self.fnameentrybox = Entry(self.mywindow)
        self.fnameentrybox.place(x=300, y=150)

        lnamebox = Label(self.mywindow, text=" Last Name")
        lnamebox.place(x=120, y=200)

        self.lnameentrybox = Entry(self.mywindow)
        self.lnameentrybox.place(x=300, y=200)

        dobbox=Label(self.mywindow,text="Date of Birth")
        dobbox.place(x=120,y=250)

        self.dobentrybox=Entry(self.mywindow)
        self.dobentrybox.place(x=300,y=250)

        genderlabel=Label(self.mywindow,text="Gender")
        genderlabel.place(x=120,y=300)

        self.gender = StringVar()
        self.gender.set(" ")

        self.malebox=Radiobutton(self.mywindow,text="Male",variable=self.gender,value="Male")
        self.femalebox=Radiobutton(self.mywindow,text="Female",variable=self.gender,value="Female")

        self.malebox.place(x=300,y=300)
        self.femalebox.place(x=350,y=300)

        phonebox = Label(self.mywindow, text="Phone")
        phonebox.place(x=120, y=350)

        self.phoneentrybox = Entry(self.mywindow)
        self.phoneentrybox.place(x=300, y=350)

        emailbox = Label(self.mywindow, text="Email")
        emailbox.place(x=120, y=400)

        self.emailentrybox = Entry(self.mywindow)
        self.emailentrybox.place(x=300, y=400)

        addressbox = Label(self.mywindow, text="Address")
        addressbox.place(x=120, y=450)

        self.addressentrybox = Text(self.mywindow, height=5, width=15)
        self.addressentrybox.place(x=300, y=450)

        pinbox=Label(self.mywindow,text="Pin Code:")
        pinbox.place(x=120,y=550)

        self.pinentry=Entry(self.mywindow)
        self.pinentry.place(x=300,y=550)

        doh=Label(self.mywindow,text="Date of hired")
        doh.place(x=530,y=250)

        self.dohentry=Entry(self.mywindow)
        self.dohentry.place(x=640,y=250)

        basic=Label(self.mywindow,text="Basic Pay:")
        basic.place(x=530,y=300)

        self.basicentry=Entry(self.mywindow)
        self.basicentry.place(x=640,y=300)


        courselabel = Label(self.mywindow, text="Designation")
        courselabel.place(x=530, y=200)

        self.fetch_designation()

        self.course = StringVar()

        coursebox = ttk.Combobox(self.mywindow, textvariable=self.course, state='readonly')
        coursebox.config(values=self.designames)
        coursebox.set("Choose Designation")
        coursebox.place(x=640, y=200)

        savebtn = Button(self.mywindow, text="Save", command=self.saveinfo, padx = 20,bg='pink',fg='red',font='bold')
        savebtn.place(x=630, y=450)

        searchbtn = Button(self.mywindow, text="Search", command=self.searchinfo, padx=20, bg='pink', fg='red', font='bold')
        searchbtn.place(x=530, y=450)

        delbtn = Button(self.mywindow, text="Delete", command=self.deleteinfo, padx=20, bg='pink', fg='red', font='bold')
        delbtn.place(x=730, y=450)

        departmentlabel = Label(self.mywindow, text="Department")
        departmentlabel.place(x=530, y=150)

        self.department = StringVar()

        self.fetch_department()

        self.department = StringVar()

        departmentbox = ttk.Combobox(self.mywindow, textvariable=self.department, state='readonly')
        departmentbox.config(values=self.departnames)
        departmentbox.set("Choose Department")
        departmentbox.place(x=640, y=150)

        mytablearea = Frame(self.mywindow)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("Fname", "Lname", "Designation", "department"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=LEFT, fill=Y)

        self.mytable.heading("Fname", text="First Name")
        self.mytable.heading("Lname", text="Last Name")
        self.mytable.heading("department", text="Department")
        # self.mytable.heading("EmpId 1", text="EmployeeID")
        self.mytable.heading("Designation", text="Designation")
        # self.mytable.heading("basic_pay", text="Basic salary")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#4', stretch=NO, minwidth=0, width=150)
        # self.mytable.column('#5', stretch=NO, minwidth=0, width=150)
        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(x=800, y=100, height=100)



    def fetch_department(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as x:
                    x.execute("select department from department_table")
                    resultdata=x.fetchall()
                    self.departnames=[]
                    for row in resultdata:
                        self.departnames.append(row[0])

                    if len(self.departnames)==0:
                        messagebox.showerror("Error Occured","No Data Available",parent=self.mywindow)

            except Exception as y:
                messagebox.showerror("Error Occured","Error in inseting query due to"+str(y),parent=self.mywindow)
        except Exception as z:
            messagebox.showerror("Error Ocured","Error in creating database due to"+str(z),parent=self.mywindow)


    def fetch_designation(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as x:
                    x.execute("select Designation from designation_table")
                    resultdata=x.fetchall()
                    self.designames=[]
                    for row in resultdata:
                        self.designames.append(row[0])

                    if len(self.designames)==0:
                        messagebox.showerror("Error Occured","No Data Available",parent=self.mywindow)

            except Exception as y:
                messagebox.showerror("Error Occured","Error in inseting query due to"+str(y),parent=self.mywindow)
        except Exception as z:
            messagebox.showerror("Error Occured","Error in creating database due to"+str(z),parent=self.mywindow)


    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from addemployee"
                                       " where Fname like %s", (self.fnameentrybox.get() + "%"))
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

    def fetchbysrno(self, e):
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        self.serialno = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from addemployee where Fname=%s",
                                   (self.serialno))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:
                        print(row)
                        self.empidentry.delete(0,END)
                        self.empidentry.insert(0,row[9])
                        self.fnameentrybox.delete(0, END)
                        self.fnameentrybox.insert(0, row[0])
                        self.lnameentrybox.delete(0, END)
                        self.lnameentrybox.insert(0, row[1])
                        self.dobentrybox.delete(0,END)
                        self.dobentrybox.insert(0,row[2])
                        self.phoneentrybox.delete(0, END)
                        self.phoneentrybox.insert(0, row[4])
                        self.emailentrybox.delete(0, END)
                        self.emailentrybox.insert(0, row[5])
                        self.pinentry.delete(0,END)
                        self.pinentry.insert(0,row[12])
                        self.department.set(row[8])
                        self.course.set(row[7])
                        if row[3]=="Male":
                            self.malebox.select()
                        else:
                            self.femalebox.select()
                        self.addressentrybox.delete('1.0', END)
                        self.addressentrybox.insert('1.0',row[6])
                        self.dohentry.delete(0,END)
                        self.dohentry.insert(0,row[11])
                        self.basicentry.delete(0,END)
                        self.basicentry.insert(0,row[10])


                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.",parent=self.mywindow)

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)


    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into addemployee(Fname,Lname,Dob,Gender,phone_num,email, address,Designation,department,emp_id,basic_pay,doh,pincode) "
                                   "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.fnameentrybox.get(),self.lnameentrybox.get() ,self.phoneentrybox.get(),self.dobentrybox.get(), self.emailentrybox.get(),self.gender.get(), self.addressentrybox.get('1.0',END),
                                                                          self.course.get(),self.department.get(),self.empidentry.get(),self.basicentry.get(),self.dohentry.get(),self.pinentry.get()))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.mywindow)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)
