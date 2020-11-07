from tkinter import *
import time
from tkinter import messagebox
import sqlite3
from ParagBillUpdateMain import Bill

class screenst1(Toplevel):

    def timer(self):
        d = time.strftime("%H:%M:%S")
        self.l2.config(text=d)
        self.l2.after(200, self.timer)

    def logstaff(self,event=""):
        try:
            if self.usernameentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Username not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Username.",parent=self)
            self.uname.set("")
            self.usernameentry.focus_set()
            return

        try:
            if self.passwordentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Password not Found !", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Password.", parent=self)
            self.pword.set("")
            self.passwordentry.focus_set()
            return

        query=""" select password from Users where username=?"""
        self.p_word=self.conn.execute(query,(self.usernameentry.get(),)).fetchone()

        try:
            query2 = """ select username from Users"""
            self.name1 = self.conn.execute(query2).fetchall()
            self.conn.commit()
            self.k = list()
            for self.i in self.name1:
                self.k.append(self.i[0])
            if (self.usernameentry.get() not in self.k):
                raise ValueError
        except:
            m = messagebox.showerror("Billing Sofware", "Please Enter Valid Username.", parent=self)
            self.uname.set("")
            self.usernameentry.focus_set()
            return

        if( self.p_word[0] == self.passwordentry.get()):
            query2 = "select count(*) from CurrentUser"
            self.cu = self.conn.execute(query2).fetchone()
            if self.cu[0] == 0:
                query3 = """ insert or ignore into CurrentUser (username) values (?)"""
                self.conn.execute(query3, (self.usernameentry.get(),))
                self.conn.commit()
            else:
                query4 = "update CurrentUser set username=?"
                self.conn.execute(query4, (self.usernameentry.get(),))
                self.conn.commit()
            self.uname.set("")
            self.pword.set("")
            obj_of_bill = Bill(self,self.main_root)
            self.usernameentry.focus_set()
        else:
            m= messagebox.showerror("Billing Software","Please Enter valid Password !",parent=self)
            self.pword.set("")
            self.passwordentry.focus_set()
            return

    def backf(self,event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self,event=""):
        i = messagebox.askyesno("Billing Software", "Are you Want to Close Application?", parent=self.root)
        if i > 0:
            self.main_root.destroy()
        else:
            return

    def c_p(self,event=""):

        self.cpframe.place(x=400, y=100, height=550, width=500)
        self.cusernamelabel.place(x=10, y=75, height=25 )
        self.cpasswordlabel.place(x=10, y=150, height=25)
        self.cusernameentry.place(x=305, y=75, height=25, width=170)
        self.cpasswordentry.place(x=305, y=150, height=25, width=170)
        self.nplabel.place(x=5, y=225, height=25)
        self.rnplabel.place(x=10, y=300, height=25)
        self.npentry.place(x=305, y=225, height=25, width=170)
        self.rnpentry.place(x=305, y=300, height=25, width=170)
        self.loginbutton.place(x=75, y=400)
        self.cpbutton.place(x=300, y=400)
        self.cusernameentry.focus_set()

    def des(self,event=""):
        self.cpframe.destroy()
        self.cusernamelabel.destroy()
        self.cusernameentry.destroy()
        self.cpasswordentry.destroy()
        self.cpasswordentry.destroy()
        self.nplabel.destroy()
        self.npentry.destroy()
        self.rnplabel.destroy()
        self.rnpentry.destroy()

    def change(self,event=""):
        try:
            if self.cusernameentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Username not Found !", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Username.", parent=self)
            self.cusernameentry.focus_set()
            return

        try:
            query2 = """ select username from Users"""
            self.name1 = self.conn.execute(query2).fetchall()
            self.conn.commit()
            self.k = list()
            for self.i in self.name1:
                self.k.append(self.i[0])
            if (self.cusernameentry.get() not in self.k):
                raise ValueError
        except:
            m = messagebox.showerror("Billing Software", "Username doesn't exist !", parent=self)
            m = messagebox.showinfo("Billing Sofware", "Please Enter Valid Username.", parent=self)
            self.cusernameentry.focus_set()
            return

        try:
            if self.cpasswordentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Current Password not found !", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Current Password.", parent=self)
            self.cpasswordentry.focus_set()
            return

        query3 = """ select password from Users where username=?"""
        self.p_word = self.conn.execute(query3, (self.cusernameentry.get(),)).fetchone()

        try:
            if (self.p_word[0] != self.cpasswordentry.get()):
                raise ValueError
        except:
            m = messagebox.showerror("Billing Software", "Please Enter valid Current Password !", parent=self)
            self.cpasswordentry.focus_set()
            return

        try:
            if self.npentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "New Password not Found !", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter New Password.", parent=self)
            self.npentry.focus_set()
            return

        try:
            if self.rnpentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Re-Password not Found !", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Re-Password.", parent=self)
            self.rnpentry.focus_set()
            return

        try:
            if (self.npentry.get() != self.rnpentry.get()) :
                raise ValueError
        except:
            m = messagebox.showerror("Billing Software", " New Password and Re-Password doesn't Matched",parent=self)
            self.np_word.set("")
            self.rnp_word.set("")
            return
        query4 = """UPDATE Users SET password=?WHERE username=?"""
        self.conn.execute(query4, (self.npentry.get(),self.cusernameentry.get()))
        self.conn.commit()
        messagebox.showinfo("Billing Software", "Password for '{0}' is changed Successfully.".format(self.cusernameentry.get()), parent=self)
        self.clr()
        self.des()

    def clr(self,event=""):

        self.u_name.set('')
        self.cp_word.set('')
        self.np_word.set('')
        self.rnp_word.set('')

    def __init__(self, root,main_root):
        self.main_root = main_root
        self.root = root
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        try:
            self.conn = sqlite3.connect('userinfo.db')
        except:
            m = messagebox.showerror("Billing Software", "Couldn't Connect with Database !",parent=self)

        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.title("Login")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.uname = StringVar()
        self.pword = StringVar()
#======================================================================================
        self.u_name = StringVar()
        self.cp_word = StringVar()
        self.np_word = StringVar()
        self.rnp_word = StringVar()
        self.u_name.set('')

##===================================================timer================================================================

        Date = StringVar()
        Time = StringVar()
        Date.set(time.strftime("%d-%m-%y"))
        f = Frame(self, bd=1, background=self.bgclr1, relief=SOLID)
        f.place(x=0, y=0, relwidth=1, height=50)
        l1 = Label(f, textvariable=Date, bg=self.bgclr2, font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2,
                   relief=SUNKEN)
        l1.place(x=20, y=12, height=25)
        self.l2 = Label(f, bg=self.bgclr2, font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2, relief=SUNKEN)
        self.l2.place(x=1220, y=12, height=25)
        l3 = Label(f, text="P & H Billing Software", bg=self.bgclr2, font=("Arial", 18, "bold"), fg='black',
                   borderwidth=2, bd=1, relief=SUNKEN)
        l3.place(x=520, y=5, height=35)

        self.timer()



##=================================================login screen=============================================================

        loginframe= Frame(self,background=self.bgclr1, relief=SOLID)
        loginframe.place(x=0,y=50,height=650,width=1350)

        llframe=LabelFrame(loginframe,background=self.bgclr1, text="Staff Login Info.",font=("Arial Bold",20),relief=SOLID)
        llframe.place(x=400,y=100,height=500,width=500)
        backbutton = Button(loginframe, text="BACK", width=10, bg=self.bgclr2, command=self.backf,bd=5,font=("Arial Bold",8))
        backbutton.place(x=10, y=10, height=25, width=75)

        usernamelabel = Label(llframe, text="Username",font=("Arial Bold", 20),bg=self.bgclr1,bd=5,fg=self.bgclr2)
        usernamelabel.place(x=50,y=150,height=25,width=170)
        passwordlabel = Label (llframe, text="Password", font=("Arial Bold",20),bg=self.bgclr1,bd=5,fg=self.bgclr2)
        passwordlabel.place(x=50,y=250,height=25,width=170)


        self.usernameentry= Entry(llframe, textvariable=self.uname,borderwidth=2,relief=SUNKEN, font=("Arial", 13, "bold"))
        self.usernameentry.place(x=250,y=150,height=25,width=170)
        self.passwordentry= Entry(llframe,show="*", textvariable=self.pword,borderwidth=2,relief=SUNKEN, font=("Arial", 13, "bold"))
        self.passwordentry.place(x=250,y=250,height=25, width=170)

        # self.uname = self.usernameentry.get()
        # self.pword = self.passwordentry.get()

        loginbutton= Button(llframe,text="LOGIN",bg=self.bgclr2,command=self.logstaff,bd=5,width=15,font=("Arial Bold",10))
        loginbutton.place(x=45,y=350)
        cpbutton = Button(llframe, text="CHANGE PASSWORD", bg=self.bgclr2, command=self.c_p, bd=5, width=20,font=("Arial Bold", 10))
        cpbutton.place(x=245, y=350)
        self.usernameentry.focus_set()

        self.cpframe = LabelFrame(self, background=self.bgclr1, text="Change Password", font=("Arial Bold", 20),
                                  relief=SOLID)
        self.cusernamelabel = Label(self.cpframe, text="Username", font=("Arial Bold", 20), bg=self.bgclr1, bd=5,
                                    fg=self.bgclr2)
        self.cpasswordlabel = Label(self.cpframe, text="Current Password", font=("Arial Bold", 20), bg=self.bgclr1,
                                    bd=5, fg=self.bgclr2)
        self.cusernameentry = Entry(self.cpframe, textvariable=self.u_name, borderwidth=2, relief=SUNKEN,
                                    font=("Arial", 13, "bold"))
        self.cpasswordentry = Entry(self.cpframe, show="*", textvariable=self.cp_word, borderwidth=2, relief=SUNKEN,
                                    font=("Arial", 13, "bold"))
        self.nplabel = Label(self.cpframe, text=" New Password", font=("Arial Bold", 20), bg=self.bgclr1, bd=5,
                             fg=self.bgclr2)
        self.rnplabel = Label(self.cpframe, text="Re-Password", font=("Arial Bold", 20), bg=self.bgclr1, bd=5,
                              fg=self.bgclr2)
        self.npentry = Entry(self.cpframe, show="*", textvariable=self.np_word, borderwidth=2, relief=SUNKEN,
                             font=("Arial", 13, "bold"))
        self.rnpentry = Entry(self.cpframe, show="*", textvariable=self.rnp_word, borderwidth=2, relief=SUNKEN,
                              font=("Arial", 13, "bold"))
        self.loginbutton = Button(self.cpframe, text="CHANGE", bg=self.bgclr2, command=self.change, bd=5, width=15,
                                  font=("Arial Bold", 10))
        self.cpbutton = Button(self.cpframe, text="CLEAR", bg=self.bgclr2, command=self.clr, bd=5, width=15,
                               font=("Arial Bold", 10))


        self.bind("<Control-q>", self.backf)
        self.bind("<Return>", self.logstaff)
        self.bind("<Control-u>", self.c_p)
        self.bind("<Control-p>", self.change)
        self.bind("<Delete>", self.des)
        self.protocol("WM_DELETE_WINDOW",self.c_w)

        self.mainloop()