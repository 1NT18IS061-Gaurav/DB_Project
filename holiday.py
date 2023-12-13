import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql
from tkcalendar import DateEntry


class ManageHoliday:
    '''this class is used to add the holidays'''

    def __init__(self, myframe):
        self.mywindow = Toplevel(myframe)
        self.mywindow.wm_title("Manage Holiday")

        self.mywindow.geometry("%dx%d+%d+%d" % (550, 400, 400, 200))

        bgcolor = Frame(self.mywindow, bg="peachpuff", width=1900, height=2500 )
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        datebox = Label(self.mywindow,font='bold', text="Date of holiday",bg="peachpuff")
        datebox.place(x=100, y=210)

        self.dateentry = DateEntry(self.mywindow, font="Arial 10", bg="peachpuff")
        self.dateentry.place(x=260, y=210)

        hnamebox = Label(self.mywindow, text="Name of holiday",font='bold',bg="peachpuff")
        hnamebox.place(x=100, y=260)

        self.holidayentry = Entry(self.mywindow)
        self.holidayentry.place(x=260, y=260)

        savebtn = Button(self.mywindow, text="Save", command=self.saveinfo,bg='pink',font='bold',fg='red',padx=20)
        savebtn.place(x=310, y=330)

        searchbtn = Button(self.mywindow, text="Search", command=self.searchbox, bg='pink', font='bold', fg='red', padx=20)
        searchbtn.place(x=400, y=70)

        delbtn = Button(self.mywindow, text="Delete", command=self.delinfo, bg='pink', font='bold', fg='red', padx=20)
        delbtn.place(x=400, y=330)

        mytablearea = Frame(self.mywindow)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("date", "hname"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=LEFT, fill=Y)

        self.mytable.heading("date", text="Date")
        self.mytable.heading("hname", text="Holiday Name")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=100)
        # self.mytable.column('#2', stretch=NO, minwidth=0, width=100)
        # self.mytable.column('#3', stretch=NO, minwidth=0, width=100)
        # self.mytable.column('#4', stretch=NO, minwidth=0, width=150)
        # self.mytable.column('#5', stretch=NO, minwidth=0, width=150)
        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(x=70, y=70, height=100)

    def searchbox(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from holiday"
                                   " where hname like %s", (self.holidayentry.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Students added yet.", parent=self.mywindow)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex), parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex), parent=self.mywindow)

    def fetchbysrno(self, e):
        # '''this function fetch  all the information of an employee as per the first name of the employee'''
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        self.serialno = selectedRow[1]

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from holiday where hname=%s",
                                       (self.serialno))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:
                        print(row)
                        self.dateentry.delete(0, END)
                        self.dateentry.insert(0, row[0])

                        self.holidayentry.delete(0, END)
                        self.holidayentry.insert(0, row[1])

                        if myresultdata == None:
                            messagebox.showerror("No Records Found", "No Students added yet.", parent=self.mywindow)

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex), parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex), parent=self.mywindow)

    def delinfo(self):
        '''this function allow the admin to delete all the information regarding a selected employee'''
        answer = askquestion("Are you sure", "Do you really want to delete record?", icon="warning",
                             parent=self.mywindow)
        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute("delete from holiday where hname=%s",
                                       self.holidayentry.get())
                        self.holidayentry.delete(0, END)
                        self.dateentry.delete(0, END)
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Holiday deleted Succesfully", parent=self.mywindow)

                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex), parent=self.mywindow)
                finally:
                    mydatabaseobj.close()
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex), parent=self.mywindow)

    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into holiday(date,hname)""values(%s,%s)",(self.dateentry.get_date(),self.holidayentry.get()))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Holiday Added Successfully",parent=self.mywindow)
                    self.dateentry.delete(0,END)
                    self.holidayentry.delete(0,END)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),parent=self.mywindow)
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex),parent=self.mywindow)


# mywindow= Tk()
# obj=ManageHoliday(mywindow)
# mywindow.mainloop()