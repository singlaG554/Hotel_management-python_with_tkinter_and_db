from tkinter import* # for GUI with python
from PIL import Image, ImageTk #write "pip install pillow" in cmd ; imports images
from tkinter import ttk # helps in stylish entry fill
from tkinter import messagebox #for validation check
from registered import SUCCESS_PAGE # type: ignore
import mysql.connector

class NEW_USER_PAGE:
    def __init__(self, root):
        self.root=root
        self.root.title("Register new user")
        self.root.geometry("1550x830+0+0") # window size
        self.root.resizable(False, False) # disables window resizing

        # =================variables for entering data(received from customer) in db in customer details frame====================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_ques = StringVar()
        self.var_ans = StringVar()
        self.var_pswd = StringVar()
        self.var_cnfrm_pswd = StringVar()
        
        # ================BACKGROUND IMAGE ===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\user1.jpeg") # r converts all backward slash to forward slash
        img1 = img1.resize((1550,830)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) # converts into displayable format

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE) #display image on window; lblimg means label image
        lblimg1.place(x=0, y=0, width=1550, height=830)

        img2 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\user2.jpg") # r converts all backward slash to forward slash
        img2 = img2.resize((350,550)) 
        self.photoimg2 = ImageTk.PhotoImage(img2) # converts into displayable format

        lblimg1 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE) #display image on window; lblimg means label image
        lblimg1.place(x=200, y=160, width=350, height=550)

        # ===================LOGIN FRAME===================
        lgn_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        lgn_frame.place(x=540, y=160, width=850, height=550)

        lbl_title = Label(lgn_frame, text="REGISTER NEW USER", font=("arial", 27, "bold"), bg="white", fg="red", bd=0, relief=RIDGE)
        lbl_title.place(x=200, y=10, width=450, height=60)

        #====================labels=====================
        #first name
        fname_lbl = Label(lgn_frame, text="First name: ", font=("arial", 15, "bold"), bg="white", fg="black") 
        fname_lbl.place(x=50, y=85)
        fname_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_fname) # box for entry
        fname_entry.place(x=50, y=115, width=230, height=25)

        #last name
        lname_lbl = Label(lgn_frame, text="Last name: ", font=("arial", 15, "bold"), bg="white", fg="black") 
        lname_lbl.place(x=450, y=85)
        lname_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_lname) # box for entry
        lname_entry.place(x=450, y=115, width=230, height=25)

        #mobile
        mobile_lbl = Label(lgn_frame, text="Contact: ", font=("arial", 15, "bold"), bg="white", fg="black") 
        mobile_lbl.place(x=50, y=165)
        mobile_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_mobile) # box for entry
        mobile_entry.place(x=50, y=195, width=230, height=25)

        #email
        mail_lbl = Label(lgn_frame, text="Email: ", font=("arial", 15, "bold"), bg="white", fg="black") 
        mail_lbl.place(x=450, y=165)
        mail_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_email) # box for entry
        mail_entry.place(x=450, y=195, width=230, height=25)

        #security question
        lbl_gender = Label(lgn_frame, text="Select Security question", font=("arial", 15, "bold"), bg="white", fg="black") #label
        lbl_gender.place(x=50, y=245)
        gender_combo = ttk.Combobox(lgn_frame, width=220, font=("arial", 13, "bold"), state="readonly", textvariable=self.var_ques) #state readonly disables text entry
        gender_combo["value"] = ("Select", "Favourite food", "Favourite place", "High school", "Birth place", "Pet name")
        gender_combo.current(0) #sets current value; no issue if not written
        gender_combo.place(x=50, y=275, width=230, height=25)

        #security ans
        ans_lbl = Label(lgn_frame, text="Security answer: ", font=("arial", 15, "bold"), bg="white", fg="black") 
        ans_lbl.place(x=450, y=245)
        ans_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_ans) # box for entry
        ans_entry.place(x=450, y=275, width=230, height=25)

        #password
        pswd_lbl = Label(lgn_frame, text="Password: ", font=("arial", 15, "bold"), bg="white", fg="black") 
        pswd_lbl.place(x=50, y=325)
        pswd_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_pswd) # box for entry
        pswd_entry.place(x=50, y=355, width=230, height=25)

        #cnfrm password
        cnfrm_pswd_lbl = Label(lgn_frame, text="Confirm password: ", font=("arial", 15, "bold"), bg="white", fg="black") 
        cnfrm_pswd_lbl.place(x=450, y=325)
        cnfrm_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_cnfrm_pswd) # box for entry
        cnfrm_entry.place(x=450, y=355, width=230, height=25)

        #checkbox
        checkbtn = Checkbutton(lgn_frame, text="I agree the terms and conditions", font=("arial", 13, "bold"), bg="white", fg="black")
        checkbtn.place(x=50, y=400)

        #==================Buttons====================
        register_btn = Button(lgn_frame, text="Register", command=self.success_details, border=10, width=10, font=("arial", 12, "bold",), bg="gold", fg="red", bd=0, cursor="hand1",)
        register_btn.place(x=285, y=450, width=90)

    def success_details(self):
        if self.var_fname.get() == "" or self.var_lname.get() == " " or self.var_mobile.get() == "" or self.var_email.get() == "" or self.var_ques.get() == "" or self.var_ans.get() == "" or self.var_pswd.get() == "" or self.var_cnfrm_pswd.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        if self.var_fname.get().isalpha() == False or self.var_lname.get().isalpha() == False or self.var_ans.get().isalpha() == False: # alphabets in names
            messagebox.showerror("Error", "Only alphabets are allowed in name fields", parent=self.root)
        if len(self.var_mobile.get()) != 10 or self.var_mobile.get().isdigit() == False: #10 digit mobile num
            messagebox.showerror("Error", "Invalid mobile number", parent=self.root)
        if self.var_pswd.get() != self.var_cnfrm_pswd.get() :
            messagebox.showerror("Error", "Password and confirm password doesn't match", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                mycursor.execute("insert into new_user_table values(%s, %s, %s, %s, %s, %s, %s, %s)", 
                                (self.var_fname.get(), self.var_lname.get(),  self.var_mobile.get(), self.var_email.get(), self.var_ques.get(),
                                self.var_ans.get(), self.var_pswd.get(), self.var_cnfrm_pswd.get()) )
                
                conn.commit()
                conn.close()
            
                #messagebox.showinfo("Success", "Customer added successfully", parent = self.root)
                self.new_window = Toplevel(self.root)
                self.app = SUCCESS_PAGE(self.new_window)
            except Exception as es:
                messagebox.showerror("Warning", "Already registered with this number", parent = self.root)

        

# creates window for the project
if __name__ == "__main__":
    root = Tk()
    obj = NEW_USER_PAGE(root)
    root.mainloop()