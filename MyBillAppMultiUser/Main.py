from tkinter import *
from screenst import screenst1
from screenad import screenad1
import time
import sqlite3
from tkinter import messagebox,filedialog
from signupcode import signupcode1
import ParagBillUpdate
import pm
import ParagBillUpdateMain
import product
import removeuser
import screenad
import screenst
import signupcode
import updateuser
import os

class Admin():

    def timer(self):
        d = time.strftime("%H:%M:%S")
        self.l2.config(text=d)
        self.l2.after(200, self.timer)

    def adminlogin(self, event=""):
        query=""" select count(*) from Users"""
        self.n_user=self.conn.execute(query).fetchone()
        query1 = """ select superuser from Users"""
        self.su_user = self.conn.execute(query1).fetchall()
        self.suser = 0
        for self.i in self.su_user:
            if self.i[0] > 0:
                self.suser = 1
                break
        if (self.n_user[0] == 0 or self.suser == 0):
            root.withdraw()
            obj_of_signup = signupcode1(root,self.main_root)
        else:
            root.withdraw()
            obj_of_screenad = screenad1(root,self.main_root)

    def stafflogin(self, event=""):
        query=""" select count(*) from Users"""
        self.n_user=self.conn.execute(query).fetchone()

        if(self.n_user[0]==0):
            root.withdraw()
            obj_of_signup = signupcode1(root,self.main_root)
        else:
            root.withdraw()
            obj_of_screenst = screenst1(root,self.main_root)

    def __init__(self, root,main_root):
        try:
            os.mkdir("C:\\MyShopBills")
        except:
            pass
        self.main_root = main_root
        self.root = root
        bgclr1 = "#0080c0"
        bgclr2 = "#e7d95a"
        try:
            self.conn = sqlite3.connect('userinfo.db')
        except:
            m = messagebox.showerror("Billing Software", "Couldn't Connect With Database !", parent=self)

        self.root.title("P & H Billing Software")
        self.root.config(background=bgclr1)
        self.root.geometry("1350x700+0+0")


    ##================================================timer====================================================================

        Date = StringVar()
        Time = StringVar()
        Date.set(time.strftime("%d-%m-%y"))
        f = Frame(self.root, bd=1, background=bgclr1, relief=SOLID)
        f.place(x=0, y=0, relwidth=1, height=50)
        l1 = Label(f, textvariable=Date, bg=bgclr2,font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2,relief=SUNKEN)
        l1.place(x=20, y=12, height=25)
        self.l2 = Label(f, bg=bgclr2, font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2, relief=SUNKEN)
        self.l2.place(x=1220, y=12, height=25)
        l3 = Label(f, text="P & H Billing Software", font=("Arial", 18, "bold"), fg='black',
                    borderwidth=2, bd=1, bg=bgclr2,relief=SUNKEN)
        l3.place(x=520, y=5, height=35)

        self.timer()
##============================================admin frame==================================================================

        adminframe= Frame(self.root,background=bgclr1, relief=SOLID)
        adminframe.place(x=50,y=50,height=650,width=1350)
        userframe= Frame(adminframe,bg=bgclr2,relief=SOLID)
        userframe.place(x=216,y=175,height=300,width=300)
        userbutton= Button(userframe,text="STAFF",command=self.stafflogin,bg=bgclr1,font=("Arial Bold",20))
        userbutton.place(x=75,y=75, height=150, width=150)

        adminframe1=Frame(adminframe,bg=bgclr2,relief=SOLID)
        adminframe1.place(x=732,y=175, height=300, width=300)
        adminbutton= Button(adminframe1,text="ADMIN", command=self.adminlogin, bg=bgclr1,font=("Arial Bold",20))
        adminbutton.place(x=75, y=75, height=150, width=150)

        self.root.bind("<Control-s>", self.stafflogin)
        self.root.bind("<Control-a>", self.adminlogin)

root = Tk()
Admin(root,root)
root.mainloop()