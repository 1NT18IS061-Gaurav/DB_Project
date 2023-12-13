from tkinter import *
from holidaylist import HolidayList
from logout import Logout
from change_password import Change_password
from Attendance_new import Attendance
from employee_list import EmployeeList
from finalCompanylistlist import  CompanyList

class Employeemenu:
    '''this class works as menu for employee.
    employees can choose options from the respective menus.'''
    def __init__(self):
        # self.mywindow = mywindow
        self.mywindow=Tk()
        self.mywindow.wm_title("Payroll Management System")
        self.mywindow.geometry("%dx%d+%d+%d" % (850, 600, 200, 50))
        # self.mywindow.wm_minsize(800,670,100,150)
        bgcolor = Frame(self.mywindow, width=1900, height=2500, bg="wheat")
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        welcome = Label(self.mywindow, text="Welcome to ", font=('arial', 16, "bold", 'italic'), fg='purple',
                        bg="wheat")
        welcome.place(x=150, y=70)

        payroll = Label(self.mywindow, text="PAYROLL ", font=('times new roman', 78, "bold", 'underline'), fg='red',
                        bg="wheat")
        payroll.place(x=120, y=110)

        mngmnt = Label(self.mywindow, text="MANAGEMENT ", bg="wheat", font=('times new roman', 78, "bold", 'underline'),
                       fg='red')
        mngmnt.place(x=50, y=240)

        system = Label(self.mywindow, text="SYSTEM ", bg="wheat", font=('times new roman', 78, "bold", 'underline'),
                       fg='red')
        system.place(x=120, y=390)

        menubar = Menu(self.mywindow,bg="yellow")
        self.mywindow.option_add("*tearOff", False)
        self.mywindow.config(menu=menubar)

        listmenu = Menu(menubar)
        # comapnymenu = Menu(menubar)
        reportmenu = Menu(menubar)
        miscmenu = Menu(menubar)

        menubar.add_cascade(menu=listmenu, label="Lists")
        menubar.add_cascade(menu=reportmenu, label="Reports")
        menubar.add_cascade(menu=miscmenu, label="Misc")

        listmenu.add_command(label="Employee List",command=self.emplistframe)
        listmenu.add_command(label="Company List", command=self.companylistframe)

        # reportmenu.add_command(label="Attendence",command=self.attendenceframe)
        reportmenu.add_command(label="Holidays",command=self.holidalistframe)


        miscmenu.add_command(label="Change Password",command=self.changepframe)
        miscmenu.add_command(label="Logout",command=self.logoutframe)


    def logoutframe(self):
        Logout(self.mywindow)

    def changepframe(self):
        Change_password(self.mywindow)

    def attendenceframe(self):
        Attendance(self.mywindow)

    def emplistframe(self):
        EmployeeList(self.mywindow)

    def holidalistframe(self):
        HolidayList(self.mywindow)

    def companylistframe(self):
        CompanyList(self.mywindow)






# myframe = Tk()
# obj = Payrollmenu(myframe)
# myframe.mainloop()
