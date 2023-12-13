from tkinter import *
from tkinter import messagebox, font
import pymysql

import menu
import menuforemployee
from createadmin import CreateAdmin


class Mylogin:
    '''this shows the login page with a stylish design'''
    def __init__(self):
        self.mywindow = Tk()
        self.mywindow.title("Login")
        self.mywindow.geometry("%dx%d+%d+%d" % (500, 500, 400, 100))

        # Styling parameters
        font_large = ('Helvetica', 20, 'bold')
        font_medium = ('Arial', 10, 'bold')
        color_bg = "#f7f7f7"
        color_button_bg = '#ff6f61'
        color_button_fg = '#ffffff'
        color_entry_bg = '#ffffff'
        color_entry_fg = '#333333'

        # Background
        self.mywindow.configure(bg=color_bg)

        # Title
        login = Label(self.mywindow, text="Login", width=20, font=font_large, bg=color_bg)
        login.place(x=90, y=53)

        # Username Entry
        username = Label(self.mywindow, text="Username:", font=font_medium, bg=color_bg)
        username.place(x=68, y=130)
        self.usernamebox = Entry(self.mywindow, bg=color_entry_bg, fg=color_entry_fg)
        self.usernamebox.place(x=240, y=130)

        # Password Entry
        password = Label(self.mywindow, text="Password:", font=font_medium, bg=color_bg)
        password.place(x=68, y=180)
        self.passwordbox = Entry(self.mywindow, show="*", bg=color_entry_bg, fg=color_entry_fg)
        self.passwordbox.place(x=240, y=180)

        # Login Button
        self.savebutton = Button(self.mywindow, text="Login", width=15, command=self.dologin,
                                 bg=color_button_bg, fg=color_button_fg, font=font_medium)
        self.savebutton.place(x=200, y=220)

        # Additional functionality (e.g., sign-up) can be added here

        self.mywindow.mainloop()

    def dologin(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                        myconn.execute("select * from usertable where username=%s and password=%s",(self.usernamebox.get(),self.passwordbox.get()))
                        result=myconn.fetchone()
                        # self.mywindow.destroy()
                        if result is not None:
                            if result[2]=="Admin":
                                self.mywindow.destroy()
                                menu.Payrollmenu()
                                # self.mywindow.destroy()
                            else:
                                self.mywindow.destroy()
                                menuforemployee.Employeemenu()
                                # self.mywindow.destroy()
                        else:
                            messagebox.showerror("Invalid", "Wrong username/password",parent=self.mywindow)
            except Exception as ex:
                messagebox.showerror("Error in Query", "Error in Query due to " + str(ex),parent=self.mywindow)
        except Exception as ex:
          messagebox.showerror("Connection Error", "Error in Connection due to " + str(ex),parent=self.mywindow)
        # self.mywindow.destroy()
        self.mywindow.mainloop()


    def signupframe(self):
        CreateAdmin()
        # self.mywindow.withdraw()
# obj=Mylogin()
# # mywindow=Tk()

# mywindow.wm_minsize(600,600)
# mywindow.wm_title("Create Account")
#
# mywindow.geometry('500x500')
# mainloop()
