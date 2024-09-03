from tkinter import* # for GUI with python
from PIL import Image, ImageTk #write "pip install pillow" in cmd ; imports images
from customer import CUSTOMER_PAGE
from room_booking import ROOM_BOOKING_PAGE
from details import DETAILS_PAGE
from reset_pswd import RESET_PAGE
from logout import LOGOUT_PAGE

class HotelManagement:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x830+0+0") # window size
        self.root.resizable(False, False) # disables window resizing

        # ================1ST IMAGE ===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\1.jpg") # r converts all backward slash to forward slash
        img1 = img1.resize((1550,200)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) # converts into displayable format

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE) #display image on window; lblimg means label image
        lblimg.place(x=0, y=0, width=1550, height=200) # bd=border; relief means border style


         # ================2ND IMAGE LOGO===================
        img2 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\2_11.jpg") 
        img2 = img2.resize((230,200)) 
        self.photoimg2 = ImageTk.PhotoImage(img2) 

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE) 
        lblimg.place(x=0, y=0, width=230, height=200)


        # ================TITLE===================
        lbl_title = Label(self.root, text="THE CROWN HOTEL", font=("times new roman", 40, "bold"), bg="blue", fg="white", bd=2, relief=RIDGE)
        lbl_title.place(x=0, y=180, width=1550, height=50)


        # ================MAIN FRAME===================
        main_frame = Frame(self.root, bd=2, relief=RIDGE)
        main_frame.place(x=0, y=225, width=1550, height=620)


        # ================MENU===================
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="blue", fg="white", bd=2, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ================BUTTON FRAME===================
        btn_frame = Frame(main_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=230, height=190)

        btn1 = Button(btn_frame, text="CUSTOMER", command=self.customer_details, width=22, font=("times new roman", 14, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn1.grid(row=0, column=0, pady=1)

        btn2 = Button(btn_frame, text="ROOM", command=self.room_booking_details, width=22, font=("times new roman", 14, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn2.grid(row=1, column=0, pady=1)

        btn3 = Button(btn_frame, text="DETAILS", command=self.room_details, width=22, font=("times new roman", 14, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn3.grid(row=2, column=0, pady=1)

        btn4 = Button(btn_frame, text="RESET", width=22, command=self.reset, font=("times new roman", 14, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn4.grid(row=3, column=0, pady=1)

        btn5 = Button(btn_frame, text="LOGOUT", width=22, command=self.logout, font=("times new roman", 14, "bold"), bg="blue", fg="white", bd=0, cursor="hand1") # type: ignore
        btn5.grid(row=4, column=0, pady=1)


         # ================3RD IMAGE RIGHT SIDE===================
        img3 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\3.jpg") 
        img3 = img3.resize((1320,600)) 
        self.photoimg3 = ImageTk.PhotoImage(img3) 

        lblimg = Label(main_frame, image=self.photoimg3, bd=2, relief=RIDGE) 
        lblimg.place(x=225, y=0, width=1330, height=610)


         # ================4TH & 5TH IMAGE DOWN===================
        img4 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\4.jpg") 
        img4 = img4.resize((230,200)) 
        self.photoimg4 = ImageTk.PhotoImage(img4) 

        lblimg = Label(main_frame, image=self.photoimg4, bd=2, relief=RIDGE) 
        lblimg.place(x=0, y=225, width=230, height=200)

        img5 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\5.jpg") 
        img5 = img5.resize((230,190)) 
        self.photoimg5 = ImageTk.PhotoImage(img5) 

        lblimg = Label(main_frame, image=self.photoimg5, bd=2, relief=RIDGE) 
        lblimg.place(x=0, y=420, width=230, height=190)


    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = CUSTOMER_PAGE(self.new_window)

    def room_booking_details(self):
        self.new_window = Toplevel(self.root)
        self.app = ROOM_BOOKING_PAGE(self.new_window)

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = DETAILS_PAGE(self.new_window)
    
    def reset(self):
        self.new_window = Toplevel(self.root)
        self.app = RESET_PAGE(self.new_window)

    def logout(self):
        self.new_window = Toplevel(self.root)
        self.app = LOGOUT_PAGE(self.new_window)


# creates window for the project
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagement(root)
    root.mainloop()