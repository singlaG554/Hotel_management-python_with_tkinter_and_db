from tkinter import* 
from PIL import Image, ImageTk 
from tkinter import ttk # helps in stylish entry fill
from tkcalendar import * # pip install tkcalendar in cmd
import random
from time import strftime
from datetime import datetime
import mysql.connector # "pip install mysql-connector-python" in cmd
from tkinter import messagebox #for validation check

class ROOM_BOOKING_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("ROOM BOOKING PAGE")
        self.root.geometry("1318x569+230+258") # window size
        self.root.resizable(False, False) # disables window resizing

        # =================variables for entering data(received from customer) in db in room details frame====================
        self.var_mobile = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavaialable = StringVar()        
        self.var_meal = StringVar()
        self.var_days = StringVar()
        self.var_taxpaid = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        # ================TITLE===================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("arial", 20, "bold"), bg="blue", fg="white", bd=2, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1318, height=50)


         # ================1ST IMAGE LOGO===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\2_11.jpg") 
        img1 = img1.resize((100,50)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) 

        lblimg = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE) 
        lblimg.place(x=0, y=0, width=100, height=50)


        # ================LEFT LABEL FRAME===================
        lbl_frameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM BOOKING DETAILS", padx=2, font=("arial", 12, "bold"))
        lbl_frameLeft.place(x=5, y=60, width=410, height=490)

        def select_date1(event): #checkin_date
            global cal, date_window
            date_window = Toplevel()
            date_window.grab_set()
            date_window.title('Select date')
            date_window.geometry('250x220+590+370')
            cal = Calendar(date_window, slectmode="day", date_pattern="mm/dd/yyyy")
            cal.place(x=0,y=0)
            submit_btn = Button(date_window, text="Submit", command=grab_date1, width=10, font=("arial", 9, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
            submit_btn.place(x=80, y=190)

        def grab_date1(): #checkin_date
            check_in_entry.delete(0, END)
            check_in_entry.insert(0, cal.get_date())
            date_window.destroy()

        def select_date2(event): #checkout_date
            global cal, date_window
            date_window = Toplevel()
            date_window.grab_set()
            date_window.title('Select date')
            date_window.geometry('250x220+590+370')
            cal = Calendar(date_window, slectmode="day", date_pattern="mm/dd/yyyy")
            cal.place(x=0,y=0)
            submit_btn = Button(date_window, text="Submit", command=grab_date2, width=10, font=("arial", 9, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
            submit_btn.place(x=80, y=190)

        def grab_date2():  #checkout_date
            check_out_entry.delete(0, END)
            check_out_entry.insert(0, cal.get_date())
            date_window.destroy()

            

        # ===============customer details in left label frame================
        #mobile number
        lbl_mobile = Label(lbl_frameLeft, text="Customer Mobile", padx=2, pady=10, font=("arial", 12, "bold")) #label
        lbl_mobile.grid(row=0, column=0, sticky=W)
        mobile_entry = ttk.Entry(lbl_frameLeft, textvariable=self.var_mobile, width=20, font=("arial", 13, "bold")) # box for entry
        mobile_entry.grid(row=0, column=1, sticky=W)

        #===================FETCH BUTTON==================
        fetch_btn = Button(lbl_frameLeft, text="Fetch Data", command=self.fetch_data, width=10, font=("arial", 9, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        fetch_btn.place(x=326, y=11)


         #Check in date
        lbl_check_in = Label(lbl_frameLeft, text="Check_in date", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_check_in.grid(row=1, column=0, sticky=W)
        check_in_entry = ttk.Entry(lbl_frameLeft, textvariable=self.var_checkin, width=28, font=("arial", 13, "bold")) # box for entry
        check_in_entry.grid(row=1, column=1)
        check_in_entry.insert(0, "dd/mm/yyyy")
        check_in_entry.bind("<1>", select_date1)

         #Check oucheck_out
        lbl_check_out = Label(lbl_frameLeft, text="Check_out date", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_check_out.grid(row=2, column=0, sticky=W)
        check_out_entry = ttk.Entry(lbl_frameLeft, textvariable=self.var_checkout, width=28, font=("arial", 13, "bold")) # box for entry
        check_out_entry.grid(row=2, column=1)
        check_out_entry.insert(0, "dd/mm/yyyy")
        check_out_entry.bind("<1>", select_date2)


        #room type
        lbl_roomtype = Label(lbl_frameLeft, text="Room type", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_roomtype.grid(row=3, column=0, sticky=W)
        roomtype_combo = ttk.Combobox(lbl_frameLeft, textvariable=self.var_roomtype, width=26, font=("arial", 13, "bold"), state="readonly") #state readonly disables text entry
        roomtype_combo["value"] = ("Single", "Double", "Luxury")
        roomtype_combo.current(0) #sets current value; no issue if not written
        roomtype_combo.grid(row=3, column=1)

        #available room
        lbl_avlbl_room = Label(lbl_frameLeft, text="Available Room ", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_avlbl_room.grid(row=4, column=0, sticky=W)
            #========room no.s feteched from table indetails page========
        conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
        mycursor = conn.cursor()
        mycursor.execute("select room_no from project_room_details_table")
        rows = mycursor.fetchall()

        avlbl_combo = ttk.Combobox(lbl_frameLeft, textvariable=self.var_roomavaialable, width=26, font=("arial", 13, "bold"), state="readonly") #state readonly disables text entry
        avlbl_combo["value"] = rows
        avlbl_combo.current(0) #sets current value; no issue if not written
        avlbl_combo.grid(row=4, column=1)

        #Meal
        lbl_meal = Label(lbl_frameLeft, text="Meal", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_meal.grid(row=5, column=0, sticky=W)
        meal_combo = ttk.Combobox(lbl_frameLeft, textvariable=self.var_meal, width=26, font=("arial", 13, "bold")) # box for entry
        meal_combo["value"] = ("Breakfast+Lunch", "Breakfast+Dinner", "Breakfast+Lunch+Dinner")
        meal_combo.current(0) #sets current value; no issue if not written
        meal_combo.grid(row=5, column=1)

        #No. of days
        lbl_days = Label(lbl_frameLeft, text="No. of days", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_days.grid(row=6, column=0, sticky=W)
        days_entry = ttk.Entry(lbl_frameLeft, textvariable=self.var_days, width=28, font=("arial", 13, "bold")) # box for entry
        days_entry.grid(row=6, column=1)

        #Paid tax
        lbl_tax = Label(lbl_frameLeft, text="Tax paid", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_tax.grid(row=7, column=0, sticky=W)
        tax_entry = ttk.Entry(lbl_frameLeft, textvariable=self.var_taxpaid, width=28, font=("arial", 13, "bold")) # box for entry
        tax_entry.grid(row=7, column=1)

        #Sub total
        lbl_subtotal = Label(lbl_frameLeft, text="Sub Total cost", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_subtotal.grid(row=8, column=0, sticky=W)
        subtotal_entry = ttk.Entry(lbl_frameLeft, textvariable=self.var_subtotal, width=28, font=("arial", 13, "bold")) # box for entry
        subtotal_entry.grid(row=8, column=1)

        #total
        lbl_total = Label(lbl_frameLeft, text="Total cost", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_total.grid(row=9, column=0, sticky=W)
        total_entry = ttk.Entry(lbl_frameLeft, textvariable=self.var_total, width=28, font=("arial", 13, "bold")) # box for entry
        total_entry.grid(row=9, column=1)

        # ==================BUTTONS IN LFT LBL FRAME===============
        bill_btn = Button(lbl_frameLeft, text="Bill", command=self.total, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        bill_btn.place(x=7, y=365, width=90, height=27) #grid(row=12, column=0, padx=1, sticky=W)


        btn_frame = Frame(lbl_frameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=413, width=395, height=32)

        btn1 = Button(btn_frame, text="Add", command=self.add_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn1.grid(row=0, column=0, padx=1)

        btn2 = Button(btn_frame, text="Update", command=self.update_values, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn2.grid(row=0, column=1, padx=1)

        btn3 = Button(btn_frame, text="Delete", command=self.delete_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn3.grid(row=0, column=2, padx=1)

        btn4 = Button(btn_frame, text="Reset", command=self.reset_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn4.grid(row=0, column=3, padx=1)

        # =============IMAGE ABOVE SEARCH SYSTEM====================
        img2 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\6.jpg") 
        img2 = img2.resize((555,300)) 
        self.photoimg2 = ImageTk.PhotoImage(img2) 
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE) 
        lblimg.place(x=760, y=70, width=555, height=220)


        # ================SEARCH SYSTEM LABEL FRAME===================
        lbl_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2, font=("arial", 12, "bold"))
        lbl_frameright.place(x=420, y=290, width=895, height=260)

        lbl_search = Label(lbl_frameright, text="Search by:", font=("arial", 12, "bold"), bg="black", fg="gold", width=10) #label
        lbl_search.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var = StringVar()
        search_combo = ttk.Combobox(lbl_frameright, textvariable=self.search_var, width=24, font=("arial", 13, "bold"), state="readonly") #combobox; state readonly disables text entry
        search_combo["values"] = ( "Room", "contact")
        search_combo.current(0) #sets current value; no issue if not written
        search_combo.grid(row=0, column=1, padx=2)
        
        self.txt_search = StringVar()
        search_entry = ttk.Entry(lbl_frameright, textvariable=self.txt_search, width=24, font=("arial", 13, "bold")) # box for entry
        search_entry.grid(row=0, column=2, padx=2)

        search_btn = Button(lbl_frameright, text="Search", command=self.search_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        search_btn.grid(row=0, column=3, padx=1)

        rslt_btn = Button(lbl_frameright, text="Show all", command=self.fetch_db_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        rslt_btn.grid(row=0, column=4, padx=1)

        # ==================DATA TABLE===================
        data_table = Frame(lbl_frameright, bd=2, relief=RIDGE)
        data_table.place(x=3, y=50, width=880, height=190)

        #scrollbar
        scroll_x = ttk.Scrollbar(data_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(data_table, column= ("contact", "check_in date", "check_out date", "room type", "room available", "meal", 
                                                                "no. of days"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact") # initial "" must be same as written in line 154 in column part
        self.room_table.heading("check_in date", text="Check_in")
        self.room_table.heading("check_out date", text="Check_out")
        self.room_table.heading("room type", text="Roomtype")
        self.room_table.heading("room available", text="Room No.")
        self.room_table.heading("meal", text=" Meal")
        self.room_table.heading("no. of days", text="Total days")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100) # inital "" must be same as written in line 154 in column part
        self.room_table.column("check_in date", width=100)
        self.room_table.column("check_out date", width=100)
        self.room_table.column("room type", width=100)
        self.room_table.column("room available", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("no. of days", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_db_data()


    #=====================DATA FETCH BY MOBILE========================
    def fetch_data(self):
        #if self.var_mobile.get() == " ":
            #messagebox.showerror("Error", "Empty contact field", parent=self.root) # parent is the name of window in which we want to display message
        #else:
            conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
            mycursor = conn.cursor()
            query = ("select name from project_cust_data_table where contact=%s")
            value=(self.var_mobile.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()

            if row==None:
                messagebox.showerror("Error", "Invalid or empty field", parent=self.root)
            else:
                conn.commit()
                conn.close()

                show_dataframe = Frame(self.root, bd=2, relief=RIDGE, padx=2)
                show_dataframe.place(x=420, y=70, width=335, height=215)
                
                #FETCH NAME
                lblname=Label(show_dataframe, text="Name:", font=("arial", 12, "bold"))
                lblname.place(x=10, y=0)
                lbl1 = Label(show_dataframe, text=row, font=("arial", 12, "bold")) #text=row displays fetched data (name) 
                lbl1.place(x=75, y=0)


                #FETCH GENDER
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = ("select gender from project_cust_data_table where contact=%s")
                value=(self.var_mobile.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()

                lblgen=Label(show_dataframe, text="Gender:", font=("arial", 12, "bold"))
                lblgen.place(x=10, y=30)
                lbl2 = Label(show_dataframe, text=row, font=("arial", 12, "bold")) #text=row displays fetched data (name) 
                lbl2.place(x=90, y=30)


                #FETCH MOTHER NAME
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = ("select mother_name from project_cust_data_table where contact=%s")
                value=(self.var_mobile.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()

                lblmom=Label(show_dataframe, text="Mother name:", font=("arial", 12, "bold"))
                lblmom.place(x=10, y=60)
                lbl3 = Label(show_dataframe, text=row, font=("arial", 12, "bold")) #text=row displays fetched data (name) 
                lbl3.place(x=130, y=60)


                #FETCH CONTACT
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = ("select Contact from project_cust_data_table where contact=%s")
                value=(self.var_mobile.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()

                lblcontact=Label(show_dataframe, text="Contact:", font=("arial", 12, "bold"))
                lblcontact.place(x=10, y=90)
                lbl4 = Label(show_dataframe, text=row, font=("arial", 12, "bold")) #text=row displays fetched data (name) 
                lbl4.place(x=90, y=90)


                #FETCH EMAIL
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = ("select email from project_cust_data_table where contact=%s")
                value=(self.var_mobile.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()

                lblmail=Label(show_dataframe, text="Email:", font=("arial", 12, "bold"))
                lblmail.place(x=10, y=120)
                lbl5 = Label(show_dataframe, text=row, font=("arial", 12, "bold")) #text=row displays fetched data (name) 
                lbl5.place(x=70, y=120)

                #FETCH ADDRESS
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = ("select address from project_cust_data_table where contact=%s")
                value=(self.var_mobile.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()

                lbladdr=Label(show_dataframe, text="Address:", font=("arial", 12, "bold"))
                lbladdr.place(x=10, y=150)
                lbl6 = Label(show_dataframe, text=row, font=("arial", 12, "bold")) #text=row displays fetched data (name) 
                lbl6.place(x=95, y=150)

                #FETCH NATIONALITY
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = ("select nationality from project_cust_data_table where contact=%s")
                value=(self.var_mobile.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()

                lblnation=Label(show_dataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblnation.place(x=10, y=180)
                lbl7 = Label(show_dataframe, text=row, font=("arial", 12, "bold")) #text=row displays fetched data (name) 
                lbl7.place(x=110, y=180)

    #===================calculates no. of days, tax, subtotal, total========================
    #==============BILL BUTTON===================
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%m/%d/%Y")        
        outDate = datetime.strptime(outDate, "%m/%d/%Y")
        self.var_days.set(abs(outDate-inDate).days)

        global c1, c2, c3, c4, days
        c1=float(500) # single perday
        c2=float(800) # double per day
        c3=float(1000) # luxury per day
        c4 = float(100) # labor per day per meal 
        days = float(self.var_days.get())
        if(self.var_meal.get() == "Breakfast+Lunch" or self.var_meal.get() == "Breakfast+Dinner" and self.var_roomtype.get() == "Single"):
            charges_per_day = float(c1+(2*c4))
            ttl_day_charges = float(charges_per_day*days)
            #tax = "Rs. "+str("%.2f"%((ttl_day_charges)*0.09))
            tax = "Rs. "+str((ttl_day_charges)*0.09)
            STTL = "Rs. "+str(ttl_day_charges)
            TTL = "Rs. "+str( ttl_day_charges+ ((ttl_day_charges)*0.09))
            #STTL = "Rs. "+str("%.2f"%((ttl_day_charges)))
            #TTL = "Rs. "+str("%.2f"% ( ttl_day_charges+ ((ttl_day_charges)*0.09)))
            self.var_taxpaid.set(tax)
            self.var_subtotal.set(STTL)
            self.var_total.set(TTL)
        
        elif(self.var_meal.get() == "Breakfast+Lunch+Dinner" and self.var_roomtype.get() == "Single"):
            charges_per_day = float(c1+(3*c4))
            ttl_day_charges = float(charges_per_day*days)
            tax = "Rs. "+str((ttl_day_charges)*0.09)
            STTL = "Rs. "+str(ttl_day_charges)
            TTL = "Rs. "+str( ttl_day_charges+ ((ttl_day_charges)*0.09))
            self.var_taxpaid.set(tax)
            self.var_subtotal.set(STTL)
            self.var_total.set(TTL)
        
        elif(self.var_meal.get() == "Breakfast+Lunch" or self.var_meal.get() == "Breakfast+Dinner" and self.var_roomtype.get() == "Double"):
            charges_per_day = float(c2+(2*c4))
            ttl_day_charges = float(charges_per_day*days)
            tax = "Rs. "+str((ttl_day_charges)*0.09)
            STTL = "Rs. "+str(ttl_day_charges)
            TTL = "Rs. "+str( ttl_day_charges+ ((ttl_day_charges)*0.09))
            self.var_taxpaid.set(tax)
            self.var_subtotal.set(STTL)
            self.var_total.set(TTL)
        
        elif(self.var_meal.get() == "Breakfast+Lunch+Dinner" and self.var_roomtype.get() == "Double"):
            charges_per_day = float(c2+(3*c4))
            ttl_day_charges = float(charges_per_day*days)
            tax = "Rs. "+str((ttl_day_charges)*0.09)
            STTL = "Rs. "+str(ttl_day_charges)
            TTL = "Rs. "+str( ttl_day_charges+ ((ttl_day_charges)*0.09))
            self.var_taxpaid.set(tax)
            self.var_subtotal.set(STTL)
            self.var_total.set(TTL)
        
        elif(self.var_meal.get() == "Breakfast+Lunch" or self.var_meal.get() == "Breakfast+Dinner" and self.var_roomtype.get() == "Luxury"):
            charges_per_day = float(c3+(2*c4))
            ttl_day_charges = float(charges_per_day*days)
            tax = "Rs. "+str((ttl_day_charges)*0.09)
            STTL = "Rs. "+str(ttl_day_charges)
            TTL = "Rs. "+str( ttl_day_charges+ ((ttl_day_charges)*0.09))
            self.var_taxpaid.set(tax)
            self.var_subtotal.set(STTL)
            self.var_total.set(TTL)

        elif(self.var_meal.get() == "Breakfast+Lunch+Dinner" and self.var_roomtype.get() == "Luxury"):
            charges_per_day = float(c3+(3*c4))
            ttl_day_charges = float(charges_per_day*days)
            tax = "Rs. "+str((ttl_day_charges)*0.09)
            STTL = "Rs. "+str(ttl_day_charges)
            TTL = "Rs. "+str( ttl_day_charges+ ((ttl_day_charges)*0.09))
            self.var_taxpaid.set(tax)
            self.var_subtotal.set(STTL)
            self.var_total.set(TTL)

        else:
            messagebox("Error", "Wrong input", parent=self.root)
    
    #====================INSERT ADDED DATA INTO TABLE==============
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_checkin.get() == "" or self.var_checkout.get() == "" or self.var_roomtype.get() == " " or self.var_roomavaialable.get() == "" or self.var_meal.get() == "" or self.var_days.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        if len(self.var_mobile.get()) != 10 or self.var_mobile.get().isdigit() == False: #10 digit mobile num
            messagebox.showerror("Error", "Invalid mobile number", parent=self.root)
        if self.var_days.get().isdigit() == False : # alphabets in names
            messagebox.showerror("Error", "Only digits are allowed in days field", parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                mycursor.execute("insert into project_room_book_table values(%s, %s, %s, %s, %s, %s, %s )", 
                                (self.var_mobile.get(), self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(),
                                self.var_roomavaialable.get(), self.var_meal.get(), self.var_days.get()) )
                
                conn.commit()
                self.fetch_db_data()
                conn.close()
            
                messagebox.showinfo("Success", "Room booked successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Warning", "Something went wrong: {str(es)}", parent = self.root)


    #======================fetches data from db and displays on window==============================
    def fetch_db_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
        mycursor = conn.cursor()
        mycursor.execute("select * from project_room_book_table")
        result = mycursor.fetchall()
        if len(result)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in result :
                self.room_table.insert("", END, values=i)
        conn.commit()
        conn.close()  

    
    #=====================displays values in lft frame when clicked on data in right frame so as for updation=====================
    def get_cursor(self, event=""):
        cursor_result = self.room_table.focus()
        content = self.room_table.item(cursor_result)
        row = content["values"]

        self.var_mobile.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavaialable.set(row[4])
        self.var_meal.set(row[5])
        self.var_days.set(row[6])

        messagebox.showinfo("Information", "Contact cannot be updated", parent=self.root)


    # ========================updates db values =============================== 
    # ===============UPDATE BUTTON ===========================
    def update_values(self):
        if self.var_mobile.get() == "" or self.var_checkin.get() == "" or self.var_checkout.get() == "" or self.var_roomtype.get() == " " or self.var_roomavaialable.get() == "" or self.var_meal.get() == "" or self.var_days.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        if len(self.var_mobile.get()) != 10 or self.var_mobile.get().isdigit() == False: #10 digit mobile num
            messagebox.showerror("Error", "Invalid mobile number", parent=self.root)
        if self.var_days.get().isdigit() == False : # alphabets in names
            messagebox.showerror("Error", "Only digits are allowed in days field", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                mycursor.execute("""update project_room_book_table set check_in_date=%s, check_out_date=%s, room_type=%s, Room=%s, meal=%s, no_of_days=%s  where contact=%s""",
                                (self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(),
                                self.var_roomavaialable.get(), self.var_meal.get(), self.var_days.get(), self.var_mobile.get()))
                
                conn.commit()
                self.fetch_db_data()
                conn.close()
                messagebox.showinfo("Success", "Updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning", "Something went wrong: {str(es)}", parent = self.root)

    
    # ==========================DELETE BUTTON=======================
    def delete_data(self):
        if self.var_mobile.get() == "" or self.var_checkin.get() == "" or self.var_checkout.get() == "" or self.var_roomtype.get() == " " or self.var_roomavaialable.get() == "" or self.var_meal.get() == "" or self.var_days.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        else:
            delete = messagebox.askyesno("Question","Do you really want to delete this entry", parent = self.root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = "delete from project_room_book_table where contact=%s"
                value = (self.var_mobile.get(),)
                mycursor.execute(query, value)
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_db_data()
            conn.close()

    # =========================RESET BUTTON====================
    def reset_data(self):
        self.var_mobile.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomavaialable.set("")        
        self.var_meal.set("")
        self.var_days.set("")
        self.var_taxpaid.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    #====================SEARCH AND SEARCH ALL BUTTON====================
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
        mycursor = conn.cursor()
        mycursor.execute("select * from project_room_book_table where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")

        fetched_rows = mycursor.fetchall()
        if len(fetched_rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            
            for i in fetched_rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()




if __name__ == "__main__":
    root = Tk()
    obj = ROOM_BOOKING_PAGE(root)
    root.mainloop()