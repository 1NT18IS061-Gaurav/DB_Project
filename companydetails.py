from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
import time

import pymysql as pymysql
from PIL import ImageTk


class CompanyDetails:
    '''this class is used to add details about the company'''

    def __init__(self, myframe):
        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title(" Manage Company")
        self.mywindow.wm_minsize(800,600)

        bgcolor = Frame(self.mywindow, width=1900, height=2500, bg="palegoldenrod")
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        namebox = Label(self.mywindow, text="Company Name",bg="palegoldenrod")
        namebox.place(x=150, y=100)

        self.nameentrybox = Entry(self.mywindow)
        self.nameentrybox.place(x=300, y=100)

        self.finalname = "logo.png"

        self.imagebox = Label(self.mywindow, text="Image",bg="lightgoldenrodyellow")
        self.imagebox.place(x=620, y=100)

        uploadbtn = Button(self.mywindow,bg='pink',fg='red',text="Upload Image", command=self.uploadimage, padx=20)
        uploadbtn.place(x=630, y=400)

        cmpid=Label(self.mywindow,text="Company ID:",bg="palegoldenrod")
        cmpid.place(x=550,y=50)

        self.cmpidentry=Entry(self.mywindow)
        self.cmpidentry.place(x=650,y=50)

        owner=Label(self.mywindow,text="Owner",bg="palegoldenrod")
        owner.place(x=150,y=150)


        self.ownerentry=Entry(self.mywindow)
        self.ownerentry.place(x=300,y=150)


        head = Label(self.mywindow, text="Company Details",bg="palegoldenrod")
        head.config(bg='yellow',fg='blue',font=('times new roman',22,'bold'))
        head.place(x=300, y=50)

        
        companyslogan=Label(self.mywindow,text="Slogan:",bg="palegoldenrod")
        companyslogan.place(x=150,y=200)
        
        self.companysloganentry=Entry(self.mywindow)
        self.companysloganentry.place(x=300,y=200)

        phonebox = Label(self.mywindow, text="Contact Number:",bg="palegoldenrod")
        phonebox.place(x=150, y=250)

        self.phoneentrybox = Entry(self.mywindow)
        self.phoneentrybox.place(x=300, y=250)

        website=Label(self.mywindow,text="Website",bg="palegoldenrod")
        website.place(x=150,y=550)

        self.websiteentry=Entry(self.mywindow)
        self.websiteentry.place(x=300,y=550)

        emailbox = Label(self.mywindow, text="Email Address",bg="palegoldenrod")
        emailbox.place(x=150, y=300)

        self.emailentrybox = Entry(self.mywindow)
        self.emailentrybox.place(x=300, y=300)

        addressbox = Label(self.mywindow, text="Address",bg="palegoldenrod")
        addressbox.place(x=150, y=350)

        self.addressentrybox = Text(self.mywindow, height=5, width=15)
        self.addressentrybox.place(x=300, y=350)
        
        
        establish=Label(self.mywindow,text="Established In:",bg="palegoldenrod")
        establish.place(x=150,y=470)
        
        self.establishentry=Entry(self.mywindow)
        self.establishentry.place(x=300,y=470)


        savebtn = Button(self.mywindow, text="Save",fg='red',font='bold',bg='pink', command=self.saveinfo, padx = 20)
        savebtn.place(x=690, y=470)

    def uploadimage(self):
        filename = askopenfilename(filetypes=[(("Picture Files", "*.jpg;*.png;*.gif"))],parent=self.mywindow)

        self.img = ImageTk.PhotoImage(file=filename)
        mydata = filename.split("/")
        self.finalname = str(int(time.time())) + mydata[-1]

        infile = open(filename, "rb")
        outfile = open("companyimage//" + self.finalname, "wb")
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
        self.imagebox.configure(image=self.img)


    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into companydetail(cname,owner,slogan,contact,email,address,yearestb,website,cmpid,logo)"
                                   "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.nameentrybox.get(), self.ownerentry.get(), self.companysloganentry.get(), self.phoneentrybox.get(),self.emailentrybox.get(),self.addressentrybox.get('1.0',END), self.establishentry.get(),self.websiteentry.get(),self.cmpidentry.get(),self.finalname))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully",parent=self.mywindow)
                    self.addressentrybox.delete('1.0',END)
                    self.emailentrybox.delete(0,END)
                    self.phoneentrybox.delete(0,END)
                    self.cmpidentry.delete(0,END)
                    self.websiteentry.delete(0,END)
                    self.establishentry.delete(0,END)
                    self.companysloganentry.delete(0,END)
                    self.ownerentry.delete(0,END)
                    self.nameentrybox.delete(0,END)
                # self.imagebox.config("")
                #     self.finalname = " "
                #     self.imagebox.config(self.finalname)
                    self.imagebox.config(image='')



            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)


# mywindow=Tk()
# obj=CompanyDetails(mywindow)
# mywindow.mainloop()