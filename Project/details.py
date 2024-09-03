from tkinter import* 
from PIL import Image, ImageTk 
from tkinter import ttk # helps in stylish entry fill
from tkcalendar import * # pip install tkcalendar in cmd
import random
from time import strftime
from datetime import datetime
import mysql.connector # "pip install mysql-connector-python" in cmd
from tkinter import messagebox #for validation check

class DETAILS_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("DETAILS PAGE")
        self.root.geometry("1318x569+230+258") # window size
        self.root.resizable(False, False) # disables window resizing

    # =================variables for entering data(received from customer) in db in room details frame====================
        self.var_floor = StringVar()
        self.var_roomno = StringVar()
        self.var_roomtype = StringVar()

    # ================TITLE===================
        lbl_title = Label(self.root, text="ROOM DEPARTMENT", font=("arial", 20, "bold"), bg="blue", fg="white", bd=2, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1318, height=50)


         # ================1ST IMAGE LOGO===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\2_11.jpg") 
        img1 = img1.resize((100,50)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) 

        lblimg = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE) 
        lblimg.place(x=0, y=0, width=100, height=50)


        # ================LEFT LABEL FRAME===================
        lbl_frameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Add new room", padx=2, font=("arial", 12, "bold"))
        lbl_frameLeft.place(x=50, y=60, width=540, height=350)


        # ===============room add details in left label frame================
        #Floor
        lbl_floor = Label(lbl_frameLeft, text="Floor", padx=20, pady=10, font=("arial", 12, "bold")) #label
        lbl_floor.grid(row=0, column=0, sticky=W)
        floor_entry = ttk.Entry(lbl_frameLeft, width=20, font=("arial", 13, "bold"), textvariable=self.var_floor) # box for entry
        floor_entry.grid(row=0, column=1, sticky=W)        
        
        #available room
        lbl_room_no = Label(lbl_frameLeft, text="Room no. ", padx=20, pady=6, font=("arial", 12, "bold")) #label
        lbl_room_no.grid(row=1, column=0, sticky=W)
        room_no_entry = ttk.Entry(lbl_frameLeft, width=20, font=("arial", 13, "bold"), textvariable=self.var_roomno) # box for entry
        room_no_entry.grid(row=1, column=1)
        
        #room type
        lbl_roomtype = Label(lbl_frameLeft, text="Room type", padx=20, pady=6, font=("arial", 12, "bold")) #label
        lbl_roomtype.grid(row=2, column=0, sticky=W)
        roomtype_combo = ttk.Combobox(lbl_frameLeft, width=18, font=("arial", 13, "bold"), state="readonly", textvariable=self.var_roomtype) #state readonly disables text entry
        roomtype_combo["value"] = ("Single", "Double", "Luxury")
        roomtype_combo.current(0) #sets current value; no issue if not written
        roomtype_combo.grid(row=2, column=1)

         # ==================BUTTONS IN LFT LBL FRAME===============
        btn_frame = Frame(lbl_frameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=5, y=150, width=395, height=32)

        btn1 = Button(btn_frame, text="Add", command=self.add_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn1.grid(row=0, column=0, padx=1)

        btn2 = Button(btn_frame, text="Update", command=self.update_values, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn2.grid(row=0, column=1, padx=1)

        btn3 = Button(btn_frame, text="Delete", command=self.delete_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn3.grid(row=0, column=2, padx=1)

        btn4 = Button(btn_frame, text="Reset", command=self.reset_data, width=10, font=("arial", 11, "bold"), bg="blue", fg="white", bd=0, cursor="hand1")
        btn4.grid(row=0, column=3, padx=1)

        # ================RIGHT LABEL FRAME===================
        dtls_tbl = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM DETAILS", padx=2, font=("arial", 12, "bold"))
        dtls_tbl.place(x=650, y=60, width=600, height=350)

        #scrollbar
        scroll_x = ttk.Scrollbar(dtls_tbl, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(dtls_tbl, orient=VERTICAL)

        self.details_tbl = ttk.Treeview(dtls_tbl, column= ("floor", "room_no","room type"), 
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.details_tbl.xview)
        scroll_y.config(command=self.details_tbl.yview)

        self.details_tbl.heading("floor", text="Floor") # initial "" must be same as written in line 154 in column part
        self.details_tbl.heading("room_no", text="Room no.")
        self.details_tbl.heading("room type", text="Roomtype")

        self.details_tbl["show"] = "headings"

        self.details_tbl.column("floor", width=100) # inital "" must be same as written in line 154 in column part
        self.details_tbl.column("room_no", width=100)
        self.details_tbl.column("room type", width=100)

        self.details_tbl.pack(fill=BOTH, expand=1)
        self.details_tbl.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_db_data()

    #====================INSERT ADDED DATA INTO TABLE==============
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "" :
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                mycursor.execute("insert into project_room_details_table values(%s, %s, %s)", 
                                (self.var_floor.get(), self.var_roomno.get(), self.var_roomtype.get()) )
                
                conn.commit()
                self.fetch_db_data()
                conn.close()
            
                messagebox.showinfo("Success", "Room Details added successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Warning", "Something went wrong: {str(es)}", parent = self.root)

    #======================fetches data from db and displays on window==============================
    def fetch_db_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
        mycursor = conn.cursor()
        mycursor.execute("select * from project_room_details_table")
        result = mycursor.fetchall()
        if len(result)!=0:
            self.details_tbl.delete(*self.details_tbl.get_children())
            for i in result :
                self.details_tbl.insert("", END, values=i)
        conn.commit()
        conn.close()  


    #=====================displays values in lft frame when clicked on data in right frame so as for updation=====================
    def get_cursor(self, event=""):
        cursor_result = self.details_tbl.focus()
        content = self.details_tbl.item(cursor_result)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])

        messagebox.showinfo("Information", "Room no. cannot be updated", parent=self.root)


    # ========================updates db values ===============================
    # ===============UPDATE BUTTON ===========================
    def update_values(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                mycursor.execute("update project_room_details_table set floor=%s, room_type=%s where room_no=%s",
                                (self.var_floor.get(), self.var_roomtype.get(), self.var_roomno.get()))
                
                conn.commit()
                self.fetch_db_data()
                conn.close()
                messagebox.showinfo("Success", "Updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Warning", "Something went wrong: {str(es)}", parent = self.root)

    
    # ==========================DELETE BUTTON=======================
    def delete_data(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "":
            messagebox.showerror("Error", "Empty field", parent=self.root) # parent is the name of window in which we want to display message
        else:
            delete = messagebox.askyesno("Question","Do you really want to delete this entry", parent = self.root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="singla123", database="gcs_2022" )
                mycursor = conn.cursor()
                query = "delete from project_room_details_table where room_no=%s"
                value = (self.var_roomno.get(),)
                mycursor.execute(query, value)
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_db_data()
            conn.close()

    # =========================RESET BUTTON====================
    def reset_data(self):
        self.var_floor.set("")
        self.var_roomno.set("")
   
if __name__ == "__main__":
    root = Tk()
    obj = DETAILS_PAGE(root)
    root.mainloop()