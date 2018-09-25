from tkinter import *
from PIL import ImageTk, Image
import os

class MainWindow():
	def __init__(self, master):
	#Window Configuration	
		master.minsize(752,512)
		master.title("Skyland Corporation")
		master.config(bg="#FFFFFF")
	
	#File Menu
		menubar = Menu(master)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="New Employee")
		filemenu.add_command(label="Open Employee List")
		filemenu.add_command(label="Version")
		filemenu.add_command(label="Exit", command=master.destroy)

		menubar.add_cascade(label="File", menu=filemenu)
	
	#Help Menu
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About Company")
		helpmenu.add_command(label="About Developer")
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
		newbutton = Button(master, image=newbuttonimage, text="New Employee", height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised")
		newbutton.place(x=50, y=450)

		editbutton = Button(master, image=editbuttonimage, text="Show Employees", height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised")
		editbutton.place(x=390, y=450)

		aboutbutton = Button(master, image=aboutbuttonimage, text="About Skyland Corp.", height = 30, width = 130, compound = LEFT, bg = "#00F4FF", relief = "raised")
		aboutbutton.place(x=700, y=450)

	#Running Loop of window
		master.mainloop()
#---------------------------------------second window: newemployeewindow-------------------------------------------------
class NewEmployeeWindow():
	def __init__(self, master):
	#Wndows configuration
		master.title("Create New Employee")
		master.minsize(600, 612)
		master.config(bg='#FFFFFF')
		
	#File Menu
		menubar = Menu(master)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label = "New Employee")
		filemenu.add_command(label = "Save")
		filemenu.add_command(label = "Version")
		filemenu.add_command(label = "Exit", command = master.destroy)

		menubar.add_cascade(label = "File", menu=filemenu)
		
	#Help Menu
		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About Company")
		helpmenu.add_command(label="About Developer")
		helpmenu.add_command(label="Donate :)")

		menubar.add_cascade(label="Help", menu=helpmenu)
		
	#attaching menu
		master.config(menu=menubar)

	#The Fillup Form



	#Running Loop of window
		master.mainloop()
#----------------------------------------------------------------------


#running Gui
master = Tk()
MainWindow(master)
master2 = Tk()
NewEmployeeWindow(master2)
