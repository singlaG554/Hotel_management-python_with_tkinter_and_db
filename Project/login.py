from tkinter import* # for GUI with python
from PIL import Image, ImageTk #write "pip install pillow" in cmd ; imports images
from tkinter import ttk # helps in stylish entry fill
from tkinter import messagebox #for validation check
#from new_user import NEW_USER_PAGE
from main_page import HotelManagement
import mysql.connector

class LOGIN_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1550x830+0+0") # window size
        self.root.resizable(False, False) # disables window resizing

        # ================BACKGROUND IMAGE ===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\bg.jpg") # r converts all backward slash to forward slash
        img1 = img1.resize((1550,830)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) # converts into displayable format

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE) #display image on window; lblimg means label image
        lblimg1.place(x=0, y=0, width=1550, height=830)


        # ===================LOGIN FRAME===================
        lgn_frame = Frame(self.root, bd=2, relief=RIDGE, bg="gray")
        lgn_frame.place(x=650, y=270, width=340, height=200)

        lbl_title = Label(lgn_frame, text="GET STARTED", font=("arial", 23, "bold"), bg="gray", fg="red", bd=0, relief=RIDGE)
        lbl_title.place(x=40, y=10, width=250, height=30)

        user_lbl = Label(lgn_frame, text="Username: ", font=("arial", 15, "bold"), bg="gray", fg="white") 
        user_lbl.place(x=10, y=60)
        self.user = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold")) # box for entry
        self.user.place(x=120, y=64, width=210, height=25)

        pswd_lbl = Label(lgn_frame, text="Password: ", font=("arial", 15, "bold"), bg="gray", fg="white") 
        pswd_lbl.place(x=10, y=100)
        self.pswd = ttk.Entry(lgn_frame, width=29, font=("arial", 13, "bold")) # box for entry
        self.pswd.place(x=120, y=104, width=210, height=25)

        btn1 = Button(lgn_frame, text="Login", command=self.check, width=10, font=("arial", 15, "bold"), bg="orange", fg="red", bd=0, cursor="hand1")
        btn1.place(x=130, y=144, width=70, height=30)

        """new_user_btn = Button(lgn_frame, text="Register new user",  border=0, width=10, font=("arial", 11, "bold", "underline"), bg="gray", fg="white", bd=0, cursor="hand1", activeforeground="red", activebackground="gray")
        new_user_btn.place(x=25, y=184, width=140)

        frgt_pswd_btn = Button(lgn_frame, text="Forget password", width=10, border=0, font=("arial", 11, "bold", "underline"), bg="gray", fg="white", bd=0, cursor="hand1",  activeforeground="red", activebackground="gray")
        #frgt_pswd_btn.place(x=10, y=208, width=132)
        frgt_pswd_btn.place(x=175, y=184, width=132)"""

    #def reg_user(self):
     #   self.new_window = Toplevel(self.root)
     #   self.app = NEW_USER_PAGE(self.new_window)


    def check(self):
        if self.user.get() == "" or self.pswd.get() == "" :
            messagebox.showerror("Error", "Empty field", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
            mycursor = conn.cursor()
            query = ("select pswd from new_user_table where First_name=%s")
            value=(self.user.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()

            if row==None or row != self.pswd.get():
                messagebox.showerror("Error", "Invalid or empty field", parent=self.root)
            elif row != self.pswd.get():
                messagebox.showerror("Error", "Invalid or empty field", parent=self.root)
            else:
            #====================takes to main page======================
                messagebox.showinfo("Success", "Welcome to Hotel Crown", parent=self.root)
                self.new_window = Toplevel(self.root)
                self.app = HotelManagement(self.new_window)
        

# creates window for the project
if __name__ == "__main__":
    root = Tk()
    obj = LOGIN_PAGE(root)
    root.mainloop()