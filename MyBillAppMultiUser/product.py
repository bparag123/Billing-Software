from tkinter import *
from signupcode import signupcode1
import time
import sqlite3
from tkinter import messagebox,filedialog
from pm import pm1

class addproduct(Toplevel):

    def timer(self):
        d = time.strftime("%H:%M:%S")
        self.l2.config(text=d)
        self.l2.after(200, self.timer)

    def user(self,event=""):
        self.withdraw()
        obj_of_signup=signupcode1(self,self.main_root)

    def u_price(self,event=""):
        self.withdraw()
        obj_of_price=pm1(self,self.main_root)

    def l_out(self, event=""):
        i = messagebox.askyesno("Billing Software", "Are you Want to Logout?", parent=self)
        if i > 0:
            self.destroy()
            self.root.deiconify()
        else:
            return
    def c_w(self,event=""):
        i = messagebox.askyesno("Billing Software", "Are you Want to Close Application?", parent=self.root)
        if i > 0:
            self.main_root.destroy()
        else:
            return

    def clr(self,event=""):
        self.p_name.set('')
        self.p_price.set('')
        self.p_quantity.set('')

    def productdetails(self,event=""):
        self.txt.config(state="normal")
        self.txt.delete(1.0, END)
        query2 = """ select * from product """
        self.pd = self.conn.execute(query2).fetchall()
        self.conn.commit()
        self.pd.sort()
        self.txt.insert(END, "\n")
        self.txt.insert(END, "\t\t\t\tProduct Details")
        self.txt.insert(END, "\n\t\t\t\t" + "="*15)
        self.txt.insert(END, "\n" + "="*84)
        self.txt.insert(END, "\n\tSr.")
        self.txt.insert(END, "\tProduct Name\t\t\t\tPrice\t\t Quantity")
        self.txt.insert(END, "\n" + "=" * 84)
        self.txt.insert(END, "\n")
        self.txt.insert(END, "\n")
        i = 1
        for self.item in self.pd:
            self.txt.insert(END,"\n\t" +str(i)+ "\t  " + self.item[0] + "\t\t\t\t " + str(self.item[1]) + "\t\t  " + str(self.item[2]))
            i = i + 1
        self.txt.config(state="disabled")

    def refresh(self,event=""):
        self.productdetails()

    def add_item(self,event=""):

        try:
            if self.nameentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Product Name not Found!", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Product Name.", parent=self)
            self.p_name.set("")
            self.nameentry.focus_set()
            return
        try:
            if self.priceentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Price not Found!", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Price.", parent=self)
            self.p_price.set("")
            self.priceentry.focus_set()
            return

        try:
            if self.qentry.get() == "":
                raise AttributeError
        except:
            m = messagebox.showerror("Billing Software", "Quantity  not Found!", parent=self)
            m = messagebox.showinfo("Billing Software", "Please Enter Quantity.", parent=self)
            self.p_quantity.set("")
            self.qentry.focus_set()
            return

        try:
            if float(self.priceentry.get()) <= 0:
                raise AttributeError
        except:
            messagebox.showerror("Billing Software","Price must be Number.", parent=self)
            self.p_price.set("")
            self.priceentry.focus_set()
            return

        try:
            if int(self.qentry.get()) <= 0:
                raise AttributeError
        except:
            messagebox.showerror("Billing Software", "Quantity must be Number.", parent=self)
            self.p_quantity.set("")
            self.qentry.focus_set()
            return

        try:
            query = """ insert into product (name, price,quantity) values(?,?,?) """
            self.conn.execute(query,(self.nameentry.get(),self.priceentry.get(),self.qentry.get()))
            self.conn.commit()
            messagebox.showinfo("Billing Software","'{0}' is Successfully Added.".format(self.nameentry.get()), parent=self)
            self.clr()
            self.nameentry.focus_set()
            self.productdetails()

        except:
            messagebox.showerror("Billing Software","'{0}' is already exist.".format(self.nameentry.get()), parent=self)
            self.p_name.set("")
            self.nameentry.focus_set()

    def __init__(self, root,main_root):
        self.main_root = main_root
        self.root = root
        messagebox.showinfo("Billing software", "You are Successfully Logged-in as an Admin.", parent=self.root)
        self.root.withdraw()
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        try:
            self.conn = sqlite3.connect('userinfo.db')
        except:
            messagebox.showerror("Billing Software","Couldn't Connect with Database !", parent=self)
        bgclr1 = "#0080c0"
        bgclr2 = "#e7d95a"
        self.title("Admin")
        self.config(background=bgclr1)
        self.geometry("1350x700+0+0")

##====================================================timer===============================================================

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

##=================================================product add frame=====================================================

        self.p_name=StringVar()
        self.p_price=StringVar()
        self.p_quantity=StringVar()

        f1 = LabelFrame(self, text="Product Info.", font=('arial', 10, "bold"), background=bgclr1, relief=SOLID)
        f1.place(x=10, y=50, width=450, height=630)

        namelabel=Label(f1,text="Product Name",font=('arial',15,'bold'),background=bgclr1,bd=5,fg=bgclr2)
        namelabel.place(x=25,y=100,height=35)
        self.nameentry=Entry(f1,textvariable=self.p_name,borderwidth=2,relief=SUNKEN, font=("Arial", 13, "bold"))
        self.nameentry.place(x=210,y=105,height=25,width=180)

        pricelabel = Label(f1, text="Price", font=('arial', 15, 'bold'), background=bgclr1,bd=5,fg=bgclr2)
        pricelabel.place(x=25, y=200, height=35)
        self.priceentry = Entry(f1,textvariable=self.p_price,borderwidth=2,relief=SUNKEN, font=("Arial", 13, "bold"))
        self.priceentry.place(x=210, y=205, height=25, width=180)

        qlabel = Label(f1, text="Quantity", font=('arial', 15, 'bold'), background=bgclr1,bd=5,fg=bgclr2)
        qlabel.place(x=25, y=300, height=35)
        self.qentry = Entry(f1,textvariable=self.p_quantity,borderwidth=2,relief=SUNKEN, font=("Arial", 13, "bold"))
        self.qentry.place(x=210, y=305, height=25, width=180)

        addbutton = Button(f1, text="ADD", bg=bgclr2, font=('arial', 15, 'bold'), command=self.add_item, bd=5)
        addbutton.place(x=100,y=450,height=35,width=100)
        clrbutton = Button(f1, text="CLEAR", bg=bgclr2, font=('arial', 15, 'bold'), command=self.clr, bd=5)
        clrbutton.place(x=275, y=450, height=35, width=100)

##================================================buttons frame============================================================

        f2 = LabelFrame(self, text="Admin-Area", font=('arial', 10, "bold"), background=bgclr1, relief=SOLID)
        f2.place(x=470, y=50, width=885, height=80)

        ubutton = Button(f2, text="REFRESH", bg=bgclr2, font=('arial', 15, 'bold'), command=self.refresh, bd=5)
        ubutton.place(x=20, y=20, width=130, height=30)
        ubutton= Button(f2,text="USERS",bg=bgclr2,font=('arial',15,'bold'),command=self.user,bd=5)
        ubutton.place(x=180,y=20,width=130,height=30)
        mnbutton = Button(f2, text="PRODUCT MANAGMENT", bg=bgclr2, font=('arial', 15, 'bold'),command=self.u_price,bd=5)
        mnbutton.place(x=340, y=20,width=320, height=30)
        lobutton = Button(f2, text="LOGOUT", bg=bgclr2, font=('arial', 15, 'bold'),command=self.l_out,bd=5)
        lobutton.place(x=700, y=20, width=140, height=30)

##=================================================data show frame========================================================

        self.f3 = LabelFrame(self, text="Available Products", font=('arial', 10, "bold"), background=bgclr1, relief=SOLID)
        self.f3.place(x=470, y=130, height=550, width=885)

        self.sc = Scrollbar(self.f3)
        self.txt = Text(self.f3, yscrollcommand=self.sc.set, borderwidth=2, relief=SUNKEN)
        self.sc.pack(side=RIGHT, fill=Y)
        self.txt.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.sc.config(command=self.txt.yview)
        self.productdetails()
        self.nameentry.focus_set()

        self.bind("<Control-q>", self.l_out)
        self.bind("<Return>", self.add_item)
        self.bind("<Control-r>", self.refresh)
        self.bind("<Control-p>", self.u_price)
        self.bind("<Delete>", self.clr)
        self.bind("<Control-u>", self.user)
        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()

