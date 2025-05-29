from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help")

        title_lbl = Label(
            self.root,
            text="💻 HELP 💻",
            font=("times new roman", 28, "bold"),  
            bg="white",
            fg="#2E8B57", 
            relief="groove", 
            bd=3,  
            padx=10,  
            pady=5
        )
        title_lbl.place(x=0, y=0, width=1366, height=42)

        img_top = Image.open("D:\\Projects\\Face_Attendance\\images\\chat.jpg")
        img_top = img_top.resize((1366,700),Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=42,width = 1366, height = 700)

        dev_label = Label(f_lbl, text="Email: sidhuarshdeep643@gmail.com ", font=("times new roman", 20, "bold", "underline"), bg="white", fg="black")
        dev_label.place(x=0, y=5)



if __name__=="__main__":
    root=Tk()
    obj = Help(root)
    root.mainloop()

