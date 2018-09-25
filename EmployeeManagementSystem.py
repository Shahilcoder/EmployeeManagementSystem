from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os

#self.master = 0
#root2 = 0
#self.master = 0
#root3 = 0
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------OOP1-------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------
class Skyland_Corporation(object):
	"""docstring for Skyland_Corporation"""
	def __init__(self, homeGui):
		self.homeGui = homeGui
		homeGui.minsize(752,512)
		homeGui.title("Skyland Corporation")
		homeGui.config(bg = "#8BCDC7")
		self.menubar = Menu(homeGui)
		self.filemenu = Menu(self.menubar, tearoff = 0)
		self.filemenu.add_command(label = "New Employee", command = self.open_Create_new_Employ)
		self.filemenu.add_command(label = "Open Employee List", command = self.open_Show_employees)
		self.filemenu.add_command(label = "Version", command = self.open_Version)
		self.filemenu.add_command(label = "Exit", command = homeGui.destroy)
		self.menubar.add_cascade(label = "File", menu = self.filemenu)
		self.helpmenu = Menu(self.menubar, tearoff = 0)
		self.helpmenu.add_command(label = "About Company", command = self.open_About_Company)
		self.helpmenu.add_command(label = "About Developer", command = self.open_About_Developer)
		self.helpmenu.add_command(label = "Donate :)", command = self.open_Donate)
		self.menubar.add_cascade(label = "Help", menu = self.helpmenu)
		homeGui.config(menu = self.menubar)
		self.main_image = Image.open('Company_img.bmp')
		#self.Logo = main_image.resize((672,300))
		self.Logo_image = ImageTk.PhotoImage(self.main_image)
		self.panel = Label(homeGui, image = self.Logo_image)
		self.panel.pack(side = "top", fill = "both", expand = "No")
		
		self.img1 = Image.open('New_button.bmp')
		self.new_img1 = self.img1.resize((20,20))
		self.photoimg1 = ImageTk.PhotoImage(self.new_img1)
		self.b1 = Button(homeGui, image = self.photoimg1, text = " New Employee", command = self.open_Create_new_Employ, height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised")
		self.b1.place(x = 50, y = 450)
		
		self.img2 = Image.open('Edit_button.bmp')
		self.new_img2 = self.img2.resize((20,20))
		self.photoimg2 = ImageTk.PhotoImage(self.new_img2)
		self.b2 = Button(homeGui, image = self.photoimg2, text = " Show Employees", command = self.open_Show_employees, height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised")
		self.b2.place(x = 390, y = 450)

		self.img3 = Image.open('About_button.bmp')
		self.new_img3 = self.img3.resize((20,20))
		self.photoimg3 = ImageTk.PhotoImage(self.new_img3)
		self.b3 = Button(homeGui, image = self.photoimg3, text = " About Skyland Corp.", command = self.open_About_Company, height = 30, width = 180, compound = LEFT, bg = "#00F4FF", relief = "raised")
		self.b3.place(x = 700, y = 450)
		homeGui.mainloop()
	
	def open_Create_new_Employ(self):
		#----------------------------------------------------------------------------
		NOTICE2()
	
	def open_Show_employees(self):
		NOTICE3()
	
	def open_About_Developer(self):
		os.startfile("About Developer.html")
	
	def open_About_Company(self):
		os.startfile("About Company.html")
	
	def open_Donate(self):
		os.startfile("Donate.html")
	
	def open_Version(self):
		os.startfile("Version.txt")

class NOTICE(object):
	"""docstring for NOTICE"""
	def __init__(self, master):
		self.master = master
		master.title("NOTICE")
		self.message = Message(master, text = "\n"
			"\t\tNotice: \n\n"
			"The following program is made for the Science Exhibition,\n\n"
			"Topic - Technological Solutions\n"
			"\nThe following program just imitates and gives a little bit idea about\n"
			"how through Technological avdancement (here Software Technological Avdancement)\n"
			"had made it really easy task to manage information about Employees in a company\n"
			"This program is just a demo and does not do the real task\n"
			"it just demonstrate an idea about the real Software\n"
			"You can try features like opening new file from menu,\n"
			"opening varoius submenus in the helpmenu too.\n\n"
			"\nMADE BY : SHAHIL HUSSAIN\n"
			"Created at  -  Jan 2018\n"
			"Version - 0.0.3",
			fg = "#FFFFFF", bg = "#000000", bd = 20, relief = "flat",
			font = ("Consolas", 17)).pack()
		self.close_button = Button(self.master, text = "OK", command = self.message_killer, width = 20, bg = "#FF8500").pack()
		self.master.mainloop()
	def message_killer(self):
		self.master.destroy()
#------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------OOP2---------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
class NOTICE2(object):
    """docstring for NOTICE2"""
    def __init__(self):
        self.master = Tk()
        self.message = Message(self.master, text = "\n"
            "\tNotice: \n\n"
            "In this program data of Employees\n"
            "is filled\n"
            "Current Version of this Software won't store data\n"
            "in reality\n"
            "it demonstrates how it works only",
            fg = "#FFFFFF", bg = "#000000", bd = 20, relief = "flat",
            font = ("Conslas", 13)).pack()
        self.close_button = Button(self.master, text = "OK", command = self.message_killer, width = 20, bg = "#FF8500").pack()
        self.master.mainloop()
    def message_killer(self):
        self.master.destroy()
        Create_new_Employ()

class Create_new_Employ(object):
    """docstring for Create_new_Employ"""
    def __init__(self):
        self.master = Tk()
        self.master.title("Create New Employ")
        self.master.minsize(600,612)#(1350,692)
        self.master.config(bg = "#98FFFF")
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff = 0)
        self.filemenu.add_command(label = "New Employee", command = self.open_Create_new_Employ)
        self.filemenu.add_command(label = "Save", command = self.saver)
        self.filemenu.add_command(label = "Version", command = self.open_Version)
        self.filemenu.add_command(label = "Exit", command = self.master.destroy)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff = 0)
        self.helpmenu.add_command(label = "About Company", command = self.open_About_Company)
        self.helpmenu.add_command(label = "About Developer", command = self.open_About_Developer)
        self.helpmenu.add_command(label = "Donate :)", command = self.open_Donate)
        self.menubar.add_cascade(label = "Help", menu = self.helpmenu)

        self.master.config(menu = self.menubar)
        
        self.Data_required = ['Employee\'s Name : ', 'Phone No. : ', 'Residence : ', 'Adhar Card No. : ']
        self.entry1 = self.entry2 = self.entry3 = self.entry4 = self.entry5 = 0
        self.entry = [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5]
        self.coordx = 50
        self.coordy = 150
        self.count = 0

        self.label1 = Label(self.master, text = "Employee Details : ", font = ('Copperplate Gothic Bold', 26, 'bold'), foreground = "#73FF0F", background = "#FFFF00").place(x = 50,y = 40)

        for i in self.Data_required:
            Label(self.master, text = i, background = "#FF7F00").place(x = self.coordx, y = self.coordy)
            self.entry[self.count] = Entry(self.master, width = 60, relief = "flat")
            self.entry[self.count].place(x = self.coordx + 130, y = self.coordy)
            self.coordy += 25
            self.count += 1

        self.label2 = Label(self.master, text = "Salary", font = ('Copperplate Gothic Bold', 26, 'bold'), foreground = "#73FF0F", background = "#FFFF00").place(x = 50,y = 300)

        self.work = StringVar(self.master)
        self.work.set("None")# ---------- initial value

        self.label3 = Label(self.master, text = "Job : ", background = "#FF7F00").place(x = 50, y = 390)

        self.work_option = OptionMenu(self.master, self.work, "None", "Backened Developer", "Frontend Developer", "Fullstack Developer", "Unit-Tester", "Customer-Care", "Infrastructure maintainer")
        self.work_option.config(bg = "#6467FF", relief = "flat") # ---------------- set bg color to green
#------------------below will colour every thing--------------------------
        self.work_option["menu"].config(bg = "#6467FF", relief = "flat")
        self.work_option.place(x = 100, y = 386)

        self.en1 = self.en2 = self.en3 =  0
        self.en = [self.en1, self.en2, self.en3]
        self.salary = ['Monthly salary(Rs.) : ', 'Annual salary(Rs.) : ', 'Advance(Rs.) : ']
        self.coordy = 430
        self.count = 0

        for i in self.salary:
            Label(self.master, text = i, background = "#FF7F00").place(x = self.coordx, y = self.coordy)
            self.en[self.count] = Entry(self.master, width = 40, relief = "flat")
            self.en[self.count].place(x = self.coordx + 130, y = self.coordy)
            self.coordy += 25
            self.count += 1

        self.label4 = Label(self.master, text = "Time Period", background = "#FF7F00").place(x = 50, y = 530)
        self.hour = StringVar(self.master)
        self.hour.set("2 hours")

        self.hour_option = OptionMenu(self.master, self.hour, "2 hours", "4 hours", "6 hours")
        self.hour_option.config(bg = "#6467FF", relief = "flat")
        self.hour_option["menu"].config(bg = "#6467FF", relief = "flat")
        self.hour_option.place(x = 140, y = 526)

        self.label5 = Label(self.master, text = "overtime", background = "#FF7F00").place(x = 50, y = 575)
        self.var = IntVar(self.master)

        self.radio1 = Radiobutton(self.master, text = "Yes", background = "#FF9BFF", relief = "flat", variable = self.var, value = 1, command = self.donothing).place(x = 120, y = 572)
        self.radio2 = Radiobutton(self.master, text = "No", background = "#FF9BFF", relief = "flat", variable = self.var, value = 2, command = self.donothing).place(x = 170, y = 572)

        self.b1 = Button(self.master, text = "cancel", command = self.master.destroy, bg = "#8138FF", relief = "flat").place(x = 550, y = 560)
        self.b2 = Button(self.master, text = "Save", command = self.saver, bg = "#8138FF", relief = "flat").place(x = 510, y = 560)

        self.master.mainloop()     

    def saver(self):
        self.master.filename = filedialog.asksaveasfilename(initialdir = "C:/", title = "Save the data", filetypes = (("all files","*.*"),("dat file","*.dat")))
        self.master.destroy()

    def donothing(self):
        juju = 0

    def open_Create_new_Employ(self):
    	Create_new_Employ()

    def open_About_Developer(self):
        os.startfile("About Developer.html")

    def open_About_Company(self):
        os.startfile("About Company.html")

    def open_Donate(self):
        os.startfile("Donate.html")

    def open_Version(self):
        os.startfile("Version.txt")
#------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------OOP3----------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
class NOTICE3(object):
	"""docstring for NOTICE3"""
	def __init__(self):
		self.master = Tk()
		Message(self.master, text = "\n"
			"\tNotice: \n\n"
			"In this program data of Employees\n"
			"is stored\n"
			"Currently Version of this Software won't show the data stored in reality\n"
			"It's just a demonstration",
			fg = "#FFFFFF", bg = "#000000", bd = 20, relief = "flat",
			font = ("Conslas", 13)).pack()
		Button(self.master, text = "OK", command = self.message_killer, width = 20, bg = "#FF8500").pack()
		self.master.mainloop()

	def message_killer(self):
		self.master.destroy()
		Show_employees()
class Show_employees(object):
	"""docstring for Show_employees"""
	def __init__(self):
		self.master = Tk()
		self.master.minsize(550,500)
		self.master.title("Employee List")

		self.label = Label(self.master, text = "Sr.No.                            Employee Name                               phone                            salary (Rs.)").pack(anchor = "nw")
		
		self.Employ_list = Listbox(self.master, height = 30, width = 550, bg = "#000000", fg = "#00FF00")
		
		for i in range(1,100):
			self.Employ_list.insert(END, str(i) + " Currently blank")
		
		self.Employ_list.place(x = 0, y = 20)

		self.scroll_bar = Scrollbar(self.master)
		self.scroll_bar.pack(side = RIGHT, fill = Y)
#---------------------------------------Attaching both
		self.Employ_list.config(yscrollcommand = self.scroll_bar.set)
		self.scroll_bar.config(command = self.Employ_list.yview)

		self.master.mainloop()
#---------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------stuffs----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
msgGui = Tk()
NOTICE(msgGui)
root1 = Tk()
Skyland_Corporation(root1)
