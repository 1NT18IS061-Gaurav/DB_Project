from tkinter import *
from  tkinter import ttk,messagebox
import pymysql

class CompanyList:
    def __init__(self,myframe):

        self.mywindow=Toplevel(myframe)
        self.mywindow.wm_title("Company List")
        self.mywindow.geometry("%dx%d+%d+%d" % (1000,550,150,50))

        bgcolor = Frame(self.mywindow, width=1900, height=2500, bg="palegoldenrod")
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        self.mytablearea=Frame(self.mywindow)
        scrollbarx= Scrollbar(self.mytablearea,orient=HORIZONTAL)
        scrollbary=Scrollbar(self.mytablearea,orient=VERTICAL)

        self.mytable=ttk.Treeview(self.mytablearea,columns=("cmpid","cname","owner","contact","email","address"),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
        self.mytable['show']='headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT,fill=Y)

        headingboxlabel=Label(self.mywindow,text="List Of Companies")
        headingboxlabel.config(font=('times new roman','24','bold'),bg='yellow',fg='blue')
        headingboxlabel.place(x=350,y=110)

        # mytable.heading("emp_id",text="emp")
        self.mytable.heading("cmpid",text="Company ID")
        self.mytable.heading("cname", text="Company Name")
        self.mytable.heading("owner", text="Owner Name")
        self.mytable.heading("contact",text="Contact Number")
        self.mytable.heading("address", text="Address")
        self.mytable.heading("email", text="Email-ID")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#4', stretch=NO, minwidth=0, width=150)
        self.mytable.column('#5', stretch=NO, minwidth=0, width=150)
        self.mytable.column('#6', stretch=NO, minwidth=0, width=200)
        # mytable.column("#14",stretch=NO,minwidth=0,width=80)

        self.mytable.pack()
        self.mytablearea.place(x=100,y=220,height=250)

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as x:
                    x.execute("select cmpid,cname,owner,contact,email,address from companydetail")
                    resultdata=x.fetchall()

                    for row in resultdata:
                        self.mytable.insert('',END,value=(row))

                    if resultdata==None:
                        messagebox.showerror("No Records Found","No Data Available",parent=self.mywindow)

            except Exception as y:
                messagebox.showerror("Error Occured","Error in fetching due to"+str(y),parent=self.mywindow)
        except Exception as z:
            messagebox.showerror("Error Ocured","Error in creating database due to"+str(z),parent=self.mywindow)


# mywindow=Tk()
# obj=CompanyList(mywindow)
# mywindow.mainloop()
