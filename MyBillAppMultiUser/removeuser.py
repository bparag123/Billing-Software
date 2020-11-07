from tkinter import *
import time
import sqlite3
from tkinter import messagebox,ttk


class removeuser1(Toplevel):

    def timer(self):
        d = time.strftime("%H:%M:%S")
        self.l2.config(text=d)
        self.l2.after(200, self.timer)

    def backf(self,event=""):
        self.destroy()
        self.root.deiconify()
    def c_w(self,event=""):
        i = messagebox.askyesno("Billing Software", "Are you Want to Close Application?", parent=self.root)
        if i > 0:
            self.main_root.destroy()
        else:
            return

    def dynamic_data_show(self):
        self.uname = StringVar()
        self.ph = StringVar()
        self.n_ame = StringVar()
        self.em = StringVar()

        self.dyframe = LabelFrame(self.removeframe,background=self.bgclr1, text="User Info.", font=("Arial Bold", 20),relief=SOLID)
        self.dyframe.place(x=800,y=50,height=500,width=500)

        self.unlabel = Label(self.dyframe, text="Username",bg=self.bgclr1, font=("Arial Bold",20),bd=5,fg=self.bgclr2)
        self.unlabel.place(x=20,y=75,height=25)
        self.unentry = Entry(self.dyframe,textvariable=self.uname,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.unentry.place(x=290,y=75,height=25)

        self.nlabel = Label(self.dyframe, text="Name",bg=self.bgclr1, font=("Arial Bold",20),bd=5,fg=self.bgclr2)
        self.nlabel.place(x=20,y=150,height=25)
        self.nentry = Entry(self.dyframe,textvariable=self.n_ame,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.nentry.place(x=290,y=150,height=25)

        self.phnolabel = Label(self.dyframe, text="Phone Number",bg=self.bgclr1, font=("Arial Bold",20),bd=5,fg=self.bgclr2)
        self.phnolabel.place(x=20,y=225,height=25)
        self.phnoentry = Entry(self.dyframe , textvariable=self.ph,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.phnoentry.place(x=290,y=225,height=25)

        self.elabel = Label(self.dyframe, text="E-mail",bg=self.bgclr1, font=("Arial Bold",20),bd=5,fg=self.bgclr2)
        self.elabel.place(x=20,y=300,height=25)
        self.eentry = Entry(self.dyframe, textvariable=self.em,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.eentry.place(x=290,y=300,height=25)

        query="select username,name, phoneno,email from Users where username = ?"
        self.cu=self.conn.execute(query,(self.uentry.get(),)).fetchone()
        self.uname.set(self.cu[0])
        self.n_ame.set(self.cu[1])
        self.ph.set(self.cu[2])
        self.em.set(self.cu[3])

        self.unentry.config(state="disabled")
        self.nentry.config(state="disabled")
        self.phnoentry.config(state="disabled")
        self.eentry.config(state="disabled")

    def selected(self, event=""):
        if self.lable_counter == 0:
            self.dynamic_data_show()
            self.lable_counter = self.lable_counter + 1

        else:
            self.dyframe.destroy()
            self.unlabel.destroy()
            self.nlabel.destroy()
            self.phnolabel.destroy()
            self.elabel.destroy()
            self.unentry.destroy()
            self.nentry.destroy()
            self.phnoentry.destroy()
            self.eentry.destroy()
            self.dynamic_data_show()

    def clr(self,event=""):
        self.dyframe.destroy()
        self.unlabel.destroy()
        self.nlabel.destroy()
        self.phnolabel.destroy()
        self.elabel.destroy()
        self.unentry.destroy()
        self.nentry.destroy()
        self.phnoentry.destroy()
        self.eentry.destroy()
        self.usernamelist.set("Select")

    def re_user(self,event=""):

        try:
            if self.uentry.get() == "Select":
                raise AttributeError
            try:
                query2=""" select username from Users"""
                self.name1=self.conn.execute(query2).fetchall()
                self.conn.commit()
                self.k = list()
                for self.i in self.name1:
                    self.k.append(self.i[0])
                if(self.uentry.get() not in self.k):
                    raise ValueError
            except:
                m = messagebox.showerror("Billing Software","Username doesn't  exist !",parent=self)

                return
        except:
            m = messagebox.showerror("Billing Software", "Username not Found !",parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Username.",parent=self)
            self.usernamelist.focus_set()
            return
        try:

            query = """select username from CurrentUser"""
            self.current_user= self.conn.execute(query).fetchone()


            if self.current_user[0]==self.uentry.get():
                m = messagebox.showerror("Billing Software","Sorry!\nYou are Currently Logged in with This Username so you can't Delete Yourself.",parent=self)
                self.clr()
            else:

                query = """ delete from Users where username= ? """
                self.conn.execute(query,(self.uentry.get(),))
                self.conn.commit()
                m = messagebox.showinfo("Billing Software","User '{}' is removed Successfully.".format(self.uentry.get()),parent=self)
                self.uentry.set("Selected")
                self.clr()
                self.withdraw()
                removeuser1(self.root,self.main_root)

        except:
            m = messagebox.showerror("Billing Software","Please Enter valid Username",parent=self)
            self.usernamelist.focus_set()


    def __init__(self, root, main_root):
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
        self.title("User Info.")
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.lable_counter = 0
##================================================timer=======================================================================

        Date = StringVar()
        Time = StringVar()
        Date.set(time.strftime("%d-%m-%y"))
        f = Frame(self, bd=1, background="#0080c0", relief=SOLID)
        f.place(x=0, y=0, relwidth=1, height=50)
        l1 = Label(f, textvariable=Date, bg='#e7d95a', font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2,
                   relief=SUNKEN)
        l1.place(x=20, y=12, height=25)
        self.l2 = Label(f, bg='#e7d95a', font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2, relief=SUNKEN)
        self.l2.place(x=1220, y=12, height=25)
        l3 = Label(f, text="P & H Billing Software", bg='#e7d95a', font=("Arial", 18, "bold"), fg='black',
                   borderwidth=2, bd=1, relief=SUNKEN)
        l3.place(x=520, y=5, height=35)

        self.timer()

##================================================removeframe====================================================================

        self.removeframe = Frame(self, background=self.bgclr1, relief=SOLID)
        self.removeframe.place(x=0, y=50, height=700, width=1350)

        self.llframe = LabelFrame(self.removeframe, background=self.bgclr1, text="User Info.", font=("Arial Bold", 20),relief=SOLID)
        self.llframe.place(x=250, y=50, height=500, width=500)

        backbutton = Button(self.removeframe, text="BACK", width=10, bg=self.bgclr2, command=self.backf, bd=5,font=("Arial Bold", 8))
        backbutton.place(x=10, y=10, height=25, width=75)

        usernamelabel= Label(self.llframe,text="Username",bg=self.bgclr1, font=("Arial Bold",20),bd=5,fg=self.bgclr2)
        usernamelabel.place(x=50,y=100,height=30)

        self.uentry=StringVar()
        self.usernamelist = ttk.Combobox(self.llframe ,state="readonly", textvariable=self.uentry,font=("Arial Bold",10))
        self.usernamelist.place(x=250,y=100,height=30)
        self.usernamelist.set("Select")
        self.usernamelist.bind("<<ComboboxSelected>>", self.selected)

        query = "select username from Users"
        self.un = self.conn.execute(query).fetchall()
        self.k = list()
        for item in self.un:
            self.k.append(item[0])
        self.usernamelist['values']=self.k

        removebutton = Button(self.llframe, text="REMOVE", command=self.re_user,bg=self.bgclr2,bd=5,font=("Arial Bold",15))
        removebutton.place(x=100,y=300,height=35)
        clrbutton = Button(self.llframe, text="CLEAR",command=self.clr,bg=self.bgclr2,bd=5,font=("Arial Bold",15))
        clrbutton.place(x=300,y=300,height=35)
        self.usernamelist.focus_set()

        self.bind("<Control-q>", self.backf)
        self.bind("<Return>", self.re_user)
        self.bind("<Delete>", self.clr)
        self.protocol("WM_DELETE_WINDOW", self.c_w)
        self.mainloop()
