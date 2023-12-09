from tkinter import*
from tkinter.ttk import Labelframe
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random

class Report:
    def __init__(self,root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1295x550+230+230")

    #=====Title====
        lbl_title = Label(self.root,text="REPORT DETAILS", font=("Mongolian Baiti",18, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

    #=====table frame=====
        tableframe1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="Stock Report", padx=2, font=("Mongolian Baiti",12, "bold"))
        tableframe1.place(x=5, y=50, width=1060, height=230)
        
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Order Report", padx=2, font=("Mongolian Baiti",12, "bold"))
        tableframe.place(x=5, y=290, width=1060, height=230)

        #=====search box=======
        lblSearchBy = Label(tableframe, text="Search By:", font=("times of roman",12, "bold"), bg="#737373", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, pady=5, padx=2)

        self.var_search = StringVar()
        ic_wt = ttk.Combobox(tableframe, width=24, textvariable=self.var_search, font=("times of roman",13),state='readonly',justify=CENTER)
        ic_wt['values']=("billid","flavour","date","name","container")
        ic_wt.current(2)
        ic_wt.grid(row=0, column=1, pady=5, padx=2)

        self.var_txtsearch = StringVar()
        txtsearch = ttk.Entry(tableframe, width=24, textvariable=self.var_txtsearch, font=("times of roman",13, "bold"))
        txtsearch.grid(row=0, column=2, pady=5, padx=2)

        btnSearch = Button(tableframe, text="Search", command=self.searchrep_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(tableframe, text="Show All", command=self.fetch_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        btnReset = Button(tableframe, text="Reset", command=self.reset_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnReset.grid(row=0, column=5, padx=1)
        
       

        #======show all data====
        tablerepdetails = Frame(tableframe, bd=2, relief=RIDGE)
        tablerepdetails.place(x=0, y=50, width=1050, height=150)

       
        scroll_y=ttk.Scrollbar(tablerepdetails,orient=VERTICAL)

        self.Rep_Table = ttk.Treeview(tablerepdetails, column=("srno","billid", "mobile", "name", "date", "flavour","container","icweight","quan", "price"),yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.Rep_Table.yview)

        self.Rep_Table.heading("srno", text="Srno")
        self.Rep_Table.heading("billid", text="BillId")
        self.Rep_Table.heading("mobile", text="Mobile")
        self.Rep_Table.heading("name", text="Name")
        self.Rep_Table.heading("date", text="Date")
        self.Rep_Table.heading("flavour", text="Flavour")
        self.Rep_Table.heading("container", text="Container")
        self.Rep_Table.heading("icweight", text="Weight")
        self.Rep_Table.heading("quan",text="Qty")
        self.Rep_Table.heading("price", text="Price")
        
        self.Rep_Table["show"]="headings"
        self.Rep_Table.column("srno",width=50)
        self.Rep_Table.column("billid",width=100)
        self.Rep_Table.column("mobile",width=100)
        self.Rep_Table.column("name",width=100)
        self.Rep_Table.column("date",width=100)
        self.Rep_Table.column("flavour",width=150)
        self.Rep_Table.column("container",width=100)
        self.Rep_Table.column("icweight",width=50)
        self.Rep_Table.column("quan",width=50)
        self.Rep_Table.column("price",width=100)
        self.Rep_Table.pack(fill=BOTH, expand=1)
        self.Rep_Table.bind("<ButtonRelease-1>")
        self.fetch_data()

    #=====image frame=====
        imageframe = LabelFrame(self.root, bd=2, relief=RIDGE,  padx=2, font=("Mongolian Baiti",12, "bold"))
        imageframe.place(x=1070, y=50, width=222, height=490)

        img1 = Image.open(r"images\rep1.jpg")
        img1 = img1.resize((222,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=1070, y=50, width=222, height=150)

        img2 = Image.open(r"images\rep2.jpg")
        img2 = img2.resize((222,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=1070, y=200, width=222, height=150)

        img3 = Image.open(r"images\rep3.jpg")
        img3 = img3.resize((222,222),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=1070, y=350, width=222, height=195)
        
        
        #=====search box for stock=======
        lblSearchBy = Label(tableframe1, text="Search By:", font=("times of roman",12, "bold"), bg="#737373", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, pady=5, padx=2)

        self.var_searchstock = StringVar()
        ic_wt = ttk.Combobox(tableframe1, width=24, textvariable=self.var_searchstock, font=("times of roman",13),state='readonly',justify=CENTER)
        ic_wt['values']=("date","id","flavour")
        ic_wt.current(2)
        ic_wt.grid(row=0, column=1, pady=5, padx=2)

        self.var_txtsearchstock = StringVar()
        txtsearch = ttk.Entry(tableframe1, width=24, textvariable=self.var_txtsearchstock, font=("times of roman",13, "bold"))
        txtsearch.grid(row=0, column=2, pady=5, padx=2)

        btnSearch = Button(tableframe1, text="Search", command=self.searchstock_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(tableframe1, text="Show All", command=self.stockfetch_data,  font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        btnReset = Button(tableframe1, text="Reset", command=self.resetstock_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnReset.grid(row=0, column=5, padx=1)
        
        #======show all data for stock====
        tablestockdetails = Frame(tableframe1, bd=2, relief=RIDGE)
        tablestockdetails.place(x=0, y=50, width=1050, height=150)

       
        scroll_y=ttk.Scrollbar(tablestockdetails,orient=VERTICAL)

        self.Stock_Table = ttk.Treeview(tablestockdetails, column=("srno","id","flavour", "date", "wt", "price"),yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_y.config(command=self.Stock_Table.yview)

        self.Stock_Table.heading("srno", text="Srno")
        self.Stock_Table.heading("id", text="Id")
        self.Stock_Table.heading("flavour", text="Flavour")
        self.Stock_Table.heading("date", text="Date")
        self.Stock_Table.heading("wt", text="Weight")
        self.Stock_Table.heading("price", text="Price")
        
       
        self.Stock_Table["show"]="headings"
        self.Stock_Table.column("srno",width=50)
        self.Stock_Table.column("id",width=50)
        self.Stock_Table.column("flavour",width=100)
        self.Stock_Table.column("date",width=100)
        self.Stock_Table.column("wt",width=50)
        self.Stock_Table.column("price",width=50)
        self.Stock_Table.pack(fill=BOTH, expand=1)
        self.Stock_Table.bind("<ButtonRelease-1>")
        self.stockfetch_data()

    #===============fetch data=====
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from report")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Rep_Table.delete(*self.Rep_Table.get_children())
            for i in rows:
                self.Rep_Table.insert("",END,values=i)
        conn.commit()
        conn.close()

    #============search data====
    def searchrep_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from report where "+str(self.var_search.get())+" LIKE '%"+str(self.var_txtsearch.get())+"%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Rep_Table.delete(*self.Rep_Table.get_children())
            for i in rows:
                self.Rep_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #=============reset=========
    def reset_data(self):
        self.var_search.set("date")
        self.var_txtsearch.set("") 
        
    #=============reset for stock=========
    def resetstock_data(self):
        self.var_searchstock.set("date")
        self.var_txtsearchstock.set("") 
        
        
    #===============fetch data for stock=====
    def stockfetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from stockrep")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for i in rows:
                self.Stock_Table.insert("",END,values=i)
        conn.commit()
        conn.close()
        
     #============search data====
    def searchstock_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from stockrep where "+str(self.var_searchstock.get())+" LIKE '%"+str(self.var_txtsearchstock.get())+"%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for i in rows:
                self.Stock_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
        
        
    
        
   
        
        
     

        
   

        

        




if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()