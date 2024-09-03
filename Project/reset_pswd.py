from tkinter import* # for GUI with python
from PIL import Image, ImageTk #write "pip install pillow" in cmd ; imports images
from tkinter import ttk # helps in stylish entry fill
from tkinter import messagebox #for validation check
from reset_login_connect import RESETCONNECT_PAGE
import mysql.connector

class RESET_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1550x830+0+0") # window size
        self.root.resizable(False, False) # disables window resizing

        # =================variables for entering data(received from customer) in db in customer details frame====================
        self.var_mobile = StringVar()
        self.var_ques = StringVar()
        self.var_ans = StringVar()
        self.var_pswd = StringVar()
        self.var_cnfrm_pswd = StringVar()

        # ================BACKGROUND IMAGE ===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\bg.jpg") # r converts all backward slash to forward slash
        img1 = img1.resize((1550,830)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) # converts into displayable format

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE) #display image on window; lblimg means label image
        lblimg1.place(x=0, y=0, width=1550, height=830)


        # =================== FRAME===================
        lgn_frame = Frame(self.root, bd=2, relief=RIDGE, bg="gray")
        lgn_frame.place(x=650, y=220, width=340, height=450)

        lbl_title = Label(lgn_frame, text="RESET PASSWORD", font=("arial", 23, "bold"), bg="gray", fg="red", bd=0, relief=RIDGE)
        lbl_title.place(x=20, y=10, width=300, height=30)

        #mobile
        mobile_lbl = Label(lgn_frame, text="Contact: ", font=("arial", 15, "bold"), bg="gray", fg="white") 
        mobile_lbl.place(x=30, y=60)
        mobile_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_mobile) # box for entry
        mobile_entry.place(x=34, y=85, width=270, height=25)

        #security question
        lbl_gender = Label(lgn_frame, text="Security Question:", font=("arial", 15, "bold"), bg="gray", fg="white") #label
        lbl_gender.place(x=30, y=120)
        gender_combo = ttk.Combobox(lgn_frame, width=220, font=("arial", 13, "bold"), state="readonly", textvariable=self.var_ques) #state readonly disables text entry
        gender_combo["value"] = ("Select", "Favourite food", "Favourite place", "High school", "Birth place", "Pet name")
        gender_combo.current(0) #sets current value; no issue if not written
        gender_combo.place(x=34, y=145, width=270, height=25)

        #security ans
        ans_lbl = Label(lgn_frame, text="Answer: ", font=("arial", 15, "bold"), bg="gray", fg="white") 
        ans_lbl.place(x=30, y=180)
        ans_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_ans) # box for entry
        ans_entry.place(x=34, y=205, width=270, height=25)

        #password
        pswd_lbl = Label(lgn_frame, text="New Password: ", font=("arial", 15, "bold"), bg="gray", fg="white") 
        pswd_lbl.place(x=30, y=240)
        pswd_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_pswd) # box for entry
        pswd_entry.place(x=34, y=265, width=270, height=25)

        #cnfrm password
        cnfrm_pswd_lbl = Label(lgn_frame, text="Confirm password: ", font=("arial", 15, "bold"), bg="gray", fg="white") 
        cnfrm_pswd_lbl.place(x=30, y=300)
        cnfrm_entry = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold"), textvariable=self.var_cnfrm_pswd) # box for entry
        cnfrm_entry.place(x=34, y=325, width=270, height=25)

        btn1 = Button(lgn_frame, text="Reset", command=self.check, width=10, font=("arial", 15, "bold"), bg="orange", fg="red", bd=0, cursor="hand1")
        btn1.place(x=120, y=370, width=70, height=30)


    def reg_user(self):
        self.new_window = Toplevel(self.root)
        #self.app = NEW_USER_PAGE(self.new_window)

    def check(self):
        if self.var_mobile.get() == "" or self.var_ques.get() == "" or self.var_ans.get() == "" or self.var_pswd.get() == "" or self.var_cnfrm_pswd.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root)
        elif len(self.var_mobile.get()) != 10 or self.var_mobile.get().isdigit() == False: #10 digit mobile num
            messagebox.showerror("Error", "Invalid mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                
            mycursor = conn.cursor()

            # Fetching question and answer from the database
            query = "SELECT ques, ans FROM new_user_table WHERE Contact=%s"
            value = (self.var_mobile.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid mobile field", parent=self.root)
            else:
                db_question, db_answer = row

                # Check if the user's input matches the stored question and answer
                if self.var_ques.get() != db_question or self.var_ans.get() != db_answer:
                    messagebox.showerror("Error", "Invalid question/answer field", parent=self.root)
                else:
                    # Update the password
                    query = "UPDATE new_user_table SET pswd=%s, cnfrm_pswd=%s WHERE Contact=%s"
                    value = (self.var_pswd.get(), self.var_cnfrm_pswd.get(), self.var_mobile.get())
                    mycursor.execute(query, value)
                    conn.commit()
                    self.new_window = Toplevel(self.root)
                    self.app = RESETCONNECT_PAGE(self.new_window)
        

# creates window for the project
if __name__ == "__main__":
    root = Tk()
    obj = RESET_PAGE(root)
    root.mainloop()