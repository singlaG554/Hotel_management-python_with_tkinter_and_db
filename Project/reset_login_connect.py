from tkinter import* # for GUI with python
from PIL import Image, ImageTk #write "pip install pillow" in cmd ; imports images
from tkinter import ttk # helps in stylish entry fill
from tkinter import messagebox #for validation check
#from login import LOGIN_PAGE


class RESETCONNECT_PAGE:
    def __init__(self, root): #constructor
        self.root=root
        self.root.title("Login page")
        self.root.geometry("200x100+674+380") # window size
        self.root.resizable(False, False) # disables window resizing
        messagebox.showinfo("Success", "Password updated successfully", parent=self.root)
        self.new_window = Toplevel(self.root)
        #self.app = LOGIN_PAGE(self.new_window)
        

# creates window for the project
if __name__ == "__main__":
    root = Tk()
    obj = RESETCONNECT_PAGE(root)
    root.mainloop()