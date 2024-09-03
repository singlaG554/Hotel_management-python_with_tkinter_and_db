from tkinter import* # for GUI with python
from PIL import Image, ImageTk #write "pip install pillow" in cmd ; imports images


class LOGOUT_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1550x830+0+0") # window size
        self.root.resizable(False, False) # disables window resizing

        # ================BACKGROUND IMAGE ===================
        img1 = Image.open(r"C:\Users\RS\OneDrive\Desktop\Project\Images\logout.png") # r converts all backward slash to forward slash
        img1 = img1.resize((580,250)) 
        self.photoimg1 = ImageTk.PhotoImage(img1) # converts into displayable format

        lblimg1 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE) #display image on window; lblimg means label image
        lblimg1.place(x=480, y=200, width=580, height=250)

# creates window for the project
if __name__ == "__main__":
    root = Tk()
    obj = LOGOUT_PAGE(root)
    root.mainloop()