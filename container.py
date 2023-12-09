from tkinter import*
from tkinter.ttk import Labelframe
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random

class Container:
    def __init__(self,root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1295x550+230+230")

    #=====variables=====
        self.var_id = StringVar()
        z = random.randint(1000,9999)
        self.var_id.set(z)
        self.var_flav = StringVar()
        self.var_wt = IntVar()
        self.var_price = IntVar()
        self.var_srno = IntVar()
        self.var_cont = StringVar()
        self.var_sf = StringVar()
        self.var_conwt = IntVar()
        self.var_conpri = IntVar()


    #=====Title====
        lbl_title = Label(self.root,text="CONTAINER DETAILS", font=("Mongolian Baiti",18, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        
    #=====Container Label Frame===
        labelframeleft1 = LabelFrame(self.root, bd=2, relief=RIDGE, text="Container Details", padx=2, font=("Mongolian Baiti",12, "bold"))
        labelframeleft1.place(x=5, y=50, width=425, height=480)
        
        #==========Srno==========
        lbl_srcon = Label(labelframeleft1, text="Srno:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_srcon.grid(row=0, column=0, sticky=W)

        enty_srcon = ttk.Entry(labelframeleft1, textvariable=self.var_srno ,width=29,  font=("times of roman",13, "bold"))
        enty_srcon.grid(row=0, column=1)
        
        #==========Container==========
        lbl_cont = Label(labelframeleft1, text="Container:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_cont.grid(row=1, column=0, sticky=W)

        enty_cont = ttk.Entry(labelframeleft1, textvariable=self.var_cont ,width=29,  font=("times of roman",13, "bold"))
        enty_cont.grid(row=1, column=1)
        
        #==========Short Form==========
        lbl_sf = Label(labelframeleft1, text="Abbreviation:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_sf.grid(row=2, column=0, sticky=W)

        enty_sf = ttk.Entry(labelframeleft1, textvariable=self.var_sf ,width=29,  font=("times of roman",13, "bold"))
        enty_sf.grid(row=2, column=1)
        
        #==========Weight==========
        lbl_wt = Label(labelframeleft1, text="Weight in kgs:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_wt.grid(row=3, column=0, sticky=W)

        enty_wt = ttk.Entry(labelframeleft1, textvariable=self.var_conwt ,width=29,  font=("times of roman",13, "bold"))
        enty_wt.grid(row=3, column=1)
        
        #==========Price==========
        lbl_conpri = Label(labelframeleft1, text="Price:", font=("times of roman",12, "bold"), padx=2, pady=6)
        lbl_conpri.grid(row=4, column=0, sticky=W)

        enty_conpri = ttk.Entry(labelframeleft1, textvariable=self.var_conpri ,width=29,  font=("times of roman",13, "bold"))
        enty_conpri.grid(row=4, column=1)
        
        #=====btns======
        btn_frame1 = Frame(labelframeleft1, bd=2, relief=RIDGE)
        btn_frame1.place(x=15, y=180, width=390, height=38)

        btnAdd = Button(btn_frame1, text="Add", command=self.conadd_data,  font=("times of roman",13 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnAdd.grid(row=0, column=0, padx=3)

        btnUpdate = Button(btn_frame1, text="Update",command=self.conupdate_data, font=("times of roman",13 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnUpdate.grid(row=0, column=1, padx=3)

        btnDelete = Button(btn_frame1, text="Delete",command=self.condel_data,  font=("times of roman",13 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnDelete.grid(row=0, column=2, padx=3)

        btnReset = Button(btn_frame1, text="Reset",command=self.conreset,  font=("times of roman",13 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnReset.grid(row=0, column=3, padx=3)
        
    
    #=====container table frame=====
        conttableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Container Table", padx=2, font=("Mongolian Baiti",12, "bold"))
        conttableframe.place(x=435, y=50, width=850, height=480)
        
        #=====search box=======
        lblSearchBy = Label(conttableframe, text="Search By:", font=("times of roman",12, "bold"), bg="#737373", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, pady=5, padx=2)

        self.var_search = StringVar()
        ic_wt = ttk.Combobox(conttableframe, width=24, textvariable=self.var_search, font=("times of roman",13),state='readonly',justify=CENTER)
        ic_wt['values']=("cont","shortform")
        ic_wt.current(1)
        ic_wt.grid(row=0, column=1, pady=5, padx=2)

        self.var_txtsearch = StringVar()
        txtsearch = ttk.Entry(conttableframe, width=24, textvariable=self.var_txtsearch, font=("times of roman",13, "bold"))
        txtsearch.grid(row=0, column=2, pady=5, padx=2)

        btnSearch = Button(conttableframe, text="Search", command=self.search_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(conttableframe, text="Show All", command=self.confetch_data, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        btnResetSearch = Button(conttableframe, text="Reset", command=self.reset_search, font=("times of roman",10 ,"bold"),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", width=8)
        btnResetSearch.grid(row=0, column=5, padx=1)
        
        #======show all data====
        contabledetails = Frame(conttableframe, bd=2, relief=RIDGE)
        contabledetails.place(x=0, y=50, width=840, height=400)
        
        scroll_y=ttk.Scrollbar(contabledetails,orient=VERTICAL)
        
        self.Con_Table = ttk.Treeview(contabledetails, column=("Srno", "cont", "shortform", "weight","price"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.Con_Table.yview)
        
        self.Con_Table.heading("Srno", text="Srno")
        self.Con_Table.heading("cont", text="Container")
        self.Con_Table.heading("shortform", text="Abbreviation")
        self.Con_Table.heading("weight", text="Weight")
        self.Con_Table.heading("price", text="Price")
        

        self.Con_Table["show"]="headings"
        self.Con_Table.column("Srno",width=10)
        self.Con_Table.column("cont",width=50)
        self.Con_Table.column("shortform",width=20)
        self.Con_Table.column("weight",width=20)
        self.Con_Table.column("price",width=30)
        
        
        self.Con_Table.pack(fill=BOTH, expand=1)
        self.Con_Table.bind("<ButtonRelease-1>",self.conget_cuersor)
        self.confetch_data()


        
    

   


    #============Container functions===============
    def conadd_data(self):
        if self.var_srno.get()=="" or  self.var_cont.get()=="" or self.var_conwt.get()=="0" or self.var_sf.get()=="" or self.var_conpri.get()=="0":
            messagebox.showerror("Error","All feilds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into container values(%s,%s,%s,%s,%s)",(self.var_srno.get(),self.var_cont.get(),self.var_sf.get(),self.var_conwt.get(),self.var_conpri.get()))
                conn.commit()
                self.confetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Data has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def confetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from container")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Con_Table.delete(*self.Con_Table.get_children())
            for i in rows:
                self.Con_Table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def conget_cuersor(self,event=""):
        cusrsor_row = self.Con_Table.focus()
        content = self.Con_Table.item(cusrsor_row)
        row = content["values"]

        self.var_srno.set(row[0]),
        self.var_cont.set(row[1]),
        self.var_sf.set(row[2]),
        self.var_conwt.set(row[3]),
        self.var_conpri.set(row[4])

    def conupdate_data(self):
        if self.var_conpri.get()=="":
            messagebox.showerror("Error","Please enter Icecream Id",parent = self.root)
        else:    
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            my_cursor.execute("update container set cont=%s,shortform=%s,weight=%s,price=%s where Srno=%s",(self.var_cont.get(),self.var_sf.get(),self.var_conwt.get(),self.var_conpri.get(),self.var_srno.get()))
            conn.commit()
            self.confetch_data()
            conn.close()
            messagebox.showinfo("Update","Container details has been updated successfully", parent = self.root)

    def condel_data(self):
        del_data = messagebox.askyesno("Icecream Management System","Do you want to delete  this container detail",parent=self.root)
        if del_data>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            query = "delete from container where Srno=%s"
            values = (self.var_srno.get(),)
            my_cursor.execute(query,values)
        else:
            if not del_data:
                return
        conn.commit()
        self.confetch_data()
        conn.close()

    def conreset(self):
        self.var_srno.set(""),
        self.var_cont.set(""),
        self.var_sf.set(""),
        self.var_conwt.set("0"),
        self.var_conpri.set("0")
        
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@123", database="icecream")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from container where "+str(self.var_search.get())+" LIKE '%"+str(self.var_txtsearch.get())+"%'")
        rows = my_cursor.fetchall()
        if len (rows)!=0:
            self.Con_Table.delete(*self.Con_Table.get_children())
            for i in rows:
                self.Con_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def reset_search(self):
        self.var_search.set("cont")
        self.var_txtsearch.set("") 

    

   








if __name__ == "__main__":
    root = Tk()
    obj = Container(root)
    root.mainloop()