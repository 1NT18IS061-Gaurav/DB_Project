from tkinter import *
from  tkinter import ttk,messagebox
import pymysql

class HolidayList:
    '''this class diplays the list of the holidays'''
    def __init__(self,myframe):
        self.mywindow=Toplevel(myframe)
        self.mywindow.wm_title("Holiday List")
        self.mywindow.geometry("%dx%d+%d+%d" % (600,450,350,100))
        bgcolor = Frame(self.mywindow, width=1900, height=2500, bg="peachpuff")
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        mytablearea=Frame(self.mywindow)
        scrollbarx= Scrollbar(mytablearea,orient=HORIZONTAL)
        scrollbary=Scrollbar(mytablearea,orient=VERTICAL)

        mytable=ttk.Treeview(mytablearea,columns=("date","hname"),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
        mytable['show']='headings'
        scrollbarx.config(command=mytable.xview)
        scrollbary.config(command=mytable.yview)

        scrollbarx.pack(side=BOTTOM,fill=X)
        scrollbary.pack(side=RIGHT,fill=Y)

        headingboxlabel=Label(self.mywindow,text="List Of Holidays")
        headingboxlabel.config(font=('times new roman','24','bold'),bg='yellow',fg='blue')
        headingboxlabel.place(x=170,y=70)

        mytable.heading("date",text="Date of Holiday")
        mytable.heading("hname", text="Holiday Name")

        mytable.column('#0',stretch=NO,minwidth=0,width=0)
        mytable.column('#1', stretch=NO, minwidth=0, width=190)
        mytable.column('#2', stretch=NO, minwidth=0, width=190)


        mytable.pack()
        mytablearea.place(x=130,y=150,height=150)

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as x:
                    x.execute("select * from holiday")
                    resultdata=x.fetchall()

                    for row in resultdata:
                        mytable.insert('',END,value=(row))

                    if resultdata==None:
                        messagebox.showerror("No Records Found","No Data Available",parent=self.mywindow)

            except Exception as y:
                messagebox.showerror("Error Occured","Error in fetching due to"+str(y),parent=self.mywindow)
        except Exception as z:
            messagebox.showerror("Error Ocured","Error in creating database due to"+str(z),parent=self.mywindow)

