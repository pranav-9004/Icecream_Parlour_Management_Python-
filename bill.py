from ctypes.wintypes import SIZE
from tkinter import*
from tkinter.ttk import Labelframe
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry
import random,os
import tempfile


class Bill:
    def __init__(self,root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1295x550+230+230")

    #=====Title====
        lbl_title = Label(self.root,text="BILL DETAILS", font=("Mongolian Baiti",18, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

    #====variables====
        self.var_billid = StringVar()
        z = random.randint(1000,9999)
        self.var_billid.set(z)
        self.var_cmobile = StringVar()
        self.var_cname = StringVar()
        self.var_date = StringVar()
        self.var_flav = StringVar()
        self.var_cont = StringVar()
        self.var_wgt = IntVar()
        self.var_icwgt = IntVar()
        self.var_contprice = IntVar()
        self.var_quan = IntVar()
        self.var_price = IntVar()
        self.var_subtotal = StringVar()
        self.var_tax = StringVar()
        self.var_total = StringVar()

    #=====Label Frame===
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Icecream Details", padx=2, font=("Mongolian Baiti",11, "bold"))
        labelframeleft.place(x=5, y=50, width=435, height=500)

    #=====bill id====
        lbl_billid = Label(labelframeleft, text="Bill Id:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_billid.grid(row=1, column=0, sticky=W)

        txtbillid = ttk.Entry(labelframeleft, textvariable=self.var_billid, width=24, font=("times of roman",11, "bold"))
        txtbillid.grid(row=1, column=1)

    #=====phone no====
        lbl_custmobile = Label(labelframeleft, text="CMobile No:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_custmobile.grid(row=2, column=0, sticky=W)

        txtcustmobile = ttk.Entry(labelframeleft, textvariable=self.var_cmobile, width=24, font=("times of roman",11, "bold"))
        txtcustmobile.grid(row=2, column=1)

        #======fetch cust name===
        btnFetchcust = Button(labelframeleft,  text="FetchData", command=self.lookupCustomer,  font=("times of roman",8 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=10)
        btnFetchcust.grid(row=2, column=2,  padx=10, pady=6)

    #======cname====
        lbl_cname = Label(labelframeleft, text="CName:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_cname.grid(row=3, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cname,  width=24, font=("times of roman",11, "bold"))
        txtcname.grid(row=3, column=1)

        

    
    #======date====
        lbl_date = Label(labelframeleft, text="Date:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_date.grid(row=4, column=0, sticky=W)

        txtdate = DateEntry(labelframeleft, selectmode="day", textvariable=self.var_date, width=22, font=("times of roman",11 ,"bold"))
        txtdate.grid(row=4, column=1)

        #======show data===
        btnShowData = Button(labelframeleft,  text="ShowData", command=self.welcome, font=("times of roman",8 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=10)
        btnShowData.grid(row=4, column=2,  padx=10, pady=6)

    
    #======flavour====
        lbl_flav = Label(labelframeleft, text="Flavour:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_flav.grid(row=5, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        options = []
        my_cursor.execute("select flavour from stock")
        rows=my_cursor.fetchall()
        


        ic_flav = ttk.Combobox(labelframeleft, textvariable=self.var_flav, width=22, font=("times of roman",11),state='readonly',justify=CENTER)
        ic_flav['values']=rows
        ic_flav.current(0)
        ic_flav.grid(row=5, column=1, pady=5, padx=2)
        ic_flav.bind("<<ComboboxSelected>>", self.lookUpPrice)

        #======fetch price===
        #btnFetchprice = Button(labelframeleft,  text="FetchPrice",  font=("times of roman",8 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=10)
        #btnFetchprice.grid(row=5, column=2,  padx=10, pady=6)
        
    #======container====
        lbl_cont = Label(labelframeleft, text="Container:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_cont.grid(row=6, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        options = []
        my_cursor.execute("select shortform from container")
        rows=my_cursor.fetchall()
        


        ic_cont = ttk.Combobox(labelframeleft, textvariable=self.var_cont, width=22, font=("times of roman",11),state='readonly',justify=CENTER)
        ic_cont['values']=rows
        ic_cont.current(0)
        ic_cont.grid(row=6, column=1, pady=5, padx=2)
        ic_cont.bind("<<ComboboxSelected>>", self.lookUpCont)
        
     
        
        
        
    #=======cont price====
        lbl_price = Label(labelframeleft, text="Cont Price:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_price.grid(row=8, column=0, sticky=W)

        txtprice = ttk.Entry(labelframeleft, textvariable=self.var_contprice, width=24, font=("times of roman",11, "bold"))
        txtprice.grid(row=8, column=1)
        
    #=======Cont weight====
        lbl_icwgt = Label(labelframeleft, text="Cont Weight:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_icwgt.grid(row=9, column=0, sticky=W)

        txticwgt = ttk.Entry(labelframeleft, textvariable=self.var_icwgt, width=24, font=("times of roman",11, "bold"))
        txticwgt.grid(row=9, column=1)
        
    #=======price====
        lbl_price = Label(labelframeleft, text="Price:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_price.grid(row=10, column=0, sticky=W)

        txtprice = ttk.Entry(labelframeleft, textvariable=self.var_price, width=24, font=("times of roman",11, "bold"))
        txtprice.grid(row=10, column=1)

    #========quantity======
        lbl_quantity = Label(labelframeleft, text="Quantity:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_quantity.grid(row=11, column=0, sticky=W)

        txtquantity = ttk.Entry(labelframeleft, textvariable=self.var_quan, width=24, font=("times of roman",11, "bold"))
        txtquantity.grid(row=11, column=1)

    #=======subtotal=====
        lbl_subtotal = Label(labelframeleft, text="Sub Total:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_subtotal.grid(row=12, column=0, sticky=W)

        txtsubtotal = ttk.Entry(labelframeleft, textvariable=self.var_subtotal,  width=24, font=("times of roman",11, "bold"))
        txtsubtotal.grid(row=12, column=1)

    #=======govtax=====
        lbl_govtax = Label(labelframeleft, text="Gov Tax:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_govtax.grid(row=13, column=0, sticky=W)

        txtgovtax = ttk.Entry(labelframeleft, textvariable=self.var_tax,  width=24, font=("times of roman",11, "bold"))
        txtgovtax.grid(row=13, column=1)

    #=======totalprice====
        lbl_total = Label(labelframeleft, text="Total Price:", font=("times of roman",10, "bold"), padx=2, pady=6)
        lbl_total.grid(row=14, column=0, sticky=W)

        txttotal = ttk.Entry(labelframeleft, textvariable=self.var_total,  width=24, font=("times of roman",11, "bold"))
        txttotal.grid(row=14, column=1)

    #======Reset Button=====
        #btnReset = Button(labelframeleft, text="Reset", command=self.reset,  font=("times of roman",11 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=9)
        #btnReset.place(x=90, y=445)

    #======Add Data Button=====
        #btnClear = Button(labelframeleft, text="Clear", command=self.clear,  font=("times of roman",11 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=9)
        #btnClear.place(x=200, y=445)

    #=====btns======
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=435, width=425, height=38)

        btnAddc = Button(btn_frame, text="Add", command=self.addIcecream, font=("times of roman",12 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=5)
        btnAddc.grid(row=0, column=0, padx=2)

        btngenetrate = Button(btn_frame, text="Generate", command=self.genBill, font=("times of roman",12 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=7)
        btngenetrate.grid(row=0, column=1, padx=2)

        btnsave = Button(btn_frame, text="Save",command=self.saveBill, font=("times of roman",12 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=5)
        btnsave.grid(row=0, column=2, padx=2)

        btnprint = Button(btn_frame, text="Print", command=self.print, font=("times of roman",12 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=6)
        btnprint.grid(row=0, column=3, padx=2)
        
        btnprint = Button(btn_frame, text="Reset", command=self.reset, font=("times of roman",12 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=5)
        btnprint.grid(row=0, column=4, padx=2)
        
        btnprint = Button(btn_frame, text="Clear", command=self.clear, font=("times of roman",12 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=6)
        btnprint.grid(row=0, column=5, padx=2)
       

    

    #=====right frame=====
        rightframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Bill Details", padx=2, font=("Mongolian Baiti",10, "bold"))
        rightframe.place(x=445, y=50, width=530, height=490)

        scroll_y = Scrollbar(rightframe, orient=VERTICAL)
        self.textarea = Text(rightframe,yscrollcommand=scroll_y.set,  bg="white",fg="blue",font=("Mongolian Baiti",11, "bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
    
    #=====image frame=====
        imageframe = LabelFrame(self.root, bd=2, relief=RIDGE,  padx=2, font=("Mongolian Baiti",10, "bold"))
        imageframe.place(x=975, y=50, width=320, height=490)

        img1 = Image.open(r"images\bill1.jpg")
        img1 = img1.resize((320,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=975, y=50, width=320, height=150)

        img2 = Image.open(r"images\bill2.png")
        img2 = img2.resize((320,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=975, y=200, width=320, height=150)

        img3 = Image.open(r"images\bill3.jpg")
        img3 = img3.resize((320,200),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=975, y=350, width=320, height=200)

        self.l = []

    #==========Bill Details======
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\tHILLTOP ICECREAM PARLOUR")
        self.textarea.insert(END,f"\n\n Bill Number:{self.var_billid.get()}")
        self.textarea.insert(END,f"\n Cust_Name:{self.var_cname.get()}")
        self.textarea.insert(END,f"\n Cust_Phoneno:{self.var_cmobile.get()}")
        self.textarea.insert(END,f"\n Date:{self.var_date.get()}")

        self.textarea.insert(END,"\n=======================================================")
        self.textarea.insert(END,f"\n Flavours\t\tQty\tCont\tPrice")
        self.textarea.insert(END,"\n=======================================================")

    #=========Add to Cart======
    def addIcecream(self):
        Tax = 1
        self.n = self.var_price.get()
        self.cp = self.var_contprice.get()
        self.m = self.var_quan.get()
        self.t = (self.n + self.cp)*self.m
        self.f = self.var_flav.get()
        self.c = self.var_cont.get()
        self.q = self.var_quan.get()
        self.l.append(self.t)
        if self.var_price.get()=="0":
            messagebox.showerror("Error","Please select any flavour")
        else:
            self.textarea.insert(END,f" \n{self.f}\t\t{self.q}\t{self.c}\t{self.t}")
            self.var_subtotal.set(str('Rs.%.2f'%(sum(self.l))))
            self.var_tax.set(str('Rs.%.2f'%((((sum(self.l)) -(self.var_price.get()))*Tax)/100)))
            self.var_total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.var_price.get()))*Tax)/100)))))

        if self.var_date.get()=="" or self.var_cname.get()=="" or self.var_cmobile.get()=="":
            messagebox.showerror("Error","All feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into report values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_billid.get(),self.var_cmobile.get(),self.var_cname.get(),self.var_date.get(),self.var_flav.get(),self.var_cont.get(),self.var_icwgt.get(),self.var_quan.get(),self.var_total.get() ))
                
                #==============Update Stock===========
                self.quantity = self.var_quan.get()
                self.up = self.var_icwgt.get()
                self.finup = self.up * self.quantity
                self.fl = self.var_flav.get()
                my_cursor.execute("update stock set wt = wt - %s where flavour = %s",(self.finup,self.fl))
                
                my_cursor.execute("delete from stock where wt <= 0")
                
                conn.commit()
                #self.fetchcust_data()
                conn.close()
                messagebox.showinfo("Sucess","Data has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)
                
            

    #==========Generate Bill======
    def genBill(self):
        if self.var_price.get()=="0":
           messagebox.showerror("Error","Please Add To Cart")
        else:
            self.s = self.var_subtotal.get()
            self.t = self.var_tax.get()
            self.tot = self.var_total.get()
            text = self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n=======================================================")
            self.textarea.insert(END,f"\n Sub Amount:\t{self.s}")
            self.textarea.insert(END,f"\n Gov Tax:\t{self.t}")
            self.textarea.insert(END,f"\n Total Price:\t{self.tot}")
            self.textarea.insert(END,"\n=======================================================")

    #=============Save Bill=======
    def saveBill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill",parent=self.root)
        if op>0:
            self.b = self.var_billid.get()
            self.bill_data = self.textarea.get(1.0,END)
            f1 = open(r'C:\Users\HP\OneDrive\Documents\Icecream Parlour Management System\Main System\bills/'+str(self.b)+".txt",'w')
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved",f"Bill_ID:{self.b} saved sucessfully",parent=self.root)
            f1.close()

    #=============Reset===========
    def reset(self):
        z = random.randint(1000,9999)
        self.var_billid.set(z),
        self.var_cmobile.set(""),
        self.var_cname.set(""),
        self.var_date.set(""),
        self.var_flav.set(""),
        self.var_price.set("0"),
        self.var_cont.set(""),
        self.var_contprice.set("0"),
        self.var_quan.set("0"),
        self.var_subtotal.set("Rs.0"),
        self.var_tax.set("Rs.0"),
        self.var_total.set("Rs.0")

    #===========print=============
    def print(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
        
    #==========clear==============
    def clear(self):
        self.textarea.delete(1.0,END)

    
    
        



     



    #======Fetch Name====
    def lookupCustomer(self):
        if self.var_cmobile.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            #=======CustName======
            global myresult
            value = self.var_cmobile.get()
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            try: 
                my_cursor.execute("SELECT * FROM customer where mobile = '" + value + "'")
                myresult = my_cursor.fetchall()
                for x in myresult:
                    self.var_cname.set(x[1])
            
            except Exception as e:
                print(e)
                
                conn.commit()
                conn.close()
            

    #=======Fetch Price=====
    def lookUpPrice(self,event=""):
        option= self.var_flav.get()
        
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        query = "SELECT * FROM STOCK WHERE flavour = %s"
        my_cursor.execute(query, (option,))
        rows = my_cursor.fetchall()
        #print(rows)
        for i in rows:
            self.var_price.set(i[4])
            self.var_quan.set(1)
            
    #=======Fetch Container Price=====
    def lookUpCont(self,event=""):
        option= self.var_cont.get()
        
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        query = "SELECT * FROM CONTAINER WHERE shortform = %s"
        my_cursor.execute(query, (option,))
        rows = my_cursor.fetchall()
        #print(rows)
        for i in rows:
            self.var_contprice.set(i[4])
            self.var_icwgt.set(i[3])

            
          











       










        

if __name__ == "__main__":
    root = Tk()
    obj = Bill(root)
    root.mainloop()