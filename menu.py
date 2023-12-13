from tkinter import *
from addEmployee import AddEmployee
from holidaylist import HolidayList
from finalCompanylistlist import CompanyList
from logout import Logout
from payment_list import payment_list
from updateemployee import UpdateEmployee
from Payment import Payment
from change_password import Change_password
from companydetails import CompanyDetails
from AddDepartment import AddDepartment
from AddDesignation import AddDesignation
from Attendance_new import Attendance
from employee_list import EmployeeList
from holiday import ManageHoliday
from createadmin import CreateAdmin
from PIL import Image


class Payrollmenu:
    '''this class is to show the menu for the admin'''

    def __init__(self):
        # self.mywindow = mywindow
        self.mywindow = Tk()
        self.mywindow.wm_title("Payroll Management System")
        self.mywindow.geometry("%dx%d+%d+%d" % (850, 600, 200, 50))
        # self.mywindow.wm_minsize(800,670,100,150)
        bgcolor = Frame(self.mywindow, width=1900, height=2500, bg="thistle")
        bgcolor.place(x=0, y=0)
        bgcolor.pack(side=TOP, expand=NO, fill=NONE)

        menubar = Menu(self.mywindow)
        self.mywindow.option_add("*tearOff", False)
        self.mywindow.config(menu=menubar)

        font_large = ('Arial', 60, 'bold')
        color_payroll = 'purple'  # Example color: blue
        color_management = 'purple3'  # Example color: orange
        color_system = 'purple'  # Example color: teal

        # Payroll Label
        payroll = Label(self.mywindow, text="PAYROLL", font=font_large, fg=color_payroll, bg='thistle')
        payroll.place(x=180, y=100)  # Adjusted position

        # Management Label
        mngmnt = Label(self.mywindow, text="MANAGEMENT", font=font_large, fg=color_management, bg='thistle')
        mngmnt.place(x=80, y=230)  # Adjusted position

        # System Label
        system = Label(self.mywindow, text="SYSTEM", font=font_large, fg=color_system, bg='thistle')
        system.place(x=180, y=360)  # Adjusted position

        employeemenu = Menu(menubar)
        comapnymenu = Menu(menubar)
        reportmenu = Menu(menubar)
        miscmenu = Menu(menubar)
        listmenu = Menu(menubar)
        menubar.add_cascade(menu=employeemenu, label="Employee")
        menubar.add_cascade(menu=comapnymenu, label="Company")
        menubar.add_cascade(menu=reportmenu, label="Reports")
        menubar.add_cascade(menu=listmenu, label="List")
        menubar.add_cascade(menu=miscmenu, label="Misc.")
        # self.present.bind("<ButtonRelease-1>",self.saveattendance)
        employeemenu.add_command(label="Add Employee", command=self.addemployeeframe)
        employeemenu.add_command(label="Update/Delete Employee", command=self.updateframe)
        employeemenu.add_cascade(label="Add new Admin/Employee",command=self.createadmin)
        # employeemenu.add_command(label="Delete Employee",command=self.delempframe)
        listmenu.add_command(label="Employee List", command=self.emplistframe)
        # employeemenu.bind("<KeyPress.Ctrl+E>",self.addemployeeframe)

        comapnymenu.add_command(label="Add Company", command=self.comdetail)
        comapnymenu.add_command(label="Add Department", command=self.departmentframe)
        comapnymenu.add_command(label="Add Designation", command=self.designationframe)
        comapnymenu.add_command(label="Add Holiday", command=self.addholidayframe)

        # reportmenu.add_command(label="Attendence", command=self.attendenceframe)
        # reportmenu.add_command(label="Deduction",command=self.deductionframe)
        reportmenu.add_command(label="Payment", command=self.paymentframe)

        listmenu.add_command(label="Holiday List", command=self.holidalistframe)
        listmenu.add_command(label="Company List", command=self.companylistftrame)
        listmenu.add_command(label="Payment List", command=self.paymentlistframe)

        miscmenu.add_command(label="Change Password", command=self.changepframe)
        miscmenu.add_command(label="Logout", command=self.logoutframe)
        # self.mywindow.withdraw()
        self.mywindow.mainloop()
        # self.mywindow.destroy()

    def addemployeeframe(self):
        AddEmployee(self.mywindow)

    def logoutframe(self):
        Logout(self.mywindow)
        # self.mywindow.destroy()

    def paymentlistframe(self):
        payment_list(self.mywindow)

    def updateframe(self):
        UpdateEmployee(self.mywindow)

    def paymentframe(self):
        Payment(self.mywindow)

    def changepframe(self):
        Change_password(self.mywindow)

    def departmentframe(self):
        AddDepartment(self.mywindow)

    def designationframe(self):
        AddDesignation(self.mywindow)

    def comdetail(self):
        CompanyDetails(self.mywindow)

    def attendenceframe(self):
        Attendance(self.mywindow)

    def emplistframe(self):
        EmployeeList(self.mywindow)

    def addholidayframe(self):
        ManageHoliday(self.mywindow)

    #
    # def delempframe(self):
    #     DeleteEmployee(self.mywindow)

    def holidalistframe(self):
        HolidayList(self.mywindow)

    def companylistftrame(self):
        CompanyList(self.mywindow)

    def createadmin(self):
        CreateAdmin()

# myframe = Tk()
# obj = Payrollmenu()
# myframe.mainloop()
