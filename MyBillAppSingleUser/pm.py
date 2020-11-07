from tkinter import *
import time
import sqlite3
from tkinter import messagebox
from tkinter import ttk

class pm1(Toplevel):

    def dynamic_data_show_rp(self):
        self.rq_label = Label(self.llframer, text="Current Quantity of\n{}".format(self.namelistr.get()),font=("Arial Bold", 12), bg=self.bgclr1, bd=5, fg=self.bgclr2)
        self.rq_label.place(x=20, y=200)
        query7 = """ select quantity from product where name = ?"""
        self.rp_quantity = self.conn.execute(query7, (self.namelistr.get(),)).fetchone()
        self.conn.commit()
        self.rq_entry_variable = IntVar()
        self.rq_entry_variable.set(self.rp_quantity[0])
        self.rq_entry = Entry(self.llframer, textvariable=self.rq_entry_variable, borderwidth=2, relief=SUNKEN,font=("Arial", 10, "bold"))
        self.rq_entry.place(x=240, y=200, height=30,width=170)
        self.rq_entry.config(state="disabled")

    def selectedrp(self, event=""):
        if self.lable_counterrp == 0:
            self.dynamic_data_show_rp()
            self.lable_counterrp = self.lable_counterrp + 1

        else:
            self.rq_label.destroy()
            self.rq_entry.destroy()
            self.dynamic_data_show_rp()

    def dynamic_data_show_price(self):
        self.p_label = Label(self.llframep, text="Current Price of\n{}".format(self.namelistp.get()),font=("Arial Bold", 12), bg=self.bgclr1, bd=5, fg=self.bgclr2)
        self.p_label.place(x=20, y=250)
        query2 = """ select price from product where name = ?"""
        self.p_price = self.conn.execute(query2, (self.namelistp.get(),)).fetchone()
        self.conn.commit()
        self.p_entry_variable = IntVar()
        self.p_entry_variable.set(self.p_price[0])
        self.p_entry = Entry(self.llframep, textvariable=self.p_entry_variable, borderwidth=2, relief=SUNKEN,font=("Arial", 10, "bold"))
        self.p_entry.place(x=240, y=250, height=30,width=170)
        self.p_entry.config(state="disabled")

    def selectedprice(self, event=""):
        if self.lable_counterp == 0:
            self.dynamic_data_show_price()
            self.n_price.set('')
            self.pentry.focus_set()
            self.lable_counterp = self.lable_counterp + 1

        else:
            self.p_label.destroy()
            self.p_entry.destroy()
            self.n_price.set('')
            self.pentry.focus_set()
            self.dynamic_data_show_price()

    def dynamic_data_show_stock(self):
        self.q_label = Label(self.llframes, text="Current Quantity of\n{}".format(self.namelistq.get()),font=("Arial Bold", 12), bg=self.bgclr1, bd=5, fg=self.bgclr2)
        self.q_label.place(x=20, y=250)
        query3 = """ select quantity from product where name = ?"""
        self.p_quantity = self.conn.execute(query3, (self.namelistq.get(),)).fetchone()
        self.conn.commit()
        self.q_entry_variable = IntVar()
        self.q_entry_variable.set(self.p_quantity[0])
        self.q_entry = Entry(self.llframes, textvariable=self.q_entry_variable, borderwidth=2, relief=SUNKEN,font=("Arial", 10, "bold"))
        self.q_entry.place(x=240, y=250, height=30,width=170)
        self.q_entry.config(state="disabled")

    def selectedstock(self, event=""):
        if self.lable_counteruq == 0:
            self.dynamic_data_show_stock()
            self.n_quantity.set('')
            self.qentry.focus_set()
            self.lable_counteruq = self.lable_counteruq + 1

        else:
            self.q_label.destroy()
            self.q_entry.destroy()
            self.n_quantity.set('')
            self.qentry.focus_set()
            self.dynamic_data_show_stock()

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

    def clrp(self,event=""):
        self.n_price.set('0')
        self.namelistp.set('Select')
        self.p_entry.destroy()
        self.p_label.destroy()
        self.lable_counterp = 0
        self.namelistp.focus_set()

    def clrs(self,event=""):
        self.n_quantity.set('0')
        self.namelistq.set('Select')
        self.q_entry.destroy()
        self.q_label.destroy()
        self.lable_counteruq = 0
        self.namelistq.focus_set()

    def clrr(self,event=""):
        self.namelistr.set('Select')
        self.rq_entry.destroy()
        self.rq_label.destroy()
        self.lable_counterrp = 0
        self.namelistr.focus_set()

    def r_m(self,event=""):
        try:
            if self.r_name.get() == "Select":
                raise AttributeError
        except:

            messagebox.showerror("Billing Software", "Please Select Product Name.",parent=self)
            self.namelistq.focus_set()
            return

        self.or_quantity = IntVar()
        query8 = """ select quantity from product where name= ? """
        self.or_quantity = self.conn.execute(query8, (self.r_name.get(),)).fetchone()
        if self.or_quantity[0] == 0 :
            query9=""" delete from product where name = ?"""
            self.conn.execute(query9,(self.r_name.get(),))
            self.conn.commit()
            messagebox.showinfo("Billing Software", "'{0}' is Successfully Removed.".format(self.r_name.get()),parent=self)
            self.clrr()
            self.withdraw()
            pm1(self.root , self.main_root)
        else:
            messagebox.showerror("Billing Software","'{}' is not Out of Stock !\nSo you can't remove it from this Application.".format(self.r_name.get()),parent=self)
            self.clrr()

    def add_p(self,event=""):

        try:
            if self.p_name.get() == "Select":
                raise AttributeError
            try:
                if self.pentry.get() == "":
                    raise AttributeError
                try:
                    float(self.pentry.get())
                    if (float(self.pentry.get())) <= 0:
                        raise AttributeError
                except:
                    m = messagebox.showerror("Billing Software", "Price must be Positive Number.",parent=self)
                    self.n_price.set("")
                    self.pentry.focus_set()
                    return
            except:
                m = messagebox.showerror("Billing Software", "Price  not Found!",parent=self)
                m = messagebox.showinfo("Billing Software", "Please Enter Price.",parent=self)
                self.n_price.set("")
                self.pentry.focus_set()
                return

        except:

            m = messagebox.showerror("Billing Software", "Please Select Product Name.",parent=self)
            self.namelistp.focus_set()
            return


        query4 = """ update product set price= ? where name = ?  """
        self.conn.execute(query4,(self.pentry.get(),self.p_name.get()))
        self.conn.commit()
        m = messagebox.showinfo("Billing Software", "Price Of '{0}' is Updated Successfully".format(self.p_name.get()),parent=self)
        self.clrp()

    def add_q(self,event=""):

        try:
            if self.q_name.get() == "Select":
                raise AttributeError
            try:
                if self.qentry.get() == "":
                    raise AttributeError
                try:
                    float(self.qentry.get())
                    if (float(self.qentry.get())) <= 0:
                        raise AttributeError
                except:

                    messagebox.showerror("Billing Software", "Quantity must be Positive Number.",parent=self)
                    self.n_quantity.set("")
                    self.qentry.focus_set()
            except:
                m = messagebox.showerror("Billing Software", "Quantity  not Found!",parent=self)
                m = messagebox.showinfo("Billing Software", "Please Enter Quantity.",parent=self)
                self.n_quantity.set("")
                self.qentry.focus_set()
                return

        except:

            messagebox.showerror("Billing Software", "Please Select Product Name.",parent=self)
            self.namelistq.focus_set()
            return

        self.o_quantity = IntVar()
        query = """ select quantity from product where name= ? """
        self.o_quantity = self.conn.execute(query, (self.q_name.get(),)).fetchone()
        self.new = self.n_quantity.get()
        i=int(self.new)
        j=int(self.o_quantity[0])
        k=i+j
        query1 = """ update product set quantity= ? where name = ?  """
        self.conn.execute(query1,(k,self.q_name.get()))
        self.conn.commit()
        messagebox.showinfo("Billing Software", "Quantity Of '{0}' Updated Suceessfully.".format(self.q_name.get()),parent=self)
        self.clrs()

    def __init__(self, root,main_root):
        self.main_root = main_root
        self.root = root
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        try:
            self.conn = sqlite3.connect('Bill.db')
        except:
            m = messagebox.showerror("Billing Software","Couldn't Connect With Database !")
        self.bgclr1 = "#0080c0"
        self.bgclr2 = "#e7d95a"
        self.config(background=self.bgclr1)
        self.geometry("1350x700+0+0")
        self.title("Product Management")
        self.qn= IntVar()
        self.lable_counterp = 0
        self.lable_counteruq = 0
        self.lable_counterrp = 0
##=====================================================timer=================================================================
        Date = StringVar()
        Time = StringVar()
        Date.set(time.strftime("%d-%m-%y"))
        f = Frame(self, bd=1, background=self.bgclr1, relief=SOLID)
        f.place(x=0, y=0, relwidth=1, height=50)
        l1 = Label(f, textvariable=Date, bg=self.bgclr2, font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2,relief=SUNKEN)
        l1.place(x=20, y=12, height=25)
        self.l2 = Label(f, bg=self.bgclr2, font=("Arial", 15, "bold"), bd=1, fg='black', borderwidth=2, relief=SUNKEN)
        self.l2.place(x=1220, y=12, height=25)
        l3 = Label(f, text="P & H Billing Software", bg=self.bgclr2, font=("Arial", 18, "bold"), fg='black',
                   borderwidth=2, bd=1, relief=SUNKEN)
        l3.place(x=520, y=5, height=35)

        self.timer()

##==============================================stock  entry=======================================================================

        stockframe = Frame(self, background=self.bgclr1, relief=SOLID,bd=1)
        stockframe.place(x=0, y=50, height=650, width=1350)

        backbutton = Button(stockframe, text="BACK", width=10, bg=self.bgclr2, command=self.backf, bd=5,font=("Arial Bold", 8))
        backbutton.place(x=10, y=10, height=25, width=75)

##===================================================remove product================================================================
        self.llframer = LabelFrame(stockframe, background=self.bgclr1, text="Remove Product", font=("Arial Bold", 20),relief=SOLID)
        self.llframer.place(x=10, y=50, height=550, width=425)

        self.r_name = StringVar()
        namelabelr = Label(self.llframer, text="Product name", font=("Arial Bold", 20), bg=self.bgclr1, bd=5,fg=self.bgclr2)
        namelabelr.place(x=5, y=75, height=30)

        self.namelistr = ttk.Combobox(self.llframer, state="readonly",textvariable=self.r_name, font=("Arial Bold", 10))
        self.namelistr.place(x=240, y=75, height=30,width=170)
        self.namelistr.bind("<<ComboboxSelected>>", self.selectedrp)
        self.namelistr.set("Select")

        self.nameup = StringVar()
        query6 = """ select name from product """
        self.namerp = self.conn.execute(query6).fetchall()
        self.conn.commit()

        self.krp = list()
        for self.irp in self.namerp:
            self.krp.append(self.irp[0])

        self.namelistr['values'] = self.krp

        rmbutton =Button(self.llframer , text="REMOVE", width=10, bg=self.bgclr2,command=self.r_m, font=("arial bold",15),bd=5)
        rmbutton.place(x=75,y=350,height=35, width=125)
        clearbuttonp = Button(self.llframer, text="CLEAR", width=10, bg=self.bgclr2, command=self.clrr,font=("arial bold", 15), bd=5)
        clearbuttonp.place(x=250, y=350, height=35, width=100)

##====================================================update price=================================================================

        self.llframep = LabelFrame(stockframe, background=self.bgclr1, text="Update Price", font=("Arial Bold", 20),relief=SOLID)
        self.llframep.place(x=450, y=50, height=550, width=425)
        self.p_name= StringVar()
        namelabelp= Label(self.llframep ,text="Product name", font=("Arial Bold",20),bg=self.bgclr1,bd=5,fg=self.bgclr2)
        namelabelp.place(x=5,y=75,height=30)

        self.namelistp = ttk.Combobox(self.llframep , state="readonly",textvariable=self.p_name,font=("Arial Bold",10))
        self.namelistp.place(x=240,y=75,height=30,width=170)
        self.namelistp.bind("<<ComboboxSelected>>", self.selectedprice)
        self.namelistp.set("Select")

        self.nameup= StringVar()
        query = """ select name from product """
        self.nameup = self.conn.execute(query).fetchall()
        self.conn.commit()

        self.kup = list()
        for self.iup in self.nameup:
            self.kup.append(self.iup[0])

        self.namelistp['values']=self.kup
        self.n_price = IntVar()

        plabel= Label(self.llframep ,text="Price",font=("Arial Bold",20),bg=self.bgclr1,bd=5,fg=self.bgclr2)
        plabel.place(x=20,y=175,height=30)
        self.pentry= Entry(self.llframep ,textvariable=self.n_price,borderwidth=2,relief=SUNKEN, font=("Arial", 10, "bold"))
        self.pentry.place(x=240,y=175,height=30,width=170)

        addbuttonp = Button(self.llframep , text="ADD", width=10, bg=self.bgclr2,command=self.add_p, font=("arial bold",15),bd=5)
        addbuttonp.place(x=75, y=350,height=35,width=100)
        clearbuttonp = Button(self.llframep , text="CLEAR", width=10, bg=self.bgclr2, command=self.clrp, font=("arial bold",15),bd=5)
        clearbuttonp.place(x=250, y=350,height=35,width=100)

##===================================================================update stock===========================================================

        self.llframes = LabelFrame(stockframe, background=self.bgclr1, text="Update Stock", font=("Arial Bold", 20),relief=SOLID)
        self.llframes.place(x=900, y=50, height=550, width=425)
        self.q_name = StringVar()

        namelabelq = Label(self.llframes, text="Product name", font=("Arial Bold", 20), bg=self.bgclr1, bd=5,fg=self.bgclr2)
        namelabelq.place(x=5, y=75, height=25)

        self.namelistq = ttk.Combobox(self.llframes,state="readonly", textvariable=self.q_name, font=("Arial Bold", 10))
        self.namelistq.place(x=240, y=75, height=25,width=170)
        self.namelistq.bind("<<ComboboxSelected>>", self.selectedstock)
        self.namelistq.set("Select")

        self.nameus = StringVar()
        query5 = """ select name from product """
        self.nameus = self.conn.execute(query5).fetchall()
        self.conn.commit()

        self.kus = list()
        for self.ius in self.nameus:
            self.kus.append(self.ius[0])

        self.namelistq['values'] = self.kus

        self.n_quantity = IntVar()
        self.n_quantity.set("0")
        qlabel = Label(self.llframes, text="Quantity", font=("Arial Bold", 20), bg=self.bgclr1, bd=5, fg=self.bgclr2)
        qlabel.place(x=20, y=175, height=30)
        self.qentry = Entry(self.llframes, textvariable=self.n_quantity, borderwidth=2, relief=SUNKEN,font=("Arial", 10, "bold"))
        self.qentry.place(x=240, y=175, height=30,width=170)

        addbuttonq = Button(self.llframes, text="ADD", width=10, bg=self.bgclr2, command=self.add_q, font=("arial bold", 15), bd=5)
        addbuttonq.place(x=75, y=350, height=35, width=100)
        clearbuttonq = Button(self.llframes, text="CLEAR", width=10, bg=self.bgclr2, command=self.clrs,font=("arial bold", 15), bd=5)
        clearbuttonq.place(x=250, y=350, height=35, width=100)

        self.bind("<Control-r>", self.r_m)
        self.bind("<Control-p>", self.add_p)
        self.bind("<Control-s>", self.add_q)
        self.bind("<Control-q>", self.backf)
        self.protocol("WM_DELETE_WINDOW", self.c_w)

        self.mainloop()
