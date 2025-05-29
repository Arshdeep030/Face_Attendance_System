from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from tkinter import messagebox
import sqlite3
import cv2
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(
            self.root,
            text="💻 TRAIN DATASET💻",
            font=("times new roman", 28, "bold"),  # Modernized font
            bg="white",
            fg="#2E8B57",  # Change to a pleasant green color
            relief="groove",  # Adds depth (3D border)
            bd=3,  # Border thickness
            padx=10,  # Padding for better spacing
            pady=5
        )
        title_lbl.place(x=0, y=0, width=1366, height=40)


        img_top = Image.open("D:\\Projects\\Face_Attendance\\images\\facialrecognition.png")
        img_top = img_top.resize((1368,290),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=40,width = 1368, height = 290)

        b1_1 = Button(self.root, text="Train Data",command=self.train_classifier,cursor="hand2", font=("times new roman", 25, "bold"),bg="darkblue", fg="white" )
        b1_1.place(x=0,y=330,width=1368,height=40) 

        img_bottom = Image.open("D:\\Projects\\Face_Attendance\\images\\face_train_bottom.jpg")
        img_bottom = img_bottom.resize((1368,330),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image = self.photoimg_bottom)
        f_lbl.place(x=0,y=370,width = 1368, height = 330)

    def train_classifier(self):
        data_dir=("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imgNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imgNp)
            ids.append(id)
            
            cv2.imshow("Training",imgNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train the classifier and save the model
        
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!")
        


if __name__=="__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()