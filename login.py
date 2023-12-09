from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
#from home import Home
from stock import Stock
from container import Container
from customer import Customer
from bill import Bill
from report import Report



def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1520x800+0+0")

    #==============variables===========
        self.var_username = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_resetP = StringVar()

    #===Bg Image===
        self.bg = ImageTk.PhotoImage(file = "images\\b2.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

    #===LEFT Image===
        self.left = ImageTk.PhotoImage(file = "images\\left_img6.png")
        left = Label(self.root, image=self.left).place(x=200, y=150, width=700, height=500)

    #===Login Frame===
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=900, y=150, width=450, height=500)

        title = Label(frame1, text="Login Now", font=("Mongolian Baiti",20,"bold"), bg="white", fg="#737373").place(x=50, y=30)

    #======Username=====
        user_name = Label(frame1, text="Username:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_username = Entry(frame1, textvariable=self.var_username, font=("times of roman",15), bg="lightgray").place(x=50, y=130, width=250)

    #======Password=====
        password = Label(frame1, text="Password:",  font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=50, y=200)
        self.txt_password = Entry(frame1, textvariable=self.var_pass, show='*', font=("times of roman",15), bg="lightgray").place(x=50, y=230, width=250)
        #check_button = Checkbutton(frame1, text="show password", command=self.show_password, font=("times of roman",10), bg="white", fg="gray", activeforeground="gray", activebackground="white")
        #check_button.place(x=50, y=260)
            
        
    #=====Login Btn====
        btn_login = Button(frame1, command=self.login_data, text="Login Now",  font=("Mongolian Baiti",20), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9").place(x=75, y=305)

    #=====Forgot Password And Registration Btn=====
        registerbtn = Button(frame1,  text="New User Register", command=self.register_window, font=("Mongolian Baiti",15), borderwidth=0, bg="white", fg="#737373", activeforeground="black", activebackground="white")
        registerbtn.place(x=20, y=380, width=160)

        forgotpassbtn = Button(frame1,  text="Forgot Password", command=self.forgotpass, font=("Mongolian Baiti",15), borderwidth=0, bg="white", fg="#737373", activeforeground="black", activebackground="white")
        forgotpassbtn.place(x=10, y=410, width=160)

    #======Function Declaration for opening register page===
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    #=======Function Declaration for login==========
    def login_data(self):
        if self.var_username.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error", "Please enter username and password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from icregister where email=%s and password=%s",(
                                                                                            self.var_username.get(),
                                                                                            self.var_pass.get()
                                                                                        ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:

                open_main = messagebox.askyesno("YesNo", "Access only for Admin")
            
                if open_main > 0 :
                    self.home_window()
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #=======Reset Password Function====
    def resetpass(self):

        self.sq = self.var_securityQ.get();
        self.sa = self.var_securityA.get();
        self.r = self.var_resetP.get();
        self.u = self.var_username.get();
        
        if self.sq=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.sa=="":
            messagebox.showerror("Error","Enter the answer",parent=self.root2)
        elif self.r=="":
            messagebox.showerror("Error","Enter new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            qry = ("select * from icregister where email=%s and securityQ=%s and securityA=%s")
            value1 = (self.u, self.sq, self.sa)
            my_cursor.execute(qry,value1)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                q = ("update icregister set password=%s where email=%s")
                value2 = (self.r,self.u)
                my_cursor.execute(q, value2)
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucess","Password updated sucessfully, enter updated password")
        
    #======Function Declaration for opening home page===
    def home_window(self):
        self.new_window1 = Toplevel(self.root)
        self.app1 = Home(self.new_window1)

    #======Forgot Password====
    def forgotpass(self):
        if self.var_username.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            self.u = self.var_username.get()
            conn = mysql.connector.connect(host="localhost", user="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            query = ("select * from icregister where email=%s")
            value = (self.u,)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+710+170")

                l=Label(self.root2,text="Forgot Password",font=("Mongolian Baiti",20, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
                l.place(x=0, y=0, relwidth=1)

                question = Label(self.root2, text="Security Question:", font=("Mongolian Baiti",15,"bold"),  fg="gray").place(x=50, y=80)
                cmb_quest = ttk.Combobox(self.root2, textvariable=self.var_securityQ, font=("times of roman",13),state='readonly',justify=CENTER)
                cmb_quest['values']=("Select","Your Birth Place","Father's Name","Favourite Cousin")
                cmb_quest.place(x=50, y=110, width=250)
                cmb_quest.current(0)

                answer = Label(self.root2, text="Answer:", font=("Mongolian Baiti",15,"bold"),  fg="gray").place(x=50, y=170)
                self.txt_answer = Entry(self.root2, textvariable=self.var_securityA, font=("times of roman",15), bg="lightgray").place(x=50, y=200, width=250)

                reset = Label(self.root2, text="Reset Password:", font=("Mongolian Baiti",15,"bold"),  fg="gray").place(x=50, y=260)
                self.txt_answer = Entry(self.root2, textvariable=self.var_resetP,  font=("times of roman",15), bg="lightgray").place(x=50, y=290, width=250)

                btn_reset = Button(self.root2, text="Reset", command=self.resetpass, font=("Mongolian Baiti",20),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9",).place(x=130, y=350)
                
    #=============show password==================
    def show_password(self):
        if  self.txt_password.cget('show') == '*':
            self.txt_password.config(show='')
        else:
             self.txt_password.config(show='*')            


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1520x800+0+0")

        #==============variables===========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()

        #===Bg Image===
        self.bg = ImageTk.PhotoImage(file = "images\\b2.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #===LEFT Image===
        self.left = ImageTk.PhotoImage(file = "images\\left2.jpeg")
        left = Label(self.root, image=self.left).place(x=100, y=100, width=500, height=600)

        #===Register Frame===
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=600, y=100, width=700, height=600)

        title = Label(frame1, text="REGISTER HERE", font=("Mongolian Baiti",20,"bold"), bg="white", fg="#737373").place(x=50, y=30)

        #======Row1
        f_name = Label(frame1, text="First Name:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, textvariable=self.var_fname, font=("times of roman",15), bg="lightgray").place(x=50, y=130, width=250)

        l_name = Label(frame1, text="Last Name:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, textvariable=self.var_lname, font=("times of roman",15), bg="lightgray").place(x=370, y=130, width=250)

        #======Row2
        contact = Label(frame1, text="Contact Number:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=50, y=200)
        self.txt_contact = Entry(frame1, textvariable=self.var_contact, font=("times of roman",15), bg="lightgray").place(x=50, y=230, width=250)

        email = Label(frame1, text="Email:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=370, y=200)
        self.txt_email = Entry(frame1, textvariable=self.var_email, font=("times of roman",15), bg="lightgray").place(x=370, y=230, width=250)

        #======Row3
        question = Label(frame1, text="Security Question:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=50, y=300)
        cmb_quest = ttk.Combobox(frame1, textvariable=self.var_securityQ, font=("times of roman",13),state='readonly',justify=CENTER)
        cmb_quest['values']=("Select","Your Birth Place","Father's Name","Favourite Cousin")
        cmb_quest.place(x=50, y=330, width=250)
        cmb_quest.current(0)

        answer = Label(frame1, text="Answer:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=370, y=300)
        self.txt_answer = Entry(frame1, textvariable=self.var_securityA, font=("times of roman",15), bg="lightgray").place(x=370, y=330, width=250)

        #======Row4
        password = Label(frame1, text="Password:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=50, y=400)
        self.txt_password = Entry(frame1, textvariable=self.var_pass, font=("times of roman",15), bg="lightgray").place(x=50, y=430, width=250)

        cpassword = Label(frame1, text="Confirm Password:", font=("Mongolian Baiti",15,"bold"), bg="white", fg="gray").place(x=370, y=400)
        self.txt_cpassword = Entry(frame1, textvariable=self.var_cpass, font=("times of roman",15), bg="lightgray").place(x=370, y=430, width=250)

        #=====Register & Login Btn
        btn_register = Button(frame1, text="Register Now", command=self.register_data, font=("Mongolian Baiti",20),bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9").place(x=75, y=500)

        btn_login = Button(frame1, text="Log In", command=self.login_window, font=("Mongolian Baiti",20), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9").place(x=425, y=500)
    
    #=======Function Declaration for registration==========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_cpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Password@123", database="icecream")
            my_cursor = conn.cursor()
            query = ("Select * from icregister where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None: 
                messagebox.showerror("Error", "User already exists, please try another email address",parent=self.root)
            else:
                my_cursor.execute("insert into icregister values(%s, %s, %s, %s, %s, %s, %s)",(
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_pass.get()
                                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess", "Registration Sucessfull",parent=self.root)
    
    #======Function Declaration for opening login page===
    def login_window(self):
        self.new_window2 = Toplevel(self.root)
        self.app2 = Login(self.new_window2)
        
    



class Home:
    def __init__(self,root):
        self.root = root
        self.root.title("Icecream Parlour Management System")
        self.root.geometry("1520x800+0+0")


    #====Upper Image===
        img1 = Image.open(r"images\home4.jpg")
        img1 = img1.resize((230,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=230, y=0, width=230, height=150)

        img5 = Image.open(r"images\homebottom3.jpg")
        img5 = img5.resize((230,150),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg = Label(self.root, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=460, y=0, width=230, height=150)

        img6 = Image.open(r"images\u1.jpg")
        img6 = img6.resize((230,150),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        lblimg = Label(self.root, image=self.photoimg6, bd=4, relief=RIDGE)
        lblimg.place(x=690, y=0, width=230, height=150)

        img7 = Image.open(r"images\homebottom1.jpg")
        img7 = img7.resize((230,150),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        lblimg = Label(self.root, image=self.photoimg7, bd=4, relief=RIDGE)
        lblimg.place(x=920, y=0, width=230, height=150)

        img8 = Image.open(r"images\u2.jpg")
        img8 = img8.resize((230,150),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        lblimg = Label(self.root, image=self.photoimg8, bd=4, relief=RIDGE)
        lblimg.place(x=1150, y=0, width=230, height=150)

        img9 = Image.open(r"images\i1.jpg")
        img9 = img9.resize((140,150),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        lblimg = Label(self.root, image=self.photoimg9, bd=4, relief=RIDGE)
        lblimg.place(x=1380, y=0, width=140, height=150)

    #====Logo Image===
        img2 = Image.open(r"images\l2.jpeg")
        img2 = img2.resize((230,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=150)

    #=====Title=====
        lbl_title = Label(self.root,text="ICECREAM PARLOUR MANAGEMENT SYSTEM", font=("Mongolian Baiti",40, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=150, width=1520, height=50)

    #=====Main Frame====
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=200, width=1520, height=620)

    #====Menu======
        lbl_menu = Label(main_frame,text="MENU", font=("Mongolian Baiti",20, "bold"), bg="#737373", fg="white", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

    #=====Main Frame====
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=230, height=220)

    #=====Buttons=======
        stock_btn = Button(btn_frame, text="Stock", command=self.stock_details, width=18, font=("Mongolian Baiti",15 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", bd=0, cursor="hand2")
        stock_btn.grid(row=0, column=0, pady=1)
        
        container_btn = Button(btn_frame, text="Container", command=self.container_details, width=18, font=("Mongolian Baiti",15 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", bd=0, cursor="hand2")
        container_btn.grid(row=1, column=0, pady=1)


        cust_btn = Button(btn_frame, text="Customer",command=self.customer_details , width=18, font=("Mongolian Baiti",15 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", bd=0, cursor="hand2")
        cust_btn.grid(row=2, column=0, pady=1)

        bill_btn = Button(btn_frame, text="Bill", command=self.bill_details, width=18, font=("Mongolian Baiti",15 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", bd=0, cursor="hand2")
        bill_btn.grid(row=3, column=0, pady=1)

        report_btn = Button(btn_frame, text="Report", command=self.report_details, width=18, font=("Mongolian Baiti",15 ,"bold"), bg="#737373", fg="white", activeforeground="black", activebackground="#D9D9D9", bd=0, cursor="hand2")
        report_btn.grid(row=4, column=0, pady=1)

        logout_btn = Button(btn_frame, text="Logout", command=self.login_details, width=18, font=("Mongolian Baiti",15 ,"bold"), bg="#737373", fg="white",activeforeground="black", activebackground="#D9D9D9", bd=0, cursor="hand2")
        logout_btn.grid(row=5, column=0, pady=1)

    #======Right Side Image====
        img3 = Image.open(r"images\homebottom.jpg")
        img3 = img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

    #======Left Side Bottom Image====
        img10 = Image.open(r"images\i2.jpg")
        img10 = img10.resize((230,200),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        lblimg2 = Label(main_frame, image=self.photoimg10, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=249, width=225, height=200)

        img11 = Image.open(r"images\i3.jpg")
        img11 = img11.resize((230,200),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        lblimg3 = Label(main_frame, image=self.photoimg11, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=450, width=225, height=150)

    def stock_details(self):
        self.new_window1 = Toplevel(self.root)
        self.app1 = Stock(self.new_window1)

    def customer_details(self):
        self.new_window2 = Toplevel(self.root)
        self.app2 = Customer(self.new_window2)

    def bill_details(self):
        self.new_window3 = Toplevel(self.root)
        self.app3 = Bill(self.new_window3)

    def report_details(self):
        self.new_window4 = Toplevel(self.root)
        self.app4 = Report(self.new_window4)

    def login_details(self):
        self.new_window5 = Toplevel(self.root)
        self.app5 = Login(self.new_window5)
        
    def container_details(self):
        self.new_window6 = Toplevel(self.root)
        self.app6 = Container(self.new_window6)

    

    

    

   






if __name__ == "__main__":
    main()


   