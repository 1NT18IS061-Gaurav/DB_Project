from tkinter import messagebox
from tkinter import *
import pymysql
import createadmin
import login


class Mainfile:
    '''this class helps the user to choose whether user want to login or to create a new account
    ,if the account is found then,automatically the login page is shown else the signup page is shown on screen so that the user can create an account'''

    def __init__(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="addemployeedb")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from usertable")
                    result=myconn.fetchone()
                    # print(result)
                    if result!=None:
                        login.Mylogin()
                    else:
                        createadmin.CreateAdmin()
            except Exception as ex:
                messagebox.showerror("Error Occured", 'Error in inserting query due to' + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error connecting due to" + str(ex))

def main():
    obj=Mainfile()

if __name__=='__main__':
    main()

