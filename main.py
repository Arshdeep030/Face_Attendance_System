from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from tkinter import messagebox
import sqlite3
import cv2 # Open Source Computer Vision Library
import numpy as np
from time import strftime
from datetime import datetime
from face_recognition import Face_recognition
from attendance import Attendance
from help import Help
import webbrowser
from train import Train

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        self.student_window = None
        self.train_window = None
        self.face_window = None
        self.attendance_window = None
        self.help_window = None

        
        # first image
        img = Image.open("D:\\Projects\\Face_Attendance\\images\\Stanford.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 500, height = 130)
        
        # second image
        img1 = Image.open("D:\\Projects\\Face_Attendance\\images\\facialrecognition.png")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=500,y=0,width = 500, height = 130) 

        # third image
        img2 = Image.open("D:\\Projects\\Face_Attendance\\images\\university.jpg")
        img2 = img2.resize((550,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width = 550, height = 130)
       


        # bgimage
        imgbg = Image.open("D:\\Projects\\Face_Attendance\\images\\BestFacialRecognition.jpg")
        imgbg = imgbg.resize((1530,710),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image = self.photoimgbg)
        bg_img.place(x=0,y=130,width = 1530, height = 600)


        # Title Label with Enhanced Visuals
        title_lbl = Label(
            bg_img,
            text="💻 FACE RECOGNITION ATTENDANCE SYSTEM 💻",
            font=("times new roman", 28, "bold"), 
            bg="white",
            fg="#2E8B57",  
            relief="groove", 
            bd=3,  
            padx=10,  
            pady=5
        )
        title_lbl.place(x=0, y=0, width=1530, height=50)

        # Adding a dynamic underline animation
        def animate_text():
            current_text = title_lbl.cget("text")
            if not current_text.endswith("_"):
                title_lbl.config(text=current_text + "_")
            else:
                title_lbl.config(text=current_text[:-1])
            root.after(500, animate_text)  # Call every 500ms

        animate_text()


        # student button
        img4 = Image.open("D:\\Projects\\Face_Attendance\\images\\student.jpg")
        img4 = img4.resize((150,150),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image = self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)

        
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=200,y=250,width=150,height=35)

        # detect face button 
        img5 = Image.open("D:\\Projects\\Face_Attendance\\images\\face_detector1.jpg")
        img5 = img5.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img, image = self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=450,y=100,width=150,height=150)

        
        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,font=("times new roman", 15, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=450,y=250,width=150,height=35)

        
         # Attendance face button 
        img6 = Image.open("D:\\Projects\\Face_Attendance\\images\\attendance.png")
        img6 = img6.resize((150,150),Image.Resampling.LANCZOS) 
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image = self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=150,height=150)

        
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=700,y=250,width=150,height=35)

        # Help Button
        img7 = Image.open("D:\\Projects\\Face_Attendance\\images\\help.jpg")
        img7 = img7.resize((150,150),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img, image = self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=950,y=100,width=150,height=150)
        
        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=950,y=250,width=150,height=35)

        # Train Face Button
        img8 = Image.open("D:\\Projects\\Face_Attendance\\images\\Train.jpg")
        img8 = img8.resize((150,150),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img, image = self.photoimg8, cursor="hand2")
        b1.place(x=315,y=330,width=150,height=150)
        
        b1_1 = Button(bg_img, text="Train", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=315,y=480,width=150,height=35)

        # Photos Face Button
        img9 = Image.open("D:\\Projects\\Face_Attendance\\images\\opencv_face_reco_more_data.jpg")
        img9 = img9.resize((150,150),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img, image = self.photoimg9, cursor="hand2")
        b1.place(x=565,y=330,width=150,height=150)
        
        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=565,y=480,width=150,height=35)

        

         # Exit Button
        img11 = Image.open("D:\\Projects\\Face_Attendance\\images\\exit.jpg")
        img11 = img11.resize((150,150),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img, image = self.photoimg11, cursor="hand2",command=self.iexit, )
        b1.place(x=815,y=330,width=150,height=150)
        
        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iexit, font=("times new roman", 15, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=815,y=480,width=150,height=35)  

    
    # Function to open the images folder
    def open_img(self):
        os.startfile("data")
    
    # Exit Function
    def iexit(self):    
        self.iexit = messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return

    # Function Buttons
    def student_details(self):
        if self.student_window is None or not self.student_window.winfo_exists():
            self.student_window = Toplevel(self.root)
            self.app = Student(self.student_window)
        else:
            self.student_window.lift()
            self.student_window.focus_force()


    def train_data(self):
        if self.train_window is None or not self.train_window.winfo_exists():
            self.train_window = Toplevel(self.root)
            self.app = Train(self.train_window)
        else:
            self.train_window.lift()
            self.train_window.focus_force()

    def face_data(self):
        if self.face_window is None or not self.face_window.winfo_exists():
            self.face_window = Toplevel(self.root)
            self.app = Face_recognition(self.face_window)
        else:
            self.face_window.lift()
            self.face_window.focus_force()

    def attendance_data(self):
        if self.attendance_window is None or not self.attendance_window.winfo_exists():
            self.attendance_window = Toplevel(self.root)
            self.app = Attendance(self.attendance_window)
        else:
            self.attendance_window.lift()
            self.attendance_window.focus_force()

    def help_data(self):
        if self.help_window is None or not self.help_window.winfo_exists():
            self.help_window = Toplevel(self.root)
            self.app = Help(self.help_window)
        else:
            self.help_window.lift()
            self.help_window.focus_force()


if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()