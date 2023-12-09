from tkinter import*
from tkinter.ttk import Labelframe
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random

class Customer:
    def __init__(self,root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1295x550+230+230")

    #=====Title====
        lbl_title = Label(self.root,text="CUSTOMER DETAILS", font=("Mongolian Baiti",18, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

    #=====variables=====
        self.var_custid = StringVar()
        z = random.randint(1000,9999)
        self.var_custid.set(z)
        self.var_name = StringVar()
        self.var_mobile = StringVar()

    #=====Label Frame===
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", padx=2, font=("Mongolian Baiti",12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

    #=====Labels and Entries====
        #=====id====
        lbl_cust_id = Label(labelframeleft, text="Customer Id:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=0, column=0, sticky=W)

        enty_custid = ttk.Entry(labelframeleft,  textvariable=self.var_custid, width=29, font=("times of roman",13, "bold"))
        enty_custid.grid(row=0, column=1)

        #=====name====
        lbl_name = Label(labelframeleft, text="Customer Name:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_name.grid(row=1, column=0, sticky=W)

        txtname = ttk.Entry(labelframeleft, width=29,  textvariable=self.var_name, font=("times of roman",13, "bold"))
        txtname.grid(row=1, column=1)

        #=====phone no====
        lbl_mobile = Label(labelframeleft, text="Mobile No:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=2, column=0, sticky=W)

        txtmobile = ttk.Entry(labelframeleft,  textvariable=self.var_mobile, width=29, font=("times of roman",13, "bold"))
        txtmobile.grid(row=2, column=1)

        

        #=====btns======
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=130, width=425, height=38)

        btnAdd = Button(btn_frame, text="Add", command=self.addcust_data, font=("times of roman",13 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=9)
        btnAdd.grid(row=0, column=0, padx=3)

        btnUpdate = Button(btn_frame, text="Update", command=self.updatecust_data, font=("times of roman",13 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=9)
        btnUpdate.grid(row=0, column=1, padx=3)

        btnDelete = Button(btn_frame, text="Delete", command=self.delcust_data, font=("times of roman",13 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=9)
        btnDelete.grid(row=0, column=2, padx=3)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("times of roman",13 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=9)
        btnReset.grid(row=0, column=3, padx=3)

        #=====table frame=====
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", padx=2, font=("Mongolian Baiti",12, "bold"))
        tableframe.place(x=435, y=50, width=860, height=490)

        #=====search box=======
        lblSearchBy = Label(tableframe, text="Search By:", font=("times of roman",12, "bold"), bg="#737373", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, pady=5, padx=2)

        self.var_search = StringVar()
        ic_wt = ttk.Combobox(tableframe, width=24, textvariable=self.var_search, font=("times of roman",13),state='readonly',justify=CENTER)
        ic_wt['values']=("custid","name")
        ic_wt.current(1)
        ic_wt.grid(row=0, column=1, pady=5, padx=2)

        self.var_txtsearch = StringVar()
        txtsearch = ttk.Entry(tableframe, width=24, textvariable=self.var_txtsearch, font=("times of roman",13, "bold"))
        txtsearch.grid(row=0, column=2, pady=5, padx=2)

        btnSearch = Button(tableframe, text="Search", command=self.searchcust_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(tableframe, text="Show All", command=self.fetchcust_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        btnResetSearch = Button(tableframe, text="Reset", command=self.reset_search, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnResetSearch.grid(row=0, column=5, padx=1)

        #======show all data====
        tablecustdetails = Frame(tableframe, bd=2, relief=RIDGE)
        tablecustdetails.place(x=0, y=50, width=850, height=415)
        
        scroll_y=ttk.Scrollbar(tablecustdetails,orient=VERTICAL)
        
        self.Cust_Table = ttk.Treeview(tablecustdetails, column=("custid", "name", "mobile"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.Cust_Table.yview)
        
        self.Cust_Table.heading("custid", text="Id")
        self.Cust_Table.heading("name", text="Name")
        self.Cust_Table.heading("mobile", text="Mobile No.")
        

        self.Cust_Table["show"]="headings"
        self.Cust_Table.pack(fill=BOTH, expand=1)
        self.Cust_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetchcust_data()
        
    def addcust_data(self):
        if self.var_custid.get()=="" or self.var_name.get()=="" or self.var_mobile.get()=="":
            messagebox.showerror("Error","All feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s)",(self.var_custid.get(),self.var_name.get(),self.var_mobile.get()))
                conn.commit()
                self.fetchcust_data()
                conn.close()
                messagebox.showinfo("Sucess","Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetchcust_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Table.delete(*self.Cust_Table.get_children())
            for i in rows:
                self.Cust_Table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cuersor(self,event=""):
        cusrsor_row = self.Cust_Table.focus()
        content = self.Cust_Table.item(cusrsor_row)
        row = content["values"]

        self.var_custid.set(row[0]),
        self.var_name.set(row[1]),
        self.var_mobile.set(row[2])

    def updatecust_data(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter Mobile Number",parent = self.root)
        else:    
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set name=%s,mobile=%s where custid=%s",(self.var_name.get(),self.var_mobile.get(),self.var_custid.get()))
            conn.commit()
            self.fetchcust_data()
            conn.close()
            messagebox.showinfo("Update","Stock details has been updated successfully", parent = self.root)

    def delcust_data(self):
        del_data = messagebox.askyesno("Icecream Management System","Do you want to delete this customer detail",parent=self.root)
        if del_data>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            query = "delete from customer where custid=%s"
            values = (self.var_custid.get(),)
            my_cursor.execute(query,values)
        else:
            if not del_data:
                return
        conn.commit()
        self.fetchcust_data()
        conn.close()

    def reset(self):
        z = random.randint(1000,9999)
        self.var_custid.set(z),
        self.var_name.set(""),
        self.var_mobile.set("")
        
    def reset_search(self):
        self.var_search.set("name")
        self.var_txtsearch.set("") 

    def searchcust_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.var_search.get())+" LIKE '%"+str(self.var_txtsearch.get())+"%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Table.delete(*self.Cust_Table.get_children())
            for i in rows:
                self.Cust_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

        

    
        




if __name__ == "__main__":
    root = Tk()
    obj = Customer(root)
    root.mainloop()