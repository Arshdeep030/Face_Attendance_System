from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import numpy as np
from tkinter import filedialog


mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Management System")

        self.var_atten_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()


        # first image
        img = Image.open("D:\\Projects\\Face_Attendance\\images\\smart-attendance.jpg")
        img = img.resize((685,150),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 685, height = 150)
        
        # second image
        img1 = Image.open("D:\\Projects\\Face_Attendance\\images\\clg.jpg")
        img1 = img1.resize((685,150),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=685,y=0,width = 685, height = 150)

        # bgimage
        imgbg = Image.open("D:\\Projects\\Face_Attendance\\images\\bg1.jpg")
        imgbg = imgbg.resize((1370,568),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image = self.photoimgbg)
        bg_img.place(x=0,y=150,width = 1370, height = 750)

        # Title Label with Enhanced Visuals
        title_lbl = Label(
            bg_img,
            text="💻 ATTENDANCE MANAGEMENT SYSTEM 💻",
            font=("times new roman", 28, "bold"),  # Modernized font
            bg="white",
            fg="#2E8B57",  # Change to a pleasant green color
            relief="groove",  # Adds depth (3D border)
            bd=3,  # Border thickness
            padx=10,  # Padding for better spacing
            pady=5
        )
        title_lbl.place(x=0, y=0, width=1530, height=40)

        # Adding a dynamic underline animation
        def animate_text():
            current_text = title_lbl.cget("text")
            if not current_text.endswith("_"):
                title_lbl.config(text=current_text + "_")
            else:
                title_lbl.config(text=current_text[:-1])
            root.after(500, animate_text)  # Call every 500ms

        animate_text()

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=0,y=38,width=1370,height=490)


        # Left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=0,y=0,width=670,height=475)

        

        img_left = Image.open("D:\\Projects\\Face_Attendance\\images\\face-recognition.png")
        img_left = img_left.resize((644,100),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 644, height = 100)

        left_inside_frame = Frame(Left_frame,relief=RIDGE,bg="white",bd=2)
        left_inside_frame.place(x=0,y=110,width=650,height=340)

        # Attendance ID
        attendanceId_label = Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=4,sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",11,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=4,sticky=W)

        # Roll
        roll_label = Label(left_inside_frame,text="Roll:",font=("times new roman",11,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=4,sticky=W)

        roll_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_roll,font=("times new roman",11,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=4,sticky=W)

        # Name
        name_label = Label(left_inside_frame,text="Name:",font=("times new roman",11,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=4,sticky=W)

        name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("times new roman",11,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=4,sticky=W)

        # Deapartment
        dep_label = Label(left_inside_frame,text="Department:",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=4,sticky=W)

        dep_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dep,font=("times new roman",11,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=4,sticky=W)

        # Time
        time_label = Label(left_inside_frame,text="Time:",font=("times new roman",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=4,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("times new roman",11,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=4,sticky=W)

        # Date
        date_label = Label(left_inside_frame,text="Date:",font=("times new roman",11,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=4,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("times new roman",11,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=4,sticky=W)

    
        attendance_label = Label(left_inside_frame,text="Attendance Status:",font=("times new roman",11,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)


        attendance_combo = ttk.Combobox(left_inside_frame,font=("times new roman",10,"bold"),textvariable=self.var_attendance,width=20,state="readonly")
        attendance_combo['values'] = ("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=10,pady=4,sticky=W)

        # Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=20,y=280,width=584,height=32)

        import_btn = Button(btn_frame,text="Import",width=15,command=self.importCsv,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text="Export",width=15,command=self.exportCsv,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        export_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",width=15,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",width=15,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        reset_btn.grid(row=0,column=3)

        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=0,width=680,height=475)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=662,height=440)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("attendance_id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("attendance_id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")  
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")


        self.AttendanceReportTable['show'] = 'headings'
        self.AttendanceReportTable.column("attendance_id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # Fetch Data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert('',END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    
    # when we click on table it will shows that data in left frame
    def get_cursor(self, event=""):
      cursor_row = self.AttendanceReportTable.focus()
      content = self.AttendanceReportTable.item(cursor_row)
      row = content["values"]
      self.var_atten_id.set(row[0])
      self.var_roll.set(row[1])
      self.var_name.set(row[2])
      self.var_dep.set(row[3])
      self.var_time.set(row[4])
      self.var_date.set(row[5])
      self.var_attendance.set(row[6])

    def reset(self):
        self.var_atten_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("") 
    
    def delete(self):
        pass
      



if __name__=="__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()
