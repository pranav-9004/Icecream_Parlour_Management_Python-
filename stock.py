from tkinter import*
from tkinter.ttk import Labelframe
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry
import random

class Stock:
    def __init__(self,root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1295x550+230+230")

    #=====variables=====
        self.var_id = StringVar()
        z = random.randint(1000,9999)
        self.var_id.set(z)
        self.var_flav = StringVar()
        self.var_date = StringVar()
        self.var_wt = IntVar()
        self.var_price = IntVar()
        


    #=====Title====
        lbl_title = Label(self.root,text="STOCK DETAILS", font=("Mongolian Baiti",18, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        
    #=====Stock Label Frame===
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Stock Details", padx=2, font=("Mongolian Baiti",12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=480)

    #=====Stock Label====
        #=====id====
        lbl_ice_id = Label(labelframeleft, text="Icecream Id:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_ice_id.grid(row=0, column=0, sticky=W)

        enty_id = ttk.Entry(labelframeleft, width=29, textvariable=self.var_id, font=("times of roman",13, "bold"))
        enty_id.grid(row=0, column=1)

        #=====flavour====
        lbl_flavour = Label(labelframeleft, text="Flavour Name:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_flavour.grid(row=1, column=0, sticky=W)

        txtflavour = ttk.Entry(labelframeleft, width=29, textvariable=self.var_flav, font=("times of roman",13, "bold"))
        txtflavour.grid(row=1, column=1)
        
        #======date====
        lbl_date = Label(labelframeleft, text="Date:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_date.grid(row=2, column=0, sticky=W)

        txtdate = DateEntry(labelframeleft, selectmode="day", textvariable=self.var_date, width=27, font=("times of roman",13 ,"bold"))
        txtdate.grid(row=2, column=1)

        #=====weight====
        lbl_weight = Label(labelframeleft, text="Weight in kgs:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_weight.grid(row=3, column=0, sticky=W)
        
        txtwt = ttk.Entry(labelframeleft, width=29, textvariable=self.var_wt, font=("times of roman",13, "bold"))
        txtwt.grid(row=3, column=1)

        #=====price====
        lbl_price = Label(labelframeleft, text="Price:", font=("times of roman" ,12 ,"bold"), padx=2, pady=6)
        lbl_price.grid(row=4, column=0, sticky=W)

        txtprice = ttk.Entry(labelframeleft, width=29, textvariable=self.var_price, font=("times of roman",13 ,"bold"))
        txtprice.grid(row=4, column=1)

    #=====btns======
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=15, y=200, width=390, height=38)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("times of roman",13 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnAdd.grid(row=0, column=0, padx=3)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("times of roman",13 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnUpdate.grid(row=0, column=1, padx=3)

        btnDelete = Button(btn_frame, text="Delete", command=self.del_data, font=("times of roman",13 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnDelete.grid(row=0, column=2, padx=3)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("times of roman",13 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnReset.grid(row=0, column=3, padx=3)

    #=====table frame=====
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Stock Table", padx=2, font=("Mongolian Baiti",12, "bold"))
        tableframe.place(x=435, y=50, width=850, height=480)

        #=====search box=======
        lblSearchBy = Label(tableframe, text="Search By:", font=("times of roman",12, "bold"), bg="#737373", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, pady=5, padx=2)

        self.var_search = StringVar()
        ic_wt = ttk.Combobox(tableframe, width=24, textvariable=self.var_search, font=("times of roman",13),state='readonly',justify=CENTER)
        ic_wt['values']=("id","flavour")
        ic_wt.current(1)
        ic_wt.grid(row=0, column=1, pady=5, padx=2)

        self.var_txtsearch = StringVar()
        txtsearch = ttk.Entry(tableframe, width=24, textvariable=self.var_txtsearch, font=("times of roman",13, "bold"))
        txtsearch.grid(row=0, column=2, pady=5, padx=2)

        btnSearch = Button(tableframe, text="Search", command=self.search_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(tableframe, text="Show All", command=self.fetch_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        btnResetSearch = Button(tableframe, text="Reset", command=self.reset_search, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnResetSearch.grid(row=0, column=5, padx=1)

        #======show all data====
        tabledetails = Frame(tableframe, bd=2, relief=RIDGE)
        tabledetails.place(x=0, y=50, width=840, height=400)
        
        scroll_y=ttk.Scrollbar(tabledetails,orient=VERTICAL)
        
        self.Stock_Table = ttk.Treeview(tabledetails, column=("id", "flavour","date", "wt", "price"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.Stock_Table.yview)
        
        self.Stock_Table.heading("id", text="Id")
        self.Stock_Table.heading("flavour", text="Flavour")
        self.Stock_Table.heading("date", text="Date")
        self.Stock_Table.heading("wt", text="Weight")
        self.Stock_Table.heading("price", text="Price")

        self.Stock_Table["show"]="headings"
        self.Stock_Table.column("id",width=50)
        self.Stock_Table.column("flavour",width=100)
        self.Stock_Table.column("date",width=100)
        self.Stock_Table.column("wt",width=50)
        self.Stock_Table.column("price",width=50)
        
        self.Stock_Table.pack(fill=BOTH, expand=1)
        self.Stock_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_id.get()=="" or self.var_date.get()=="" or self.var_flav.get()=="" or self.var_price.get()=="" or self.var_wt.get()=="0":
            messagebox.showerror("Error","All feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into stock values(%s,%s,%s,%s,%s)",(self.var_id.get(),self.var_flav.get(),self.var_date.get(),self.var_wt.get(),self.var_price.get()))
                my_cursor.execute("insert into stockrep values(NULL,%s,%s,%s,%s,%s)",(self.var_id.get(),self.var_flav.get(),self.var_date.get(),self.var_wt.get(),self.var_price.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Stock has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from stock")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for i in rows:
                self.Stock_Table.insert("",END,values=i)
        
        conn.commit()
        conn.close()

    def get_cuersor(self,event=""):
        cusrsor_row = self.Stock_Table.focus()
        content = self.Stock_Table.item(cusrsor_row)
        row = content["values"]

        self.var_id.set(row[0]),
        self.var_flav.set(row[1]),
        self.var_date.set(row[2]),
        
        self.var_wt.set(row[3]),
        self.var_price.set(row[4])

    def update_data(self):
        if self.var_price.get()=="":
            messagebox.showerror("Error","Please enter Icecream Id",parent = self.root)
        else:    
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            my_cursor.execute("update stock set flavour=%s, date=%s, wt=%s, price=%s where id=%s",(self.var_flav.get(),self.var_date.get(),self.var_wt.get(),self.var_price.get(),self.var_id.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Stock details has been updated successfully", parent = self.root)

    def del_data(self):
        del_data = messagebox.askyesno("Icecream Management System","Do you want to delete  this stock detail",parent=self.root)
        if del_data>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            query = "delete from stock where id=%s"
            values = (self.var_id.get(),)
            my_cursor.execute(query,values)
        else:
            if not del_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        z = random.randint(1000,9999)
        self.var_id.set(z),
        self.var_flav.set(""),
        self.var_date.set(""),
        self.var_wt.set("0"),
        self.var_price.set("")
        
    def reset_search(self):
        self.var_search.set("flavour")
        self.var_txtsearch.set("")    

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from stock where "+str(self.var_search.get())+" LIKE '%"+str(self.var_txtsearch.get())+"%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Stock_Table.delete(*self.Stock_Table.get_children())
            for i in rows:
                self.Stock_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    

    

   








if __name__ == "__main__":
    root = Tk()
    obj = Stock(root)
    root.mainloop()