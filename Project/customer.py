from tkinter import* 
from PIL import Image, ImageTk 
from tkinter import ttk # helps in stylish entry fill
import random
import mysql.connector # "pip install mysql-connector-python" in cmd
from tkinter import messagebox #for validation check

class CUSTOMER_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("CUSTOMER PAGE")
        self.root.geometry("1318x569+230+258") # window size
        self.root.resizable(False, False) # disables window resizing

        # =================variables for entering data(received from customer) in db in customer details frame====================
        self.var_ref_num = StringVar()
        x = random.randint(1000, 10000) #generates random number
        self.var_ref_num.set(str(x))

        self.var_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idproof_num = StringVar()
        self.var_address = StringVar()


         # ================TITLE===================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("arial", 20, "bold"), bg="blue", fg="white", bd=2, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1318, height=50)


         # ================1ST IMAGE LOGO===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\2_11.jpg") 
        img1 = img1.resize((100,50)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) 

        lblimg = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE) 
        lblimg.place(x=0, y=0, width=100, height=50)


        # ================LEFT LABEL FRAME===================
        lbl_frameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="CUSTOMER DETAILS", padx=2, font=("arial", 12, "bold"))
        lbl_frameLeft.place(x=5, y=60, width=410, height=490)


        # ===============customer details in left label frame================
        #customer reference
        lbl_cust_ref = Label(lbl_frameLeft, text="Customer ref", padx=2, pady=10, font=("arial", 12, "bold")) #label
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        ref_entry = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), state="readonly", textvariable=self.var_ref_num) # box for entry
        ref_entry.grid(row=0, column=1)

        #customer name
        cust_name = Label(lbl_frameLeft, text="Customer Name", padx=2, pady=6, font=("arial", 12, "bold")) #label
        cust_name.grid(row=1, column=0, sticky=W)
        txt_cust_name = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), textvariable=self.var_name) # box for entry
        txt_cust_name.grid(row=1, column=1)

        #mother name
        m_name = Label(lbl_frameLeft, text="Mother Name", padx=2, pady=6, font=("arial", 12, "bold")) #label
        m_name.grid(row=2, column=0, sticky=W)
        txt_m_name = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), textvariable=self.var_mother) # box for entry
        txt_m_name.grid(row=2, column=1)

        #gender
        lbl_gender = Label(lbl_frameLeft, text="Gender", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_gender.grid(row=3, column=0, sticky=W)
        gender_combo = ttk.Combobox(lbl_frameLeft, width=27, font=("arial", 13, "bold"), state="readonly", textvariable=self.var_gender) #state readonly disables text entry
        gender_combo["value"] = ("Male", "Female", "Other")
        gender_combo.current(0) #sets current value; no issue if not written
        gender_combo.grid(row=3, column=1)

        #postcode
        lbl_postcode = Label(lbl_frameLeft, text="PostCode", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_postcode.grid(row=4, column=0, sticky=W)
        postcode_entry = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), textvariable=self.var_postcode) # box for entry
        postcode_entry.grid(row=4, column=1)

        #mobile number
        lbl_mobile = Label(lbl_frameLeft, text="Mobile", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_mobile.grid(row=5, column=0, sticky=W)
        mobile_entry = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), textvariable=self.var_mobile) # box for entry
        mobile_entry.grid(row=5, column=1)

        #email
        lbl_email = Label(lbl_frameLeft, text="Email", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_email.grid(row=6, column=0, sticky=W)
        email_entry = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), textvariable=self.var_email) # box for entry
        email_entry.grid(row=6, column=1)

        #nationality
        lbl_country = Label(lbl_frameLeft, text="Nationality", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_country.grid(row=7, column=0, sticky=W)
        country_combo = ttk.Combobox(lbl_frameLeft, width=27, font=("arial", 13, "bold"), state="readonly", textvariable=self.var_nationality) #combobox; state readonly disables text entry
        country_combo["value"] = ("Indian", "Pakistani", "British", "Korean", "Spanish")
        country_combo.current(0) #sets current value; no issue if not written
        country_combo.grid(row=7, column=1)

        #idproof type
        lbl_proof = Label(lbl_frameLeft, text="Id Proof Type", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_proof.grid(row=8, column=0, sticky=W)
        proof_combo = ttk.Combobox(lbl_frameLeft, width=27, font=("arial", 13, "bold"), state="readonly", textvariable=self.var_idproof) #combobox; state readonly disables text entry
        proof_combo["value"] = ("Aadhar Card", "Pan Card", "Passport", "Driving License")
        proof_combo.current(0) #sets current value; no issue if not written
        proof_combo.grid(row=8, column=1)

        #id number
        lbl_proof_num = Label(lbl_frameLeft, text="Id number", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_proof_num.grid(row=9, column=0, sticky=W)
        proof_num_entry = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), textvariable=self.var_idproof_num) # box for entry
        proof_num_entry.grid(row=9, column=1)

        #address
        lbl_addr = Label(lbl_frameLeft, text="Address", padx=2, pady=6, font=("arial", 12, "bold")) #label
        lbl_addr.grid(row=10, column=0, sticky=W)
        addr_entry = ttk.Entry(lbl_frameLeft, width=29, font=("arial", 13, "bold"), textvariable=self.var_address) # box for entry
        addr_entry.grid(row=10, column=1)


        # ==================BUTTONS IN LFT LBL FRAME===============
        btn_frame = Frame(lbl_frameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=413, width=402, height=32)

        btn1 = Button(btn_frame, text="Add", command=self.add_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn1.grid(row=0, column=0, padx=2)

        btn2 = Button(btn_frame, text="Update", command=self.update_values, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn2.grid(row=0, column=1, padx=2)

        btn3 = Button(btn_frame, text="Delete", command=self.delete_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn3.grid(row=0, column=2, padx=2)

        btn4 = Button(btn_frame, text="Reset", command=self.reset_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn4.grid(row=0, column=3, padx=2)



        # ================SEARCH SYSTEM LABEL FRAME===================
        lbl_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2, font=("arial", 12, "bold"))
        lbl_frameright.place(x=420, y=60, width=895, height=490)

        lbl_search = Label(lbl_frameright, text="Search by:", font=("arial", 12, "bold"), bg="black", fg="gold", width=10) #label
        lbl_search.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var = StringVar()
        search_combo = ttk.Combobox(lbl_frameright, textvariable=self.search_var, width=24, font=("arial", 13, "bold"), state="readonly") #combobox; state readonly disables text entry
        search_combo["values"] = ( "Ref_num", "Contact")
        search_combo.current(0) #sets current value; no issue if not written
        search_combo.grid(row=0, column=1, padx=2)
        
        self.txt_search = StringVar()
        search_entry = ttk.Entry(lbl_frameright, textvariable=self.txt_search, width=24, font=("arial", 13, "bold")) # box for entry
        search_entry.grid(row=0, column=2, padx=2)

        search_btn = Button(lbl_frameright, text="Search", command=self.search_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        search_btn.grid(row=0, column=3, padx=1)

        rslt_btn = Button(lbl_frameright, text="Show all", command=self.fetch_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        rslt_btn.grid(row=0, column=4, padx=1)


        # ==================DATA TABLE===================
        data_table = Frame(lbl_frameright, bd=2, relief=RIDGE)
        data_table.place(x=3, y=50, width=880, height=350)

        #scrollbar
        scroll_x = ttk.Scrollbar(data_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(data_table, orient=VERTICAL)

        self.Cust_data_table = ttk.Treeview(data_table, column= ("ref num", "name", "mother name", "gender", "postcode", "mobile no.", 
                                                                   "email", "nationality", "idproof type", "idproof no.", "address"), 
                                                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_data_table.xview)
        scroll_y.config(command=self.Cust_data_table.yview)

        self.Cust_data_table.heading("ref num", text="Ref num") # initial "" must be same as written in line 154 in column part
        self.Cust_data_table.heading("name", text="Name")
        self.Cust_data_table.heading("mother name", text="Mother name")
        self.Cust_data_table.heading("gender", text="Gender")
        self.Cust_data_table.heading("postcode", text="Postcode")
        self.Cust_data_table.heading("mobile no.", text="Mobile no.")
        self.Cust_data_table.heading("email", text="Email")
        self.Cust_data_table.heading("nationality", text="Nationality")
        self.Cust_data_table.heading("idproof type", text="id proof type")
        self.Cust_data_table.heading("idproof no.", text="id proof no.")
        self.Cust_data_table.heading("address", text="address")

        self.Cust_data_table["show"] = "headings"

        self.Cust_data_table.column("ref num", width=100) # inital "" must be same as written in line 154 in column part
        self.Cust_data_table.column("name", width=100)
        self.Cust_data_table.column("mother name", width=100)
        self.Cust_data_table.column("gender", width=100)
        self.Cust_data_table.column("postcode", width=100)
        self.Cust_data_table.column("mobile no.", width=100)
        self.Cust_data_table.column("email", width=100)
        self.Cust_data_table.column("nationality", width=100)
        self.Cust_data_table.column("idproof type", width=100)
        self.Cust_data_table.column("idproof no.", width=100)
        self.Cust_data_table.column("address", width=100)
        
        self.Cust_data_table.pack(fill=BOTH, expand=1)
        self.Cust_data_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()



    # table created in mysql db with column name same as in line 154
    # install extensions SQLTools and SQLTools MySQL/MariaDB/TiDB in vs code to connect mysql db
    # =========================ADDS DATA IN DB====================
    def add_data(self):
        if self.var_name.get() == "" or self.var_mother.get() == " " or self.var_gender.get() == "" or self.var_postcode.get() == "" or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_nationality.get() == "" or self.var_idproof.get() == "" or self.var_idproof_num.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        if self.var_name.get().isalpha() == False or self.var_mother.get().isalpha() == False: # alphabets in names
            messagebox.showerror("Error", "Only alphabets are allowed in name fields", parent=self.root)
        if len(self.var_postcode.get()) != 6 or self.var_postcode.get().isdigit() == False: #postcode 6 digit number
            messagebox.showerror("Error", "6 digit numeric allowed in postcode", parent=self.root)
        if len(self.var_mobile.get()) != 10 or self.var_mobile.get().isdigit() == False: #10 digit mobile num
            messagebox.showerror("Error", "Invalid mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                mycursor.execute("insert into project_cust_data_table values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )", 
                                (self.var_ref_num.get(), self.var_name.get(), self.var_mother.get(), self.var_gender.get(),
                                self.var_postcode.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                                self.var_idproof.get(), self.var_idproof_num.get(), self.var_address.get()) )
                
                conn.commit()
                self.fetch_data()
                conn.close()
            
                messagebox.showinfo("Success", "Customer added successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Warning", "Something went wrong: {str(es)}", parent = self.root)

    #======================fetches data from db and displays on window==============================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
        mycursor = conn.cursor()
        mycursor.execute("select * from project_cust_data_table")
        result = mycursor.fetchall()
        if len(result)!=0:
            self.Cust_data_table.delete(*self.Cust_data_table.get_children())
            for i in result :
                self.Cust_data_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    #=====================displays values in lft frame when clicked on data in right frame so as for updation=====================
    def get_cursor(self, event=""):
        cursor_result = self.Cust_data_table.focus()
        content = self.Cust_data_table.item(cursor_result)
        row = content["values"]

        self.var_ref_num.set(row[0])
        self.var_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_postcode.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idproof_num.set(row[9])
        self.var_address.set(row[10])


    # ========================updates db values ===============================
    # ===============UPDATE BUTTON ===========================
    def update_values(self):
        if self.var_name.get() == "" or self.var_mother.get() == " " or self.var_gender.get() == "" or self.var_postcode.get() == "" or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_nationality.get() == "" or self.var_idproof.get() == "" or self.var_idproof_num.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root)
        if self.var_name.get().isalpha() == False or self.var_mother.get().isalpha() == False: # alphabets in names
            messagebox.showerror("Error", "Only alphabets are allowed in name fields", parent=self.root)
            set_focus(self.var_name.get()) # type: ignore
            set_focus(self.var_mother.get()) # type: ignore
        if len(self.var_postcode.get()) != 6 or self.var_postcode.get().isdigit() == False: #postcode 6 digit number
            messagebox.showerror("Error", "6 digit numeric allowed in postcode", parent=self.root)
            set_focus(self.var_postcode.get()) # type: ignore
        if len(self.var_mobile.get()) != 10 or self.var_mobile.get().isdigit() == False: #10 digit mobile num
            messagebox.showerror("Error", "Invalid mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                mycursor.execute("""update project_cust_data_table set name=%s, mother_name=%s, gender=%s, postcode=%s, Contact=%s, email=%s, nationality=%s, idproof_type=%s, idproof_no=%s, address=%s where Ref_num=%s""",
                                (self.var_name.get(), self.var_mother.get(), self.var_gender.get(),
                                    self.var_postcode.get(), self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(),
                                    self.var_idproof.get(), self.var_idproof_num.get(), self.var_address.get(), self.var_ref_num.get()
                                    ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning", "Something went wrong: {str(es)}", parent = self.root)

    
    # ==========================DELETE BUTTON=======================
    def delete_data(self):
        if self.var_name.get() == "" or self.var_mother.get() == " " or self.var_gender.get() == "" or self.var_postcode.get() == "" or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_nationality.get() == "" or self.var_idproof.get() == "" or self.var_idproof_num.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root)
        else:
            delete = messagebox.askyesno("Question","Do you really want to delete this entry", parent = self.root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                #mycursor.execute("select * from project_cust_data_table")
                query = "delete from project_cust_data_table where ref_num=%s"
                value = (self.var_ref_num.get(),)
                mycursor.execute(query, value)
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()


    # =========================RESET BUTTON====================
    def reset_data(self):
        # self.var_ref_num.set("")
        self.var_name.set("")
        self.var_mother.set("")
        #self.var_gender.set("")
        self.var_postcode.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        # self.var_nationality.set("")
        #self.var_idproof.set("")
        self.var_idproof_num.set("")
        self.var_address.set("")

        x = random.randint(1000, 10000) #generates random number in ref string
        self.var_ref_num.set(str(x))


    # =========================SEARCH BUTTON==================
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
        mycursor = conn.cursor()
        mycursor.execute("select * from project_cust_data_table where " +str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")

        fetched_rows = mycursor.fetchall()
        if len(fetched_rows) != 0:
            self.Cust_data_table.delete(*self.Cust_data_table.get_children())
            
            for i in fetched_rows:
                self.Cust_data_table.insert("", 'end', values=i)
            conn.commit()
        conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = CUSTOMER_PAGE(root)
    root.mainloop()