from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from PIL import ImageTk
import time
import pymysql as pymysql
from tkcalendar import *


class AddEmployee:
    '''this class allow the admin to add new employee'''

    def __init__(self,myframe):
        # myframe=Tk()
        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title("Register Employee")
        self.mywindow.wm_minsize(1350,1000)
        self.finalname = "default.png"
        bgcolor = Frame(self.mywindow,bg="lavender", width=1900, height=2500)
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        headingbox=Label(self.mywindow,text="Employee Registration Form",fg='blue',bg='white')
        headingbox.config(font=('times new roman',24,'bold'))
        headingbox.place(x=450,y=50)

        empidlabel=Label(self.mywindow,text="Employee ID",bg="lavender")
        empidlabel.place(x=450,y=100)

        self.empidentry=Entry(self.mywindow)
        self.empidentry.place(x=550,y=100)

        fnamebox = Label(self.mywindow, text=" First Name",bg="lavender")
        fnamebox.place(x=120, y=150)

        self.fnameentrybox = Entry(self.mywindow)
        self.fnameentrybox.place(x=300, y=150)

        lnamebox = Label(self.mywindow, text=" Last Name",bg="lavender")
        lnamebox.place(x=120, y=200)

        self.lnameentrybox = Entry(self.mywindow)
        self.lnameentrybox.place(x=300, y=200)

        dobbox=Label(self.mywindow,text="Date of Birth",bg="lavender")
        dobbox.place(x=120,y=250)

        self.dobentrybox= DateEntry(self.mywindow, font="Arial 10",bg="lavender")
        self.dobentrybox.place(x=300,y=250)

        genderlabel=Label(self.mywindow,text="Gender",bg="lavender")
        genderlabel.place(x=120,y=300)

        self.gender = StringVar()
        self.gender.set(" ")

        malebox=Radiobutton(self.mywindow,text="Male",variable=self.gender,value="Male",bg="lavender")
        femalebox=Radiobutton(self.mywindow,text="Female",variable=self.gender,value="Female",bg="lavender")

        malebox.place(x=300,y=300)
        femalebox.place(x=350,y=300)

        phonebox = Label(self.mywindow, text="Phone",bg="lavender")
        phonebox.place(x=120, y=350)

        self.phoneentrybox = Entry(self.mywindow)
        self.phoneentrybox.place(x=300, y=350)

        emailbox = Label(self.mywindow, text="Email",bg="lavender")
        emailbox.place(x=120, y=400)

        self.emailentrybox = Entry(self.mywindow)
        self.emailentrybox.place(x=300, y=400)

        addressbox = Label(self.mywindow, text="Address",bg="lavender")
        addressbox.place(x=120, y=450)

        self.addressentrybox = Text(self.mywindow, height=5, width=15)
        self.addressentrybox.place(x=300, y=450)

        pinbox=Label(self.mywindow,text="Pin Code:",bg="lavender")
        pinbox.place(x=120,y=550)

        self.pinentry=Entry(self.mywindow)
        self.pinentry.place(x=300,y=550)

        doh=Label(self.mywindow,text="Date of hired",bg="lavender")
        doh.place(x=530,y=250)

        self.dohentry = DateEntry(self.mywindow, font="Arial 10",bg="lavender")
        self.dohentry.place(x=640, y=250)

        # self.dohentry=Calendar(self.mywindow,font="Arial 14")
        # self.dohentry.place(x=640,y=250)

        basic=Label(self.mywindow,text="Basic Pay:",bg="lavender")
        basic.place(x=530,y=300)

        self.basicentry=Entry(self.mywindow)
        self.basicentry.place(x=640,y=300)

        self.status = StringVar()

        statuslabel = Label(self.mywindow, text="Status:",bg="lavender")
        statuslabel.place(x=530, y=350)

        statusbox = ttk.Combobox(self.mywindow, textvariable=self.status, state='readonly')
        statusbox.config(values=("Active", "Inactive"))
        statusbox.set("Choose Status")
        statusbox.place(x=640, y=350)

        # self.imagebox = Label(self.mywindow,bg="lavender", text="Image",height=300,width=300,font='bold')
        # self.imagebox.place(x=900, y=100)

        self.imagebox = Label(self.mywindow,bg="lavender",text=".",font='bold')
        self.imagebox.place(x=840, y=100)

        uploadbtn = Button(self.mywindow, text="Upload Image", command=self.uploadimage, padx=20)
        uploadbtn.place(x=950, y=450)


        courselabel = Label(self.mywindow, text="Designation",bg="lavender")
        courselabel.place(x=530, y=200)

        self.fetch_designation()

        self.course = StringVar()

        coursebox = ttk.Combobox(self.mywindow, textvariable=self.course, state='readonly')
        coursebox.config(values=self.designames)
        coursebox.set("Choose Designation")
        coursebox.place(x=640, y=200)

        savebtn = Button(self.mywindow, text="Save", command=self.saveinfo, padx = 20,bg='pink',fg='red',font='bold')
        savebtn.place(x=630, y=450)


        departmentlabel = Label(self.mywindow, text="Department",bg="lavender")
        departmentlabel.place(x=530, y=150)

        self.fetch_department()

        self.department = StringVar()

        departmentbox = ttk.Combobox(self.mywindow, textvariable=self.department, state='readonly')
        departmentbox.config(values=self.departnames)
        departmentbox.set("Choose Department")
        departmentbox.place(x=640, y=150)

        # self.mywindow.mainloop()
        # self.imageuploadbutton=Button(self.mywindow,text="upload")

    def uploadimage(self):
        '''uploads image'''
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
    #
    #     self.filename = askopenfilename(
    #     filetypes=[(("Picture Files",
    #                          "*.jpg;*.png;*.gif"))])  # show an "Open" dialog box and return the path to the selected file
    #     img = ImageTk.Image.open(self.filename)
    #     self.finalname = str(int(time.time()))
    #     img.save("uploadedimage//" + self.finalname + ".jpg")
    #     tkimage = ImageTk.PhotoImage(img)
    #     self.imagebox.config(image=tkimage)
    #     self.imagebox.image = tkimage
        # infile=open(filename,'rb')
        # outfile=open()
        # filename = askopenfilename(filetypes=[(("Picture Files", "*.jpg;*.png;*.gif"))])
        #
        # self.img = ImageTk.PhotoImage(PIL.ImageTk.Image.open(filename))
        #
        # self.imagebox.configure(image=self.img)
        # # (ImageTk.PhotoImage(PIL.ImageTk.Image.(filename)))
        # # self.img.show()
        # # self.img.__reduce__()



    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into addemployee(Fname,Lname,Dob,Gender,phone_num, email, address,Designation,department,emp_id,basic_pay,doh,pincode,image,status) "
                                   "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.fnameentrybox.get(),self.lnameentrybox.get()
                                        ,self.dobentrybox.get_date(),self.gender.get(),self.phoneentrybox.get(), self.emailentrybox.get(), self.addressentrybox.get('1.0',END),self.course.get(),self.department.get(),self.empidentry.get(),self.basicentry.get(),self.dohentry.get_date(),self.pinentry.get(),self.finalname,self.status.get()))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.mywindow)

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
                    self.status.set("Choose status")
                    self.course.set("Choose Designation")
                    self.gender.set(" ")
                                   #     self.femalebox.select()
                    self.addressentrybox.delete('1.0', END)
                    #                     # self.addressentrybox.insert('1.0',row[6])
                    self.dohentry.delete(0, END)
                    #                     # self.dohentry.insert(0,row[11])
                    self.basicentry.delete(0, END)
                    self.imagebox.config(image='')


            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)

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
# #zzz
# mywindow=Tk()
# obj=AddEmployee(mywindow)
# mywindow.mainloop()
