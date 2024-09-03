from tkinter import* # for GUI with python
from PIL import Image, ImageTk #write "pip install pillow" in cmd ; imports images
from login import LOGIN_PAGE

class SUCCESS_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1550x830+0+0") # window size
        self.root.resizable(False, False) # disables window resizing

        # ================BACKGROUND IMAGE ===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\registered.png") # r converts all backward slash to forward slash
        img1 = img1.resize((400,300)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) # converts into displayable format

        lblimg1 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE) #display image on window; lblimg means label image
        lblimg1.place(x=550, y=200, width=400, height=300)


        new_user_btn = Button(self.root, text="LOGIN", command=self.login_details,  border=0, width=10, font=("arial", 13, "bold", "underline"), fg="red", bd=0, cursor="hand1")
        new_user_btn.place(x=670, y=440, width=140)


    def login_details(self):
        self.new_window = Toplevel(self.root)
        self.app = LOGIN_PAGE(self.new_window)



# creates window for the project
if __name__ == "__main__":
    root = Tk()
    obj = SUCCESS_PAGE(root)
    root.mainloop()