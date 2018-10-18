from tkinter import *
from PIL import ImageTk, Image
import os
from database_connection import *

#-----------------------------------------Important functions-----------------------------------------------------
def open_version_file():
	os.startfile("Version.txt")

def open_about_page():
	os.startfile("About Company.html")

def open_about_dev_page():
	os.startfile("About Developer.html")
def open_new_employee_window():
	master2 = Tk()
	NewEmployeeWindow(master2)
def open_edit_employees_window():
	master3 = Tk()
	EditEmployeesWindow(master3)
#--------------------------------------------------------------------------------------------------------------------------

class MainWindow():
	def __init__(self, master):
	#Window Configuration	
		master.minsize(752,512)
		master.title("Skyland Corporation")
		master.config(bg="#FFFFFF")
	
	#File Menu
		menubar = Menu(master)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New Employee", command=open_new_employee_window)
		filemenu.add_command(label="Open Employee List", command=open_edit_employees_window)
		filemenu.add_command(label="Version", command=open_version_file)
		filemenu.add_command(label="Exit", command=master.destroy)

		menubar.add_cascade(label="File", menu=filemenu)
	
	#Help Menu
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About Company", command=open_about_page)
		helpmenu.add_command(label="About Developer", command=open_about_dev_page)
		helpmenu.add_command(label="Donate :)")

		menubar.add_cascade(label="Help", menu=helpmenu)
	
	#attaching menu
		master.config(menu=menubar)

	#The Main image
		main_image = Image.open('Company_img.bmp')
		logo = ImageTk.PhotoImage(main_image)

		panel = Label(master, image=logo)
		panel.pack(side="top", fill="both", expand="No")
	#The Button images
		image1 = Image.open('New_button.bmp')
		resize_img1 = image1.resize((20,20))
		newbuttonimage = ImageTk.PhotoImage(resize_img1)

		image2 = Image.open('Edit_button.bmp')
		resize_img2 = image2.resize((20,20))
		editbuttonimage = ImageTk.PhotoImage(resize_img2)

		image3 = Image.open('About_button.bmp')
		resize_img3 = image3.resize((20,20))
		aboutbuttonimage = ImageTk.PhotoImage(resize_img3)
	#The Buttons
		newbutton = Button(master, image=newbuttonimage, text="New Employee", height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised", command=open_new_employee_window)
		newbutton.place(x=50, y=450)

		editbutton = Button(master, image=editbuttonimage, text="Show Employees", height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised", command=open_edit_employees_window)
		editbutton.place(x=390, y=450)

		aboutbutton = Button(master, image=aboutbuttonimage, text="About Skyland Corp.", height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised", command=open_about_page)
		aboutbutton.place(x=700, y=450)

	#Running Loop of window
		master.mainloop()


#---------------------------------------second window: newemployeewindow-------------------------------------------------


class NewEmployeeWindow():
	def __init__(self, master):

		def create_the_employee():
			"""
			this function fetches the data and submits to database
			"""
			Name = Name_entry.get()
			Moblie_number = Number_entry.get()
			Address = Address_entry.get()
			Branch = Branch_var.get()
			Salary = Salary_entry.get()

			employee = (Name, Moblie_number, Address, Branch, Salary)

			conn = create_connection()
			if conn is not None:
				create_table_employees(conn)

				with conn:
					create_employee(conn, employee)

			else:
				print('failed!')

			master.destroy()

	#Wndows configuration
		master.title("Create New Employee")
		master.minsize(680, 450)
		master.config(bg='#FFFFFF')
		
	#File Menu
		menubar = Menu(master)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label = "New Employee", command=open_new_employee_window)
		filemenu.add_command(label = "Save", command=create_the_employee)
		filemenu.add_command(label = "Version", command=open_version_file)
		filemenu.add_command(label = "Exit", command = master.destroy)

		menubar.add_cascade(label = "File", menu=filemenu)
		
	#Help Menu
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About Company", command=open_about_page)
		helpmenu.add_command(label="About Developer", command=open_about_dev_page)
		helpmenu.add_command(label="Donate :)")

		menubar.add_cascade(label="Help", menu=helpmenu)
		
	#attaching menu
		master.config(menu=menubar)

	#The Fillup Form

		Name_var = StringVar()
		Name_label = Label(master, text="Name Of Employee : ", textvariable=Name_var)
		Name_label.place(x=30, y=150)
		Name_entry = Entry(master, width=50)
		Name_entry.place(x=160, y=150)

		Moblie_number_var = IntVar()
		Number_label = Label(master, text="Moblie No. : ", textvariable=Moblie_number_var)
		Number_label.place(x=30, y=175)
		Number_entry = Entry(master, width=24)
		Number_entry.place(x=160, y=175)

		Address_var = StringVar()
		Address_label = Label(master, text="Address : ", textvariable=Address_var)
		Address_label.place(x=30, y=200)
		Address_entry = Entry(master, width=80)
		Address_entry.place(x=160, y=200)

	#Dropbox
		Branch_var = StringVar(master)
		Branch_var.set("None")

		Branch_label = Label(master, text="Branch : ")
		Branch_label.place(x=30, y=235)

		Branch_dropbox = OptionMenu(master, Branch_var, "None", "Branch1", "Branch2", "Branch3")
		Branch_dropbox.place(x=100, y=231)

	#end of dropbox

		Salary_var = IntVar()
		Salary_label = Label(master, text="Salary : ", textvariable=Salary_var)
		Salary_label.place(x=30, y=275)
		Salary_entry = Entry(master, width=20)
		Salary_entry.place(x=160, y=275)
			
	#Buttons
		cancel_button = Button(master, text = "cancel", command=master.destroy, relief="flat")
		cancel_button.place(x=550, y=400)

		save_button = Button(master, text = "save", relief = "flat", command=create_the_employee)
		save_button.place(x=510, y=400)

	#End of Form

	#Running Loop of window
		master.mainloop()

#-----------------------------------------------third window: Edit employees window----------------------------------------------------------------------------

class EditEmployeesWindow():
	def __init__(self, master):
	#windows configuration
		master.minsize(1250,600)
		master.title("Edit Employees")
		master.config(bg='#FFFFFF')

	#File Menu
		menubar = Menu(master)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label = "New Employee", command=open_new_employee_window)
		filemenu.add_command(label = "Version", command=open_version_file)
		filemenu.add_command(label = "Exit", command = master.destroy)

		menubar.add_cascade(label = "File", menu=filemenu)
		
	#Help Menu
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About Company", command=open_about_page)
		helpmenu.add_command(label="About Developer", command=open_about_dev_page)
		helpmenu.add_command(label="Donate :)")

		menubar.add_cascade(label="Help", menu=helpmenu)
		
	#attaching menu
		master.config(menu=menubar)

	#Listbox: the place where the data will be shown
		
		Employee_list = Listbox(master, width=207)
		Employee_list.pack(side=LEFT)

	#scroll bar for the listbox
		
		scroll_bar = Scrollbar(master)
		scroll_bar.pack(side=RIGHT, fill=Y)

	#attaching scrollbar and listbox
		Employee_list.config(yscrollcommand=scroll_bar.set)
		scroll_bar.config(command=Employee_list.yview)

	#getting data from database and then showing it in the list box
		conn = create_connection()

		if conn is not None:
			create_table_employees(conn)

			with conn:
				rows = select_all_employees(conn)

			if rows is not None:

				for row in rows:
					#gettin data from row tuple in string form with spaces
					Data = '    '.join(map(str, row))
					print(Data)
					Employee_list.insert(END, Data)

			else:
				Employee_list.insert(END, "\n\t\tThere is no data currtently")


	#Running loop of window
		master.mainloop()

#----------------------------------------------------------------------


#running Gui
master = Tk()
MainWindow(master)
