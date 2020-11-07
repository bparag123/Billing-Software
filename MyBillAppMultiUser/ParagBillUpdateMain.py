from tkinter import *
from tkinter import ttk,messagebox,simpledialog,filedialog
import time
import sqlite3
from ParagBillUpdate import Edit_Window
from reportlab.pdfgen import canvas
import webbrowser
import qrcode


class Bill(Toplevel):

    def __init__(self, root,main_root):
        self.main_root =main_root
        self.root = root
        messagebox.showinfo("Billing software", "You are Successfully Logged-in as a Staff-User.")
        self.root.withdraw()
        Toplevel.__init__(self)
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()
        try:
            self.db = sqlite3.connect('Bill.db')
        except:
            messagebox.showerror("Billing Software", "Couldn't Connect with Database !",parent=self)
        try:
            self.db1 = sqlite3.connect('userinfo.db')
        except:
            messagebox.showerror("Billing Software", "Couldn't Connect with Database !",parent=self)
        self.geometry("1350x700+0+0")
        self.title("P & H Billing Software")
        bgclr = "#0080c0"
        self.configure(background=bgclr)
        # ===============================Variables============================================

        self.t = StringVar()
        self.cn = StringVar()
        self.pr = StringVar()
        self.a_q = StringVar()
        self.bi = IntVar()
        self.q = StringVar()
        self.amt = 0
        self.ttl = 0
        self.counter = 0
        self.click = False
        self.update_qnt = 0
        self.cancel_counter = False
        query = """select * from CurrentUser"""
        self.creator = self.db1.execute(query).fetchone()

        try:
            x = self.db.execute("""SELECT count(*) FROM Bill""").fetchone()
            y = self.db.execute("""SELECT * FROM D_Bill""").fetchone()
            self.b = x[0] + 1 + y[0]
            self.bi.set(self.b)
        except:
            self.b = 1
            self.bi.set(self.b)

        self.t.set("0")
        self.cn.set("")
        self.pr.set("0")
        self.q.set("0")
        self.a_q.set("0")

        #==================================FRAME1=======================================
        Date = StringVar()
        Time = StringVar()
        Date.set(time.strftime("%d-%m-%y"))
        f = Frame(self,bd=1,background=bgclr,relief=SOLID)
        f.place(x=0,y=0,relwidth=1,height=50)
        l1 = Label(f,textvariable=Date,bg='#e7d95a',font=("Arial",15,"bold"),bd=1,fg='black',borderwidth=2,relief=SUNKEN)
        l1.place(x=20,y=12,height=25)
        self.l2 = Label(f,bg='#e7d95a',font=("Arial",15,"bold"),bd=1,fg='black',borderwidth=2,relief=SUNKEN)
        self.l2.place(x=1220,y=12,height=25)
        l3 = Label(f,text="P & H Billing Software",bg='#e7d95a',font=("Arial",18,"bold"),fg='black',borderwidth=2,bd=1,relief=SUNKEN)
        l3.place(x=520,y=5,height=35)

        # ===================================FRAME2=====================================

        f1 = LabelFrame(self, text="Product Info.", font=('tahoma', 10, "bold"), background=bgclr,relief=SOLID)
        f1.place(x=10, y=50, width=450, height=500)
        l4 = Label(f1, text="Product", bg=bgclr, font=("Arial", 15, "bold"), fg='#e7d95a', bd=5)
        l4.place(x=5,y=50,height=35)
        l5 = Label(f1, text="Quantity", bg=bgclr, font=("Arial", 15, "bold"), fg='#e7d95a', bd=5)
        l5.place(x=5,y=150,height=35)
        l6 = Label(f1, text="Price", bg=bgclr,font=("Arial", 15, "bold"), fg='#e7d95a', bd=5)
        l6.place(x=5,y=250,height=35)
        l7 = Label(f1, text="Availabe\nQuantity", bg=bgclr, font=("Arial", 15, "bold"), fg='#e7d95a', bd=5)
        l7.place(x=5, y=350, height=55)
        self.combo_var = StringVar()
        self.cb1 = ttk.Combobox(f1,state="readonly", textvariable=self.combo_var, font=("Arial Bold", 15))
        self.cb1.place(x=130, y=50, height=30)
        self.cb1.bind("<<ComboboxSelected>>", self.f)
        self.cb1.set("Select")
        query = """ select name from product """
        self.names = self.db1.execute(query).fetchall()
        self.k = list()
        for i in self.names:
            self.k.append(i[0])

        self.cb1['values'] = self.k
        self.qnt = Entry(f1, width=20,textvariable=self.q, font=("Arial", 15, "bold"),borderwidth=2,relief=SUNKEN)
        self.qnt.place(x=130,y=150,height=35)
        self.prc = Entry(f1, width=20,  textvariable=self.pr,font=("Arial", 15, "bold"),borderwidth=2,relief=SUNKEN,state='disabled')
        self.prc.place(x=130,y=250,height=35)
        self.avail_qnt_entry = Entry(f1, width=20, textvariable=self.a_q, font=("Arial", 15, "bold"), borderwidth=2, relief=SUNKEN,state='disabled')
        self.avail_qnt_entry.place(x=130, y=350, height=35)

        # ===================================FRAME3=====================================


        f3 = Frame(self, background=bgclr, relief=SOLID)
        f3.place(x=10,y=600,height=100, width=450)
        self.b_add = Button(f3,text="ADD",bd=5,width=5, bg='#e7d95a',font=('tahoma',10,"bold"),command=self.add)
        self.b_add.grid(row=0, column=1,padx=1)
        self.b_print = Button(f3,text="GENERATE BILL",bd=5,width=15, bg='#e7d95a',font=('tahoma',10,"bold"),command=self.gen)
        self.b_print.grid(row=0, column=2,padx=1)
        self.b_reset = Button(f3,text="RESET", bd=5,width=7,bg='#e7d95a',font=('tahoma',10,"bold"),command=self.reset)
        self.b_reset.grid(row=0, column=3,padx=1)
        self.b_exit = Button(f3,text="LOGOUT", bd=5,width=7,bg='#e7d95a',font=('tahoma',10,"bold"), command=self.exit)
        self.b_exit.grid(row=0, column=4,padx=1)




        #=====================================FRAME4========================================

        f4 = LabelFrame(self,text="Customer Details",font=('tahoma',10,"bold"), background=bgclr, relief=SOLID)
        f4.place(x=470, y=50, width=885, height=80)

        cn = Label(f4, text="Customer Name", bg=bgclr, font=("Arial", 15, "bold"), fg='#e7d95a', bd=5)
        cn.grid(row=0, column=0, padx=5)
        bir = Label(f4, text="Bill Id", bg=bgclr, font=("Arial", 15, "bold"), fg='#e7d95a', bd=5)
        bir.grid(row=0, column=3,padx=10)

        self.c_name = Entry(f4, width=15, textvariable=self.cn,font="Arial",borderwidth=2,relief=SUNKEN)
        self.c_name.grid(row=0, column=1,padx=10)
        self.bid = Entry(f4, width=15, textvariable=self.bi,font="Arial",state="disabled",borderwidth=2,relief=SUNKEN)
        self.bid.grid(row=0, column=4,padx=10)
        self.b_show = Button(f4, text="Search / Edit Bills",width=18, bd=5, bg='#e7d95a', font=('tahoma', 10, "bold"), command=self.watch)
        self.b_show.grid(row=0, column=5, padx=10)

        #=====================================FRAME5========================================

        f5 = LabelFrame(self, text="Preview", font=('tahoma', 10, "bold"), background=bgclr, relief=SOLID)
        f5.place(x=470, y=130, height=550, width=885)

        sc = Scrollbar(f5)
        self.txt = Text(f5,yscrollcommand=sc.set,borderwidth=2,relief=SUNKEN)
        self.txt.config(state="disabled")
        sc.pack(side=RIGHT, fill=Y)
        self.txt.pack(fill=BOTH,expand=1, padx=5,pady=5)
        sc.config(command=self.txt.yview)

        #Starting of Bill
        self.txt.config(state="normal")
        self.txt.delete(1.0, END)
        self.txt.insert(END, "\n")
        self.txt.insert(END, "\t\t\tP & H Billing Software")
        self.txt.insert(END, "\n\t\t\t=======================")
        self.txt.insert(END, "\nDate : " + time.strftime("%d - %m - %y"))
        self.txt.insert(END, "\nTime : " + time.strftime("%H : %M : %S"))
        self.txt.insert(END, "\nCreated by : " + self.creator[0])
        self.txt.insert(END, "\nBill ID : " + str(self.bid.get()))
        self.txt.insert(END, "\n" + "=" * 67)
        self.txt.insert(END, "\nSr No.\tProduct\t  Quantity            Price              Amount")
        self.txt.insert(END, "\n" + "=" * 67)
        self.txt.config(state="disabled")
        self.c_name.focus_set()




#======================================================================================
        self.bind("<Control-s>", self.gen)
        self.bind("<Delete>", self.reset)
        self.bind("<Control-q>", self.exit)
        self.bind("<Control-f>", self.watch)
        self.bind("<Return>", self.add)
        self.protocol("WM_DELETE_WINDOW", self.c_w)
        
        self.timer()
        self.products=[]
#======================================================================================


    def timer(self):
        d = time.strftime("%H:%M:%S")
        self.l2.config(text=d)
        self.l2.after(200, self.timer)

    def f(self,event):

        query = """select price,quantity from product where name= (?)"""
        set_data= self.db1.execute(query, (self.cb1.get(),)).fetchone()
        self.pr.set(set_data[0])
        self.a_q.set(set_data[1])
        self.q.set('')
        self.qnt.focus_set()

    def exit(self,event=""):
        i = messagebox.askyesno("Billing Software", "Are you Want to Logout?", parent=self)
        if i>0:
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

    def add(self,event=""):

        if self.counter==0:
            if self.c_name.get()!="":
                self.c_name.config(state="normal")
                self.txt.config(state="normal")
                self.txt.delete(1.0, END)
                self.txt.insert(END, "\n")
                self.txt.insert(END, "\t\t\tP & H Billing Software")
                self.txt.insert(END, "\n\t\t\t=======================")
                self.txt.insert(END, "\nDate : " + time.strftime("%d - %m - %y"))
                self.txt.insert(END, "\nTime : " + time.strftime("%H : %M : %S"))
                self.txt.insert(END, "\nCreated by : " + self.creator[0])
                self.txt.insert(END, "\nBill ID : " + str(self.bid.get()))
                self.txt.insert(END, "\nCustomer Name : " + str(self.c_name.get()))
                self.c_name.config(state="disabled")
                self.txt.insert(END, "\n" + "=" * 67)
                self.txt.insert(END, "\nSr No.\tProduct\t  Quantity            Price              Amount")
                self.txt.insert(END, "\n" + "=" * 67)
                self.txt.config(state="disabled")
                self.counter = self.counter + 1
            try:
                if self.c_name.get()=="":
                    raise AttributeError
            except:
                m = messagebox.showerror("Billing Software", "Customer Name not Found!", parent=self)
                m = messagebox.showinfo("Billing Software", "Please Enter Customer Name and ADD it!", parent=self)
                self.c_name.focus_set()
                self.counter=0



        else:
            if self.counter == 1:
                try:
                    if self.cb1.get() == "Select":
                        raise AttributeError
                    try:
                        float(self.q.get())
                        if float(self.q.get()) <= 0:
                            raise AttributeError

                        query = """select quantity from product where name= (?)"""
                        self.available_qnt = self.db1.execute(query, (self.cb1.get(),)).fetchone()
                        self.update_qnt = int(self.available_qnt[0]) - int(self.q.get())


                        if int(self.update_qnt) < 0:
                            messagebox.showwarning("Billing Software","In-sufficient Stock of '{}'".format(self.cb1.get()),parent=self)
                            self.q.set("")
                            self.qnt.focus_set()
                        else:
                            query = """update product set quantity = (?) where name= (?)"""
                            self.db1.execute(query,(self.update_qnt, self.cb1.get()))

                            self.txt.config(state="normal")
                            self.txt.insert(END, "\n  " + str(self.counter))
                            self.amt = float(float(self.q.get()) * float(self.pr.get()))
                            self.txt.insert(END, " " * (4 - len(str(self.counter))) + str(self.cb1.get()))
                            self.txt.insert(END, " " * (16 - (len(self.cb1.get()))) + self.q.get())
                            self.txt.insert(END, " " * (17 - (len(self.q.get()))) + self.pr.get())
                            self.txt.insert(END, " " * (19 - (len(self.pr.get()))) + str(self.amt))
                            sr_no = str(self.counter)
                            item = str(self.cb1.get())
                            quantity = self.q.get()
                            price = self.pr.get()
                            amount = str(self.amt)
                            self.products.append((sr_no,item,quantity,price,amount))
                            
                            self.cb1.set("Select")
                            self.t.set("0")
                            self.pr.set("0")
                            self.a_q.set("0")
                            self.q.set("0")
                            self.ttl = self.ttl + self.amt
                            self.txt.insert(END, "\n\n" + "=" * 28 + " Total = " + str(round(self.ttl, 2)) + "=" * 26)
                            self.counter = self.counter + 1
                            self.cb1.focus_set()
                            self.txt.config(state="disabled")
                            self.cancel_counter = True



                    except:

                        messagebox.showerror("Billing Software", "Quantity must be Positive Number.", parent=self)
                        self.q.set('')
                        self.qnt.focus_set()

                except:

                    messagebox.showinfo("Billing Software", "Please Enter Details Of Product First.", parent=self)
                    self.cb1.focus_set()
            else:
                try:
                    if self.cb1.get() == "Select":
                        raise AttributeError
                    try:
                        float(self.q.get())
                        if float(self.q.get()) <= 0:
                            raise AttributeError

                        query = """select quantity from product where name= (?)"""
                        self.available_qnt = self.db1.execute(query, (self.cb1.get(),)).fetchone()
                        self.update_qnt = int(self.available_qnt[0]) - int(self.q.get())

                        if int(self.update_qnt) < 0:

                            messagebox.showwarning("Billing Software","In-sufficient Stock of '{}'".format(self.cb1.get()),parent=self)
                            self.q.set("")
                            self.qnt.focus_set()
                        else:

                            query = """update product set quantity = (?) where name= (?)"""

                            self.db1.execute(query, (self.update_qnt, self.cb1.get()))



                            self.txt.config(state="normal")
                            self.txt.delete("end-1l", "end")
                            self.txt.insert(END, "  " + str(self.counter))
                            self.amt = float(float(self.q.get()) * float(self.pr.get()))
                            self.txt.insert(END, " " * (4 - len(str(self.counter))) + str(self.cb1.get()))
                            self.txt.insert(END, " " * (16 - (len(self.cb1.get()))) + self.q.get())
                            self.txt.insert(END, " " * (17 - (len(self.q.get()))) + self.pr.get())
                            self.txt.insert(END, " " * (19 - (len(self.pr.get()))) + str(self.amt))
                            sr_no = str(self.counter)
                            item = str(self.cb1.get())
                            quantity = self.q.get()
                            price = self.pr.get()
                            amount = str(self.amt)
                            self.products.append((sr_no, item, quantity, price, amount))
                           
                            self.cb1.set("Select")
                            self.t.set("0")
                            self.pr.set("0")
                            self.a_q.set("0")
                            self.q.set("0")
                            self.ttl = self.ttl + self.amt
                            self.txt.insert(END, "\n\n" + "=" * 28 + " Total = " + str(round(self.ttl, 2)) + "=" * 26)
                            self.counter = self.counter + 1
                            self.cb1.focus_set()
                            self.txt.config(state="disabled")
                            self.cancel_counter = True



                    except:

                        messagebox.showerror("Billing Software", "Quantity must be Positive Number.", parent=self)
                        self.q.set('')
                        self.qnt.focus_set()

                except:

                    messagebox.showinfo("Billing Software", "Please Enter Details Of Product First.", parent=self)

                    self.cb1.focus_set()

    def reset(self,event=""):

        if self.cancel_counter == True:

            self.db1.rollback()


        self.cb1.set("Select")
        self.t.set("0")
        self.cn.set("")
        self.pr.set("0")
        self.a_q.set("0")
        self.q.set("0")
        self.bid.config(state="normal")
        self.bi.set(self.b)
        self.bid.config(state="disabled")
        self.amt=0
        self.ttl=0
        self.counter=0
        self.update_qnt = 0
        self.cancel_counter = False
        self.txt.config(state="normal")
        self.c_name.config(state="normal")

        self.txt.delete(1.0,END)

        self.txt.insert(END, "\n")
        self.txt.insert(END, "\t\t\tP & H Billing Software")
        self.txt.insert(END, "\n\t\t\t=======================")
        self.txt.insert(END, "\nDate : " + time.strftime("%d - %m - %y"))
        self.txt.insert(END, "\nTime : " + time.strftime("%H : %M : %S"))
        self.txt.insert(END, "\nCreated by : " + self.creator[0])
        self.txt.insert(END, "\nBill ID : " + str(self.bid.get()))
        self.txt.insert(END, "\n" + "=" * 67)
        self.txt.insert(END, "\nSr No.\tProduct\t  Quantity            Price              Amount")
        self.txt.insert(END, "\n" + "=" * 67)
        self.txt.config(state="disabled")
        self.c_name.focus_set()
        self.products.clear()

    def pre_designed(self,pdf):
        pdf.setTitle("Invoice")
        pdf.setPageSize((600, 900))
        # logo="logo.jpeg"
        # pdf.drawInlineImage(logo,190,253)
        timedate = time.asctime()
        date = timedate[4:8] + timedate[8:10] + ", " + timedate[20:24] + "."
        c_time = " " + timedate[11:20]
        pdf.line(30, 820, 350, 820)
        pdf.setFontSize(20)
        pdf.drawString(30, 800, "Company Name")
        pdf.setFontSize(11)
        pdf.drawString(30, 785, "Address Line 1,")
        pdf.drawString(30, 770, "Address Line 2")
        pdf.drawString(30, 755, "Phone: ")

        pdf.line(30, 750, 350, 750)

        pdf.drawString(30, 735, "Invoice Number: "+str(self.bid.get()))
        pdf.drawString(30, 720, "Customer Name: "+str(self.c_name.get()))
        pdf.drawString(30, 705, "Created by: " + self.creator[0])
        pdf.drawString(30, 690, "Date: " + date)

        qr = qrcode.QRCode(
            version=1,
            box_size=2,
            border=2
        )

        data = 'InvoiceNumber:'+ str(self.bid.get()) + '\nTime:'+ str(c_time) + "\nShop Owner" + "\nShop Web-Site\n1 : Sold items can't be return accepted or changed.\n2:Warranty is provided by respective Service Center.\n3 : Other Terms & Conditions.\nTHANK YOU\nBE CONNECTED WITH US."
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        pdf.drawInlineImage(img, 400, 685)
        # ===================================================================================================
        pdf.line(30, 680, 550, 680)

        pdf.drawString(30, 668, "Sr.No.")
        pdf.drawString(75, 668, "            Product Name")

        pdf.drawString(320, 668, "     Quantity")

        pdf.drawString(400, 668, "      Price")
        pdf.drawString(490, 668, "Amount")

        pdf.line(30, 662, 550, 662)
        pdf.line(73, 680, 73, 150)

        pdf.line(318, 680, 318, 150)

        pdf.line(398, 680, 398, 150)
        pdf.line(468, 680, 468, 150)
        pdf.line(30, 150, 550, 150)
        # ===============================================================================================
        

    def pdfgenerate(self):
        c_date_pdfname = time.strftime("%d_%m_%y")
        pdf = canvas.Canvas("C:\\MyShopBills\\" + "Bill(" + self.bid.get() +")"+ str(c_date_pdfname) + ".pdf")
        self.pre_designed(pdf)
        y= 650
        pdf.setFontSize(10)
        for i in self.products:
            if y<50:
                pdf.showPage()
                y = 840
                pdf.setFontSize(11)
                pdf.line(30, 880, 550, 880)
                pdf.line(30, 860, 550, 860)
                pdf.drawString(30, 863, "Sr.No.")
                pdf.drawString(75, 863, "            Product Name")
                pdf.drawString(320, 863, "     Quantity")
                pdf.drawString(400, 863, "      Price")
                pdf.drawString(490, 863, "Amount")
                pdf.line(73, 880, 73, 150)
                pdf.line(318, 880, 318, 150)
                pdf.line(398, 880, 398, 150)
                pdf.line(468, 880, 468, 150)
                pdf.line(30, 149, 550, 149)
                pdf.setFontSize(10)
                
            pdf.drawString(35,y,str(i[0]))
            pdf.drawString(80,y,str(i[1]))
            pdf.drawString(350,y,str(i[2]))
            pdf.drawString(422,y,str(i[3]))
            pdf.drawString(500,y,str(i[4]))
            y = y-15
        if y > 150:
            pdf.drawString(30, 135, "Total Discount: 0")
            pdf.drawString(30, 120, "Gross Total(Discount Included): 0")
            pdf.drawString(30, 105, "Tax: 0")
            pdf.line(30, 100, 550, 100)
            pdf.setFontSize(13)
            pdf.drawString(30, 65, "Grand Total: " + str(round(self.ttl, 2)))
            pdf.setFontSize(11)
            pdf.drawString(400, 50, "Authorized Signatory")
            pdf.setFontSize(7)
            pdf.drawString(15, 15, "Scan QR code for Applied Terms & Conditions.")
        else:
            pdf.showPage()
            pdf.drawString(30, 800, "Total Discount: 0")
            pdf.drawString(30, 785, "Gross Total(Discount Included): 0")
            pdf.drawString(30, 770, "Tax: 0")
            pdf.line(30, 740, 550, 740)
            pdf.setFontSize(13)
            pdf.drawString(30, 720, "Grand Total: " + str(round(self.ttl, 2)))
            pdf.setFontSize(11)
            pdf.drawString(400, 700, "Authorized Signatory")
            pdf.setFontSize(7)
            pdf.drawString(15, 15, "Scan QR code for Applied Terms & Conditions.")

        pdf.save()
        webbrowser.open("C:\\MyShopBills\\" + "Bill(" + self.bid.get() +")"+ str(c_date_pdfname) + ".pdf")




    def gen(self,event=""):
        try:
            if self.counter == 0:
                raise AttributeError
            m = messagebox.askyesnocancel("Billing Software", "Are you want to Generate the Bill?", parent=self)

            if m== True:
                try:
                    data = self.txt.get(1.0, END)
                    query = """insert into Bill(CNAME,TOTAL,CFILE) values (?,?,?)"""
                    if self.cancel_counter == True:
                        self.db.execute(query, (self.c_name.get(), self.ttl, data))
                    else:
                        messagebox.showerror("Billing Software","You have not Inserted anything yet !")
                        return
                    self.db.commit()
                    self.db1.commit()
                    self.b = self.b + 1
                    messagebox.showinfo("Billing Software","Bill of '{}' is Saved Successfully in your Database!".format(self.c_name.get()), parent=self)
                    x = messagebox.askyesno("Billing Software","Are you want to save Bill as a PDF ?", parent=self)
                    if x>0:
                        self.pdfgenerate()
                        messagebox.showinfo("Billing Software", "Your PDF File is Generated Successfully!", parent=self)
                    self.cancel_counter = False
                    self.reset()

                except:
                    messagebox.showerror("Billing Software", "Your Operation is Unsuccessfull ! ", parent=self)
                    messagebox.showinfo("Billing Software", "Try Again !", parent=self)
            elif m == False:
                self.db1.rollback()
                self.reset()
                return
            else:
                self.cancel_counter = True

                return
        except:
            messagebox.showerror("Billing Software", "You Don't have entered Customer Name.", parent=self)
            self.c_name.focus_set()




    def watch(self,event=""):


        self.reset()
        self.withdraw()
        new_window = Edit_Window(self,self.main_root)
        self.mainloop()