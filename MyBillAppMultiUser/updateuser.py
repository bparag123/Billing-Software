from tkinter import *
import sqlite3
import time
from tkinter import messagebox,ttk
from validate_email import validate_email

class uadateuser1(Toplevel):

    def timer(self):
        d = time.strftime("%H:%M:%S")
        self.l2.config(text=d)
        self.l2.after(200, self.timer)

    def u_update(self,event=""):

        try:
            if self.passwordentry.get() == "":
                raise AttributeError
        except:
            messagebox.showerror("Billing Software", "Password not Found !", parent=self)
            messagebox.showinfo("Billing Software", "Please Enter Password.", parent=self)
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
            return

        try:
            if self.nameentry.get() == "":
                raise AttributeError
        except:
            messagebox.showerror("Billing Software", "Name not Found !",parent=self)
            messagebox.showinfo("Billing Software", "Please Enter Name.",parent=self)
            self.nameentry.focus_set()
            return

        try:
            if self.phonenumberentry.get() == "":
                raise AttributeError
        except:
            messagebox.showerror("Billing Software", "Phone Number not Found !",parent=self)
            messagebox.showinfo("Billing Software", "Please Enter Phone Number.",parent=self)
            self.phonenumberentry.focus_set()
            return

        self.ph = list(self.phonenumberentry.get())
        try:
            if (len(self.ph) != 10):
                raise AttributeError
        except:
            messagebox.showerror("Billing Software", "Phone Number must be 10 Digits !", parent=self)
            return

        try:
            self.no = int(self.phonenumberentry.get())
            if (int(self.no >= 0)):
                pass
            else:
                raise ValueError

        except:
            m = messagebox.showerror("Billing Software", "Phone Number must be in Numeric !", parent=self)
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
            messagebox.showerror("Billing Software", "E-mail not Found !",parent=self)
            messagebox.showinfo("Billing Software", "Please Enter E-mail.",parent=self)
            self.emailentry.focus_set()
            return

        valid = validate_email(self.emailentry.get())
        if not valid:
            m = messagebox.showerror("Billing Software", "Please Enter E-mail in valid Format", parent=self)
            self.emailentry.focus_set()
            return

        query="""UPDATE Users SET password=?,name=?, phoneno=?,superuser=?, email=? WHERE username=?"""
        self.conn.execute(query,(self.passwordentry.get(),self.nameentry.get(),self.phonenumberentry.get(),self.s_user.get(),self.emailentry.get(),self.uentry.get()))
        self.conn.commit()
        if self.s_user.get() == 1:
            messagebox.showinfo("Billing Software", "User Details Updated Successfully.\n'{}' is assigned as an Admin.".format(self.nameentry.get()),parent=self)
        else:
            messagebox.showinfo("Billing Software", "User Details Updated Successfully.\n'{}' is assigned as a Staff User.".format(self.nameentry.get()),parent=self)
        self.clearset()
        self.usernamelist.focus_set()

    def clearset(self,event=""):

        self.p_word.set('')
        self.rp_word.set('')
        self.name.set('')
        self.p_number.set('')
        self.s_user.set(0)
        self.email.set('')
        self.usernamelist.set("Select")
        self.usernamelist.focus_set()

    def backf(self,event=""):
        self.destroy()
        self.root.deiconify()

    def c_w(self,event=""):
        i = messagebox.askyesno("Billing Software", "Are you Want to Close Application?", parent=self.root)
        if i > 0:
            self.main_root.destroy()
        else:
            return

    def selected(self, event=""):
        query = "select password,name, phoneno,superuser,email from Users where username = ?"
        self.cu = self.conn.execute(query, (self.uentry.get(),)).fetchone()
        self.p_word.set(self.cu[0])
        self.rp_word.set(self.cu[0])
        self.name.set(self.cu[1])
        self.p_number.set(self.cu[2])
        self.email.set(self.cu[4])
        self.s_user.set(self.cu[3])

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
            messagebox.showerror("Billing Software", "Couldn't Connect with Database !",parent=self)
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.title("Update-User")
        self.config(background=self.bgclr1)
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
        self.lable_counter = 0

##============================================timer====================================================================
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

##===========================================signup frame=============================================================


        self.signupframe=Frame(self,background=self.bgclr1,relief=SOLID)
        self.signupframe.place(x=0,y=50,height=700,width=1350)

        llframe = LabelFrame(self.signupframe, background=self.bgclr1, text="Update User", font=("Arial Bold", 20),relief=SOLID)
        llframe.place(x=400,y=0, height=650, width=500)

        backbutton = Button(self.signupframe, text="BACK", width=10, bg=self.bgclr2, command=self.backf, bd=5, font=("Arial Bold", 8))
        backbutton.place(x=10, y=10, height=25, width=75)

##==============================================signup frame=================================================

        usernamelabel = Label(llframe, text="Username", bd=5, font=("Arial Bold", 20), bg=self.bgclr1, fg=self.bgclr2)
        usernamelabel.place(x=50, y=75, height=25)

        self.uentry = StringVar()
        self.usernamelist = ttk.Combobox(llframe, state="readonly",textvariable=self.uentry, font=("Arial Bold", 10))
        self.usernamelist.place(x=300, y=75, height=25,width=150)
        self.usernamelist.set("Select")
        self.usernamelist.bind("<<ComboboxSelected>>", self.selected)

        query = "select username from Users"
        self.un = self.conn.execute(query).fetchall()
        query = "select username from CurrentUser"
        self.c_u = self.conn.execute(query).fetchone()
        self.k = list()
        for item in self.un:
            if self.c_u[0] != item[0]:
                self.k.append(item[0])
        self.usernamelist['values'] = self.k

        passwordlabel = Label(llframe, text="Password", bd=5, font=("Arial Bold", 20), bg=self.bgclr1, fg=self.bgclr2)
        passwordlabel.place(x=50, y=125, height=25)
        self.passwordentry = Entry(llframe, textvariable=self.p_word, borderwidth=2, relief=SUNKEN,show="*",
                                   font=("Arial", 10, "bold"))
        self.passwordentry.place(x=300, y=125, height=25, width=150)

        repasswordlabel = Label(llframe, text=" Re-Password", bd=5, font=("Arial Bold", 20), bg=self.bgclr1, fg=self.bgclr2)
        repasswordlabel.place(x=43, y=175, height=25)
        self.repasswordentry = Entry(llframe, textvariable=self.rp_word, borderwidth=2, relief=SUNKEN,show="*",
                                     font=("Arial", 10, "bold"))
        self.repasswordentry.place(x=300, y=175, height=25, width=150)

        namelabel = Label(llframe, text="Name", bd=5, font=("Arial Bold", 20), bg=self.bgclr1, fg=self.bgclr2)
        namelabel.place(x=50, y=225, height=25)
        self.nameentry = Entry(llframe, textvariable=self.name, borderwidth=2, relief=SUNKEN,
                               font=("Arial", 10, "bold"))
        self.nameentry.place(x=300, y=225, height=25, width=150)

        phonenumberlabel = Label(llframe, bd=5, text="Phone Number", font=("Arial Bold", 20), bg=self.bgclr1, fg=self.bgclr2)
        phonenumberlabel.place(x=50, y=275, height=25)
        self.phonenumberentry = Entry(llframe, textvariable=self.p_number, borderwidth=2, relief=SUNKEN,
                                      font=("Arial", 10, "bold"))
        self.phonenumberentry.place(x=300, y=275, height=25, width=150)

        emaillabel = Label(llframe, text="E-mail", bd=5, font=("Arial Bold", 20), bg=self.bgclr1, fg=self.bgclr2)
        emaillabel.place(x=50, y=325, height=25)
        self.emailentry = Entry(llframe, textvariable=self.email, borderwidth=2, relief=SUNKEN,
                                font=("Arial", 10, "bold"))
        self.emailentry.place(x=300, y=325, height=25, width=150)

        self.susercb = Checkbutton(llframe, text="Apoint As An Admin ", variable=self.s_user, bd=5,font=("Arial Bold", 12), bg=self.bgclr1, fg='black')
        self.susercb.place(x=50, y=375)

        submitbutton = Button(llframe, text="UPDATE", bg=self.bgclr2, width=12, command=self.u_update, bd=5,
                              font=("Arial Bold", 15))
        submitbutton.place(x=45, y=500, height=30)
        clearbutton = Button(llframe, text="CLEAR", bg=self.bgclr2, width=12, command=self.clearset, bd=5,
                             font=("Arial Bold", 15))
        clearbutton.place(x=270, y=500, height=30)
        self.usernamelist.focus_set()

        self.bind("<Control-q>", self.backf)
        self.bind("<Return>", self.u_update)
        self.bind("<Delete>", self.clearset)
        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()