from tkinter import *
from tkinter import font, ttk, messagebox, simpledialog
from PIL import ImageTk, Image 
import time
import customtkinter
import os
import sqlite3
from time import strftime
import calendar
import pandas as pd
import csv
from tkinter import filedialog
import collections
from collections import defaultdict
import shutil
import datetime
import mysql.connector
import mysql.connector as mysql
from mysql.connector import Error
attemptadmin = 0
attempuser= 0
sched_id = 0

conn = mysql.connect(host='sql6.freemysqlhosting.net',port='3306', database='sql6584558', user='sql6584558', password='ZalIZx2tmG')
			

w=Tk()

#Using piece of code from old splash screen
width_of_window = 1000
height_of_window = 500
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar


Frame(w, width=1000, height=500).place(x=0,y=0)
img= (Image.open("pic/1.png"))
resized_image_splash= img.resize((1000,500))
photo= ImageTk.PhotoImage(resized_image_splash)

image_a=ImageTk.PhotoImage(Image.open('pic/dot2.png'))
image_b=ImageTk.PhotoImage(Image.open('pic/dot1.png'))


# for i in range(5):
#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#     # loading text
#     label2=Label(w, text='Loading', fg='white', bg='#dab015') #decorate it 
#     label2.configure(font=("Calibri", 17))
#     label2.place(x=10,y=465)
#     # background image
#     label = Label(w, image = photo)
#     label.pack()
#     # loading dot animation
#     l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=90, y=480)
#     l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=110, y=480)
#     l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=130, y=480)
#     l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=150, y=480)
#     w.update_idletasks()
#     time.sleep(0.5)

#new window to open
def new_win():
	customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
	customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


	main_window=customtkinter.CTk()
	main_window.title('main window')

	width_of_main_window = 1362
	height_of_main_window = 692
	main_window_width = main_window.winfo_screenwidth()
	main_window_height = main_window.winfo_screenheight()
	x_main_window = (main_window_width/2)-(width_of_main_window/2 )
	y_main_window = (main_window_height/2)-(height_of_main_window/2)
	main_window.geometry("%dx%d+%d+%d" %(width_of_main_window,height_of_main_window,x_main_window,y_main_window))


	# main_window.geometry('1362x692')
	# main_window.state('zoomed')
	main_window.resizable(False,False)
	# main_window.rowconfigure(0, weight=2)
	# main_window.columnconfigure(1, weight=1)
	
	page1 = Frame(main_window)
	page2 = Frame(main_window)
	page3 = Frame(main_window)
	page4 = Frame(main_window)
	attendance_record = Frame(main_window)
	faculty_information = Frame(main_window)
	mathematics_att_record = Frame(main_window)
	employee_login = Frame(main_window)
	attendance_monitoring = Frame(main_window)
	developers = Frame(main_window)
	about = Frame(main_window)
	about_clg_goal = Frame(main_window)
	about_program= Frame(main_window)
	psychology_att_record = Frame(main_window)
	applied_physics_att_record = Frame(main_window)
	ite_att_record = Frame(main_window)
	create_account = Frame(main_window)
	class_moniroting = Frame(main_window)


	for frame in (page1, page2, page3, page4, attendance_record,faculty_information,mathematics_att_record,employee_login,attendance_monitoring,developers,about,about_clg_goal,about_program,psychology_att_record,applied_physics_att_record,ite_att_record,create_account,class_moniroting):
		frame.grid(row=0, column=0, sticky='nsew')

	def show_frame(frame):
		frame.tkraise()

	show_frame(attendance_record)

    # ============= Page 1 Frame =========================================================================================================================================
	def reverse(tuples):
		new_tup = tuples[::-1]
		return new_tup


        # open background image
	page1.pg1_image = Image.open('pic/2.png')
	page1.pg1_resize_image = page1.pg1_image.resize((1362, 692))
	page1.photo = ImageTk.PhotoImage(page1.pg1_resize_image)
	page1.pg1_bg_img_lb = Label(page1, image = page1.photo)
	page1.pg1_bg_img_lb.pack()

	    # Login Button
	pg1_login_img_btn = PhotoImage(file = "pic/btn_login.png")
	pg1_button_admin = Button(page1,image=pg1_login_img_btn, borderwidth=0, bg='#1f2a76',command=lambda: show_frame(page3))
	pg1_button_admin.place(x=99, y=422)

	    # Biomettric Button
	biometric_img_btn = PhotoImage(file = "pic/bttn_biometric.png")
	pg1_button_bio = Button(page1,image=biometric_img_btn, borderwidth=0,bg='#1f2a76', command=lambda: show_frame(page2))
	pg1_button_bio.place(x=99, y=256)

############################################################################### Sign In Part ###################################################################################################################################


	# ======== Page 3 Admin Sign In Frame ====================================================================================================================================

	    # open background image
	page3.pg3_image = Image.open('pic/4.png')
	page3.pg3_resize_image = page3.pg3_image.resize((1362, 692))
	page3.photo = ImageTk.PhotoImage(page3.pg3_resize_image)
	page3.pg3_bg_img_lb = Label(page3, image = page3.photo)
	page3.pg3_bg_img_lb.pack()

		# Text Box Username and Password
	username_lbl_pg3 = Label(page3, text='Username', fg='Black', bg ='#1f2a76', font = "Heltvetica 27 bold")
	username_lbl_pg3.place(x=116, y=207)
	pg3_txtbox_username = Entry(page3, borderwidth=0, width=16, font=('Arial',30))
	# pg3_txtbox_username.insert(0,"Username")
	pg3_txtbox_username.place(x=116, y=256, height=92)

	password_lbl_pg3 = Label(page3, text='Password', fg='Black', bg ='#1f2a76', font = "Heltvetica 27 bold")
	password_lbl_pg3.place(x=116, y=370)
	pg3_txtbox_pass = Entry(page3, borderwidth=0, width=16, font=('Arial', 30), show='*')
	# pg3_txtbox_pass.insert(0,"Password")
	pg3_txtbox_pass.place(x=116, y=422, height=90)

	def check_duplicate_Username_admin():
		Username = pg3_txtbox_username.get()
		
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(Username) + "'")
		records = cursor.fetchone()

		if records is not None:
		    return True
		else:
		    return False

		conn.commit()

	def check_duplicate_Pass_admin():
		Password = pg3_txtbox_pass.get()
		
		cursor = conn.cursor()

		cursor.execute("SELECT * FROM faculty_data WHERE Password = '" + str(Password) + "'")
		records = cursor.fetchone()

		if records is not None:
		    return True
		else:
		    return False

		conn.commit()

	def verify_admin():
		try:
			if conn.is_connected():
			    
				cursor = conn.cursor()
				getinact = conn.cursor()

				# cursor.execute("""CREATE TABLE IF NOT EXISTS  `faculty_data` (
				# 						  `ID` int(11) NOT NULL,
				# 						  `Employee_Number` text(100) CHARACTER SET utf8 NOT NULL,
				# 						  `Employee_Name` text(100) CHARACTER SET utf8 NOT NULL,
				# 						  `Department` text(100) CHARACTER SET utf8 NOT NULL,
				# 						  `Status` text(100) CHARACTER SET utf8 NOT NULL,
				# 						  `Username` text(100) CHARACTER SET utf8 NOT NULL,
				# 						  `Password` text(100) CHARACTER SET utf8 NOT NULL
				# 						) ENGINE=MyISAM DEFAULT CHARSET=latin1;""")

				# cursor.execute("INSERT INTO faculty_data (Employee_Number,Employee_Name,Department,Status,Username,Password) VALUES ('787567', 'rogem' , 'Mathematics','Activated', 'admin' , 'admin')")


				global attemptadmin 
				uname = pg3_txtbox_username.get()
				pwd = pg3_txtbox_pass.get()
				state = "Activated"

				getinact.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND Status ='Deactivated'")
				inactive = getinact.fetchone()

				if uname=='' or pwd=='':
					messagebox.showinfo("Error", "Please Fill The Empty Field!!")
				elif attemptadmin >=0 and attemptadmin <=2:
					cursor.execute("SELECT * FROM faculty_data WHERE Username = '" + str(uname) + "' AND  Password = '" + str(pwd) + "' AND Status ='" + str(state) + "'")
					if cursor.fetchone():
						show_frame(page4)
						messagebox.showinfo("Messgae", "WELCOME USER")

						pg3_txtbox_username.delete(0, END)
						pg3_txtbox_pass.delete(0, END)
						# check_button.deselect()

					elif inactive:
						messagebox.showinfo("Messgae", "Please inform the  Co-Admin to Activate your Account!!\nThank You!! ")
					elif check_duplicate_Username_admin()==False:
						# messagebox.showinfo("Error", "Username Is Incorrect!!")
						attemptadmin += 1
						count = 3 - attemptadmin
						messagebox.showinfo("Messge", "Username Is Incorrect!!\n\nReamaining Attempt: "+ str(count))
						pg3_txtbox_username.delete(0, END)
						pg3_txtbox_pass.delete(0, END)
						# check_button.deselect()
						return
					elif check_duplicate_Pass_admin()==False:
						# messagebox.showinfo("Error", "Password Is Incorrect!!")
						attemptadmin += 1
						count = 3 - attemptadmin
						messagebox.showinfo("Messge", "Password Is Incorrect!!\n\nReamaining Attempt: "+ str(count))
						pg3_txtbox_username.delete(0, END)
						pg3_txtbox_pass.delete(0, END)
						# check_button.deselect()
						return

					else:
						attemptadmin += 1
						count = 3 - attemptadmin
						messagebox.showinfo("Messge", "Please provide correct Username and Password!!\n\nReamaining Attempt: "+ str(count))
						pg3_txtbox_username.delete(0, END)
						pg3_txtbox_pass.delete(0, END)
				else:
					messagebox.showinfo("Error", "Access denied, Out of try!!\n\nYour Account has Deactivate!!\n\nPlease contact your Co-Admin!!")

		except Error as e:
		    print("Error while connecting to MySQL", e)
		

		conn.commit()
		conn.close()
		# try:
		# 	if conn.is_connected():
		# 	    db_Info = conn.get_server_info()
		# 	    print("Connected to MySQL Server version ", db_Info)
		# 	    show_frame(page4)
		# 	    # cursor = conn.cursor()
		# 	    # cursor.execute("select database();")
		# 	    # record = cursor.fetchone()
		# 	    # print("You're connected to database: ", record)

		# except Error as e:
		#     print("Error while connecting to MySQL", e)

	    
	

	    # Login Button
	login_img_btn = PhotoImage(file = "pic/login.png")
	pg3_button = Button(page3, image=login_img_btn, borderwidth=0, bg='#1f2a76', command=verify_admin)
	pg3_button.place(x=180, y=557)

	    # show and hide Password
	def show_password():
		if  pg3_txtbox_pass.cget('show') =='*':
			pg3_txtbox_pass.configure(show='')
		else:
			pg3_txtbox_pass.configure(show='*')
	check_button = Checkbutton(page3, text="show password",bg="#1f2a76", command=show_password, font="Arial", activebackground="#1f2a76",)
	check_button.place(x=116,y=520)

		# Back Button
	pg3_back = PhotoImage(file = "pic/btn_back_log.png")
	pg3_button_back = customtkinter.CTkButton(master=page3,image=pg3_back, text="" ,
	                                            corner_radius=5,bg_color='#e4b50b', fg_color="#e4b50b",hover_color="#006699", command=lambda: show_frame(page1))
	pg3_button_back.place(x=5, y=5, height=40,width=70)

############################################################################### Home Part ###################################################################################################################################


	# ============= Page 4 Home  Frame ====================================================================================================================

        # open background image
	page4.pg4_image = Image.open('pic/7.png')
	page4.pg4_resize_image = page4.pg4_image.resize((1362, 692))
	page4.photo = ImageTk.PhotoImage(page4.pg4_resize_image)
	page4.pg4_bg_img_lb = Label(page4, image = page4.photo)
	page4.pg4_bg_img_lb.pack()

	    # Admin Name Label
	pg4_lb_name = Label(page4, bg ='#ffffff', fg='#ffffff', font = "Heltvetica 9")
	pg4_lb_name.place(x=540, y=10)

	    # Admin Department Label
	pg4_lb_dept = Label(page4, bg ='#ffffff', fg='#ffffff', font = "Heltvetica 9")
	pg4_lb_dept.place(x=640, y=10)

	    # Faculty Information Button
	faculty_info_btn = PhotoImage(file = "pic/faculty_info.png")
	pg4_button_faculty = customtkinter.CTkButton(master=page4,image=faculty_info_btn, text="" ,
	                                            corner_radius=30,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(faculty_information))
	pg4_button_faculty.place(x=100, y=314, height=134,width=562)

	    # Class monitoring Button
	att_rec_btn = PhotoImage(file = "pic/classmonitoring.png")
	pg4_button_att_rec = customtkinter.CTkButton(master=page4,image=att_rec_btn, text="" ,
	                                            corner_radius=30,bg_color='#ffffff', fg_color="#cc9900",hover_color="#fdca34", command=lambda: show_frame(class_moniroting))
	pg4_button_att_rec.place(x=100, y=469, height=178,width=330)

	    # About Button
	about_btn = PhotoImage(file = "pic/about.png")
	pg4_button_photo = customtkinter.CTkButton(master=page4,image=about_btn, text="" ,
	                                            corner_radius=30,bg_color='#ffffff', fg_color="#cc9900",hover_color="#fdca34", command=lambda: show_frame(about))
	pg4_button_photo.place(x=456, y=469, height=178,width=197)

	    # Create Account Button
	create_btn = PhotoImage(file = "pic/btn_create_account.png")
	pg4_button_create = customtkinter.CTkButton(master=page4,image=create_btn, text="" ,
	                                            corner_radius=30,bg_color='#ffffff', fg_color="#cc9900",hover_color="#fdca34", command=lambda:show_frame(create_account))
	pg4_button_create.place(x=683, y=315, height=134,width=348)

	    # Attendace Record Button
	att_btn = PhotoImage(file = "pic/attendance_rec.png")
	pg4_button_atten = customtkinter.CTkButton(master=page4,image=att_btn, text="" ,
	                                            corner_radius=30,bg_color='#ffffff', fg_color="#cc9900",hover_color="#fdca34", command=lambda:show_frame(attendance_record))
	pg4_button_atten.place(x=683, y=469, height=178,width=348)

	    # Developers Button
	developers_btn = PhotoImage(file = "pic/developers.png")
	pg4_button_developers = customtkinter.CTkButton(master=page4,image=developers_btn, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(developers))
	pg4_button_developers.place(x=1048, y=314, height=134,width=246)

	# Logout Button
	logout_btn = PhotoImage(file = "pic/home_logout.png")
	pg4_button_logout = customtkinter.CTkButton(master=page4,image=logout_btn, text="" ,
	                                            corner_radius=30,bg_color='#ffffff', fg_color="#ffffff",hover_color="#6699cc", command=lambda: show_frame(page3))
	pg4_button_logout.place(x=1075, y=469, height=178,width=197)

	 # ============= Developers Frame ========================================================================================================================================

	    # open background image
	developers.dev_image = Image.open('pic/8a.png')
	developers.dev_resize_image = developers.dev_image.resize((1362, 692))
	developers.photo = ImageTk.PhotoImage(developers.dev_resize_image)
	developers.dev_bg_img_lb = Label(developers, image = developers.photo)
	developers.dev_bg_img_lb.pack()

	    # Back Button
	dev_back = PhotoImage(file = "pic/btn_back_page.png")
	dev_button_back = customtkinter.CTkButton(master=developers,image=dev_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	dev_button_back.place(x=45, y=595, height=50,width=140)

############################################################################### About Part ###################################################################################################################################


	# ============= About(the Collage) Frame ================================================================================================================================
	# #fcd24f
	    # open background image
	about.abt_image = Image.open('pic/9a.png')
	about.abt_resize_image = about.abt_image.resize((1362, 692))
	about.photo = ImageTk.PhotoImage(about.abt_resize_image)
	about.abt_bg_img_lb = Label(about, image = about.photo)
	about.abt_bg_img_lb.pack()

	    # Next Button
	next_btn = PhotoImage(file = "pic/btn_forward.png")
	button_next = customtkinter.CTkButton(master=about,image=next_btn, text="" ,
	                                            corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about_clg_goal))
	button_next.place(x=1250, y=320, height=100,width=100)

	    # Back Button
	abt_back = PhotoImage(file = "pic/btn_back_page.png")
	abt_button_back = customtkinter.CTkButton(master=about,image=abt_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	abt_button_back.place(x=20, y=595, height=50,width=140)

	# ============= About(Collage Goals) Frame ================================================================================================================================

	    # open background image
	about_clg_goal.abt_clg_goal_image = Image.open('pic/9b.png')
	about_clg_goal.abt_clg_goal_resize_image = about_clg_goal.abt_clg_goal_image.resize((1362, 692))
	about_clg_goal.abt_clg_goal_photo = ImageTk.PhotoImage(about_clg_goal.abt_clg_goal_resize_image)
	about_clg_goal.abt_clg_goal_bg_img_lb = Label(about_clg_goal, image = about_clg_goal.abt_clg_goal_photo)
	about_clg_goal.abt_clg_goal_bg_img_lb.pack()

	    # Next Button
	next_btn_abt_clg_goal = PhotoImage(file = "pic/btn_forward.png")
	abt_clg_goal_button_next = customtkinter.CTkButton(master=about_clg_goal,image=next_btn_abt_clg_goal, text="" ,
	                                            corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about_program))
	abt_clg_goal_button_next.place(x=1250, y=320, height=100,width=100)

	    # Back Button
	abt_clg_goal_back_btn = PhotoImage(file = "pic/btn_back.png")
	abt_clg_goal_button_back = customtkinter.CTkButton(master=about_clg_goal,image=abt_clg_goal_back_btn, text="" ,
	                                            corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about))
	abt_clg_goal_button_back.place(x=20, y=320, height=100,width=100)

	    # Back Button
	abt_clg_goal_back = PhotoImage(file = "pic/btn_back_page.png")
	abt_clg_goal_button_back = customtkinter.CTkButton(master=about_clg_goal,image=abt_clg_goal_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	abt_clg_goal_button_back.place(x=20, y=595, height=50,width=140)

	# ============= About(Collage Goals) Frame =================================================================================================================================

	    # open background image
	about_program.abt_prog_image = Image.open('pic/9c.png')
	about_program.abt_prog_resize_image = about_program.abt_prog_image.resize((1362, 692))
	about_program.abt_prog_photo = ImageTk.PhotoImage(about_program.abt_prog_resize_image)
	about_program.abt_prog_bg_img_lb = Label(about_program, image = about_program.abt_prog_photo)
	about_program.abt_prog_bg_img_lb.pack()

	    # Back Button
	abt_prog_back_btn = PhotoImage(file = "pic/btn_back.png")
	abt_prog_button_back = customtkinter.CTkButton(master=about_program,image=abt_prog_back_btn, text="" ,
	                                            corner_radius=6,fg_color="#ffffff",hover_color="#006699", command=lambda: show_frame(about_clg_goal))
	abt_prog_button_back.place(x=20, y=320, height=100,width=100)

	    # Back Button
	abt_prog_back = PhotoImage(file = "pic/btn_back_page.png")
	abt_prog_button_back = customtkinter.CTkButton(master=about_program,image=abt_prog_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	abt_prog_button_back.place(x=20, y=595, height=50,width=140)

############################################################################### Attendance Record Part ###################################################################################################################################


	# ============= Attendace Record Frame ======================================================================================================================================

        # open background image
	attendance_record.att_rec_image = Image.open('pic/8.png')
	attendance_record.att_rec_resize_image = attendance_record.att_rec_image.resize((1362, 692))
	attendance_record.photo = ImageTk.PhotoImage(attendance_record.att_rec_resize_image)
	attendance_record.att_rec_bg_img_lb = Label(attendance_record, image = attendance_record.photo)
	attendance_record.att_rec_bg_img_lb.pack()

	    # Mathematics Faculty Button
	math_fac_btn = PhotoImage(file = "pic/math_faculty.png")
	att_rec_button_math_fac = customtkinter.CTkButton(master=attendance_record,image=math_fac_btn, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(mathematics_att_record))
	att_rec_button_math_fac.place(x=254, y=254, height=99,width=413)

	    # Psychology Faculty Button
	psyc_fac_btn = PhotoImage(file = "pic/psyc_faculty.png")
	att_rec_button_psyc_fac = customtkinter.CTkButton(master=attendance_record,image=psyc_fac_btn, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(psychology_att_record))
	att_rec_button_psyc_fac.place(x=731, y=254, height=99,width=413)

	    # ITE Faculty Button
	ite_fac_btn = PhotoImage(file = "pic/ite_faculty.png")
	att_rec_button_ite_fac = customtkinter.CTkButton(master=attendance_record,image=ite_fac_btn, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(ite_att_record))
	att_rec_button_ite_fac.place(x=254, y=394, height=99,width=413)

	    # Applied Psychology Faculty Button
	app_psyc_fac_btn = PhotoImage(file = "pic/applied_psyc_faculty.png")
	att_rec_button_app_psyc_fac = customtkinter.CTkButton(master=attendance_record,image=app_psyc_fac_btn, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command=lambda: show_frame(applied_physics_att_record))
	att_rec_button_app_psyc_fac.place(x=731, y=394, height=99,width=413)

	    # Back Button
	att_rec_back = PhotoImage(file = "pic/btn_back_page.png")
	att_rec_button_back = customtkinter.CTkButton(master=attendance_record,image=att_rec_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	att_rec_button_back.place(x=45, y=595, height=50,width=140)

############################################################################### Schedule Part ###################################################################################################################################


	def Schedule():
		popupwindow_sched = Toplevel(main_window)
		popupwindow_sched.title("Schedule")

		width_of_popupwindow_sched = 1020
		height_of_popupwindow_sched = 650
		popupwindow_sched_width = popupwindow_sched.winfo_screenwidth()
		popupwindow_sched_height = popupwindow_sched.winfo_screenheight()
		x_popupwindow_sched = (popupwindow_sched_width/2)-(width_of_popupwindow_sched/2 )
		y_popupwindow_sched = (popupwindow_sched_height/2)-(height_of_popupwindow_sched/2)
		popupwindow_sched.geometry("%dx%d+%d+%d" %(width_of_popupwindow_sched,height_of_popupwindow_sched,x_popupwindow_sched,y_popupwindow_sched))

		# popupwindow_sched.geometry('1020x670')
		popupwindow_sched.grab_set()
		popupwindow_sched.resizable(False,False)

		    # open background image
		popupwindow_sched.sched_image = Image.open('pic/12.png')
		popupwindow_sched.sched_resize_image = popupwindow_sched.sched_image.resize((1020,670))
		popupwindow_sched.photo = ImageTk.PhotoImage(popupwindow_sched.sched_resize_image)
		popupwindow_sched.sched_bg_img_lb = Label(popupwindow_sched, image = popupwindow_sched.photo)
		popupwindow_sched.sched_bg_img_lb.pack()
		def Monday():
			btn_mon_sched.configure(fg_color="#00436e")
			btn_tue_sched.configure(fg_color="#ffb000")
			btn_wed_sched.configure(fg_color="#ffb000")
			btn_thur_sched.configure(fg_color="#ffb000")
			btn_fri_sched.configure(fg_color="#ffb000")
			btn_sat_sched.configure(fg_color="#ffb000")

		def Tuesday():
			btn_mon_sched.configure(fg_color="#ffb000")
			btn_tue_sched.configure(fg_color="#00436e")
			btn_wed_sched.configure(fg_color="#ffb000")
			btn_thur_sched.configure(fg_color="#ffb000")
			btn_fri_sched.configure(fg_color="#ffb000")
			btn_sat_sched.configure(fg_color="#ffb000")

		def Wednesday():
			btn_mon_sched.configure(fg_color="#ffb000")
			btn_tue_sched.configure(fg_color="#ffb000")
			btn_wed_sched.configure(fg_color="#00436e")
			btn_thur_sched.configure(fg_color="#ffb000")
			btn_fri_sched.configure(fg_color="#ffb000")
			btn_sat_sched.configure(fg_color="#ffb000")

		def Thursday():
			btn_mon_sched.configure(fg_color="#ffb000")
			btn_tue_sched.configure(fg_color="#ffb000")
			btn_wed_sched.configure(fg_color="#ffb000")
			btn_thur_sched.configure(fg_color="#00436e")
			btn_fri_sched.configure(fg_color="#ffb000")
			btn_sat_sched.configure(fg_color="#ffb000")

		def Friday():
			btn_mon_sched.configure(fg_color="#ffb000")
			btn_tue_sched.configure(fg_color="#ffb000")
			btn_wed_sched.configure(fg_color="#ffb000")
			btn_thur_sched.configure(fg_color="#ffb000")
			btn_fri_sched.configure(fg_color="#00436e")
			btn_sat_sched.configure(fg_color="#ffb000")

		def Saturday():
			btn_mon_sched.configure(fg_color="#ffb000")
			btn_tue_sched.configure(fg_color="#ffb000")
			btn_wed_sched.configure(fg_color="#ffb000")
			btn_thur_sched.configure(fg_color="#ffb000")
			btn_fri_sched.configure(fg_color="#ffb000")
			btn_sat_sched.configure(fg_color="#00436e")

		    # Data Table "TreeView"
		scrollbary_sched = Scrollbar(popupwindow_sched, orient=VERTICAL)
		scrollbary_sched.place(x=1030, y=230, height=350)

		# style = ttk.Style()
		# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

		data_table_sched = ttk.Treeview(popupwindow_sched)
		data_table_sched.place(x=145, y=415, width=740, height=215)
		data_table_sched.configure(yscrollcommand=scrollbary_sched.set)

		scrollbary_sched.configure(command=data_table_sched.yview)

		data_table_sched['columns'] = ("Start Time","End Time","Subject","Room","Section")
		# Format Columns
		data_table_sched.column("#0", width=0, stretch=NO)
		data_table_sched.column("Start Time", anchor=CENTER,width=0)
		data_table_sched.column("End Time", anchor=CENTER, width=50)
		data_table_sched.column("Subject", anchor=CENTER, width=50)
		data_table_sched.column("Room", anchor=CENTER, width=50)
		data_table_sched.column("Section", anchor=CENTER, width=50)

		# Create Headings
		data_table_sched.heading("Start Time", text="Start Time", anchor=CENTER)
		data_table_sched.heading("End Time", text="End Time", anchor=CENTER)
		data_table_sched.heading("Subject", text="Subject", anchor=CENTER)
		data_table_sched.heading("Room", text="Room", anchor=CENTER)
		data_table_sched.heading("Section", text="Section", anchor=CENTER)

		    # Entry Employee Name
		sched_name = Entry(popupwindow_sched, state='disabled')
		sched_name.place(x=180, y=172, width=150)

		    # Entry Day
		day_sched = ttk.Combobox(popupwindow_sched,  state='readonly', values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
		day_sched.place(x=180, y=209, width=150)

		    # Subject Label
		sub_sched_lb = Label(popupwindow_sched, fg='#f0f0f0', font = "Heltvetica 9")
		sub_sched_lb.place(x=180, y=235)

		    # Entry Subject
		sub_sched = Entry(popupwindow_sched)
		sub_sched.place(x=180, y=258, width=150)

		    # ComboBox College Department
		sched_department_combobox = ttk.Combobox(popupwindow_sched, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
		sched_department_combobox.place(x=545, y=172, width=150)

		#     # Entry Start Time
		# strttime_sched= Entry(popupwindow_sched,textvariable=time_format)
		# strttime_sched.place(x=545, y=209, width=150)

		    # Entry Start Time Hour
		var_hr_strt = IntVar()
		var_hr_strt.set(00)
		hr_strttime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=12, format="%02.0f",textvariable=var_hr_strt)
		hr_strttime_sched.place(x=545, y=209, width=35)

		    # Entry Start Time Minute
		var_min_strt = IntVar()
		var_min_strt.set(00)
		min_strttime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_min_strt)
		min_strttime_sched.place(x=585, y=209, width=35)

		    # Entry Start Time Second
		var_sec_strt = IntVar()
		var_sec_strt.set(00)
		sec_strttime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_sec_strt)
		sec_strttime_sched.place(x=625, y=209, width=35)

		    # ComboBox College Department
		p_strttime_sched = ttk.Combobox(popupwindow_sched, state='readonly', values=["AM", "PM",])
		p_strttime_sched.set("AM")
		p_strttime_sched.place(x=665, y=209, width=45)

		    # Entry Room
		room_sched = Entry(popupwindow_sched)
		room_sched.place(x=545, y=258, width=150)

		#     # Entry End Time
		# endtime_sched = Entry(popupwindow_sched)
		# endtime_sched.place(x=810, y=209, width=150)

		    # Entry End Time Hour
		var_hr_end = IntVar()
		var_hr_end.set(00)
		hr_endtime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=12, format="%02.0f",textvariable=var_hr_end)
		hr_endtime_sched.place(x=810, y=209, width=35)

		    # Entry End Time Minute
		var_min_end = IntVar()
		var_min_end.set(00)
		min_endtime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_min_end)
		min_endtime_sched.place(x=850, y=209, width=35)

		    # Entry End Time Second
		var_sec_end = IntVar()
		var_sec_end.set(00)
		sec_endtime_sched = Spinbox(popupwindow_sched, state='readonly', from_=00, to=59, format="%02.0f",textvariable=var_sec_end)
		sec_endtime_sched.place(x=890, y=209, width=35)

		    # ComboBox College Department
		p_endtime_sched = ttk.Combobox(popupwindow_sched, state='readonly', values=["AM", "PM",])
		p_endtime_sched.set("AM")
		p_endtime_sched.place(x=930, y=209, width=45)

		    # Entry Section
		section_sched = Entry(popupwindow_sched)
		section_sched.place(x=810, y=258, width=150)

		sched_name.configure(state='normal')
		sched_department_combobox.configure(state='normal')
		# sched_name.insert(0, name_emp)
		# sched_department_combobox.insert(0, depart)
		sched_name.configure(state='disabled')
		sched_department_combobox.configure(state='disabled')

		    # Save Data Button
		save_pic = PhotoImage(file = "pic/btn_save.png")
		save_button_sched = customtkinter.CTkButton(master=popupwindow_sched,image=save_pic, text="" ,
		                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command='save_sched')
		save_button_sched.place(x=315, y=290, height=32,width=131)

		    # Updated Button
		update_pic = PhotoImage(file = "pic/btn_update.png")
		button_update_sched = customtkinter.CTkButton(master=popupwindow_sched,state='disabled',image=update_pic, text="" ,
		                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command='update_sched')
		button_update_sched.place(x=460, y=290, height=32,width=131)

		    # Reset Button
		reset_btnsched = PhotoImage(file = "pic/btn_reset.png")
		button_resetsched = customtkinter.CTkButton(master=popupwindow_sched,image=reset_btnsched, text="" ,
		                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command='clear_sched')
		button_resetsched.place(x=605, y=290, height=32,width=131)

		    # Moday Button
		mon_btn = PhotoImage(file = "pic/btn_mon.png")
		btn_mon_sched = customtkinter.CTkButton(master=popupwindow_sched,image=mon_btn, text="" ,
		                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command=Monday)
		btn_mon_sched.place(x=90, y=373, height=28,width=131)

		    # Tuesday Button
		tue_btn = PhotoImage(file = "pic/btn_tue.png")
		btn_tue_sched = customtkinter.CTkButton(master=popupwindow_sched,image=tue_btn, text="" ,
		                                            corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Tuesday)
		btn_tue_sched.place(x=235, y=373, height=28,width=131)

		     # Wednesday Button
		wed_btn = PhotoImage(file = "pic/btn_wed.png")
		btn_wed_sched = customtkinter.CTkButton(master=popupwindow_sched,image=wed_btn, text="" ,
		                                            corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Wednesday)
		btn_wed_sched.place(x=380, y=373, height=28,width=131)

		     # Thursday Button
		thur_btn = PhotoImage(file = "pic/btn_thu.png")
		btn_thur_sched = customtkinter.CTkButton(master=popupwindow_sched,image=thur_btn, text="" ,
		                                            corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Thursday)
		btn_thur_sched.place(x=525, y=373, height=28,width=131)

		     # Friday Button
		fri_btn = PhotoImage(file = "pic/btn_fri.png")
		btn_fri_sched = customtkinter.CTkButton(master=popupwindow_sched,image=fri_btn, text="" ,
		                                            corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Friday)
		btn_fri_sched.place(x=670, y=373, height=28,width=131)

		     # Saturday Button
		sat_btn = PhotoImage(file = "pic/btn_sat.png")
		btn_sat_sched = customtkinter.CTkButton(master=popupwindow_sched,image=sat_btn, text="" ,
		                                            corner_radius=6, fg_color="#ffb000",hover_color="#006699", command=Saturday)
		btn_sat_sched.place(x=815, y=373, height=28,width=131)

############################################################################### Faculty Information Part ###################################################################################################################################


	# ============= Faculty Information Frame ===================================================================================================================================================

        # open background image
	faculty_information.fac_inf_image = Image.open('pic/FacultyInfo.png')
	faculty_information.fac_inf_resize_image = faculty_information.fac_inf_image.resize((1362, 692))
	faculty_information.photo = ImageTk.PhotoImage(faculty_information.fac_inf_resize_image)
	faculty_information.fac_inf_bg_img_lb = Label(faculty_information, image = faculty_information.photo)
	faculty_information.fac_inf_bg_img_lb.pack()

		# Clear Text on ENtry Box
	def clear_facultyinfo():
		add_button_fac_inf.configure(state='normal')
		button_update.configure(state='disabled')
		department_combobox.configure(state='normal')
		status_combobox_fac_inf.configure(state='normal')

		department_combobox.delete(0, END)
		employee_num_fac_inf.delete(0, END)
		employee_name_fac_inf.delete(0, END)
		department_combobox.delete(0, END)
		status_combobox_fac_inf.delete(0,END)

		department_combobox.configure(state='readonly')
		status_combobox_fac_inf.configure(state='disabled')
		loads_button_fac_inf.configure(state='disabled')

		# Select Row from Table
	def select_row_facultyinfo(e):
		clear_facultyinfo()

		selected = facultyinfo_table.focus()
		values = facultyinfo_table.item(selected, 'values')

		if values:
			add_button_fac_inf.configure(state='disabled')
			button_update.configure(state='normal')
			department_combobox.configure(state='normal')
			status_combobox_fac_inf.configure(state='normal')


			employee_num_fac_inf.insert(0, values[0])
			employee_name_fac_inf.insert(0, values[1])
			department_combobox.insert(0, values[2])
			status_combobox_fac_inf.insert(0,values[3])

			department_combobox.configure(state='readonly')
			status_combobox_fac_inf.configure(state='readonly')
			loads_button_fac_inf.configure(state='normal')
            
		else:
			messagebox.showinfo("Message", "PLease select a row on the table !!")

		# Display data to Treewiew
	def read():
		cursor = conn.cursor()

		cursor.execute("SELECT Employee_Number,Employee_Name,Department,Status FROM faculty_data")
		results = cursor.fetchall()
		conn.commit()
		return results

		# Refresh treeview Table
	def refreshTable_facultyinfo():
		for data in facultyinfo_table.get_children():
			facultyinfo_table.delete(data)

		for result in reverse(read()):
			facultyinfo_table.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")
		facultyinfo_table.tag_configure('orow', background='#EEEEEE')

		# Check Cuplicate for Employee Number
	def check_duplicate():
		Employee_No = employee_num_fac_inf.get()

		cursor = conn.cursor()

		cursor.execute("SELECT * FROM faculty_data WHERE Employee_Number = '" + str(Employee_No) + "'")
		records = cursor.fetchone()

		if records is not None:
			return True
		else:
			return False

		conn.commit()

		# Save data Entry to Database
	def Save_Data():
		department_combobox.configure(state='normal')
		save_college_department = department_combobox.get()
		save_employee_number = employee_num_fac_inf.get()
		save_employee_name = employee_name_fac_inf.get()
		save_status = 'Activated'

		save_facutyinfo = conn.cursor()

		if save_employee_number == "" or save_employee_name == "" or save_college_department == "":
			messagebox.showinfo("Error", "Please fill up the blank entry!!")
			return
		else:
			if check_duplicate() == True:
				messagebox.showinfo("Error", "Employee Number Already Exist!!")
				return
			elif not save_employee_number.isdigit():
				messagebox.showinfo("Error","Not a valid Employee Number, Please enter numbers only!!")
				return
			else:
				clear_facultyinfo()

				insertdata = str(save_employee_number),str(save_employee_name),str(save_college_department),str(save_status),'none','none'
				save_facutyinfo.execute("""INSERT INTO faculty_data (Employee_Number,Employee_Name,Department,Status,Username,Password) 
											VAlUES(%s,%s,%s,%s,%s,%s)""", insertdata)

				loads_button_fac_inf.configure(state='disabled')
				refreshTable_facultyinfo()
				messagebox.showinfo("Messgae", "Data Added!!")
		
		refreshTable_facultyinfo()
		conn.commit()

		# Search Data on Table
	def search_data_facultyinfo():
		lookup_record = search_fac_inf.get()
		try:
			if conn.is_connected():
				curs = conn.cursor()

				# Clear the Treeview
				for record in facultyinfo_table.get_children():
					facultyinfo_table.delete(record)

				lk_rec = '%' + lookup_record + '%'
				curs.execute("SELECT Employee_Number,Employee_Name,Department,Status FROM faculty_data WHERE Employee_Number LIKE '" + str(lk_rec) + "' or  Employee_Name LIKE '" + str(lk_rec) + "' or  Department LIKE '" + str(lk_rec) + "' or Status LIKE '" + str(lk_rec) + "'")
				records = curs.fetchall()

				global count
				count = 0

				for record in records:
					if count % 2 == 0:
						facultyinfo_table.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3]), tag="evenrow")
					else:
						facultyinfo_table.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3]), tag="oddrow")
					count += 1
					facultyinfo_table.tag_configure('evenrow', background='#EEEEEE')
					facultyinfo_table.tag_configure('oddrow', background='#EEEEEE')
					search_fac_inf.delete(0, END)

				conn.commit()
		except Error as e:
		    print("Error while connecting to MySQL", e)

		   
        # Updating Selected Data
	def Update_Data_facultyinfo():
		department_combobox.configure(state='normal')
		status_combobox_fac_inf.configure(state='normal')

		save_employee_number = employee_num_fac_inf.get()
		save_employee_name = employee_name_fac_inf.get()
		save_college_department = department_combobox.get()
		save_status = status_combobox_fac_inf.get()

		if save_employee_number == "" or save_employee_name == "" or save_college_department == "":
			messagebox.showinfo("Error", "Please fill up the blank entry!!")
			return
		else:
			messagebox.showinfo("Messgae", "Data Updated!!")
			cursor = conn.cursor()
			cursor.execute("UPDATE faculty_data SET Employee_Number= '" + str(save_employee_number) + "', Employee_Name= '" + str(save_employee_name) + "', Department = '" + str(save_college_department) + "', Status = '" + str(save_status) + "' WHERE Employee_Number = '"+ str(save_employee_number)+"' or Employee_Name= '" + str(save_employee_name) + "'")
			conn.commit()

			department_combobox.configure(state='readonly')
			status_combobox_fac_inf.configure(state='disabled')
			loads_button_fac_inf.configure(state='disabled')
			button_update.configure(state='disabled')
			clear_facultyinfo()
			refreshTable_facultyinfo()
				

	     # Data Table "TreeView"
	scrollbarx_facultyinfo = Scrollbar(faculty_information, orient=HORIZONTAL)
	scrollbarx_facultyinfo.place(x=730, y=584, width=465)
	scrollbary_facultyinfo  = Scrollbar(faculty_information, orient=VERTICAL)
	scrollbary_facultyinfo.place(x=1180, y=284, height=300)

	style = ttk.Style()
	style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	facultyinfo_table = ttk.Treeview(faculty_information)
	facultyinfo_table.place(x=730, y=284, width=450, height=300)
	facultyinfo_table.configure(yscrollcommand=scrollbary_facultyinfo.set, xscrollcommand=scrollbarx_facultyinfo.set)

	scrollbarx_facultyinfo.configure(command=facultyinfo_table.xview)
	scrollbary_facultyinfo.configure(command=facultyinfo_table.yview)

	facultyinfo_table['columns'] = ("Employee No.","Employee Name","College Department","Status")
	# Format Columns
	facultyinfo_table.column("#0", width=0, stretch=NO)
	facultyinfo_table.column("Employee No.", anchor=CENTER, width=50)
	facultyinfo_table.column("Employee Name", anchor=CENTER, width=50)
	facultyinfo_table.column("College Department", anchor=CENTER, width=50)
	facultyinfo_table.column("Status", anchor=CENTER, width=30)

	# Create Headings
	facultyinfo_table.heading("Employee No.", text="Employee No.", anchor=CENTER)
	facultyinfo_table.heading("Employee Name", text="Employee Name", anchor=CENTER)
	facultyinfo_table.heading("College Department", text="College Department", anchor=CENTER)
	facultyinfo_table.heading("Status", text="Status", anchor=CENTER)

	facultyinfo_table.bind("<ButtonRelease-1>", select_row_facultyinfo)

	refreshTable_facultyinfo()

	    # ComboBox College Department
	department_combobox = ttk.Combobox(faculty_information, font="Heltvetica 13",state='readonly', values=["NONE","Mathematics", "ITE", "Psychology", "Applied Physics"])
	department_combobox.set('NONE')
	department_combobox.place(x=382, y=202, width=200, height=22)

	    # Entry Employee Number
	employee_num_fac_inf = Entry(faculty_information, font="Heltvetica 13")
	employee_num_fac_inf.place(x=385, y=278, width=150, height=22)

	    # Entry Employee Name
	employee_name_fac_inf = Entry(faculty_information, font="Heltvetica 13")
	employee_name_fac_inf.place(x=385, y=314, width=150, height=22)

	    # Entry Status
	status_combobox_fac_inf = ttk.Combobox(faculty_information, font="Heltvetica 13",state='disabled', values=["Activated", "Deactivated"])
	# status_combobox_fac_inf.bind("<<ComboboxSelected>>", combobox_event)
	status_combobox_fac_inf.place(x=385, y=346, width=150, height=22)

	    # Search Entry
	search_ent_val = StringVar()
	search_fac_inf = Entry(faculty_information, textvariable = search_ent_val)
	search_fac_inf.place(x=850, y=205, width=200)

	    # Employee Loads Button
	loads_fac_btn = PhotoImage(file = "pic/btn_employee_loads.png")
	loads_button_fac_inf = customtkinter.CTkButton(master=faculty_information,state='disabled',image=loads_fac_btn, text="" ,
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command=Schedule)
	loads_button_fac_inf.place(x=383, y=410, height=25,width=128)

	    # Add Faculty Button
	add_fac_btn = PhotoImage(file = "pic/btn_add_faculty.png")
	add_button_fac_inf = customtkinter.CTkButton(master=faculty_information,image=add_fac_btn, text="" ,
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command=Save_Data)
	add_button_fac_inf.place(x=380, y=506, height=32,width=131)

	    # Update Button
	# def Update():
	#     print("update")
	update_btn = PhotoImage(file = "pic/btn_update.png")
	button_update = customtkinter.CTkButton(master=faculty_information,image=update_btn, text="", state='disabled',
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command=Update_Data_facultyinfo)
	button_update.place(x=212, y=506, height=32,width=131)

	    # Reset Button
	reset_btn = PhotoImage(file = "pic/btn_reset.png")
	button_reset = customtkinter.CTkButton(master=faculty_information,image=reset_btn, text="" ,
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command=clear_facultyinfo)
	button_reset.place(x=548, y=506, height=32,width=131)

	    # Search Button
	search_btn = PhotoImage(file = "pic/btn_search.png")
	button_search = customtkinter.CTkButton(master=faculty_information,image=search_btn, text="" ,
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command=search_data_facultyinfo)
	button_search.place(x=1065, y=204, height=20,width=90)

	    # Show All Button
	showall_btn = PhotoImage(file = "pic/btn_showall.png")
	button_showall = customtkinter.CTkButton(master=faculty_information,image=showall_btn, text="" ,
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command= refreshTable_facultyinfo)
	button_showall.place(x=923, y=603, height=28,width=110)

	    # Back Button
	fac_inf_back = PhotoImage(file = "pic/btn_back_page.png")
	fac_inf_button_back = customtkinter.CTkButton(master=faculty_information,image=fac_inf_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	fac_inf_button_back.place(x=20, y=595, height=50,width=140)

############################################################################### Class Momitoring Part ###################################################################################################################################


	# ============= Class Monitoring Frame ========================================================================================================================

	    # open background image
	class_moniroting.mntoring_image = Image.open('pic/btl_classmonitoring.png')
	class_moniroting.mntoring_resize_image = class_moniroting.mntoring_image.resize((1362, 692))
	class_moniroting.photo = ImageTk.PhotoImage(class_moniroting.mntoring_resize_image)
	class_moniroting.mntoring_bg_img_lb = Label(class_moniroting, image = class_moniroting.photo)
	class_moniroting.mntoring_bg_img_lb.pack()

		# Data Table "TreeView"
	scrollbary_mntoring = Scrollbar(class_moniroting, orient=VERTICAL)
	scrollbary_mntoring.place(x=1110, y=170, height=350)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_mntoring = ttk.Treeview(class_moniroting)
	data_table_mntoring.place(x=220, y=170, width=890, height=350)
	data_table_mntoring.configure(yscrollcommand=scrollbary_mntoring.set)

	scrollbary_mntoring.configure(command=data_table_mntoring.yview)

	data_table_mntoring['columns'] = ("Date","Employee ID","Name","Room","Subject","Start Time","End TIme","Remark")
	# Format Columns
	data_table_mntoring.column("#0", width=0, stretch=NO)
	data_table_mntoring.column("Date", anchor=CENTER, width=50)
	data_table_mntoring.column("Employee ID", anchor=CENTER, width=50)
	data_table_mntoring.column("Name", anchor=CENTER, width=50)
	data_table_mntoring.column("Room", anchor=CENTER, width=50)
	data_table_mntoring.column("Subject", anchor=CENTER, width=50)
	data_table_mntoring.column("Start Time", anchor=CENTER, width=50)
	data_table_mntoring.column("End TIme", anchor=CENTER, width=50)
	data_table_mntoring.column("Remark", anchor=CENTER, width=50)

	# Create Headings
	data_table_mntoring.heading("Date", text="Date", anchor=CENTER)
	data_table_mntoring.heading("Employee ID", text="Employee ID", anchor=CENTER)
	data_table_mntoring.heading("Name", text="Name", anchor=CENTER)
	data_table_mntoring.heading("Room", text="Room", anchor=CENTER)
	data_table_mntoring.heading("Subject", text="Subject", anchor=CENTER)
	data_table_mntoring.heading("Start Time", text="Start Time", anchor=CENTER)
	data_table_mntoring.heading("Start Time", text="Start Time", anchor=CENTER)
	data_table_mntoring.heading("End TIme", text="End TIme", anchor=CENTER)
	data_table_mntoring.heading("Remark", text="Remark", anchor=CENTER)

		# Search Entry
	search_entry_mntoring = StringVar()
	search_mntoring = Entry(class_moniroting, textvariable = search_entry_mntoring, font="Heltvetica 13")
	search_mntoring.place(x=525, y=117, width=200, height=22)

	    # Search Button
	search_btn_mntoring = PhotoImage(file = "pic/btn_search.png")
	mntoring_button_search = customtkinter.CTkButton(master=class_moniroting,image=search_btn_mntoring, text="" ,
	                                            corner_radius=6,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_data_log')
	mntoring_button_search.place(x=760, y=116, height=25,width=95)

	    # Show All Button
	showall_btn_mntoring = PhotoImage(file = "pic/btn_showall.png")
	mntoring_button_showall = customtkinter.CTkButton(master=class_moniroting,image=showall_btn_mntoring, text="" ,
	                                            corner_radius=10,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command='refreshTable_log')
	mntoring_button_showall.place(x=599, y=525, height=30,width=150)

	    # Back Button
	mntoring_back = PhotoImage(file = "pic/btn_back_page.png")
	mntoring_button_back = customtkinter.CTkButton(master=class_moniroting,image=mntoring_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	mntoring_button_back.place(x=30, y=320, height=50,width=140)


############################################################################### Create Account Part ###################################################################################################################################


	# ============= Create Account Frame ========================================================================================================================

	    # open background image
	create_account.act_image = Image.open('pic/frame_create_account.png')
	create_account.act_resize_image = create_account.act_image.resize((1362, 692))
	create_account.photo = ImageTk.PhotoImage(create_account.act_resize_image)
	create_account.act_bg_img_lb = Label(create_account, image = create_account.photo)
	create_account.act_bg_img_lb.pack()

	     # Data Table "TreeView"
	scrollbarx_account = Scrollbar(create_account, orient=HORIZONTAL)
	scrollbarx_account.place(x=730, y=584, width=465)
	scrollbary_account = Scrollbar(create_account, orient=VERTICAL)
	scrollbary_account.place(x=1180, y=284, height=300)

	style = ttk.Style()
	style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	account_table = ttk.Treeview(create_account)
	account_table.place(x=730, y=284, width=450, height=300)
	account_table.configure(yscrollcommand=scrollbary_account.set, xscrollcommand=scrollbarx_account.set)

	scrollbarx_account.configure(command=account_table.xview)
	scrollbary_account.configure(command=account_table.yview)

	account_table['columns'] = ("Employee No.","Employee Name","Username","Password")
	# Format Columns
	account_table.column("#0", width=0, stretch=NO)
	account_table.column("Employee No.", anchor=CENTER, width=50)
	account_table.column("Employee Name", anchor=CENTER, width=50)
	account_table.column("Username", anchor=CENTER, width=50)
	account_table.column("Password", anchor=CENTER, width=50)


	# Create Headings
	account_table.heading("Employee No.", text="Employee No.", anchor=CENTER)
	account_table.heading("Employee Name", text="Employee Name", anchor=CENTER)
	account_table.heading("Username", text="Username", anchor=CENTER)
	account_table.heading("Password", text="Password", anchor=CENTER)

	    # Entry Username
	username_create = Entry(create_account, font="Heltvetica 13 bold")
	username_create.place(x=345, y=340, width=160, height=25)

	    # Entry Password
	password_create = Entry(create_account, font="Heltvetica 13 bold")
	password_create.place(x=345, y=379, width=160, height=25)

	    # Entry  Re Enter Password
	re_password_create = Entry(create_account, font="Heltvetica 13 bold")
	re_password_create.place(x=455, y=425, width=160, height=25)

		# Create Button
	create_update_btn = PhotoImage(file = "pic/btn_acc_create.png")
	create_button_update = customtkinter.CTkButton(master=create_account,image=create_update_btn, text="",
	                                            corner_radius=10, fg_color="#00436e",hover_color="#006699", command= 'Update_Data')
	create_button_update.place(x=250, y=522, height=38,width=160)

		# Update Button
	create_acc_btn = PhotoImage(file = "pic/btn_acc_update.png")
	create_acc_update = customtkinter.CTkButton(master=create_account,image=create_acc_btn, text="",
	                                            corner_radius=10, fg_color="#00436e",hover_color="#006699", command= 'Update_Data')
	create_acc_update.place(x=465, y=522, height=38,width=160)

	    # Search Entry
	search_create_val = StringVar()
	search_create = Entry(create_account, textvariable = search_create_val, font="Heltvetica 13")
	search_create.place(x=825, y=203, width=200, height=22)
	    # Search Button
	create_search_btn = PhotoImage(file = "pic/btn_search.png")
	create_button_search = customtkinter.CTkButton(master=create_account,image=create_search_btn, text="" ,
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command= 'search_data')
	create_button_search.place(x=1065, y=202, height=25,width=100)

	    # Show All Button
	create_showall_btn = PhotoImage(file = "pic/btn_showall.png")
	create_button_showall = customtkinter.CTkButton(master=create_account,image=create_showall_btn, text="" ,
	                                            corner_radius=6, fg_color="#00436e",hover_color="#006699", command= 'refreshTable')
	create_button_showall.place(x=923, y=603, height=28,width=110)

	    # Back Button
	create_inf_back = PhotoImage(file = "pic/btn_back_page.png")
	create_button_back = customtkinter.CTkButton(master=create_account,image=create_inf_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(page4))
	create_button_back.place(x=20, y=595, height=50,width=140)

############################################################################### Individual Summary Report Part ###################################################################################################################################

	# ============= Mathematics Summary Report In Frame ========================================================================================================================

	def summary_math():
		popupwindow = Toplevel(main_window)
		popupwindow.title("Individual Summary Report")

		width_of_popupwindow = 1020
		height_of_popupwindow = 650
		popupwindow_width = popupwindow.winfo_screenwidth()
		popupwindow_height = popupwindow.winfo_screenheight()
		x_popupwindow = (popupwindow_width/2)-(width_of_popupwindow/2 )
		y_popupwindow = (popupwindow_height/2)-(height_of_popupwindow/2)
		popupwindow.geometry("%dx%d+%d+%d" %(width_of_popupwindow,height_of_popupwindow,x_popupwindow,y_popupwindow))

		# popupwindow.geometry('1020x650')
		popupwindow.grab_set()
		popupwindow.resizable(False,False)

		    # open background image
		popupwindow.summary_image = Image.open('pic/16.png')
		popupwindow.summary_resize_image = popupwindow.summary_image.resize((1020,650))
		popupwindow.photo = ImageTk.PhotoImage(popupwindow.summary_resize_image)
		popupwindow.summary_bg_img_lb = Label(popupwindow, image = popupwindow.photo)
		popupwindow.summary_bg_img_lb.pack()

		         # Data Table "TreeView"
		scrollbarx_summary = Scrollbar(popupwindow, orient=HORIZONTAL)
		scrollbarx_summary.place(x=500, y=579, width=367)
		scrollbary_summary = Scrollbar(popupwindow, orient=VERTICAL)
		scrollbary_summary.place(x=869, y=225, height=358)

		# style = ttk.Style()
		# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

		data_table_summary = ttk.Treeview(popupwindow)
		data_table_summary.place(x=500, y=225, width=368, height=353)
		data_table_summary.configure(yscrollcommand=scrollbary_summary.set, xscrollcommand=scrollbarx_summary.set)

		scrollbarx_summary.configure(command=data_table_summary.xview)
		scrollbary_summary.configure(command=data_table_summary.yview)

		data_table_summary['columns'] = ("Date","Subject","Room","Start Time","End Time","Remark")
		# Format Columns
		data_table_summary.column("#0", width=0, stretch=NO)
		data_table_summary.column("Date", anchor=W, width=100)
		data_table_summary.column("Subject", anchor=W, width=100)
		data_table_summary.column("Room", anchor=W, width=100)
		data_table_summary.column("Start Time", anchor=W, width=100)
		data_table_summary.column("End Time", anchor=W, width=100)
		data_table_summary.column("Remark", anchor=W, width=100)

		# Create Headings
		data_table_summary.heading("Date", text="Date", anchor=CENTER)
		data_table_summary.heading("Subject", text="Subject", anchor=CENTER)
		data_table_summary.heading("Room", text="Room", anchor=CENTER)
		data_table_summary.heading("Start Time", text="Start Time", anchor=CENTER)
		data_table_summary.heading("End Time", text="End Time", anchor=CENTER)
		data_table_summary.heading("Remark", text="Remark", anchor=CENTER)
		

		    # ComboBox College Department
		summary_department_combobox = ttk.Combobox(popupwindow, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
		summary_department_combobox.place(x=253, y=245, width=175)

		    # Entry Employee Number
		employee_num_summary = Entry(popupwindow, state='disabled')
		employee_num_summary.place(x=240, y=308, width=80)

		    # Entry Employee Name
		employee_name_summary = Entry(popupwindow, state='disabled')
		employee_name_summary.place(x=240, y=330, width=80)

		    # Entry Attendance Satatus
		att_status_summary = Entry(popupwindow, state='disabled')
		att_status_summary.place(x=240, y=352, width=80)

		    # Entry Time In
		time_in_summary = Entry(popupwindow, state='disabled')
		time_in_summary.place(x=370, y=308, width=80)

		    # Entry Time Out
		time_out_summary = Entry(popupwindow, state='disabled')
		time_out_summary.place(x=370, y=330, width=80)

		    # Entry Date
		date_summary = Entry(popupwindow, state='disabled')
		date_summary.place(x=370, y=352, width=80)

		   # Entry dtr
		dtr_summary = Entry(popupwindow)
		dtr_summary.place(x=152, y=470, width=80)

		    # Button Present
		present_btn_summary = PhotoImage(file = "pic/btn_present.png")
		summary_button_present = customtkinter.CTkButton(master=popupwindow,image=present_btn_summary, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_present')
		summary_button_present.place(x=175, y=103, height=78,width=150)

		    # Button Late
		late_btn_summary = PhotoImage(file = "pic/btn_late.png")
		summary_button_late = customtkinter.CTkButton(master=popupwindow,image=late_btn_summary, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_late')
		summary_button_late.place(x=355, y=103, height=78,width=150)

		    # Button Absent
		absent_btn_summary = PhotoImage(file = "pic/btn_absent.png")
		summary_button_absent = customtkinter.CTkButton(master=popupwindow,image=absent_btn_summary, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_absent')
		summary_button_absent.place(x=525, y=103, height=78,width=150)

		    # Button Early Dismisal
		ed_btn_summary = PhotoImage(file = "pic/btn_early_dis.png")
		summary_button_ed = customtkinter.CTkButton(master=popupwindow,image=ed_btn_summary, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_earlydismissal')
		summary_button_ed.place(x=705, y=103, height=78,width=150)

		    # Total Present Label
		total_present_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_present_lb_summary.place(x=225, y=136)

		    # Total Late Label
		total_late_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_late_lb_summary.place(x=405, y=136)

		    # Total Absent Label
		total_absent_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_absent_lb_summary.place(x=575, y=136)

		    # Total Early Dismisal Label
		total_earldis_lb_summary = Label(popupwindow, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_earldis_lb_summary.place(x=755, y=136)

		    # Print Button
		print_btn_summary = PhotoImage(file = "pic/btn_print.png")
		summary_button_print = customtkinter.CTkButton(master=popupwindow,image=print_btn_summary, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_math_report')
		summary_button_print.place(x=258, y=375, height=20,width=80)

		    # Generate Button
		generate_btn_summary = PhotoImage(file = "pic/btn_generate.png")
		summary_button_generate = customtkinter.CTkButton(master=popupwindow,image=generate_btn_summary, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='search_date_math')
		summary_button_generate.place(x=258, y=468, height=20,width=80)

		    # Print Button
		summary_button_print1 = customtkinter.CTkButton(master=popupwindow,state='disabled',image=print_btn_summary, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_math_report')
		summary_button_print1.place(x=358, y=468, height=20,width=80)

		    # Show All Button
		showall_btn_summary = PhotoImage(file = "pic/btn_showall_small.png")
		summary_button_showall = customtkinter.CTkButton(master=popupwindow,image=showall_btn_summary, text="" ,
		                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command='refreshTable_math_report')
		summary_button_showall.place(x=650, y=598, height=20,width=90)

	# ============= Psychology Summary Report  ========================================================================================================================

	def summary_psyc():
		popupwindow_psyc = Toplevel(main_window)
		popupwindow_psyc.title("Individual Summary Report")

		width_of_popupwindow_psyc = 1020
		height_of_popupwindow_psyc = 650
		popupwindow_psyc_width = popupwindow_psyc.winfo_screenwidth()
		popupwindow_psyc_height = popupwindow_psyc.winfo_screenheight()
		x_popupwindow_psyc = (popupwindow_psyc_width/2)-(width_of_popupwindow_psyc/2 )
		y_popupwindow_psyc = (popupwindow_psyc_height/2)-(height_of_popupwindow_psyc/2)
		popupwindow_psyc.geometry("%dx%d+%d+%d" %(width_of_popupwindow_psyc,height_of_popupwindow_psyc,x_popupwindow_psyc,y_popupwindow_psyc))

		# popupwindow_psyc.geometry('1020x650')
		popupwindow_psyc.grab_set()
		popupwindow_psyc.resizable(False,False)

		    # open background image
		popupwindow_psyc.summary_image = Image.open('pic/16.png')
		popupwindow_psyc.summary_resize_image = popupwindow_psyc.summary_image.resize((1020,650))
		popupwindow_psyc.photo = ImageTk.PhotoImage(popupwindow_psyc.summary_resize_image)
		popupwindow_psyc.summary_bg_img_lb = Label(popupwindow_psyc, image = popupwindow_psyc.photo)
		popupwindow_psyc.summary_bg_img_lb.pack()

		         # Data Table "TreeView"
		scrollbarx_summary_psyc = Scrollbar(popupwindow_psyc, orient=HORIZONTAL)
		scrollbarx_summary_psyc.place(x=500, y=579, width=367)
		scrollbary_summary_psyc = Scrollbar(popupwindow_psyc, orient=VERTICAL)
		scrollbary_summary_psyc.place(x=869, y=225, height=358)

		# style = ttk.Style()
		# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

		data_table_summary_psyc = ttk.Treeview(popupwindow_psyc)
		data_table_summary_psyc.place(x=500, y=225, width=368, height=353)
		data_table_summary_psyc.configure(yscrollcommand=scrollbary_summary_psyc.set, xscrollcommand=scrollbarx_summary_psyc.set)

		scrollbarx_summary_psyc.configure(command=data_table_summary_psyc.xview)
		scrollbary_summary_psyc.configure(command=data_table_summary_psyc.yview)

		data_table_summary_psyc['columns'] = ("Date","Subject","Room","Start Time","End Time","Remark")
		# Format Columns
		data_table_summary_psyc.column("#0", width=0, stretch=NO)
		data_table_summary_psyc.column("Date", anchor=W, width=100)
		data_table_summary_psyc.column("Subject", anchor=W, width=100)
		data_table_summary_psyc.column("Room", anchor=W, width=100)
		data_table_summary_psyc.column("Start Time", anchor=W, width=100)
		data_table_summary_psyc.column("End Time", anchor=W, width=100)
		data_table_summary_psyc.column("Remark", anchor=W, width=100)

		# Create Headings
		data_table_summary_psyc.heading("Date", text="Date", anchor=CENTER)
		data_table_summary_psyc.heading("Subject", text="Subject", anchor=CENTER)
		data_table_summary_psyc.heading("Room", text="Room", anchor=CENTER)
		data_table_summary_psyc.heading("Start Time", text="Start Time", anchor=CENTER)
		data_table_summary_psyc.heading("End Time", text="End Time", anchor=CENTER)
		data_table_summary_psyc.heading("Remark", text="Remark", anchor=CENTER)

		    # ComboBox College Department
		summary_department_combobox_psyc = ttk.Combobox(popupwindow_psyc, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
		summary_department_combobox_psyc.place(x=253, y=245, width=175)

		    # Entry Employee Number
		employee_num_summary_psyc = Entry(popupwindow_psyc, state='disabled')
		employee_num_summary_psyc.place(x=240, y=308, width=80)

		    # Entry Employee Name
		employee_name_summary_psyc = Entry(popupwindow_psyc, state='disabled')
		employee_name_summary_psyc.place(x=240, y=330, width=80)

		    # Entry Attendance Satatus
		att_status_summary_psyc = Entry(popupwindow_psyc, state='disabled')
		att_status_summary_psyc.place(x=240, y=352, width=80)

		    # Entry Time In
		time_in_summary_psyc = Entry(popupwindow_psyc, state='disabled')
		time_in_summary_psyc.place(x=370, y=308, width=80)

		    # Entry Time Out
		time_out_summary_psyc = Entry(popupwindow_psyc, state='disabled')
		time_out_summary_psyc.place(x=370, y=330, width=80)

		    # Entry Date
		date_summary_psyc_psyc = Entry(popupwindow_psyc, state='disabled')
		date_summary_psyc_psyc.place(x=370, y=352, width=80)

		   # Entry dtr
		dtr_summary_psyc = Entry(popupwindow_psyc,)
		dtr_summary_psyc.place(x=152, y=470, width=80)

		    # Button Present
		present_btn_summary_psyc = PhotoImage(file = "pic/btn_present.png")
		summary_button_present_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=present_btn_summary_psyc, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_present')
		summary_button_present_psyc.place(x=175, y=103, height=78,width=150)

		    # Button Late
		late_btn_summary_psyc = PhotoImage(file = "pic/btn_late.png")
		summary_button_late_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=late_btn_summary_psyc, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_late')
		summary_button_late_psyc.place(x=355, y=103, height=78,width=150)

		    # Button Absent
		absent_btn_summary_psyc = PhotoImage(file = "pic/btn_absent.png")
		summary_button_absent_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=absent_btn_summary_psyc, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_absent')
		summary_button_absent_psyc.place(x=525, y=103, height=78,width=150)

		    # Button Early Dismisal
		ed_btn_summary_psyc = PhotoImage(file = "pic/btn_early_dis.png")
		summary_button_ed_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=ed_btn_summary_psyc, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_earlydismissal')
		summary_button_ed_psyc.place(x=705, y=103, height=78,width=150)

		    # Total Present Label
		total_present_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_present_lb_summary_psyc.place(x=225, y=136)

		    # Total Late Label
		total_late_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_late_lb_summary_psyc.place(x=405, y=136)

		    # Total Absent Label
		total_absent_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_absent_lb_summary_psyc.place(x=575, y=136)

		    # Total Early Dismisal Label
		total_earldis_lb_summary_psyc = Label(popupwindow_psyc, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_earldis_lb_summary_psyc.place(x=755, y=136)

		    # Print Button
		print_btn_summary_psyc = PhotoImage(file = "pic/btn_print.png")
		summary_button_print_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=print_btn_summary_psyc, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_psyc')
		summary_button_print_psyc.place(x=258, y=375, height=20,width=80)

		    # Generate Button
		generate_btn_summary_psyc = PhotoImage(file = "pic/btn_generate.png")
		summary_button_generate_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=generate_btn_summary_psyc, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='search_date_psyc')
		summary_button_generate_psyc.place(x=258, y=468, height=20,width=80)

		    # Print Button
		summary_button_print1_psyc = customtkinter.CTkButton(master=popupwindow_psyc,state='disabled',image=print_btn_summary_psyc, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_psyc')
		summary_button_print1_psyc.place(x=358, y=468, height=20,width=80)

		    # Show All Button
		showall_btn_summary_psyc = PhotoImage(file = "pic/btn_showall_small.png")
		summary_button_showall_psyc = customtkinter.CTkButton(master=popupwindow_psyc,image=showall_btn_summary_psyc, text="" ,
		                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command='refreshTable_psyc_report')
		summary_button_showall_psyc.place(x=650, y=598, height=20,width=90)

	# ============= Applied Physics Summary Report ========================================================================================================================

	def summary_applied():
		popupwindow_applied = Toplevel(main_window)
		popupwindow_applied.title("Individual Summary Report")

		width_of_popupwindow_applied = 1020
		height_of_popupwindow_applied = 650
		popupwindow_applied_width = popupwindow_applied.winfo_screenwidth()
		popupwindow_applied_height = popupwindow_applied.winfo_screenheight()
		x_popupwindow_applied = (popupwindow_applied_width/2)-(width_of_popupwindow_applied/2 )
		y_popupwindow_applied = (popupwindow_applied_height/2)-(height_of_popupwindow_applied/2)
		popupwindow_applied.geometry("%dx%d+%d+%d" %(width_of_popupwindow_applied,height_of_popupwindow_applied,x_popupwindow_applied,y_popupwindow_applied))

		# popupwindow_applied.geometry('1020x650')
		popupwindow_applied.grab_set()
		popupwindow_applied.resizable(False,False)

		    # open background image
		popupwindow_applied.summary_image = Image.open('pic/16.png')
		popupwindow_applied.summary_resize_image = popupwindow_applied.summary_image.resize((1020,650))
		popupwindow_applied.photo = ImageTk.PhotoImage(popupwindow_applied.summary_resize_image)
		popupwindow_applied.summary_bg_img_lb = Label(popupwindow_applied, image = popupwindow_applied.photo)
		popupwindow_applied.summary_bg_img_lb.pack()

		    # Data Table "TreeView"
		scrollbarx_summary_applied = Scrollbar(popupwindow_applied, orient=HORIZONTAL)
		scrollbarx_summary_applied.place(x=500, y=579, width=367)
		scrollbary_summary_applied = Scrollbar(popupwindow_applied, orient=VERTICAL)
		scrollbary_summary_applied.place(x=869, y=225, height=358)

		# style = ttk.Style()
		# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

		data_table_summary_applied = ttk.Treeview(popupwindow_applied)
		data_table_summary_applied.place(x=500, y=225, width=368, height=353)
		data_table_summary_applied.configure(yscrollcommand=scrollbary_summary_applied.set, xscrollcommand=scrollbarx_summary_applied.set)

		scrollbarx_summary_applied.configure(command=data_table_summary_applied.xview)
		scrollbary_summary_applied.configure(command=data_table_summary_applied.yview)

		data_table_summary_applied['columns'] = ("Date","Subject","Room","Start Time","End Time","Remark")
		# Format Columns
		data_table_summary_applied.column("#0", width=0, stretch=NO)
		data_table_summary_applied.column("Date", anchor=W, width=100)
		data_table_summary_applied.column("Subject", anchor=W, width=100)
		data_table_summary_applied.column("Room", anchor=W, width=100)
		data_table_summary_applied.column("Start Time", anchor=W, width=100)
		data_table_summary_applied.column("End Time", anchor=W, width=100)
		data_table_summary_applied.column("Remark", anchor=W, width=100)

		# Create Headings
		data_table_summary_applied.heading("Date", text="Date", anchor=CENTER)
		data_table_summary_applied.heading("Subject", text="Subject", anchor=CENTER)
		data_table_summary_applied.heading("Room", text="Room", anchor=CENTER)
		data_table_summary_applied.heading("Start Time", text="Start Time", anchor=CENTER)
		data_table_summary_applied.heading("End Time", text="End Time", anchor=CENTER)
		data_table_summary_applied.heading("Remark", text="Remark", anchor=CENTER)

		# ComboBox College Department
		summary_department_combobox_applied = ttk.Combobox(popupwindow_applied, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
		summary_department_combobox_applied.place(x=253, y=245, width=175)

		    # Entry Employee Number
		employee_num_summary_applied = Entry(popupwindow_applied, state='disabled')
		employee_num_summary_applied.place(x=240, y=308, width=80)

		    # Entry Employee Name
		employee_name_summary_applied = Entry(popupwindow_applied, state='disabled')
		employee_name_summary_applied.place(x=240, y=330, width=80)

		    # Entry Attendance Satatus
		att_status_summary_applied = Entry(popupwindow_applied, state='disabled')
		att_status_summary_applied.place(x=240, y=352, width=80)

		    # Entry Time In
		time_in_summary_applied = Entry(popupwindow_applied, state='disabled')
		time_in_summary_applied.place(x=370, y=308, width=80)

		    # Entry Time Out
		time_out_summary_applied = Entry(popupwindow_applied, state='disabled')
		time_out_summary_applied.place(x=370, y=330, width=80)

		    # Entry Date
		date_summary_applied = Entry(popupwindow_applied, state='disabled')
		date_summary_applied.place(x=370, y=352, width=80)

		   # Entry dtr
		dtr_summary_applied = Entry(popupwindow_applied)
		dtr_summary_applied.place(x=152, y=470, width=80)

		    # Button Present
		present_btn_summary_applied = PhotoImage(file = "pic/btn_present.png")
		summary_button_present_applied = customtkinter.CTkButton(master=popupwindow_applied,image=present_btn_summary_applied, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_present')
		summary_button_present_applied.place(x=175, y=103, height=78,width=150)

		    # Button Late
		late_btn_summary_applied = PhotoImage(file = "pic/btn_late.png")
		summary_button_late_applied = customtkinter.CTkButton(master=popupwindow_applied,image=late_btn_summary_applied, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_late')
		summary_button_late_applied.place(x=355, y=103, height=78,width=150)

		    # Button Absent
		absent_btn_summary_applied = PhotoImage(file = "pic/btn_absent.png")
		summary_button_absent_applied = customtkinter.CTkButton(master=popupwindow_applied,image=absent_btn_summary_applied, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_absent')
		summary_button_absent_applied.place(x=525, y=103, height=78,width=150)

		    # Button Early Dismisal
		ed_btn_summary_applied = PhotoImage(file = "pic/btn_early_dis.png")
		summary_button_ed_applied = customtkinter.CTkButton(master=popupwindow_applied,image=ed_btn_summary_applied, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_earlydismissal')
		summary_button_ed_applied.place(x=705, y=103, height=78,width=150)

		    # Total Present Label
		total_present_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_present_lb_summary_applied.place(x=225, y=136)

		    # Total Late Label
		total_late_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_late_lb_summary_applied.place(x=405, y=136)

		    # Total Absent Label
		total_absent_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_absent_lb_summary_applied.place(x=575, y=136)

		    # Total Early Dismisal Label
		total_earldis_lb_summary_applied = Label(popupwindow_applied, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_earldis_lb_summary_applied.place(x=755, y=136)

		    # Print Button
		print_btn_summary_applied = PhotoImage(file = "pic/btn_print.png")
		summary_button_print_applied = customtkinter.CTkButton(master=popupwindow_applied,image=print_btn_summary_applied, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_applied')
		summary_button_print_applied.place(x=258, y=375, height=20,width=80)

		    # Generate Button
		generate_btn_summary_applied = PhotoImage(file = "pic/btn_generate.png")
		summary_button_generate_applied = customtkinter.CTkButton(master=popupwindow_applied,image=generate_btn_summary_applied, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='search_date_applied')
		summary_button_generate_applied.place(x=258, y=468, height=20,width=80)

		    # Print Button
		summary_button_print1_applied = customtkinter.CTkButton(master=popupwindow_applied,state='disabled',image=print_btn_summary_applied, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_applied')
		summary_button_print1_applied.place(x=358, y=468, height=20,width=80)

		    # Show All Button
		showall_btn_summary_applied = PhotoImage(file = "pic/btn_showall_small.png")
		summary_button_showall_applied = customtkinter.CTkButton(master=popupwindow_applied,image=showall_btn_summary_applied, text="" ,
		                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command='refreshTable_applied_report')
		summary_button_showall_applied.place(x=650, y=598, height=20,width=90)

	# ============= ITE Summary Report In Frame ========================================================================================================================

	def summary_ite():
		popupwindow_ite = Toplevel(main_window)
		popupwindow_ite.title("Individual Summary Report")

		width_of_popupwindow_ite = 1020
		height_of_popupwindow_ite = 650
		popupwindow_ite_width = popupwindow_ite.winfo_screenwidth()
		popupwindow_ite_height = popupwindow_ite.winfo_screenheight()
		x_popupwindow_ite = (popupwindow_ite_width/2)-(width_of_popupwindow_ite/2 )
		y_popupwindow_ite = (popupwindow_ite_height/2)-(height_of_popupwindow_ite/2)
		popupwindow_ite.geometry("%dx%d+%d+%d" %(width_of_popupwindow_ite,height_of_popupwindow_ite,x_popupwindow_ite,y_popupwindow_ite))

		# popupwindow_ite.geometry('1020x650')
		popupwindow_ite.grab_set()
		popupwindow_ite.resizable(False,False)

		    # open background image
		popupwindow_ite.summary_image = Image.open('pic/16.png')
		popupwindow_ite.summary_resize_image = popupwindow_ite.summary_image.resize((1020,650))
		popupwindow_ite.photo = ImageTk.PhotoImage(popupwindow_ite.summary_resize_image)
		popupwindow_ite.summary_bg_img_lb = Label(popupwindow_ite, image = popupwindow_ite.photo)
		popupwindow_ite.summary_bg_img_lb.pack()


		         # Data Table "TreeView"
		scrollbarx_summary_ite = Scrollbar(popupwindow_ite, orient=HORIZONTAL)
		scrollbarx_summary_ite.place(x=500, y=579, width=367)
		scrollbary_summary_ite = Scrollbar(popupwindow_ite, orient=VERTICAL)
		scrollbary_summary_ite.place(x=869, y=225, height=358)

		# style = ttk.Style()
		# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

		data_table_summary_ite = ttk.Treeview(popupwindow_ite)
		data_table_summary_ite.place(x=500, y=225, width=368, height=353)
		data_table_summary_ite.configure(yscrollcommand=scrollbary_summary_ite.set, xscrollcommand=scrollbarx_summary_ite.set)

		scrollbarx_summary_ite.configure(command=data_table_summary_ite.xview)
		scrollbary_summary_ite.configure(command=data_table_summary_ite.yview)

		data_table_summary_ite['columns'] = ("Date","Subject","Room","Start Time","End Time","Remark")
		# Format Columns
		data_table_summary_ite.column("#0", width=0, stretch=NO)
		data_table_summary_ite.column("Date", anchor=W, width=100)
		data_table_summary_ite.column("Subject", anchor=W, width=100)
		data_table_summary_ite.column("Room", anchor=W, width=100)
		data_table_summary_ite.column("Start Time", anchor=W, width=100)
		data_table_summary_ite.column("End Time", anchor=W, width=100)
		data_table_summary_ite.column("Remark", anchor=W, width=100)
		

		# Create Headings
		data_table_summary_ite.heading("Date", text="Date", anchor=CENTER)
		data_table_summary_ite.heading("Subject", text="Subject", anchor=CENTER)
		data_table_summary_ite.heading("Room", text="Room", anchor=CENTER)
		data_table_summary_ite.heading("Start Time", text="Start Time", anchor=CENTER)
		data_table_summary_ite.heading("End Time", text="End Time", anchor=CENTER)
		data_table_summary_ite.heading("Remark", text="Remark", anchor=CENTER)
		


		    # ComboBox College Department
		summary_department_combobox_ite = ttk.Combobox(popupwindow_ite, state='disabled', values=["Mathematics", "ITE", "Psychology", "Applied Physics"])
		summary_department_combobox_ite.place(x=253, y=245, width=175)

		    # Entry Employee Number
		employee_num_summary_ite = Entry(popupwindow_ite, state='disabled')
		employee_num_summary_ite.place(x=240, y=308, width=80)

		    # Entry Employee Name
		employee_name_summary_ite = Entry(popupwindow_ite, state='disabled')
		employee_name_summary_ite.place(x=240, y=330, width=80)

		    # Entry Attendance Satatus
		att_status_summary_ite = Entry(popupwindow_ite, state='disabled')
		att_status_summary_ite.place(x=240, y=352, width=80)

		    # Entry Time In
		time_in_summary_ite = Entry(popupwindow_ite, state='disabled')
		time_in_summary_ite.place(x=370, y=308, width=80)

		    # Entry Time Out
		time_out_summary_ite = Entry(popupwindow_ite, state='disabled')
		time_out_summary_ite.place(x=370, y=330, width=80)

		    # Entry Date
		date_summary_ite = Entry(popupwindow_ite, state='disabled')
		date_summary_ite.place(x=370, y=352, width=80)

		   # Entry dtr
		dtr_summary_ite = Entry(popupwindow_ite)
		dtr_summary_ite.place(x=152, y=470, width=80)

		    # Button Present
		present_btn_summary_ite = PhotoImage(file = "pic/btn_present.png")
		summary_button_present_ite = customtkinter.CTkButton(master=popupwindow_ite,image=present_btn_summary_ite, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_present')
		summary_button_present_ite.place(x=175, y=103, height=78,width=150)

		    # Button Late
		late_btn_summary_ite = PhotoImage(file = "pic/btn_late.png")
		summary_button_late_ite = customtkinter.CTkButton(master=popupwindow_ite,image=late_btn_summary_ite, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_late')
		summary_button_late_ite.place(x=355, y=103, height=78,width=150)

		    # Button Absent
		absent_btn_summary_ite = PhotoImage(file = "pic/btn_absent.png")
		summary_button_absent_ite = customtkinter.CTkButton(master=popupwindow_ite,image=absent_btn_summary_ite, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_absent')
		summary_button_absent_ite.place(x=525, y=103, height=78,width=150)

		    # Button Early Dismisal
		ed_btn_summary_ite = PhotoImage(file = "pic/btn_early_dis.png")
		summary_button_ed_ite = customtkinter.CTkButton(master=popupwindow_ite,image=ed_btn_summary_ite, text="" ,
		                                            corner_radius=10,bg_color='#ffffff', fg_color="#00436e",hover_color="#006699", command='search_earlydismissal')
		summary_button_ed_ite.place(x=705, y=103, height=78,width=150)

		    # Total Present Label
		total_present_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_present_lb_summary_ite.place(x=225, y=136)

		    # Total Late Label
		total_late_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_late_lb_summary_ite.place(x=405, y=136)

		    # Total Absent Label
		total_absent_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_absent_lb_summary_ite.place(x=575, y=136)

		    # Total Early Dismisal Label
		total_earldis_lb_summary_ite = Label(popupwindow_ite, text='000', fg='white', bg ='#00436e', font = "Heltvetica 20 bold")
		total_earldis_lb_summary_ite.place(x=755, y=136)

		    # Print Button
		print_btn_summary_ite = PhotoImage(file = "pic/btn_print.png")
		summary_button_print_ite = customtkinter.CTkButton(master=popupwindow_ite,image=print_btn_summary_ite, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_ite')
		summary_button_print_ite.place(x=258, y=375, height=20,width=80)

		    # Generate Button
		generate_btn_summary_ite = PhotoImage(file = "pic/btn_generate.png")
		summary_button_generate_ite = customtkinter.CTkButton(master=popupwindow_ite,image=generate_btn_summary_ite, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='search_date')
		summary_button_generate_ite.place(x=258, y=468, height=20,width=80)

		    # Print Button
		summary_button_print1_ite = customtkinter.CTkButton(master=popupwindow_ite,state='disabled',image=print_btn_summary_ite, text="",
		                                            corner_radius=3, fg_color="#00436e",hover_color="#006699", command='print_data_ite')
		summary_button_print1_ite.place(x=358, y=468, height=20,width=80)

		    # Show All Button
		showall_btn_summary_ite = PhotoImage(file = "pic/btn_showall_small.png")
		summary_button_showall_ite = customtkinter.CTkButton(master=popupwindow_ite,image=showall_btn_summary_ite, text="" ,
		                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command='refreshTable_ite_report')
		summary_button_showall_ite.place(x=650, y=598, height=20,width=90)

############################################################################### Attentandance Rerord Part ###################################################################################################################################

	 # ============= Mathematics Attendance Record Frame =============================================================================

	    # open background image
	mathematics_att_record.math_rec_image = Image.open('pic/15.png')
	mathematics_att_record.math_rec_resize_image = mathematics_att_record.math_rec_image.resize((1362, 692))
	mathematics_att_record.photo = ImageTk.PhotoImage(mathematics_att_record.math_rec_resize_image)
	mathematics_att_record.math_rec_bg_img_lb = Label(mathematics_att_record, image = mathematics_att_record.photo)
	mathematics_att_record.math_rec_bg_img_lb.pack()

	     # Get Current Time and Date
	def time_math():
		string_time = strftime('%H:%M %p')
		time_lb_math_rec.configure(text = string_time)
		time_lb_math_rec.after(1000, time_math)

		string_date = strftime('%d-%m-20%y')
		date_lb_math_rec.configure(text = string_date)

		# GET the Count of Total Faculty, Total Present, Total Late and Total Absent
	def count_data():
		total_faculty = conn.cursor()
		total_present = conn.cursor()
		total_absent = conn.cursor()

		date_mathematics = date_lb_math_rec.cget("text")

		total_faculty.execute("SELECT COUNT(*) FROM faculty_data WHERE  Department='Mathematics'")
		total_math = total_faculty.fetchall()

		total_present.execute("SELECT COUNT(Remark) FROM attendance_record WHERE  Department='Mathematics' AND Remark ='Present' AND _Date='"+ str(date_mathematics) +"'")
		present_math = total_present.fetchall()

		total_absent.execute("SELECT COUNT(Remark) FROM attendance_record WHERE Department='Mathematics' AND Remark='Absent' AND _Date='"+ str(date_mathematics) +"'")
		absent_math = total_absent.fetchall()

		total_faculty_lb_math_rec.configure(text=total_math)
		total_present_lb_math_rec.configure(text=present_math)
		total_absent_lb_math_rec.configure(text=absent_math)

		conn.commit()

	    # Get And Disply the data in the table
	def math_read():
		cursor = conn.cursor()
		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE Department='Mathematics'")
		results_math = cursor.fetchall()
		conn.commit()
		return results_math

	        # Refresh the tabble on Treeview
	def refreshTable_math():
		for data_math in data_table_math_rec.get_children():
			data_table_math_rec.delete(data_math)

		for results_math_rec in reverse(math_read()):
			data_table_math_rec.insert(parent='', index='end', iid=results_math_rec, text="", values=(results_math_rec), tag="orow")
		data_table_math_rec.tag_configure('orow', background='#EEEEEE')

	def search_data_math():
		lookup_record = search_math_rec.get()
		cursor = conn.cursor()

		# Clear the Treeview
		for record in data_table_math_rec.get_children():
			data_table_math_rec.delete(record)

		lk_rec = '%' +lookup_record+ '%'
		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE (_Date LIKE '" + str(lk_rec) + "' or Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "' or Department LIKE '" + str(lk_rec) + "' or Time_in LIKE '" + str(lk_rec) + "' or Time_out LIKE '" + str(lk_rec) + "') AND Department='Mathematics'")

		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
				data_table_math_rec.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="evenrow")
			else:
				data_table_math_rec.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="oddrow")
			count += 1
			data_table_math_rec.tag_configure('evenrow', background='#EEEEEE')
			data_table_math_rec.tag_configure('oddrow', background='#EEEEEE')
			search_math_rec.delete(0, END)

		conn.commit()

	def print_math():
		file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

		cols = ['Date','Employee No.','Name','Department','Time in','Time out']
		path = 'excelfile/read_data_employee_mathematics.csv'
		excel_name = 'excelfile/new_datasave.xlsx'
		lst = []
		with open(path,"w",newline='') as myfile:
			csvwriter = csv.writer(myfile, delimiter=',')
			for row_id in data_table_math_rec.get_children():
				row = data_table_math_rec.item(row_id,'values')
				lst.append(row)
			lst = list(map(list,lst))
			lst.insert(0,cols)
			for row in lst:
				csvwriter.writerow(row)

		writer = pd.ExcelWriter(excel_name)
		df = pd.read_csv(path)
		df.to_excel(writer,'sheet1', startrow = 3, index = False)

		workbook = writer.book
		worksheet = writer.sheets['sheet1']
		worksheet.write(0,0,'Departmet:_Mathematics_ ', workbook.add_format({'bold': True}))
		worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
		worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

		writer.save()
		source = "excelfile/new_datasave.xlsx"
		if file:
			shutil.copy(source,file) 
		else:
			messagebox.showinfo("Message", "You did not save the file!!")

	     # Data Table "TreeView"
	scrollbarx_math_rec = Scrollbar(mathematics_att_record, orient=HORIZONTAL)
	scrollbarx_math_rec.place(x=710, y=584, width=347)
	scrollbary_math_rec = Scrollbar(mathematics_att_record, orient=VERTICAL)
	scrollbary_math_rec.place(x=1040, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_math_rec = ttk.Treeview(mathematics_att_record)
	data_table_math_rec.place(x=710, y=366, width=330, height=219)
	data_table_math_rec.configure(yscrollcommand=scrollbary_math_rec.set, xscrollcommand=scrollbarx_math_rec.set)

	scrollbarx_math_rec.configure(command=data_table_math_rec.xview)
	scrollbary_math_rec.configure(command=data_table_math_rec.yview)

	data_table_math_rec['columns'] = ("Date","Employee No.","Name","Department","Time in","Time out")
	# Format Columns
	data_table_math_rec.column("#0", width=0, stretch=NO)
	data_table_math_rec.column("Date", anchor=W, width=100)
	data_table_math_rec.column("Employee No.", anchor=W, width=100)
	data_table_math_rec.column("Name", anchor=W, width=100)
	data_table_math_rec.column("Department", anchor=W, width=100)
	data_table_math_rec.column("Time in", anchor=W, width=100)
	data_table_math_rec.column("Time out", anchor=W, width=100)

	# Create Headings
	data_table_math_rec.heading("Date", text="Date", anchor=CENTER)
	data_table_math_rec.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_math_rec.heading("Name", text="Name", anchor=CENTER)
	data_table_math_rec.heading("Department", text="Department", anchor=CENTER)
	data_table_math_rec.heading("Time in", text="Time in", anchor=CENTER)
	data_table_math_rec.heading("Time out", text="Time out", anchor=CENTER)

	refreshTable_math()

	def math_read_IR():
		cursor = conn.cursor()

		cursor.execute("SELECT DISTINCT Employee_Number,Employee_Name FROM faculty_data WHERE Department='Mathematics'")
		results_math_IR = cursor.fetchall()

		conn.commit()
		return results_math_IR

	def refreshTable_math_IR():
		for data_math_IR in data_table_math_rec_IR.get_children():
			data_table_math_rec_IR.delete(data_math_IR)

		for results_math_rec_IR in reverse(math_read_IR()):
			data_table_math_rec_IR.insert(parent='', index='end', iid=results_math_rec_IR, text="", values=(results_math_rec_IR), tag="orow")
		data_table_math_rec_IR.tag_configure('orow', background='#EEEEEE')

	def search_data_math_IR():
		lookup_record = search_math_rec_IR.get()

		# Clear the Treeview
		for record in data_table_math_rec_IR.get_children():
			data_table_math_rec_IR.delete(record)
        
		lk_rec = '%'+lookup_record+'%'
		cursor.execute("SELECT Employee_Number,Employee_Name FROM faculty_data WHERE (Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "') AND Department='Mathematics'")
		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
			    data_table_math_rec_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="evenrow")
			else:
			    data_table_math_rec_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="oddrow")
			count += 1
			data_table_math_rec_IR.tag_configure('evenrow', background='#EEEEEE')
			data_table_math_rec_IR.tag_configure('oddrow', background='#EEEEEE')
			search_math_rec_IR.delete(0, END)

		conn.commit()

	def select_row_math(e):
		selected = data_table_math_rec_IR.focus()
		values = data_table_math_rec_IR.item(selected, 'values')

		if values :
			math_rec_button_report.configure(state='normal')
			employee_num_math_rec.configure(state='normal')
			employee_name_math_rec.configure(state='normal')

			employee_num_math_rec.delete(0, END)
			employee_name_math_rec.delete(0, END)

			employee_num_math_rec.insert(0, values[0])
			employee_name_math_rec.insert(0, values[1])

			employee_num_math_rec.configure(state='disabled',text='')
			employee_name_math_rec.configure(state='disabled')
		else:
			messagebox.showinfo("Error", "There is no selected data on the table !!")

	     # Data Table "TreeView" Individual Report
	scrollbary_math_rec = Scrollbar(mathematics_att_record, orient=VERTICAL)
	scrollbary_math_rec.place(x=645, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_math_rec_IR = ttk.Treeview(mathematics_att_record)
	data_table_math_rec_IR.place(x=315, y=366, width=330, height=219)
	data_table_math_rec_IR.configure(yscrollcommand=scrollbary_math_rec.set)

	scrollbary_math_rec.configure(command=data_table_math_rec_IR.yview)

	data_table_math_rec_IR['columns'] = ("Employee No.","Name")
	# Format Columns Individual Report
	data_table_math_rec_IR.column("#0", width=0, stretch=NO)
	data_table_math_rec_IR.column("Employee No.", anchor=W, width=50)
	data_table_math_rec_IR.column("Name", anchor=W, width=100)

	# Create Headings Individual Report
	data_table_math_rec_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_math_rec_IR.heading("Name", text="Name", anchor=CENTER)

	data_table_math_rec_IR.bind("<ButtonRelease-1>", select_row_math)

	refreshTable_math_IR()

	    # Time Text
	time_lb = Label(mathematics_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb.place(x=540, y=10)

	    # date Text
	date_lb = Label(mathematics_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb.place(x=710, y=10)

	    # Time Label
	time_lb_math_rec = Label(mathematics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb_math_rec.place(x=590, y=10)

	    # date Label
	date_lb_math_rec = Label(mathematics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb_math_rec.place(x=760, y=10)
	
	    # Total Faculty Label
	total_faculty_lb_math_rec = Label(mathematics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_faculty_lb_math_rec.place(x=447, y=190)

	    # Total Present Label
	total_present_lb_math_rec = Label(mathematics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_present_lb_math_rec.place(x=665, y=190)

	    # Total Absent Label
	total_absent_lb_math_rec = Label(mathematics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_absent_lb_math_rec.place(x=872, y=190)

	    # Entry Employee Number
	employee_num_math_rec = Entry(mathematics_att_record)
	employee_num_math_rec.place(x=315, y=586, width=100)

	    # Entry Employee Name
	employee_name_math_rec = Entry(mathematics_att_record)
	employee_name_math_rec.place(x=425, y=586, width=100)

	    # Summary Report Button 
	math_rec_button_report = customtkinter.CTkButton(master=mathematics_att_record, state='disabled', text="Summary Report" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=summary_math)
	math_rec_button_report.place(x=550, y=586, height=21,width=110)

	     # Search Entry Individual Report
	search_ent_math_rec_IR = StringVar()
	search_math_rec_IR = Entry(mathematics_att_record, textvariable = search_ent_math_rec_IR)
	search_math_rec_IR.place(x=385, y=305, width=190)

	    # Search Button Individual Report
	search_btn_math_rec_IR = PhotoImage(file = "pic/btn_search_small.png")
	math_rec_button_search_IR = customtkinter.CTkButton(master=mathematics_att_record,image=search_btn_math_rec_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_math_IR)
	math_rec_button_search_IR.place(x=590, y=307, height=17,width=70)

	    # Show All Button Individual Report
	showall_btn_math_rec_IR = PhotoImage(file = "pic/btn_showall_small.png")
	math_rec_button_showall_IR = customtkinter.CTkButton(master=mathematics_att_record,image=showall_btn_math_rec_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_math_IR)
	math_rec_button_showall_IR.place(x=445, y=608, height=21,width=90)

	    # Search Entry
	search_ent = StringVar()
	search_math_rec = Entry(mathematics_att_record, textvariable = search_ent)
	search_math_rec.place(x=780, y=307, width=190)

	    # Search Button
	search_btn_math_rec = PhotoImage(file = "pic/btn_search_small.png")
	math_rec_button_search = customtkinter.CTkButton(master=mathematics_att_record,image=search_btn_math_rec, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_math)
	math_rec_button_search.place(x=975, y=307, height=17,width=70)

	    # Show All Button
	showall_btn_math_rec = PhotoImage(file = "pic/btn_showall_small.png")
	math_rec_button_showall = customtkinter.CTkButton(master=mathematics_att_record,image=showall_btn_math_rec, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_math)
	math_rec_button_showall.place(x=885, y=608, height=21,width=90)

	    # Print Button
	print_btn_math_rec = PhotoImage(file = "pic/btn_print.png")
	math_rec_button_print = customtkinter.CTkButton(master=mathematics_att_record,image=print_btn_math_rec, text="",
	                                                corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_math)
	math_rec_button_print.place(x=785, y=608, height=20,width=80)

	    # Back Button
	math_rec_back = PhotoImage(file = "pic/btn_back_page.png")
	math_rec_button_back = customtkinter.CTkButton(master=mathematics_att_record,image=math_rec_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
	math_rec_button_back.place(x=45, y=595, height=50,width=140)

	time_math()
	count_data()

	# ============= Psychology Attendance Record Frame =============================================================================

	    # open background image
	psychology_att_record.psyc_image = Image.open('pic/17.png')
	psychology_att_record.psyc_resize_image = psychology_att_record.psyc_image.resize((1362, 692))
	psychology_att_record.photo = ImageTk.PhotoImage(psychology_att_record.psyc_resize_image)
	psychology_att_record.psyc_bg_img_lb = Label(psychology_att_record, image = psychology_att_record.photo)
	psychology_att_record.psyc_bg_img_lb.pack()

	     # Get Current Time and Date
	def time_psyc():
		string_time_psyc = strftime('%H:%M %p')
		time_lb_psyc.configure(text = string_time_psyc)
		time_lb_psyc.after(1000, time_psyc)

		string_date_psyc = strftime('%d-%m-20%y')
		date_lb_psyc.configure(text = string_date_psyc)

		# GET the Count of Total Faculty, Total Present, Total Late and Total Absent
	def count_data_psyc():
		total_faculty = conn.cursor()
		total_present = conn.cursor()
		total_absent = conn.cursor()

		date_psychology = date_lb_psyc.cget("text")

		total_faculty.execute("SELECT COUNT(*) FROM faculty_data WHERE Department='Psychology'")
		total_psyc = total_faculty.fetchall()

		total_present.execute("SELECT COUNT(Remark) FROM attendance_record WHERE  Department='Psychology' AND Remark='Present' AND _Date='"+ str(date_psychology) +"'")
		present_psyc = total_present.fetchall()

		total_absent.execute("SELECT COUNT(Remark) FROM attendance_record WHERE Department='Psychology' AND Remark='Absent' AND _Date='"+ str(date_psychology) +"'")
		absent_psyc = total_absent.fetchall()

		total_faculty_lb_psyc.configure(text=total_psyc)
		total_present_lb_psyc.configure(text=present_psyc)
		total_absent_lb_psyc.configure(text=absent_psyc)

		conn.commit()

		# Get And Disply the data in the table
	def psyc_read():
		cursor = conn.cursor()

		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE Department='Psychology'")
		results_psyc = cursor.fetchall()

		conn.commit()
		return results_psyc

		# Refresh the tabble on Treeview
	def refreshTable_psyc():
		for data_psyc in data_table_psyc.get_children():
			data_table_psyc.delete(data_psyc)

		for results_psyc_rec in reverse(psyc_read()):
			data_table_psyc.insert(parent='', index='end', iid=results_psyc_rec, text="", values=(results_psyc_rec), tag="orow")
		data_table_psyc.tag_configure('orow', background='#EEEEEE')

	def search_data_psyc():
		lookup_record = search_psyc.get()

		cursor = conn.cursor()

		# Clear the Treeview
		for record in data_table_psyc.get_children():
			data_table_psyc.delete(record)
        
		lk_rec = '%' +lookup_record+ '%'
		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE (_Date LIKE '" + str(lk_rec) + "' or Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "' or Department LIKE '" + str(lk_rec) + "' or Time_in LIKE '" + str(lk_rec) + "' or Time_out LIKE '" + str(lk_rec) + "') AND Department='Psychology'")
		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
				data_table_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="evenrow")
			else:
				data_table_psyc.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="oddrow")
			count += 1
			data_table_psyc.tag_configure('evenrow', background='#EEEEEE')
			data_table_psyc.tag_configure('oddrow', background='#EEEEEE')
			search_psyc.delete(0, END)

		conn.commit()

	def print_psyc():
		file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

		cols = ['Date','Employee No.','Name','Department','Time in','Time out']
		path = 'excelfile/read_data_employee_psychology.csv'
		excel_name = 'excelfile/new_datasave_psychology.xlsx'
		lst = []
		with open(path,"w",newline='') as myfile:
			csvwriter = csv.writer(myfile, delimiter=',')
			for row_id in data_table_psyc.get_children():
				row = data_table_psyc.item(row_id,'values')
				lst.append(row)
			lst = list(map(list,lst))
			lst.insert(0,cols)
			for row in lst:
				csvwriter.writerow(row)

		writer = pd.ExcelWriter(excel_name)
		df = pd.read_csv(path)
		df.to_excel(writer,'sheet1', startrow = 3, index = False)

		workbook = writer.book
		worksheet = writer.sheets['sheet1']
		worksheet.write(0,0,'Departmet:_Psychology_ ', workbook.add_format({'bold': True}))
		worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
		worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

		writer.save()
		source = "excelfile/new_datasave_psychology.xlsx"
		if file:
			shutil.copy(source,file)
		else:
			messagebox.showinfo("Message", "You did not save the file!!")

	     # Data Table "TreeView"
	scrollbarx_psyc = Scrollbar(psychology_att_record, orient=HORIZONTAL)
	scrollbarx_psyc.place(x=710, y=584, width=347)
	scrollbary_psyc = Scrollbar(psychology_att_record, orient=VERTICAL)
	scrollbary_psyc.place(x=1040, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_psyc = ttk.Treeview(psychology_att_record)
	data_table_psyc.place(x=710, y=366, width=330, height=219)
	data_table_psyc.configure(yscrollcommand=scrollbary_psyc.set, xscrollcommand=scrollbarx_psyc.set)

	scrollbarx_psyc.configure(command=data_table_psyc.xview)
	scrollbary_psyc.configure(command=data_table_psyc.yview)

	data_table_psyc['columns'] = ("Date","Employee No.","Name","Department","Time in","Time out")
	# Format Columns
	data_table_psyc.column("#0", width=0, stretch=NO)
	data_table_psyc.column("Date", anchor=W, width=100)
	data_table_psyc.column("Employee No.", anchor=W, width=100)
	data_table_psyc.column("Name", anchor=W, width=100)
	data_table_psyc.column("Department", anchor=W, width=100)
	data_table_psyc.column("Time in", anchor=W, width=100)
	data_table_psyc.column("Time out", anchor=W, width=100)

	# Create Headings
	data_table_psyc.heading("Date", text="Date", anchor=CENTER)
	data_table_psyc.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_psyc.heading("Name", text="Name", anchor=CENTER)
	data_table_psyc.heading("Department", text="Department", anchor=CENTER)
	data_table_psyc.heading("Time in", text="Time in", anchor=CENTER)
	data_table_psyc.heading("Time out", text="Time out", anchor=CENTER)

	refreshTable_psyc()

	def psyc_read_IR():
		cursor = conn.cursor()

		cursor.execute("SELECT DISTINCT Employee_Number,Employee_Name FROM faculty_data WHERE Department='Psychology'")
		results_psyc_IR = cursor.fetchall()

		conn.commit()
		return results_psyc_IR

        # Refresh the tabble on Treeview
	def refreshTable_psyc_IR():
		for data_psyc in data_table_psyc_IR.get_children():
			data_table_psyc_IR.delete(data_psyc)

		for results_psyc_rec_IR in reverse(psyc_read_IR()):
			data_table_psyc_IR.insert(parent='', index='end', iid=results_psyc_rec_IR, text="", values=(results_psyc_rec_IR), tag="orow")
		data_table_psyc_IR.tag_configure('orow', background='#EEEEEE')

	def search_data_psyc_IR():
		lookup_record = search_psyc_IR.get()

		cursor = conn.cursor()

		# Clear the Treeview
		for record in data_table_psyc_IR.get_children():
			data_table_psyc_IR.delete(record)
        
		lk_rec = '%' +lookup_record+ '%'
		cursor.execute("SELECT Employee_Number,Employee_Name FROM faculty_data WHERE (Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "') AND Department='Psychology'")
		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
				data_table_psyc_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="evenrow")
			else:
				data_table_psyc_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="oddrow")
			count += 1
			data_table_psyc_IR.tag_configure('evenrow', background='#EEEEEE')
			data_table_psyc_IR.tag_configure('oddrow', background='#EEEEEE')
			search_psyc_IR.delete(0, END)

		conn.commit()

	def select_row_psyc(e):
		selected = data_table_psyc_IR.focus()
		values = data_table_psyc_IR.item(selected, 'values')

		if values:
			psyc_button_report.configure(state='normal')
			employee_num_psyc.configure(state='normal')
			employee_name_psyc.configure(state='normal')

			employee_num_psyc.delete(0, END)
			employee_name_psyc.delete(0, END)

			employee_num_psyc.insert(0, values[0])
			employee_name_psyc.insert(0, values[1])

			employee_num_psyc.configure(state='disabled')
			employee_name_psyc.configure(state='disabled')
		else:
			messagebox.showinfo("Error", "There is no  selected data on the table !!")

	     # Data Table "TreeView"
	scrollbary_psyc_IR = Scrollbar(psychology_att_record, orient=VERTICAL)
	scrollbary_psyc_IR.place(x=645, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_psyc_IR = ttk.Treeview(psychology_att_record)
	data_table_psyc_IR.place(x=315, y=366, width=330, height=219)
	data_table_psyc_IR.configure(yscrollcommand=scrollbary_psyc_IR.set)

	scrollbary_psyc_IR.configure(command=data_table_psyc_IR.yview)

	data_table_psyc_IR['columns'] = ("Employee No.","Name")
	# Format Columns
	data_table_psyc_IR.column("#0", width=0, stretch=NO)
	data_table_psyc_IR.column("Employee No.", anchor=W, width=50)
	data_table_psyc_IR.column("Name", anchor=W, width=100)

	# Create Headings
	data_table_psyc_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_psyc_IR.heading("Name", text="Name", anchor=CENTER)

	data_table_psyc_IR.bind("<ButtonRelease-1>", select_row_psyc)

	refreshTable_psyc_IR()

		# Time Text
	time_lb = Label(psychology_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb.place(x=540, y=10)

		# date Text
	date_lb = Label(psychology_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb.place(x=710, y=10)

		# Time Label
	time_lb_psyc = Label(psychology_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb_psyc.place(x=590, y=10)

		# date Label
	date_lb_psyc = Label(psychology_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb_psyc.place(x=760, y=10)

	    # Total Faculty Label
	total_faculty_lb_psyc = Label(psychology_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_faculty_lb_psyc.place(x=447, y=190)

	    # Total Present Label
	total_present_lb_psyc = Label(psychology_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_present_lb_psyc.place(x=665, y=190)

	    # Total Absent Label
	total_absent_lb_psyc = Label(psychology_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_absent_lb_psyc.place(x=872, y=190)

	    # Entry Employee Number
	employee_num_psyc = Entry(psychology_att_record)
	employee_num_psyc.place(x=315, y=586, width=100)

	    # Entry Employee Name
	employee_name_psyc = Entry(psychology_att_record)
	employee_name_psyc.place(x=425, y=586, width=100)

	    # Summary Report Button 
	psyc_button_report = customtkinter.CTkButton(master=psychology_att_record,state='disabled', text="Summary Report",
	                                            corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=summary_psyc)
	psyc_button_report.place(x=550, y=586, height=21,width=110)

	     # Search Entry Individual Report
	search_ent_psyc_IR = StringVar()
	search_psyc_IR = Entry(psychology_att_record, textvariable = search_ent_psyc_IR)
	search_psyc_IR.place(x=385, y=305, width=190)

	    # Search Button Individual Report
	search_btn_psyc_IR = PhotoImage(file = "pic/btn_search_small.png")
	psyc_button_search_IR = customtkinter.CTkButton(master=psychology_att_record,image=search_btn_psyc_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_psyc_IR)
	psyc_button_search_IR.place(x=590, y=307, height=17,width=70)

	    # Show All Button Individual Report
	showall_btn_psyc_IR = PhotoImage(file = "pic/btn_showall_small.png")
	psyc_button_showall_IR = customtkinter.CTkButton(master=psychology_att_record,image=showall_btn_psyc_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_psyc_IR)
	psyc_button_showall_IR.place(x=445, y=608, height=21,width=90)

	    # Search Entry
	search_ent_psyc = StringVar()
	search_psyc = Entry(psychology_att_record, textvariable = search_ent_psyc)
	search_psyc.place(x=780, y=307, width=190)

	    # Search Button
	search_btn_psyc = PhotoImage(file = "pic/btn_search_small.png")
	psyc_button_search = customtkinter.CTkButton(master=psychology_att_record,image=search_btn_psyc, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_psyc)
	psyc_button_search.place(x=975, y=307, height=17,width=70)

	    # Show All Button
	showall_btn_psyc = PhotoImage(file = "pic/btn_showall_small.png")
	psyc_button_showall = customtkinter.CTkButton(master=psychology_att_record,image=showall_btn_psyc, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_psyc)
	psyc_button_showall.place(x=885, y=608, height=21,width=90)

	    # Print Button
	print_btn_psyc = PhotoImage(file = "pic/btn_print.png")
	psyc_button_print = customtkinter.CTkButton(master=psychology_att_record,image=print_btn_psyc, text="",
	                                                corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_psyc)
	psyc_button_print.place(x=785, y=608, height=20,width=80)

	    # Back Button
	psyc_back = PhotoImage(file = "pic/btn_back_page.png")
	psyc_button_back = customtkinter.CTkButton(master=psychology_att_record,image=psyc_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
	psyc_button_back.place(x=45, y=595, height=50,width=140)

	time_psyc()
	count_data_psyc()

    # ============= Applied Physics Attendance Record Frame =============================================================================

	    # open background image
	applied_physics_att_record.applied_image = Image.open('pic/18.png')
	applied_physics_att_record.applied_resize_image = applied_physics_att_record.applied_image.resize((1362, 692))
	applied_physics_att_record.photo = ImageTk.PhotoImage(applied_physics_att_record.applied_resize_image)
	applied_physics_att_record.applied_bg_img_lb = Label(applied_physics_att_record, image = applied_physics_att_record.photo)
	applied_physics_att_record.applied_bg_img_lb.pack()

	    #  Get Current Time and Date
	def time_applied():
		string_time_applied = strftime('%H:%M %p')
		time_lb_applied.configure(text = string_time_applied)
		time_lb_applied.after(1000, time_applied)

		string_date_applied = strftime('%d-%m-20%y')
		date_lb_applied.configure(text = string_date_applied)

		# GET the Count of Total Faculty, Total Present, Total Late and Total Absent
	def count_data_applied():
		total_faculty = conn.cursor()
		total_present = conn.cursor()
		total_absent = conn.cursor()

		date_physics = date_lb_applied.cget("text")

		total_faculty.execute("SELECT COUNT(*) FROM faculty_data WHERE Department='Applied Physics'")
		total_physics = total_faculty.fetchall()

		total_present.execute("SELECT COUNT(Remark) FROM attendance_record WHERE  Department='Applied Physics' AND Remark='Present' AND _Date='"+ str(date_physics) +"'")
		present_physics = total_present.fetchall()

		total_absent.execute("SELECT COUNT(Remark) FROM attendance_record WHERE Department='Applied Physics' AND Remark='Absent' AND _Date='"+ str(date_physics) +"'")
		absent_physics = total_absent.fetchall()

		total_faculty_lb_applied.configure(text=total_physics)
		total_present_lb_applied.configure(text=present_physics)
		total_absent_lb_applied.configure(text=absent_physics)

		conn.commit()

            # Get And Disply the data in the table
	def applied_read():
		cursor = conn.cursor()

		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE Department='Applied Physics'")
		results_applied = cursor.fetchall()

		conn.commit()
		return results_applied

        # Refresh the tabble on Treeview
	def refreshTable_applied():
		for data_applied in data_table_applied.get_children():
			data_table_applied.delete(data_applied)

		for results_applied_rec in reverse(applied_read()):
			data_table_applied.insert(parent='', index='end', iid=results_applied_rec, text="", values=(results_applied_rec), tag="orow")
		data_table_applied.tag_configure('orow', background='#EEEEEE')

	def search_data_applied():
		lookup_record = search_applied.get()
		cursor = conn.cursor()

		# Clear the Treeview
		for record in data_table_applied.get_children():
			data_table_applied.delete(record)

		lk_rec = '%' +lookup_record+ '%'
		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE (_Date LIKE '" + str(lk_rec) + "' or Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "' or Department LIKE '" + str(lk_rec) + "' or Time_in LIKE '" + str(lk_rec) + "' or Time_out LIKE '" + str(lk_rec) + "') AND Department='Applied Physics'")
		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
				data_table_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="evenrow")
			else:
				data_table_applied.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="oddrow")
			count += 1
			data_table_applied.tag_configure('evenrow', background='#EEEEEE')
			data_table_applied.tag_configure('oddrow', background='#EEEEEE')
			search_applied.delete(0, END)

		conn.commit()

	def print_applied():
		file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

		cols =  ['Date','Employee No.','Name','Department','Time in','Time out']
		path = 'excelfile/read_data_employee_appliedphysics.csv'
		excel_name = 'excelfile/new_datasave_appliedphysics.xlsx'
		lst = []
		with open(path,"w",newline='') as myfile:
			csvwriter = csv.writer(myfile, delimiter=',')
			for row_id in data_table_applied.get_children():
				row = data_table_applied.item(row_id,'values')
				lst.append(row)
			lst = list(map(list,lst))
			lst.insert(0,cols)
			for row in lst:
				csvwriter.writerow(row)

		writer = pd.ExcelWriter(excel_name)
		df = pd.read_csv(path)
		df.to_excel(writer,'sheet1', startrow = 3, index = False)

		workbook = writer.book
		worksheet = writer.sheets['sheet1']
		worksheet.write(0,0,'Departmet:_Applied Physics_ ', workbook.add_format({'bold': True}))
		worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
		worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

		writer.save()
		source = "excelfile/new_datasave_appliedphysics.xlsx"
		if file:
			shutil.copy(source,file)
		else:
			messagebox.showinfo("Message", "You did not save the file!!")

	     # Data Table "TreeView"
	scrollbarx_applied = Scrollbar(applied_physics_att_record, orient=HORIZONTAL)
	scrollbarx_applied.place(x=710, y=584, width=347)
	scrollbary_applied = Scrollbar(applied_physics_att_record, orient=VERTICAL)
	scrollbary_applied.place(x=1040, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_applied = ttk.Treeview(applied_physics_att_record)
	data_table_applied.place(x=710, y=366, width=330, height=219)
	data_table_applied.configure(yscrollcommand=scrollbary_applied.set, xscrollcommand=scrollbarx_applied.set)

	scrollbarx_applied.configure(command=data_table_applied.xview)
	scrollbary_applied.configure(command=data_table_applied.yview)

	data_table_applied['columns'] = ("Date","Employee No.","Name","Department","Time in","Time out")
	# Format Columns
	data_table_applied.column("#0", width=0, stretch=NO)
	data_table_applied .column("Date", anchor=W, width=100)
	data_table_applied.column("Employee No.", anchor=W, width=100)
	data_table_applied.column("Name", anchor=W, width=100)
	data_table_applied.column("Department", anchor=W, width=100)
	data_table_applied.column("Time in", anchor=W, width=100)
	data_table_applied.column("Time out", anchor=W, width=100)

	# Create Headings
	data_table_applied.heading("Date", text="Date", anchor=CENTER)
	data_table_applied.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_applied.heading("Name", text="Name", anchor=CENTER)
	data_table_applied.heading("Department", text="Department", anchor=CENTER)
	data_table_applied.heading("Time in", text="Time in", anchor=CENTER)
	data_table_applied.heading("Time out", text="Time out", anchor=CENTER)

	refreshTable_applied()

	def applied_read_IR():
		cursor = conn.cursor()

		cursor.execute("SELECT DISTINCT Employee_Number,Employee_Name FROM faculty_data WHERE Department='Applied Physics'")
		results_applied_IR = cursor.fetchall()

		conn.commit()
		return results_applied_IR

        # Refresh the tabble on Treeview
	def refreshTable_applied_IR():
		for data_applied_IR in data_table_applied_IR.get_children():
			data_table_applied_IR.delete(data_applied_IR)

		for results_applied_rec_IR in reverse(applied_read_IR()):
			data_table_applied_IR.insert(parent='', index='end', iid=results_applied_rec_IR, text="", values=(results_applied_rec_IR), tag="orow")
		data_table_applied_IR.tag_configure('orow', background='#EEEEEE')

	def search_data_applied_IR():
		lookup_record = search_applied_IR.get()

		cursor = conn.cursor()

		# Clear the Treeview
		for record in data_table_applied_IR.get_children():
			data_table_applied_IR.delete(record)

		lk_rec = '%' +lookup_record+ '%'
		cursor.execute("SELECT Employee_Number,Employee_Name FROM faculty_data WHERE (Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "')AND Department='Applied Physics'")
		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
				data_table_applied_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="evenrow")
			else:
				data_table_applied_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="oddrow")
			count += 1
			data_table_applied_IR.tag_configure('evenrow', background='#EEEEEE')
			data_table_applied_IR.tag_configure('oddrow', background='#EEEEEE')
			search_applied_IR.delete(0, END)

		conn.commit()

	def select_row_applied_IR(e):
		selected = data_table_applied_IR.focus()
		values = data_table_applied_IR.item(selected, 'values')

		if values:
			applied_button_report.configure(state='normal')
			employee_num_applied.configure(state='normal')
			employee_name_applied.configure(state='normal')

			employee_num_applied.delete(0, END)
			employee_name_applied.delete(0, END)

			employee_num_applied.insert(0, values[0])
			employee_name_applied.insert(0, values[1])

			employee_num_applied.configure(state='disabled')
			employee_name_applied.configure(state='disabled')
		else:
			messagebox.showinfo("Error", "There is no selected data on the table !!")

	 # Data Table "TreeView" Individual Report
	scrollbary_applied_IR = Scrollbar(applied_physics_att_record, orient=VERTICAL)
	scrollbary_applied_IR.place(x=645, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_applied_IR = ttk.Treeview(applied_physics_att_record)
	data_table_applied_IR.place(x=315, y=366, width=330, height=219)
	data_table_applied_IR.configure(yscrollcommand=scrollbary_applied_IR.set)

	scrollbary_applied_IR.configure(command=data_table_applied_IR.yview)

	data_table_applied_IR['columns'] = ("Employee No.","Name")
	# Format Columns Individual Report
	data_table_applied_IR.column("#0", width=0, stretch=NO)
	data_table_applied_IR.column("Employee No.", anchor=W, width=50)
	data_table_applied_IR.column("Name", anchor=W, width=100)

	# Create Headings Individual Report
	data_table_applied_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_applied_IR.heading("Name", text="Name", anchor=CENTER)

	data_table_applied_IR.bind("<ButtonRelease-1>", select_row_applied_IR)

	refreshTable_applied_IR()

		# Time Text
	time_lb = Label(applied_physics_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb.place(x=540, y=1)

		# date Text
	date_lb = Label(applied_physics_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb.place(x=710, y=1)

		# Time Label
	time_lb_applied = Label(applied_physics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb_applied.place(x=590, y=1)

		# date Label
	date_lb_applied = Label(applied_physics_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb_applied.place(x=760, y=1)

	    # Total Faculty Label
	total_faculty_lb_applied = Label(applied_physics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_faculty_lb_applied.place(x=447, y=190)

	    # Total Present Label
	total_present_lb_applied = Label(applied_physics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_present_lb_applied.place(x=665, y=190)

	    # Total Absent Label
	total_absent_lb_applied = Label(applied_physics_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_absent_lb_applied.place(x=872, y=190)
	    # Entry Employee Number
	employee_num_applied = Entry(applied_physics_att_record)
	employee_num_applied.place(x=315, y=586, width=100)

	    # Entry Employee Name
	employee_name_applied = Entry(applied_physics_att_record)
	employee_name_applied.place(x=425, y=586, width=100)

	    # Summary Report Button 
	applied_button_report = customtkinter.CTkButton(master=applied_physics_att_record, state='disabled', text="Summary Report" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=summary_applied)
	applied_button_report.place(x=550, y=586, height=21,width=110)

	     # Search Entry Individual Report
	search_ent_applied_IR = StringVar()
	search_applied_IR = Entry(applied_physics_att_record, textvariable = search_ent_applied_IR)
	search_applied_IR.place(x=385, y=305, width=190)

	    # Search Button Individual Report
	search_btn_applied_IR = PhotoImage(file = "pic/btn_search_small.png")
	applied_button_search_IR = customtkinter.CTkButton(master=applied_physics_att_record,image=search_btn_applied_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_applied_IR)
	applied_button_search_IR.place(x=590, y=307, height=17,width=70)

	    # Show All Button Individual Report
	showall_btn_applied_IR = PhotoImage(file = "pic/btn_showall_small.png")
	applied_button_showall_IR = customtkinter.CTkButton(master=applied_physics_att_record,image=showall_btn_applied_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_applied_IR)
	applied_button_showall_IR.place(x=445, y=608, height=21,width=90)

	    # Search Entry
	search_ent_applied = StringVar()
	search_applied = Entry(applied_physics_att_record, textvariable = search_ent_applied)
	search_applied.place(x=780, y=307, width=190)

	    # Search Button
	search_btn_applied = PhotoImage(file = "pic/btn_search_small.png")
	applied_button_search = customtkinter.CTkButton(master=applied_physics_att_record,image=search_btn_applied, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_applied)
	applied_button_search.place(x=975, y=307, height=17,width=70)

	    # Show All Button
	showall_btn_applied = PhotoImage(file = "pic/btn_showall_small.png")
	applied_button_showall = customtkinter.CTkButton(master=applied_physics_att_record,image=showall_btn_applied, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_applied)
	applied_button_showall.place(x=885, y=608, height=21,width=90)

	    # Print Button
	print_btn_applied = PhotoImage(file = "pic/btn_print.png")
	applied_button_print = customtkinter.CTkButton(master=applied_physics_att_record,image=print_btn_applied, text="",
	                                                corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_applied)
	applied_button_print.place(x=785, y=608, height=20,width=80)

	    # Back Button
	applied_back = PhotoImage(file = "pic/btn_back_page.png")
	applied_button_back = customtkinter.CTkButton(master=applied_physics_att_record,image=applied_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
	applied_button_back.place(x=45, y=595, height=50,width=140)

	time_applied()
	count_data_applied()

	 # ============= ITE Attendance Record Frame =============================================================================

	    # open background image
	ite_att_record.ite_image = Image.open('pic/20.png')
	ite_att_record.ite_resize_image = ite_att_record.ite_image.resize((1362, 692))
	ite_att_record.photo = ImageTk.PhotoImage(ite_att_record.ite_resize_image)
	ite_att_record.ite_bg_img_lb = Label(ite_att_record, image = ite_att_record.photo)
	ite_att_record.ite_bg_img_lb.pack()

	    #  Get Current Time and Date
	def time_ite():
		string_time_ite = strftime('%H:%M %p')
		time_lb_ite.configure(text = string_time_ite)
		time_lb_ite.after(1000, time_ite)

		string_date_ite = strftime('%d-%m-20%y')
		date_lb_ite.configure(text = string_date_ite)

	def count_data_ite():
		total_faculty = conn.cursor()
		total_present = conn.cursor()
		total_absent = conn.cursor()

		date_IT = date_lb_ite.cget("text")

		total_faculty.execute("SELECT COUNT(*) FROM faculty_data WHERE Department='ITE'")
		total_IT = total_faculty.fetchall()

		total_present.execute("SELECT COUNT(Remark) FROM attendance_record WHERE Department='ITE' AND Remark='Present' AND _Date='"+ str(date_IT) +"'")
		present_IT = total_present.fetchall()

		total_absent.execute("SELECT COUNT(Remark) FROM attendance_record WHERE Department='ITE' AND Remark='Absent' AND _Date='"+ str(date_IT) +"'")
		absent_IT = total_absent.fetchall()

		total_faculty_lb_ite.configure(text=total_IT)
		total_present_lb_ite.configure(text=present_IT)
		total_absent_lb_ite.configure(text=absent_IT)

		conn.commit()

        # Get And Disply the data in the table
	def ite_read():
		cursor = conn.cursor()

		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE Department='ITE'")
		results_ite = cursor.fetchall()

		conn.commit()
		return results_ite

        # Refresh the tabble on Treeview
	def refreshTable_ite():
		for data_ite in data_table_ite.get_children():
			data_table_ite.delete(data_ite)

		for results_ite_rec in reverse(ite_read()):
			data_table_ite.insert(parent='', index='end', text="", values=(results_ite_rec), tag="orow")
		data_table_ite.tag_configure('orow', background='#EEEEEE')

	def search_data_ite():
		lookup_record = search_ite.get()
		cursor = conn.cursor()

		# Clear the Treeview
		for record in data_table_ite.get_children():
			data_table_ite.delete(record)

		lk_rec = '%' +lookup_record+ '%'
		cursor.execute("SELECT _Date,Employee_Number,Employee_Name,Department,Time_in,Time_out FROM attendance_record WHERE (_Date LIKE '" + str(lk_rec) + "' or Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "' or Department LIKE '" + str(lk_rec) + "' or Time_in LIKE '" + str(lk_rec) + "' or Time_out LIKE '" + str(lk_rec) + "') AND Department='ITE'")
		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
				data_table_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="evenrow")
			else:
				data_table_ite.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tag="oddrow")
			count += 1
			data_table_ite.tag_configure('evenrow', background='#EEEEEE')
			data_table_ite.tag_configure('oddrow', background='#EEEEEE')
			search_ite.delete(0, END)

		conn.commit()

	def print_ite():
		file = filedialog.asksaveasfilename(title="Select file",initialfile="datafile.xlsx", defaultextension=".xlsx",filetypes=[("Execl file","*.xlsx")])

		cols = ['Date','Employee No.','Name','Department','Time in','Time out']
		path = 'excelfile/read_data_employee_ite.csv'
		excel_name = 'excelfile/new_datasave_ite.xlsx'
		lst = []
		with open(path,"w",newline='') as myfile:
			csvwriter = csv.writer(myfile, delimiter=',')
			for row_id in data_table_ite.get_children():
				row = data_table_ite.item(row_id,'values')
				lst.append(row)
			lst = list(map(list,lst))
			lst.insert(0,cols)
			for row in lst:
				csvwriter.writerow(row)

		writer = pd.ExcelWriter(excel_name)
		df = pd.read_csv(path)
		df.to_excel(writer,'sheet1', startrow = 3, index = False)

		workbook = writer.book
		worksheet = writer.sheets['sheet1']
		worksheet.write(0,0,'Departmet:_ITE_ ', workbook.add_format({'bold': True}))
		worksheet.write(1,0,'Name:________________ ', workbook.add_format({'bold': True}))
		worksheet.write(1,3,'Employee No:________________ ', workbook.add_format({'bold': True}))

		writer.save()
		source = "excelfile/new_datasave_ite.xlsx"
		if file:
			shutil.copy(source,file)
		else:
			messagebox.showinfo("Message", "You did not save the file!!")


	     # Data Table "TreeView"
	scrollbarx_ite = Scrollbar(ite_att_record, orient=HORIZONTAL)
	scrollbarx_ite.place(x=710, y=584, width=347)
	scrollbary_ite = Scrollbar(ite_att_record, orient=VERTICAL)
	scrollbary_ite.place(x=1040, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_ite = ttk.Treeview(ite_att_record)
	data_table_ite.place(x=710, y=366, width=330, height=219)
	data_table_ite.configure(yscrollcommand=scrollbary_ite.set, xscrollcommand=scrollbarx_ite.set)

	scrollbarx_ite.configure(command=data_table_ite.xview)
	scrollbary_ite.configure(command=data_table_ite.yview)

	data_table_ite['columns'] = ("Date","Employee No.","Name","Department","Time in","Time out")
	# Format Columns
	data_table_ite.column("#0", width=0, stretch=NO)
	data_table_ite.column("Date", anchor=W, width=100)
	data_table_ite.column("Employee No.", anchor=W, width=100)
	data_table_ite.column("Name", anchor=W, width=100)
	data_table_ite.column("Department", anchor=W, width=200)
	data_table_ite.column("Time in", anchor=W, width=100)
	data_table_ite.column("Time out", anchor=W, width=100)

	# Create Headings
	data_table_ite.heading("Date", text="Date", anchor=CENTER)
	data_table_ite.heading("Name", text="Name", anchor=CENTER)
	data_table_ite.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_ite.heading("Department", text="Department", anchor=CENTER)
	data_table_ite.heading("Time in", text="Time in", anchor=CENTER)
	data_table_ite.heading("Time out", text="Time out", anchor=CENTER)

	refreshTable_ite()

	def ite_read_IR():
		cursor = conn.cursor()

		cursor.execute("SELECT DISTINCT Employee_Number,Employee_Name FROM faculty_data WHERE Department='ITE'")
		results_ite_IR = cursor.fetchall()

		conn.commit()
		return results_ite_IR

        # Refresh the tabble on Treeview
	def refreshTable_ite_IR():
		for data_ite_IR in data_table_ite_IR.get_children():
			data_table_ite_IR.delete(data_ite_IR)

		for results_ite_rec_IR in reverse(ite_read_IR()):
			data_table_ite_IR.insert(parent='', index='end', text="", values=(results_ite_rec_IR), tag="orow")
		data_table_ite_IR.tag_configure('orow', background='#EEEEEE')

	def search_data_ite_IR():
		lookup_record = search_ite_IR.get()
		cursor = conn.cursor()

		# Clear the Treeview
		for record in data_table_ite_IR.get_children():
			data_table_ite_IR.delete(record)

		lk_rec = '%' +lookup_record+ '%'
		cursor.execute("SELECT Employee_Number,Employee_Name FROM faculty_data WHERE (Employee_Number LIKE '" + str(lk_rec) + "' or Employee_Name LIKE '" + str(lk_rec) + "') AND Department='ITE'")
		records = cursor.fetchall()

		global count
		count = 0

		for record in records:
			if count % 2 == 0:
				data_table_ite_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="evenrow")
			else:
				data_table_ite_IR.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1]), tag="oddrow")
			count += 1
			data_table_ite_IR.tag_configure('evenrow', background='#EEEEEE')
			data_table_ite_IR.tag_configure('oddrow', background='#EEEEEE')
			search_ite_IR.delete(0, END)

		conn.commit()

	def select_row_ite_IR(e):
		selected = data_table_ite_IR.focus()
		values = data_table_ite_IR.item(selected, 'values')

		if values:
			ite_button_report.configure(state='normal')
			employee_num_ite.configure(state='normal')
			employee_name_ite.configure(state='normal')

			employee_num_ite.delete(0, END)
			employee_name_ite.delete(0, END)

			employee_num_ite.insert(0, values[0])
			employee_name_ite.insert(0, values[1])

			employee_num_ite.configure(state='disabled',text='')
			employee_name_ite.configure(state='disabled')

		else:
			messagebox.showinfo("Error", "There is no selected data on the table !!")

	 	# Data Table "TreeView" Individual Report
	# scrollbarx_ite_IR = Scrollbar(ite_att_record, orient=HORIZONTAL)
	# scrollbarx_ite_IR.place(x=710, y=584, width=347)
	scrollbary_ite_IR = Scrollbar(ite_att_record, orient=VERTICAL)
	scrollbary_ite_IR.place(x=645, y=366, height=219)

	# style = ttk.Style()
	# style.configure("Treeview.Heading", font=("yu gothic ui", 10, "bold"))

	data_table_ite_IR = ttk.Treeview(ite_att_record)
	data_table_ite_IR.place(x=315, y=366, width=330, height=219)
	data_table_ite_IR.configure(yscrollcommand=scrollbary_ite_IR.set)

	# scrollbarx_ite_IR.configure(command=data_table_ite.xview)
	scrollbary_ite_IR.configure(command=data_table_ite.yview)

	data_table_ite_IR['columns'] = ("Employee No.","Name",)
	# Format Columns Individual Report
	data_table_ite_IR.column("#0", width=0, stretch=NO)
	data_table_ite_IR.column("Employee No.", anchor=W, width=50)
	data_table_ite_IR.column("Name", anchor=W, width=100)

	# Create Headings Individual Report
	data_table_ite_IR.heading("Employee No.", text="Employee No.", anchor=CENTER)
	data_table_ite_IR.heading("Name", text="Name", anchor=CENTER)

	data_table_ite_IR.bind("<ButtonRelease-1>", select_row_ite_IR)

	refreshTable_ite_IR()

		# Time Text
	time_lb = Label(ite_att_record, text='Time:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb.place(x=540, y=10)

	    # date Text
	date_lb = Label(ite_att_record, text='Date:', fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb.place(x=710, y=10)

	    # Time Label
	time_lb_ite = Label(ite_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	time_lb_ite.place(x=590, y=10)

	    # date Label
	date_lb_ite = Label(ite_att_record, fg='#000000', bg ='#ffffff', font = "Heltvetica 12 bold")
	date_lb_ite.place(x=760, y=10)

	    # Total Faculty Label
	total_faculty_lb_ite = Label(ite_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_faculty_lb_ite.place(x=445, y=190)

	    # Total Present Label
	total_present_lb_ite = Label(ite_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_present_lb_ite.place(x=665, y=190)

	    # Total Absent Label
	total_absent_lb_ite = Label(ite_att_record, text='000', fg='white', bg ='#00436e', font = "Heltvetica 27 bold")
	total_absent_lb_ite.place(x=870, y=190)

	    # Entry Employee Number
	employee_num_ite = Entry(ite_att_record)
	employee_num_ite.place(x=315, y=586, width=100)

	    # Entry Employee Name
	employee_name_ite = Entry(ite_att_record)
	employee_name_ite.place(x=425, y=586, width=100)

	     # Summary Report Button 
	ite_button_report = customtkinter.CTkButton(master=ite_att_record,state='disabled', text="Summary Report" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#C0C0C0",hover_color="#006699", command=summary_ite)
	ite_button_report.place(x=550, y=586, height=21,width=110)

	     # Search Entry Individual Report
	search_ent_ite_IR = StringVar()
	search_ite_IR = Entry(ite_att_record, textvariable = search_ent_ite_IR)
	search_ite_IR.place(x=385, y=305, width=190)

	    # Search Button Individual Report
	search_btn_ite_IR = PhotoImage(file = "pic/btn_search_small.png")
	ite_button_search_IR = customtkinter.CTkButton(master=ite_att_record,image=search_btn_ite_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_ite_IR)
	ite_button_search_IR.place(x=590, y=307, height=17,width=70)

	    # Show All Button Individual Report
	showall_btn_ite_IR = PhotoImage(file = "pic/btn_showall_small.png")
	ite_button_showall_IR = customtkinter.CTkButton(master=ite_att_record,image=showall_btn_ite_IR, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_ite_IR)
	ite_button_showall_IR.place(x=445, y=608, height=21,width=90)

	    # Search Entry
	search_ent_ite = StringVar()
	search_ite = Entry(ite_att_record, textvariable = search_ent_ite)
	search_ite.place(x=780, y=307, width=190)

	    # Search Button
	search_btn_ite = PhotoImage(file = "pic/btn_search_small.png")
	ite_button_search = customtkinter.CTkButton(master=ite_att_record,image=search_btn_ite, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=search_data_ite)
	ite_button_search.place(x=975, y=307, height=17,width=70)

	     # Print Button
	print_btn_ite = PhotoImage(file = "pic/btn_print.png")
	ite_button_print = customtkinter.CTkButton(master=ite_att_record,image=print_btn_ite, text="",
	                                                corner_radius=3, fg_color="#00436e",hover_color="#006699", command=print_ite)
	ite_button_print.place(x=785, y=608, height=20,width=80)

	    # Show All Button
	showall_btn_ite = PhotoImage(file = "pic/btn_showall_small.png")
	ite_button_showall = customtkinter.CTkButton(master=ite_att_record,image=showall_btn_ite, text="" ,
	                                            corner_radius=3,bg='#ffffff', fg_color="#00436e",hover_color="#006699", command=refreshTable_ite)
	ite_button_showall.place(x=885, y=608, height=21,width=90)

	    # Back Button
	ite_back = PhotoImage(file = "pic/btn_back_page.png")
	ite_button_back = customtkinter.CTkButton(master=ite_att_record,image=ite_back, text="" ,
	                                            corner_radius=20,bg_color='#ffffff', fg_color="#fcd24f",hover_color="#006699", command=lambda: show_frame(attendance_record))
	ite_button_back.place(x=45, y=595, height=50,width=140)

	time_ite()
	count_data_ite()

	main_window.mainloop()

w.destroy()
new_win()
w.mainloop()