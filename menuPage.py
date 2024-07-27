from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from datetime import datetime
py=sys.executable

class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(width=160, height=300)
        self.canvas.pack()
        self.maxsize(500,200)
        self.minsize(500,200)
        self.title('SALARY MANAGEMENT SYSTEM - APEX THERMOCON')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)
        year = datetime.now().year
        month = datetime.now().month
        yes = "Y"

        if month == 2:
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                            database='salary',
                                            user='root', password='123456')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("select * from reset_holidays where year=%s",[year])
                self.rows = self.myCursor.fetchall()
                if self.rows == []:
                        self.myCursor.execute("insert into reset_holidays values(%s,%s)",[year,yes])
                        self.conn.commit()
                        self.myCursor.execute("UPDATE remaining_holidays SET holidays=12")
                        self.conn.commit()
                self.myCursor.close()
                self.conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error","Something went wrong")

        def a_e():
            os.system('%s %s' % (py, 'addEmployee.py'))
        
        def c_a():
            os.system('%s %s' % (py,'attend_save.py'))

        self.addEmp = Button(self, text="ADD EMPLOYEE", width=30, font=('Garamond', 15), command=a_e).place(x=70, y=50)
       
        self.searchSal = Button(self, text="ENTER ATTENDANCE", width=30, font=('Garamond', 15), command=c_a).place(x=70, y=100)


MainWin().mainloop()
