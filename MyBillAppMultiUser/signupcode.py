from tkinter import *
import sqlite3
import time
from tkinter import messagebox
from removeuser import removeuser1
from updateuser import uadateuser1
from validate_email import validate_email

class signupcode1(Toplevel):
    def timer(self):
        d = time.strftime("%H:%M:%S")
        self.l2.config(text=d)
        self.l2.after(200, self.timer)

    def r_user(self,event=""):
        self.withdraw()
        obj_of_removeuser=removeuser1(self,self.main_root)

    def u_user(self,event=""):
        self.withdraw()
        obj_of_updateuser=uadateuser1(self,self.main_root)

    def addvalue(self,event=""):
        try:
            if self.usernameentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Username not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Username.",parent=self)
            self.usernameentry.focus_set()
            return
        try:
            query2 = """ select username from Users"""
            self.name1 = self.conn.execute(query2).fetchall()
            self.conn.commit()
            self.k = list()
            for self.i in self.name1:
                self.k.append(self.i[0])
            if (self.usernameentry.get() in self.k):
                raise ValueError
        except:
            m = messagebox.showerror("Billing Software", "Username already exist", parent=self)
            m = messagebox.showinfo("Billing Sofware", "Please Enter New Username.", parent=self)
            self.usernameentry.focus_set()
            return

        try:
            if self.passwordentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Password not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Password.",parent=self)
            self.passwordentry.focus_set()
            return
        try:
            if self.repasswordentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Re-Password not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Re-Password.",parent=self)
            self.passwordentry.focus_set()
            return
        try:
            if (self.passwordentry.get() != self.repasswordentry.get()) :
                raise ValueError
        except:
            m = messagebox.showerror("Billing Software", "Password and Re-Password doesn't Matched !",parent=self)
            self.p_word.set("")
            self.rp_word.set("")
            self.passwordentry.focus_set()
            return
        try:
            if self.nameentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Name not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Name.",parent=self)
            self.nameentry.focus_set()
            return

        try:
            if self.phonenumberentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Phone Number not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Phone Number.",parent=self)
            self.phonenumberentry.focus_set()
            return
        try:
            self.ph = list(self.phonenumberentry.get())
            if (len(self.ph) != 10):
                raise AttributeError

        except:
            m = messagebox.showerror("Billing Software", "Phone Number must be of 10 Digits.", parent=self)
            self.phonenumberentry.focus_set()
            return

        try:
            self.no = int(self.phonenumberentry.get())
            if (int(self.no >= 0)):
                pass
            else:
                raise ValueError

        except:
            m = messagebox.showerror("Billing Software", "Phone Number must be Numeric !", parent=self)
            self.phonenumberentry.focus_set()
            return

        try:
            self.uno = ('9', '8', '7', '6')
            if (self.ph[0] not in self.uno):
                raise ValueError
        except:
            m = messagebox.showerror("billing Software", "Phone Number is not Valid !", parent=self)
            self.phonenumberentry.focus_set()
            return

        try:
            if self.emailentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "E-mail not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter E-mail.",parent=self)
            self.emailentry.focus_set()
            return

        valid= validate_email(self.emailentry.get())
        if not valid:
            m = messagebox.showerror("Billing Software","Please Enter E-mail in valid Format",parent=self)
            self.emailentry.focus_set()
            return

        query="""insert or ignore into Users(username, password,name, phoneno,superuser, email) VALUES(?,?,?,?,?,?)"""
        self.conn.execute(query,(self.usernameentry.get(),self.passwordentry.get(),self.nameentry.get(),self.phonenumberentry.get(),self.s_user.get(),self.emailentry.get()))
        self.conn.commit()
        if self.counter == 0:
            messagebox.showinfo("Billing Software", "User Details Entered Successfully! \n'{0}' is Assigned as an Admin.\nBecause '{0}' is the First User of This Application.".format(self.usernameentry.get()),parent=self)
            self.counter += self.counter
            self.destroy()
            self.root.deiconify()
        else:
            if self.s_user.get() == 0:
                messagebox.showinfo("Billing Software", "User Details Entered Successfully! \n'{0}' is Assigned as a Staff User.".format(self.usernameentry.get()), parent=self)
                self.clearset()
            else:
                messagebox.showinfo("Billing Software", "User Details Entered Successfully \n'{0}' is Assigned as an Admin.".format(self.usernameentry.get()), parent=self)
                self.clearset()
            self.usernameentry.focus_set()

    def clearset(self,event=""):
        self.u_name.set('')
        self.p_word.set('')
        self.rp_word.set('')
        self.name.set('')
        self.p_number.set('')
        self.email.set('')
        if (self.n_user[0] == 0):
            self.s_user.set(1)
            self.susercb.config(state="disabled")
            self.counter = 0
        else:
            self.counter = 1
            self.susercb.config(state="normal")
            self.s_user.set(0)
        self.usernameentry.focus_set()

    def backf(self,event=""):
        self.destroy()
        self.root.deiconify()
    def c_w(self,event=""):
        i = messagebox.askyesno("Billing Software", "Are you Want to Close Application?", parent=self.root)
        if i > 0:
            self.main_root.destroy()
        else:
            return

    def __init__(self, root,main_root):
        self.main_root= main_root
        self.root = root
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        try:
            self.conn = sqlite3.connect('userinfo.db')
        except:
            m = messagebox.showerror("Billing Software" , "Couldn't Connect with Database !" , parent=self)
        bgclr1 = "#0080c0"
        bgclr2 = "#e7d95a"
        self.title("Sign Up")
        self.config(background=bgclr1)
        self.geometry("1350x700+0+0")
##======================================variable========================================================================
        self.u_name = StringVar()
        self.p_word = StringVar()
        self.rp_word=StringVar()
        self.name = StringVar()
        self.p_number = IntVar()
        self.p_number.set('')
        self.s_user = IntVar()
        self.email = StringVar()
##============================================timer====================================================================
        Date = StringVar()
        Time = StringVar()
        Date.set(time.strftime("%d-%m-%y"))
        f = Frame(self, bd=1, background=bgclr1, relief=SOLID)
        f.place(x=0, y=0, relwidth=1, height=50)
        l1 = Label(f, textvariable=Date, bg=bgclr2, font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2,
                   relief=SUNKEN)
        l1.place(x=20, y=12, height=25)
        self.l2 = Label(f, bg=bgclr2, font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2, relief=SUNKEN)
        self.l2.place(x=1220, y=12, height=25)
        l3 = Label(f, text="P & H Billing Software", bg=bgclr2, font=("Arial", 18, "bold"), fg='black',
                   borderwidth=2, bd=1, relief=SUNKEN)
        l3.place(x=520, y=5, height=35)
        self.timer()
##===========================================signup frame=============================================================
        signupframe=Frame(self,background=bgclr1,relief=SOLID)
        signupframe.place(x=0, y=50, height=700, width=1350)
        llframe = LabelFrame(signupframe, background=bgclr1, text="User Info.", font=("Arial Bold", 20),relief=SOLID)
        llframe.place(x=400, y=0, height=650, width=500)
        backbutton = Button(signupframe, text="BACK", width=10, bg=bgclr2, command=self.backf, bd=5,font=("Arial Bold", 8))
        backbutton.place(x=10, y=10, height=25, width=75)
        uubutton = Button(signupframe, text="UPDATE USER", bg=bgclr2,width=15,command=self.u_user,bd=5,font=("Arial Bold",10))
        uubutton.place(x=1200, y=50, height=35)
        rubutton = Button(signupframe, text="USER INFO",bg=bgclr2, width=15, command=self.r_user, bd=5,font=("Arial Bold",10))
        rubutton.place(x=1200, y=125, height=35)
##==============================================signup frame================================================
        usernamelabel = Label(llframe , text="Username",bd=5, font=("Arial Bold", 20), bg=bgclr1,fg=bgclr2)
        usernamelabel.place(x=50, y=75, height=25)
        self.usernameentry= Entry(llframe,textvariable=self.u_name,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.usernameentry.place(x=300, y=75, height=25,width=150)

        passwordlabel = Label(llframe, text="Password",bd=5, font=("Arial Bold", 20), bg=bgclr1,fg=bgclr2)
        passwordlabel.place(x=50, y=125, height=25)
        self.passwordentry= Entry(llframe,textvariable=self.p_word,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"),show="*")
        self.passwordentry.place(x=300, y=125, height=25, width=150)

        repasswordlabel = Label(llframe, text=" Re-Password", bd=5, font=("Arial Bold", 20), bg=bgclr1, fg=bgclr2)
        repasswordlabel.place(x=43, y=175, height=25)
        self.repasswordentry = Entry(llframe, textvariable=self.rp_word, borderwidth=2, relief=SUNKEN,
                                   font=("Arial", 10, "bold"),show="*")
        self.repasswordentry.place(x=300, y=175, height=25, width=150)

        namelabel = Label(llframe, text="Name", bd=5,font=("Arial Bold", 20), bg=bgclr1,fg=bgclr2)
        namelabel.place(x=50, y=225, height=25)
        self.nameentry = Entry(llframe,textvariable=self.name,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.nameentry.place(x=300, y=225,height=25,width=150)

        phonenumberlabel = Label(llframe,bd=5, text="Phone Number", font=("Arial Bold", 20), bg=bgclr1,fg=bgclr2)
        phonenumberlabel.place(x=50, y=275, height=25)
        self.phonenumberentry = Entry(llframe,textvariable=self.p_number,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.phonenumberentry.place(x=300, y=275, height=25,width=150)

        emaillabel = Label(llframe, text="E-mail",bd=5, font=("Arial Bold", 20), bg=bgclr1,fg=bgclr2)
        emaillabel.place(x=50, y=325, height=25)
        self.emailentry = Entry(llframe,textvariable=self.email,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.emailentry.place(x=300, y=325, height=25, width=150)

        self.susercb = Checkbutton(llframe,text="Apoint As An Admin", variable=self.s_user,bd=5,font=("Arial Bold",12), bg=bgclr1,fg='black')
        self.susercb.place(x=50,y=375)

        submitbutton= Button(llframe , text="SUBMIT" , bg=bgclr2 , width=12 , command=self.addvalue,bd=5 , font=("Arial Bold" , 15))
        submitbutton.place(x=45 , y=500 , height=30)
        clearbutton= Button(llframe , text="CLEAR", bg=bgclr2 , width=12 , command=self.clearset , bd=5 , font=("Arial Bold" , 15))
        clearbutton.place(x=270 , y=500 , height=30)

        query = """ select count(*) from Users"""
        self.n_user = self.conn.execute(query).fetchone()
        query1 = """ select superuser from Users"""
        self.su_user = self.conn.execute(query1).fetchall()
        self.suser = 0
        for self.i in self.su_user:
            if self.i[0] > 0:
                self.suser = 1
                break
        if (self.n_user[0] == 0 or self.suser==0):
            self.s_user.set(1)
            self.susercb.config(state="disabled")
            self.counter = 0
        else:
            self.counter = 1
            self.susercb.config(state="normal")
            self.s_user.set(0)

        self.bind("<Control-q>", self.backf)
        self.bind("<Return>", self.addvalue)
        self.bind("<Control-i>", self.r_user)
        self.bind("<Delete>", self.clearset)
        self.bind("<Control-u>", self.u_user)
        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.usernameentry.focus_set()
