from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from tkinter import messagebox
import sqlite3
import cv2 
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class Face_recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root,
            text="💻 FACE RECOGNITION💻",
            font=("times new roman", 28, "bold"),  # Modernized font
            bg="white",
            fg="#2E8B57",  # Change to a pleasant green color
            relief="groove",  # Adds depth (3D border)
            bd=3,  # Border thickness
            padx=10,  # Padding for better spacing
            pady=5
        )
        title_lbl.place(x=0, y=0, width=1366, height=42)
       
        # Left Image
        img_left = Image.open("D:\\Projects\\Face_Attendance\\images\\face_detector1.jpg")
        img_left = img_left.resize((660,610),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root,image = self.photoimg_left)
        f_lbl.place(x=0,y=42,width = 660, height = 610)
        
        # Right Image
        img_right = Image.open("D:\\Projects\\Face_Attendance\\images\\facial_recognition_right_image.jpg")
        img_right = img_right.resize((750,610),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root,image = self.photoimg_right)
        f_lbl.place(x=620,y=42,width =750, height = 610)

        b1_1 = Button(f_lbl, text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman", 14, "bold"),bg="darkgreen", fg="white" )
        b1_1.place(x=270,y=540,width=200,height=35) 

    # Mark Attendance
    def mark_attendance(self,d,n,s,r):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((d not in name_list) and (n not in name_list) and (s not in name_list) and (r not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{d},{n},{s},{r},{dtString},{d1},Present")



    # Face Recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coords = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                face_img = gray_image[y:y + h, x:x + w]
                if face_img.size == 0:
                    return img  # or skip/continue

                id, pred = clf.predict(face_img)

                confidence = int(100 * (1 - pred / 300))

                conn = mysql.connector.connect(
                        host="localhost",
                        port="3306",
                        user="root",
                        password="sidhu1234@deep",
                        database="face_recognizer",
                        ssl_disabled=True
                    )

                my_cursor = conn.cursor()

                # Safely fetch data from the database

                my_cursor.execute("SELECT student_id FROM student WHERE student_id ="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(str(val) for val in d) if d else "Unknown"

                my_cursor.execute("SELECT student_name FROM student WHERE student_id ="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(str(val) for val in n) if n else "Unknown"

                my_cursor.execute("SELECT roll_no FROM student WHERE student_id ="+str(id))
                s = my_cursor.fetchone()
                s = "+".join(str(val) for val in s) if s else "Unknown"

                my_cursor.execute("SELECT department FROM student WHERE student_id ="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(str(val) for val in r) if r else "Unknown"
                self.mark_attendance(d,n,s,r)

                

                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {d}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No: {s}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {r}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coords = [x, y, w, h]

            return coords

        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        # Load classifiers and recognizer
        faceCascade = cv2.CascadeClassifier("D:/Projects/Face_Attendance/haarcascade_frontalface_default.xml")

        if faceCascade.empty():
            raise FileNotFoundError("Error loading haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        try:
            clf.read("classifier.xml")
        except cv2.error as e:
            raise FileNotFoundError("Error loading classifier.xml") from e

        # Video stream
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, img = video_capture.read()
            if not ret or img is None:
                print("Error: Unable to read video stream")
                continue

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        
        video_capture.release()
        cv2.destroyAllWindows()
    

if __name__=="__main__":
    root=Tk()
    obj = Face_recognition(root)
    root.mainloop()
