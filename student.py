from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
   

        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_student_id = StringVar()
        self.var_student_name = StringVar()
        self.var_class_division = StringVar()
        self.var_roll_no = StringVar()
        self.var_gender = StringVar()
        self.var_DOB = StringVar()
        self.var_email = StringVar()
        self.var_phone_no = StringVar()
        self.var_address = StringVar()
        self.var_teacher_name = StringVar()

        # first image
        img = Image.open("D:\\Projects\\Face_Attendance\\images\\student_1.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 500, height = 120)
        
        # second image
        img1 = Image.open("D:\\Projects\\Face_Attendance\\images\\face-recognition.png")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=500,y=0,width = 500, height = 120)

        # third image
        img2 = Image.open("D:\\Projects\\Face_Attendance\\images\\student_2.jpg")
        img2 = img2.resize((550,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width = 550, height = 120)
        
        # bgimage
        imgbg = Image.open("D:\\Projects\\Face_Attendance\\images\\bg1.jpg")
        imgbg = imgbg.resize((1500,600),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimgbg = ImageTk.PhotoImage(imgbg)

        bg_img = Label(self.root,image = self.photoimgbg)
        bg_img.place(x=0,y=120,width = 1500, height = 600)


        # Title Label with Enhanced Visuals
        title_lbl = Label(
            bg_img,
            text="💻 STUDENT MANAGEMENT SYSTEM 💻",
            font=("times new roman", 28, "bold"),  
            bg="white",
            fg="#2E8B57", 
            relief="groove",  # Adds depth (3D border)
            bd=3,  
            padx=10,
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
            root.after(500, animate_text) 

        animate_text()

        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10,y=48,width=1340,height=515)

        # Left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=5,width=660,height=502)

        
        img_left = Image.open("D:\\Projects\\Face_Attendance\\images\\stud_details.jpg")
        img_left = img_left.resize((644,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width = 644, height = 100)

        # Current Course
        curr_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",11,"bold"))
        curr_course_frame.place(x=5,y=105,width=644,height=95)

        # Department
        dep_label = Label(curr_course_frame,text="Department",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_department,font=("times new roman",10,"bold"),width=15,state="readonly")
        dep_combo['values'] = ("Select Department","Computer","IT","Electronics","Electrical","Civil","Chemical","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course 
        course_label = Label(curr_course_frame,text="Course",font=("times new roman",11,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=15,state="readonly")
        course_combo['values'] = ("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)

        # Year
        year_label = Label(curr_course_frame,text="Year",font=("times new roman",11,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=15,state="readonly")
        year_combo['values'] = ("Select Year","2018-2019","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        # Semester
        sem_label = Label(curr_course_frame,text="Semester",font=("times new roman",11,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10)

        sem_combo = ttk.Combobox(curr_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=15,state="readonly")
        sem_combo['values'] = ("Select Semester","Semseter-1","Semseter-2","Semseter-3","Semseter-4","Semseter-5","Semseter-6","Semseter-7","Semseter-8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",11,"bold"))
        class_student_frame.place(x=5,y=200,width=644,height=278)
        
        # Student ID
        StudentId_label = Label(class_student_frame,text="Student ID:",font=("times new roman",11,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=4,sticky=W)

        StudentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_student_id,width=20,font=("times new roman",11,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=4,sticky=W)

        # Student name
        Studentname_label = Label(class_student_frame,text="Student Name:",font=("times new roman",11,"bold"),bg="white")
        Studentname_label.grid(row=0,column=2,padx=10,pady=4,sticky=W)

        Studentname_entry = ttk.Entry(class_student_frame,textvariable=self.var_student_name,width=20,font=("times new roman",11,"bold"))
        Studentname_entry.grid(row=0,column=3,padx=10,pady=4,sticky=W)

        # Class Division
        class_dev_label = Label(class_student_frame,text="Class Division:",font=("times new roman",11,"bold"),bg="white")
        class_dev_label.grid(row=1,column=0,padx=10,pady=4,sticky=W)

        

        class_dev_combo = ttk.Combobox(class_student_frame,textvariable= self.var_class_division,font=("times new roman",10,"bold"),width=20,state="readonly")
        class_dev_combo['values'] = ("Select Division","A","B","C","D")
        class_dev_combo.current(0)
        class_dev_combo.grid(row=1,column=1,padx=10,pady=4,sticky=W)

        # Roll no
        roll_no_label = Label(class_student_frame,text="Roll Number:",font=("times new roman",11,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=4,sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll_no, width=20,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=4,sticky=W)

        # Gender
        gender_label = Label(class_student_frame,text="Gender:",font=("times new roman",11,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=4,sticky=W)

        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=20,state="readonly")
        gender_combo['values'] = ("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=4,sticky=W)

        # DOB
        dob_label = Label(class_student_frame,text="DOB:",font=("times new roman",11,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=4,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_DOB,width=20,font=("times new roman",11,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=4,sticky=W)

        # Email
        email_label = Label(class_student_frame,text="Email:",font=("times new roman",11,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=4,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",11,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=4,sticky=W)

        # phone_no
        phone_label = Label(class_student_frame,text="Phone Number:",font=("times new roman",11,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=4,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",11,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=4,sticky=W)

        # Address
        address_label = Label(class_student_frame,text="Address:",font=("times new roman",11,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=4,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",11,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=4,sticky=W)

        # Teacher Name
        teacher_label = Label(class_student_frame,text="Teacher Name:",font=("times new roman",11,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=4,sticky=W)

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher_name, width=20,font=("times new roman",11,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=4,sticky=W)

        # Radio Buttons
        self.var_radio1 =  StringVar()
        radbutton1 = Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radbutton1.grid(row=5,column=0)
        
        radbutton2 = Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radbutton2.grid(row=5,column=1)

        # Button Frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=20,y=190,width=584,height=32)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",width=15,command=self.update_data,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",width=15,command=self.delete_data,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",width=15,command=self.reset_data,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=20,y=222,width=584,height=32)

        take_photo_btn = Button(btn_frame1,text="Take Photo Sample",command=self.generate_data_set,width=33,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",width=33,font=("times new roman",12,"bold"),bg="#2E8B57",fg="white")
        update_photo_btn.grid(row=0,column=1)
        



        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=680,y=5,width=660,height=502)

        img_right = Image.open("D:\\Projects\\Face_Attendance\\images\\student_3.jpg")
        img_right = img_right.resize((644,130),Image.Resampling.LANCZOS) #resize and converting high level img to low level img.
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width = 644, height = 100)

        # Search System
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",11,"bold"))
        Search_frame.place(x=5,y=105,width=644,height=60)

        search_label = Label(Search_frame,text="Search By:",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(Search_frame,font=("times new roman",10,"bold"),width=16,state="read only")
        search_combo['values'] = ("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        search_entry = ttk.Entry(Search_frame,width=16,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=3,sticky=W)

        search_btn = Button(Search_frame,text="Search",width=10,font=("times new roman",11,"bold"),bg="#2E8B57",fg="white")
        search_btn.grid(row=0,column=3,padx=3)

        showAll_btn = Button(Search_frame,text="Show All",width=10,font=("times new roman",11,"bold"),bg="#2E8B57",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

        # Table Frame
        table_frame =Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=168,width=644,height=310)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("department","course","year","semester","student_id","student_name","class_division","roll_no","gender","DOB","email","phone_no","address","teacher_name","photo_sample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("student_id",text="Student ID")
        self.student_table.heading("student_name",text="Name")
        self.student_table.heading("class_division",text="Division")
        self.student_table.heading("roll_no",text="Roll Number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone_no",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher_name",text="Teacher")
        self.student_table.heading("photo_sample",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("student_id",width=100)
        self.student_table.column("student_name",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("class_division",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher_name",width=100)
        self.student_table.column("photo_sample",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor) 
        self.fetch_data()

    # Function declaration
    def add_data(self):
        if self.var_department.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_semester.get()=="" or self.var_student_id.get()=="" or self.var_student_name.get()=="" or self.var_class_division.get()=="" or self.var_roll_no.get()==""or self.var_gender.get() == "" or self.var_DOB.get()=="" or self.var_email.get()==""or self.var_phone_no.get()=="" or self.var_address.get()=="" or self.var_teacher_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try: 
                conn = mysql.connector.connect(host="localhost",port="3306", user="root", password="sidhu1234@deep",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_student_id.get(),
                    self.var_student_name.get(),
                    self.var_class_division.get(),
                    self.var_roll_no.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_email.get(),
                    self.var_phone_no.get(),
                    self.var_address.get(),
                    self.var_teacher_name.get(),
                    self.var_radio1.get()    ))     

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)    
            # if we dont use except statement, will get error
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)        
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",port="3306", user="root", password="sidhu1234@deep",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")  
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # when we click on table data left table will be filled with this data
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        if data and len(data) > 0:
            self.var_department.set(data[0])
        else:
            # Fallback or error message
            print("No data returned for department")
            self.var_department.set("")  # or some default value

        self.var_department.set(data[0])        
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_student_id.set(data[4])
        self.var_student_name.set(data[5])
        self.var_class_division.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gender.set(data[8])
        self.var_DOB.set(data[9])
        self.var_email.set(data[10])
        self.var_phone_no.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher_name.set(data[13])
        self.var_radio1.set(data[14])    

    # Update function
    def update_data(self):
        if self.var_department.get()=="" or self.var_course.get()=="" or self.var_year.get()=="" or self.var_semester.get()=="" or self.var_student_id.get()=="" or self.var_student_name.get()=="" or self.var_class_division.get()=="" or self.var_roll_no.get()==""or self.var_gender.get() == "" or self.var_DOB.get()=="" or self.var_email.get()==""or self.var_phone_no.get()=="" or self.var_address.get()=="" or self.var_teacher_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",port="3306", user="root", password="sidhu1234@deep",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set department=%s,course=%s,year=%s,semester=%s,student_name=%s,class_division=%s,roll_no =%s, gender = %s, DOB=%s,email=%s,phone_no=%s,address=%s,teacher_name=%s,photo_sample=%s where student_id=%s",(
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_student_name.get(),
                        self.var_class_division.get(),
                        self.var_roll_no.get(),
                        self.var_gender.get(),
                        self.var_DOB.get(),
                        self.var_email.get(),
                        self.var_phone_no.get(),
                        self.var_address.get(),
                        self.var_teacher_name.get(),
                        self.var_radio1.get(), 
                        self.var_student_id.get()
                        )) 
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",port="3306", user="root", password="sidhu1234@deep",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def reset_data(self):
        self.var_department.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_student_id.set("")
        self.var_student_name.set("")
        self.var_class_division.set("")
        self.var_roll_no.set("")
        self.var_gender.set("")
        self.var_DOB.set("")    
        self.var_email.set("")
        self.var_phone_no.set("")
        self.var_address.set("")
        self.var_teacher_name.set("")
        self.var_radio1.set("")

    def generate_data_set(self):
        if (
            self.var_department.get() == "" or
            self.var_course.get() == "" or
            self.var_year.get() == "" or
            self.var_semester.get() == "" or
            self.var_student_id.get() == "" or
            self.var_student_name.get() == "" or
            self.var_class_division.get() == "" or
            self.var_roll_no.get() == "" or
            self.var_gender.get() == "" or
            self.var_DOB.get() == "" or
            self.var_email.get() == "" or
            self.var_phone_no.get() == "" or
            self.var_address.get() == "" or
            self.var_teacher_name.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost",
                    port="3306",
                    user="root",
                    password="sidhu1234@deep",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()

                # Use student_id directly from the input field
                id = self.var_student_id.get()  # This gives the unique student_id

                # Fetch current student details for the given student_id
                my_cursor.execute("SELECT * FROM student WHERE student_id = %s", (id,))
                myresult = my_cursor.fetchone()  # Fetch data for the specific student

                if myresult:
                    # Update student record
                    my_cursor.execute(
                        """
                        UPDATE student SET 
                        department=%s, course=%s, year=%s, semester=%s,
                        student_name=%s, class_division=%s, roll_no=%s,
                        gender=%s, DOB=%s, email=%s, phone_no=%s,
                        address=%s, teacher_name=%s, photo_sample=%s
                        WHERE student_id=%s
                        """,
                        (
                            self.var_department.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_student_name.get(),
                            self.var_class_division.get(),
                            self.var_roll_no.get(),
                            self.var_gender.get(),
                            self.var_DOB.get(),
                            self.var_email.get(),
                            self.var_phone_no.get(),
                            self.var_address.get(),
                            self.var_teacher_name.get(),
                            self.var_radio1.get(),
                            id
                        )
                    )

                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # Load face detection model
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            return img[y:y+h, x:x+w]

                    # Open camera
                    cap = cv2.VideoCapture(0)
                    img_id = 0

                    while True:
                        ret, my_frame = cap.read()
                        cropped_face = face_cropped(my_frame)
                        if cropped_face is not None:
                            img_id += 1
                            face = cv2.resize(cropped_face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            # Use the student_id in the image path to avoid overwrite
                            file_path = f"data/user.{id}.{img_id}.jpg"
                            cv2.imwrite(file_path, face)
                            cv2.putText(
                                face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2
                            )
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data set completed")

                else:
                    messagebox.showerror("Error", "Student not found in the database", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()