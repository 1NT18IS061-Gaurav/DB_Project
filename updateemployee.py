import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askquestion

import pymysql as pymysql
from PIL import ImageTk
import time


class UpdateEmployee:
    '''this class is invoked under the admin section  called employee menu named  update employee,
    this class helps the admin to update information of an employee of the selected employee'''

    def __init__(self, myframe):

        # myframe=Tk()
        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title("Update Employee")
        self.mywindow.wm_minsize(1350,1000)
        self.finalname = "default.png"

        bgcolor = Frame(self.mywindow, bg="lavenderblush", width=1900, height=2500)
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        # self.img2=ImageTk.PhotoImage(file="image//back.jpg")
        # imglabel=Label(self.mywindow,image=self.img2)
        # imglabel.place(x=0,y=0)
        #                # ,rewidth=1,reheight=1)
        # # imglabel.place(x=0,y=0)
                       # ,relwidth=1,relheight=1)

        headingbox=Label(self.mywindow,text="Employee Modification Form",fg='blue',bg='yellow')
        headingbox.config(font=('times new roman',24,'bold'))
        headingbox.place(x=450,y=50)

        empidlabel=Label(self.mywindow,text="Employee ID", bg="lavenderblush")
        empidlabel.place(x=450,y=100)

        self.empidentry=Entry(self.mywindow)
        self.empidentry.place(x=550,y=100)

        fnamebox = Label(self.mywindow, text=" First Name", bg="lavenderblush")
        fnamebox.place(x=120, y=150)

        self.fnameentrybox = Entry(self.mywindow)
        self.fnameentrybox.place(x=300, y=150)

        lnamebox = Label(self.mywindow, text=" Last Name", bg="lavenderblush")
        lnamebox.place(x=120, y=200)

        self.lnameentrybox = Entry(self.mywindow)
        self.lnameentrybox.place(x=300, y=200)

        dobbox=Label(self.mywindow,text="Date of Birth", bg="lavenderblush")
        dobbox.place(x=120,y=250)

        self.dobentrybox=Entry(self.mywindow)
        self.dobentrybox.place(x=300,y=250)

        genderlabel=Label(self.mywindow,text="Gender", bg="lavenderblush")
        genderlabel.place(x=120,y=300)

        self.gender = StringVar()
        self.gender.set(" ")
        self.malebox=Radiobutton(self.mywindow,text="Male",variable=self.gender,value="Male", bg="lavenderblush")
        self.femalebox=Radiobutton(self.mywindow,text="Female",variable=self.gender,value="Female", bg="lavenderblush")

        self.malebox.place(x=300,y=300)
        self.femalebox.place(x=350,y=300)

        phonebox = Label(self.mywindow, text="Phone", bg="lavenderblush")
        phonebox.place(x=120, y=350)

        self.phoneentrybox = Entry(self.mywindow)
        self.phoneentrybox.place(x=300, y=350)

        emailbox = Label(self.mywindow, text="Email", bg="lavenderblush")
        emailbox.place(x=120, y=400)

        self.emailentrybox = Entry(self.mywindow)
        self.emailentrybox.place(x=300, y=400)

        addressbox = Label(self.mywindow, text="Address", bg="lavenderblush")
        addressbox.place(x=120, y=450)

        self.addressentrybox = Text(self.mywindow, height=5, width=15, bg="lavenderblush")
        self.addressentrybox.place(x=300, y=450)

        pinbox=Label(self.mywindow,text="Pin Code:", bg="lavenderblush")
        pinbox.place(x=120,y=550)

        self.pinentry=Entry(self.mywindow)
        self.pinentry.place(x=300,y=550)

        doh=Label(self.mywindow,text="Date of hired", bg="lavenderblush")
        doh.place(x=530,y=250)

        self.dohentry=Entry(self.mywindow)
        self.dohentry.place(x=640,y=250)

        basic=Label(self.mywindow,text="Basic Pay:", bg="lavenderblush")
        basic.place(x=530,y=300)

        self.basicentry=Entry(self.mywindow)
        self.basicentry.place(x=640,y=300)

        self.status = StringVar()

        statuslabel = Label(self.mywindow, text="Status:", bg="lavenderblush")
        statuslabel.place(x=530, y=350)

        statusbox = ttk.Combobox(self.mywindow, textvariable=self.status, state='readonly')
        statusbox.config(values=("Active", "Inactive"))
        statusbox.set("Choose Status")
        statusbox.place(x=640, y=350)

        courselabel = Label(self.mywindow, text="Designation:", bg="lavenderblush")
        courselabel.place(x=530, y=200)

        self.fetch_designation()

        self.course = StringVar()

        coursebox = ttk.Combobox(self.mywindow, textvariable=self.course, state='readonly')
        coursebox.config(values=self.designames)
        coursebox.set("Choose Designation")
        coursebox.place(x=640, y=200)

        updatebtn = Button(self.mywindow, text="Update", command=self.updateinfo, padx = 20,bg='pink',fg='red',font='bold')
        updatebtn.place(x=630, y=450)

        searchbtn = Button(self.mywindow, text="Search", command=self.searchinfo, padx=20, bg='pink', fg='red', font='bold')
        searchbtn.place(x=530, y=450)

        deletebtn = Button(self.mywindow, text="Delete", command=self.deleteinfo, padx=20, bg='pink', fg='red', font='bold')
        deletebtn.place(x=730, y=450)

        uploadbtn = Button(self.mywindow, text="Upload Image", command=self.uploadimage, padx=20, bg='pink', fg='red',
                           font='bold')
        uploadbtn.place(x=950, y=450)

        self.imagebox = Label(self.mywindow, text="Image", bg="lavenderblush")
                              # ,height=150,width=140)
        # , bg="lavenderblush")
        # height=100, width=100)
        self.imagebox.place(x=900, y=100)

        departmentlabel = Label(self.mywindow, text="Department:", bg="lavenderblush")
        departmentlabel.place(x=530, y=150)

        self.fetch_department()

        self.department = StringVar()

        departmentbox = ttk.Combobox(self.mywindow, textvariable=self.department, state='readonly')
        departmentbox.config(values=self.departnames)
        departmentbox.set("Choose Department")
        departmentbox.place(x=640, y=150)

        mytablearea = Frame(self.mywindow)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("Fname", "Lname"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=LEFT, fill=Y)

        self.mytable.heading("Fname", text="First Name")
        self.mytable.heading("Lname", text="Last Name")
        # self.mytable.heading("department", text="Department")
        # self.mytable.heading("EmpId 1", text="EmployeeID")
        # self.mytable.heading("Designation", text="Designation")
        # self.mytable.heading("basic_pay", text="Basic salary")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=100)
        # self.mytable.column('#3', stretch=NO, minwidth=0, width=100)
        # self.mytable.column('#4', stretch=NO, minwidth=0, width=150)
        # self.mytable.column('#5', stretch=NO, minwidth=0, width=150)
        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(x=490, y=530, height=100)


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
        '''this function fetch  all the information of an employee as per the first name of the employee'''
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        self.serialno = selectedRow[0]
        # self.imagebox1=selectedRow[13]
        # self.imagebox = ImageTk.PhotoImage(filetypes="uploadedimage//" + row[13])
        # self.imagebox.tk(image=self.filename)
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
                        self.status.set(row[14])
                        self.course.set(row[7])
                        self.filename = ImageTk.PhotoImage(file="employeeimage//" + row[13])

                        self.imagebox.config(image=self.filename)
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
                        # self.finalname.s
                        # self.imagebox1.
                        # self.imagebox.


                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.",parent=self.mywindow)

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)

    def updateinfo(self):
        '''this function allows the admin to update  the information of selected employee from the table shown a per the first name'''
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("update addemployee set Fname =%s,Lname =%s,Dob =%s,Gender=%s,phone_num=%s,email=%s ,address=%s,Designation=%s,department=%s,emp_id=%s,basic_pay=%s,doh=%s,pincode=%s,status=%s,image=%s where Fname=%s",
                                   (self.fnameentrybox.get(),self.lnameentrybox.get(),self.dobentrybox.get(),self.gender.get(),self.phoneentrybox.get(),self.emailentrybox.get(),self.addressentrybox.get('1.0',END),self.course.get(),self.department.get(),self.empidentry.get()
                                    ,self.basicentry.get(),self.dohentry.get(),self.pinentry.get(),self.status.get(),self.serialno,self.finalname))
                                   # ,self.finalname +".jpg")
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Updated Succesfully", parent=self.mywindow)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)
        self.empidentry.delete(0, END)
        self.fnameentrybox.delete(0, END)
        self.lnameentrybox.delete(0, END)
        #                     # self.lnameentrybox.insert(0, row[1])
        self.dobentrybox.delete(0, END)
        #                     # self.dobentrybox.insert(0,row[2])
        self.phoneentrybox.delete(0, END)
        #                     # self.phoneentrybox.insert(0, row[4])
        self.emailentrybox.delete(0, END)
        #                     # self.emailentrybox.insert(0, row[5])
        self.pinentry.delete(0, END)
        #                     # self.pinentry.insert(0,row[12])
        self.department.set("Choose Department")
        self.status.set(" choose status")
        self.course.set("Choose Designation")
        self.gender.set(" ")
        #                     # if row[3]=="Male":
        #                     #     self.malebox.select()
        #                     # else:
        #                     #     self.femalebox.select()
        self.addressentrybox.delete('1.0', END)
        #                     # self.addressentrybox.insert('1.0',row[6])
        self.dohentry.delete(0, END)
        #                     # self.dohentry.insert(0,row[11])
        self.basicentry.delete(0, END)
        self.imagebox.config(image='')

    def deleteinfo(self):
        '''this function allow the admin to delete all the information regarding a selected employee'''
        answer=askquestion("Are you sure","Do you really want to delete record?",icon="warning",parent=self.mywindow)
        if answer=="yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute("delete from addemployee where Fname=%s",
                                       self.fnameentrybox.get())

                        mydatabaseobj.commit()
                        messagebox.showinfo("Success","Employee deleted Succesfully",parent=self.mywindow)
                        self.empidentry.delete(0, END)
                        self.fnameentrybox.delete(0, END)
                        self.lnameentrybox.delete(0, END)
                        #                     # self.lnameentrybox.insert(0, row[1])
                        self.dobentrybox.delete(0, END)
                        #                     # self.dobentrybox.insert(0,row[2])
                        self.phoneentrybox.delete(0, END)
                        #                     # self.phoneentrybox.insert(0, row[4])
                        self.emailentrybox.delete(0, END)
                        #                     # self.emailentrybox.insert(0, row[5])
                        self.pinentry.delete(0, END)
                        #                     # self.pinentry.insert(0,row[12])
                        self.department.set("Choose Department")
                        self.status.set(" choose status")
                        self.course.set("Choose Designation")
                        self.gender.set("")
                        self.imagebox.config(image='')
                        #                     # if row[3]=="Male":
                        #                     #     self.malebox.select()
                        #                     # else:
                        #                     #     self.femalebox.select()
                        self.addressentrybox.delete('1.0', END)
                        #                     # self.addressentrybox.insert('1.0',row[6])
                        self.dohentry.delete(0, END)
                        #                     # self.dohentry.insert(0,row[11])
                        self.basicentry.delete(0, END)

                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex),parent=self.mywindow)
                finally:
                    mydatabaseobj.close()
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)

    def uploadimage(self):
        '''uploads image when upload button is clicked

        this function is invoked inside the upload button'''
        filename = askopenfilename(filetypes=[(("Picture Files", "*.jpg;*.png;*.gif"))],parent=self.mywindow)

        self.img = ImageTk.PhotoImage(file=filename)
        mydata = filename.split("/")
        self.finalname = str(int(time.time())) + mydata[-1]

        infile = open(filename, "rb")
        outfile = open("employeeimage//" + self.finalname, "wb")
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
        self.imagebox.configure(image=self.img)


    # def uploadimage(self):

        # self.filename = askopenfilename(
        # filetypes=[(("Picture Files",
        #                      "*.jpg;*.png;*.gif"))])  # show an "Open" dialog box and return the path to the selected file
        # img = ImageTk.Image.open(self.filename)
        # self.finalname = str(int(time.time()))
        # img.save("uploadedimage//" + self.finalname + ".jpg")
        # tkimage = ImageTk.PhotoImage(img)
        # self.imagebox.configure(image=tkimage)
        # self.imagebox.image = tkimage



# mywindow=Tk()
# obj=UpdateEmployee(mywindow)
# mywindow.mainloop()
