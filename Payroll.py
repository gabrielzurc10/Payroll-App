from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from sqlite3 import Error
import datetime
import sqlite3

class DataBase:
	def __init__(self):
		self.employee_id = ''
		self.first_name = ''
		self.middle_name = ''
		self.last_name = ''
		self.marital_status = ''
		self.email = ''
		self.phonenumber = ''
		self.hourly_rate = ''
		self.position = ''
		self.employeelist = []

	def createConnection(self):
		try:
			self.connection = sqlite3.connect("PayrollDb.db")
			return self.connection

		except Error as e:
			mb.showerror("Error", e)
		
	def getEmployee(self, connection, employee_id):
		self.cursor = connection.cursor()
		self.cursor.execute("SELECT * FROM Employee WHERE Employeeid =\'"+employee_id+"\';")
		return self.cursor.fetchone()

	def AddEmployee(self, connection, first_name, middle_name, last_name, marital_status, email, phonenumber, hourly_rate, position, overtime, sickpay, vacation, holiday):
		self.cursor = connection.cursor()
		self.cursor.execute("INSERT INTO Employee (Firstname, Middlename, Lastname, Maritalstatus, Email, Phonenumber, Hourlyrate, Position, Overtime, SickPay, Vacation, Holiday) VALUES (\'"+first_name+"\', \'"+middle_name+"\', \'"+last_name+"\', \'"+marital_status+"\', \'"+email+"\', \'"+phonenumber+"\', \'"+hourly_rate+"\', \'"+position+"\', \'"+overtime+"\', \'"+sickpay+"\', \'"+vacation+"\', \'"+holiday+"\');")
		connection.commit()

d = DataBase()
connection = d.createConnection()

class Login:
	def __init__(self):
		self.window = Tk()
		self.window.title("Payroll - Login")			
		self.window.geometry("500x500+500+100")
		self.window.configure(bg = "white")
		self.frame = Frame(self.window, bg = "white")
		self.frame.pack()

		self.usernameInput = StringVar()
		self.passwordInput = StringVar()

		self.usernameLabel = Label(self.frame, text = "USERNAME", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.usernameTextBox = Entry(self.frame, textvariable = self.usernameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.passwordLabel = Label(self.frame, text = "PASSWORD", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.passwordTextBox = Entry(self.frame, textvariable = self.passwordInput, width = 30, show = "●", font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.loginButton = Button(self.frame, width = 30, text = "LOGIN", relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.loginButtonClickEvent) 
		self.createAccountButton = Button(self.frame, width = 20, text = "CREATE A NEW ACCOUNT", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.createAccountButtonClickEvent)

		self.usernameLabel.grid(row = 0, column = 0, pady = (150, 0))
		self.usernameTextBox.grid(row = 1, column = 0, pady = (10, 0))
		self.passwordLabel.grid(row = 2, column = 0, pady = (10, 0))
		self.passwordTextBox.grid(row = 3, column = 0, pady = (10, 0))
		self.loginButton.grid(row = 4, column = 0, pady = (30, 0))
		self.createAccountButton.grid(row = 5, column = 0, pady = (130, 0))

		self.window.mainloop()

	def loginButtonClickEvent(self):
		try:
			self.cursor = connection.cursor()
			self.cursor.execute("SELECT * FROM Account WHERE Username = \'"+self.usernameTextBox.get()+"\' AND Password = \'"+self.passwordTextBox.get()+"\';")
			results = self.cursor.fetchall()
			if(str(results) == "[]"):
				mb.showerror("Invalid", "Credentials are invalid.")
			else:
				for row in results:
					if(self.usernameTextBox.get() == row[3] and self.passwordTextBox.get() == row [4]):
						self.window.destroy()
						MainMenuAdmin()				
		except:
			mb.showerror("Invalid", "Credentials are invalid.")

	def createAccountButtonClickEvent(self):
		self.window.destroy()
		CreateAccount()

class CreateAccount:
	def __init__(self):
		self.window = Tk()
		self.window.title("Payroll - Create Account")
		self.window.geometry("650x500+430+80")
		self.window.configure(bg = "white")
		self.frame = Frame(self.window, bg = "white")
		self.frame.pack(padx = (0,85))

		self.firstNameInput = StringVar()
		self.middleNameInput = StringVar()
		self.lastNameInput = StringVar()
		self.usernameInput = StringVar()
		self.phoneNumberInput = StringVar()
		self.passwordInput = StringVar()
		self.positionInput = StringVar()
		self.hourlyRateInput = StringVar()

		self.firstNameLabel = Label(self.frame, text = "First Name:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.firstNameTextBox = Entry(self.frame, textvariable = self.firstNameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.middleNameLabel = Label(self.frame, text = "Middle Name:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.middleNameTextBox = Entry(self.frame, textvariable = self.middleNameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.lastNameLabel = Label(self.frame, text = "Last Name:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.lastNameTextBox = Entry(self.frame, textvariable = self.lastNameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.usernameLabel = Label(self.frame, text = "Username:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.usernameTextBox = Entry(self.frame, textvariable = self.usernameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.passwordLabel = Label(self.frame, text = "Password:", font = ("calibri", 11), bg = "white", fg = "#383838", justify = RIGHT)
		self.passwordTextBox = Entry(self.frame, textvariable = self.passwordInput, width = 30, show = "●", font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.createButton = Button(self.frame, width = 30, text = "CREATE ACCOUNT", relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.createButtonClickEvent) 
		self.backButton = Button(self.frame, width = 10, text = "BACK", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.backButtonClickEvent)

		self.firstNameLabel.grid(row = 1, column = 1, pady = (110, 0), sticky = E)
		self.firstNameTextBox.grid(row = 1, column = 2, pady = (110, 0))
		self.middleNameLabel.grid(row = 2, column = 1, pady = (10, 0), sticky = E)
		self.middleNameTextBox.grid(row = 2, column = 2, pady = (10, 0))
		self.lastNameLabel.grid(row = 3, column = 1, pady = (10, 0), sticky = E)
		self.lastNameTextBox.grid(row = 3, column = 2, pady = (10, 0))
		self.usernameLabel.grid(row = 4, column = 1, pady = (10, 0), sticky = E)
		self.usernameTextBox.grid(row = 4, column = 2, pady = (10, 0))
		self.passwordLabel.grid(row = 5, column = 1, pady = (10, 0), sticky = E)
		self.passwordTextBox.grid(row = 5, column = 2, pady = (10, 0))
		self.createButton.grid(row = 6, column = 2, pady = (30, 0), sticky = E)
		self.backButton.grid(row = 7, column = 2, pady = (135, 0))

	def createButtonClickEvent(self):
		n = 0 
		m = 0
		if(self.firstNameTextBox.get() == "" or self.middleNameTextBox.get() == "" or self.lastNameTextBox.get() == "" or self.usernameTextBox.get() == "" or self.passwordTextBox.get() == ""):
			mb.showerror("Invalid", "Please fill out all the forms.")
		else:
			n = 1
		if(n == 1):
			try:
				self.cursor = connection.cursor()
				self.cursor.execute("SELECT Username FROM Account WHERE Username =\'"+self.usernameTextBox.get()+"\';")
				row = str(self.cursor.fetchall())
				if (str(row) == "[]"):
					m += 1
				else:
					mb.showerror("Invalid","Username already exists.")
			except:
				mb.showerror("Please enter the correct values")
		if(n == 1):
			try:
				self.cursor = connection.cursor()
				self.cursor.execute("SELECT Password FROM Account WHERE Password =\'"+self.passwordTextBox.get()+"\';")
				row = str(self.cursor.fetchall())
				if (str(row) == "[]"):
					m += 1
				else:
					mb.showerror("Invalid","Password already exists.")
			except:
				mb.showerror("Please enter the correct values")
		if(m == 2):
			self.cursor = connection.cursor()
			self.cursor.execute("INSERT INTO Account (Firstname, Middlename, Lastname, Username, Password) VALUES (\'"+self.firstNameTextBox.get()+"\', \'"+self.middleNameTextBox.get()+"\', \'"+self.lastNameTextBox.get()+"\', \'"+self.usernameTextBox.get()+"\', \'"+self.passwordTextBox.get()+"\');")
			connection.commit()
			mb.showinfo("Success", "Account successfully created.")
			self.window.destroy()
			Login()

	def backButtonClickEvent(self):
		self.window.destroy()
		Login()

class MainMenuAdmin():
	def __init__(self):
		self.window = Tk()
		self.window.title("Payroll - Main Menu")
		self.window.geometry("500x570+500+100")
		self.window.configure(bg = "white")
		self.frame = Frame(self.window, bg = "white")
		self.frame.pack()

		self.payrollButton = Button(self.frame, width = 30, text = "PAYROLL", relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.payrollButtonClickEvent)
		self.savedButton = Button(self.frame, width = 30, text = "SAVED PAYROLL", relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.savedButtonClickEvent)
		self.employeesButton = Button(self.frame, width = 30, text = "EMPLOYEES", relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.employeesButtonClickEvent)
		self.logoutButton = Button(self.frame, width = 10, text = "LOGOUT", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.backButtonClickEvent)

		self.payrollButton.grid(row = 1, column = 1, pady = (200, 0))
		self.savedButton.grid(row = 2, column = 1, pady = (20, 0))
		self.employeesButton.grid(row = 3, column = 1, pady = (20, 0))
		self.logoutButton.grid(row = 4, column = 1, pady = (200, 0))

	def payrollButtonClickEvent(self):
		self.window.destroy()
		Payroll()

	def savedButtonClickEvent(self):
		self.window.destroy()
		Saves()

	def employeesButtonClickEvent(self):
		self.window.destroy()
		Employees()

	def backButtonClickEvent(self):
		self.window.destroy()
		Login()

class Payroll:
	def __init__(self):
		self.window = Tk()
		self.window.title("Payroll - Management")
		self.window.geometry("1000x700+250+70")
		self.window.configure(bg = "white")
		## main frame
		self.mainFrame = Frame(self.window, bg = "white")		
		self.mainFrame.pack()
		## frames
		self.employeeFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1, height = 103, width = 541)
		self.payDatesFrame = Frame(self.mainFrame, bg  = "white", highlightbackground = "#e0e0e0", highlightthickness = 1)
		self.earningsFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1, height = 218, width = 541)
		self.taxesFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1)
		self.totalFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1)
		self.buttonFrame = Frame(self.mainFrame, bg = "white")

		self.loadID(connection)

		## employee frame 
		self.employeeNumberInput = StringVar()
		self.employeeNumberLabel = Label(self.employeeFrame, text = "Employee ID:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.employeeNameLabel = Label(self.employeeFrame, text = "Name:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.positionLabel = Label(self.employeeFrame, text = "Job Title:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.hourlyRateLabel = Label(self.employeeFrame, text = "Pay Rate:", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.employeeNumberCb = ttk.Combobox(self.employeeFrame, font = ("calibri", 11), textvariable = self.employeeNumberInput)
		self.employeeNumberCb['values'] = (self.idlist)
		self.employeeNumberCb.set('Select')
		self.goButton = Button(self.employeeFrame, text = "GO", relief = FLAT, font = ("calibri", 10, "bold"), bg = "#a260f7", fg = "white", command = self.loadEmployee)
		self.employeeNameValue = Label(self.employeeFrame, text = self.name, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.positionValue = Label(self.employeeFrame, text = self.position, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.hourlyRateValue = Label(self.employeeFrame, text = self.hourlyrate, font = ("calibri", 12), bg = "white", fg = "#383838")
		# employee frame grids
		self.employeeFrame.grid(row =1, column = 1, pady = (130,0), sticky = W)
		self.employeeFrame.grid_propagate(False)
		self.employeeNumberLabel.grid(row = 1, column = 1, sticky = W)
		self.employeeNumberCb.grid(row = 1, column = 2, padx = (43,0), sticky = W)
		self.goButton.grid(row =1, column = 2, padx = (210,0), sticky = W)
		self.employeeNameLabel.grid(row = 2, column = 1, sticky = W)
		self.employeeNameValue.grid(row = 2, column = 2, padx = (40,278), sticky = W)
		self.positionLabel.grid(row = 3, column = 1, sticky = W)
		self.positionValue.grid(row = 3, column = 2, padx = (40,278), sticky = W)
		self.hourlyRateLabel.grid(row = 4, column = 1, sticky = W)
		self.hourlyRateValue.grid(row = 4, column = 2, padx = (40,278), sticky = W)

		## pay date frame 
		self.payIDLabel = Label(self.payDatesFrame, text = "Pay ID:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.startDateLabel = Label(self.payDatesFrame, text = "Start Date:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.endDateLabel = Label(self.payDatesFrame, text = "End Date:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.issueDateLabel = Label(self.payDatesFrame, text = "Issue Date:", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.startDateInput = StringVar()
		self.endDateInput = StringVar()
		self.issueDateInput = StringVar()

		self.payIDValue = Label(self.payDatesFrame, text = "", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.startDateValue = Entry(self.payDatesFrame, textvariable = self.startDateInput, width = 10, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.endDateValue =  Entry(self.payDatesFrame, textvariable = self.endDateInput, width = 10, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.issueDateValue = Entry(self.payDatesFrame, textvariable = self.issueDateInput, width = 10, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		# pay date frame grids
		self.payDatesFrame.grid(row =1, column = 2, pady = (130,0), sticky = E)
		self.payIDLabel.grid(row = 1, column = 1, sticky = W)
		self.payIDValue.grid(row = 1, column = 2, padx = (100,0), sticky = W)
		self.startDateLabel.grid(row = 2, column = 1, sticky = W)
		self.startDateValue.grid(row = 2, column = 2, padx = (100,0), sticky = W)
		self.endDateLabel.grid(row = 3, column = 1, sticky = W)
		self.endDateValue.grid(row = 3, column = 2, padx = (100,0), sticky = W)
		self.issueDateLabel.grid(row = 4, column = 1, sticky = W)
		self.issueDateValue.grid(row = 4, column = 2, padx = (100,0), sticky = W)

		## earnings frame 
		self.typeHeaderLabel = Label(self.earningsFrame, text = "Type", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.straighttimeLabel = Label(self.earningsFrame, text = "Straight Time:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.overtimeLabel = Label(self.earningsFrame, text = "Overtime:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.sickpayLabel = Label(self.earningsFrame, text = "Sick Pay:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.vacaytionpayLabel = Label(self.earningsFrame, text = "Vacation Pay:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.holidayPayLabel = Label(self.earningsFrame, text= "Holiday Pay:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalLabel = Label(self.earningsFrame, text = "Total:", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.straighttimeInput = StringVar()
		self.overtimeInput = StringVar()
		self.sickpayInput = StringVar()
		self.vacaytionpayInput = StringVar()
		self.holidayPayInput = StringVar()

		self.hoursHeaderLabel = Label(self.earningsFrame, text = "Hours", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.straighttimeValue = Entry(self.earningsFrame, textvariable = self.straighttimeInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.overtimeValue = Entry(self.earningsFrame, textvariable = self.overtimeInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.sickpayValue = Entry(self.earningsFrame, textvariable = self.sickpayInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.vacaytionpayValue = Entry(self.earningsFrame, textvariable = self.vacaytionpayInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.holidayPayValue = Entry(self.earningsFrame, textvariable = self.holidayPayInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.totalTime = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.straighttimeValue.insert(0, "0.00")
		self.overtimeValue.insert(0, "0.00")
		self.sickpayValue.insert(0, "0.00")
		self.vacaytionpayValue.insert(0, "0.00")
		self.holidayPayValue.insert(0, "0.00")

		self.overtimeRateInput = StringVar()
		self.sickpayRateInput = StringVar()
		self.vacaytionRatepayInput = StringVar()
		self.holidayRateInput = StringVar()

		self.rateHeaderLabel = Label(self.earningsFrame, text = "Rates", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.rateValue = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.overtimeRate = Entry(self.earningsFrame, textvariable = self.overtimeRateInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.sickpayRate = Entry(self.earningsFrame, textvariable = self.sickpayRateInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.vacaytionpayRate = Entry(self.earningsFrame, textvariable = self.vacaytionRatepayInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.holidayRate = Entry(self.earningsFrame, textvariable = self.holidayRateInput, width = 8, font = ("calibri", 12), bg = "#ededed", relief = FLAT, justify = RIGHT)
		self.totalRate = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.overtimeRate.insert(END, "0.00")
		self.sickpayRate.insert(END, "0.00")
		self.vacaytionpayRate.insert(END, "0.00")
		self.holidayRate.insert(END, "0.00")

		self.earningsHeaderLabel = Label(self.earningsFrame, text = "Earnings", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.rateEarning = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.overtimeEarning = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.sickpayEarning = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.vacaytionpayEarning = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.holidayPayEarning = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.totalEarning = Label(self.earningsFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		# earnings frame grids
		self.earningsFrame.grid(row = 2, column = 1, pady = (10,0), sticky = W)
		self.typeHeaderLabel.grid(row = 1, column = 1, sticky = W)
		self.straighttimeLabel.grid(row = 2, column = 1, pady = (20,0), sticky = W)
		self.overtimeLabel.grid(row = 3, column = 1, sticky = W)
		self.sickpayLabel.grid(row = 4, column = 1, sticky = W)
		self.vacaytionpayLabel.grid(row = 5, column = 1, sticky = W)
		self.holidayPayLabel.grid(row = 6, column = 1, sticky = W)
		self.totalLabel.grid(row = 7, column = 1, pady = (20,0), sticky = W)

		self.hoursHeaderLabel.grid(row = 1, column = 2, padx = (80,30), sticky = E)
		self.straighttimeValue.grid(row = 2, column = 2, pady = (20,0), padx = (80,30), sticky = E)
		self.overtimeValue.grid(row = 3, column = 2, padx = (80,30), sticky = E)
		self.sickpayValue.grid(row = 4, column = 2, padx = (80,30), sticky = E)
		self.vacaytionpayValue.grid(row = 5, column = 2, padx = (80,30), sticky = E)
		self.holidayPayValue.grid(row = 6, column = 2, padx = (80,30), sticky = E)
		self.totalTime.grid(row = 7, column = 2, pady = (20,0), padx = (80,30), sticky = E)

		self.rateHeaderLabel.grid(row = 1, column = 3, padx = (60,100), sticky = E)
		self.rateValue.grid(row = 2, column = 3, pady = (20,0), padx = (30,80), sticky = E)
		self.overtimeRate.grid(row = 3, column = 3, padx = (30,80), sticky = E)
		self.sickpayRate.grid(row = 4, column = 3, padx = (30,80), sticky = E)
		self.vacaytionpayRate.grid(row = 5, column = 3, padx = (30,80), sticky = E)
		self.holidayRate.grid(row = 6, column = 3, padx = (30,80), sticky = E)
		self.totalRate.grid(row = 7, column = 3, pady = (20,0), padx = (30,80), sticky = E)

		self.earningsHeaderLabel.grid(row = 1, column = 4, sticky = E)
		self.rateEarning.grid(row = 2, column = 4, pady = (20,0), sticky = E)
		self.overtimeEarning.grid(row = 3, column = 4, sticky = E)
		self.sickpayEarning.grid(row = 4, column = 4, sticky = E)
		self.vacaytionpayEarning.grid(row = 5, column = 4, sticky = E)
		self.holidayPayEarning.grid(row = 6, column = 4, sticky = E)
		self.totalEarning.grid(row = 7, column = 4, pady = (20,0), sticky = E)

		## taxes frame 
		self.taxesHeadingLabel = Label(self.taxesFrame, text = "TAXES", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.descriptionLabel = Label(self.taxesFrame, text = "Description", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedWitholdingLabel = Label(self.taxesFrame, text = "Fed Withholding", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedMedLabel = Label(self.taxesFrame, text = "Fed Med/EE", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedOASDIEELabel = Label(self.taxesFrame, text = "Fed OASDI/EE", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.amountLabel = Label(self.taxesFrame, text = "Amount", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedWitholdingAmount = Label(self.taxesFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedMedAmount = Label(self.taxesFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedOASDIEEAmount = Label(self.taxesFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.taxesTotalLabel = Label(self.taxesFrame, text = "Total:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalAmount = Label(self.taxesFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		# taxes frame grids
		self.taxesFrame.grid(row = 2, column = 2, pady = (10,0), padx = (10,0), sticky = N)
		self.taxesHeadingLabel.grid(row = 1, column = 2, sticky = W)
		self.descriptionLabel.grid(row = 2, column = 1, pady = (20,0), sticky = W)
		self.fedWitholdingLabel.grid(row = 3, column = 1, pady = (10,0), sticky = W)
		self.fedMedLabel.grid(row = 4, column = 1, sticky = W)
		self.fedOASDIEELabel.grid(row = 5, column = 1, sticky = W)

		self.amountLabel.grid(row = 2, column = 3, pady = (20,0), padx = (50,0), sticky = E)
		self.fedWitholdingAmount.grid(row = 3, column = 3, pady = (10,0), sticky = E)
		self.fedMedAmount.grid(row = 4, column = 3, sticky = E)
		self.fedOASDIEEAmount.grid(row = 5, column = 3, sticky = E)

		self.taxesTotalLabel.grid(row = 6, column = 1, pady = (35,0), sticky = W)
		self.totalAmount.grid(row = 6, column = 3, pady = (35,0), sticky = E)

		## total frame
		self.totalGrossLabel = Label(self.totalFrame, text = "TOTAL GROSS", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalGrossAmount = Label(self.totalFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalTaxesLabel = Label(self.totalFrame, text = "TOTAL TAXES", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalTaxesAmount = Label(self.totalFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.netPayLabel = Label(self.totalFrame, text = "NET PAY", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.netPayAmount = Label(self.totalFrame, text = "0.00", font = ("calibri", 12), bg = "white", fg = "#383838")
		#total frame grids
		self.totalFrame.grid(row = 3, column = 1, pady = (10,0),sticky = W)
		self.totalGrossLabel.grid(row = 1, column = 1, sticky = W)
		self.totalGrossAmount.grid(row = 2, column = 1, pady = (20,0), sticky = W)
		self.totalTaxesLabel.grid(row = 1, column = 2, padx = (144,0), sticky = E)
		self.totalTaxesAmount.grid(row = 2, column = 2, pady = (20,0), sticky = E)
		self.netPayLabel.grid(row = 1, column = 3, padx = (144,0), sticky = E)
		self.netPayAmount.grid(row = 2, column = 3, pady = (20,0), sticky = E)

		## buttons frame
		self.calculateButton = Button(self.buttonFrame, text = "CALCULATE", width = 32, relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.calculateButtonClickEvent)
		self.saveButton = Button(self.buttonFrame, text = "SAVE", width = 15, relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.saveButtonClickEvent)
		self.clearButton = Button(self.buttonFrame, text = "CLEAR", width = 15, relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.clearButtonClickEvent)
		# buttons frame grid
		self.buttonFrame.grid(row = 3, column = 2, pady = (10,0), sticky = E)
		self.calculateButton.grid(row = 1, column = 1, columnspan = 2, sticky = N)
		self.saveButton.grid(row = 2, column = 1, pady = (5,0), sticky = SW)
		self.clearButton.grid(row = 2, column = 2, pady = (5,0), sticky = SE)

		##back button
		self.backButton = Button(self.mainFrame, width = 10, text = "BACK", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.backButtonClickEvent)
		self.backButton.grid(row = 4, column = 1, columnspan = 2, pady = 125)

	def loadID(self, connection):
		self.idlist = []
		self.name = ""
		self.maritalstatus = ""
		self.email = ""
		self.phonenumber = ""
		self.hourlyrate = ""
		self.position = ""
		self.overtime = ""
		self.sickpay = ""
		self.vacaytionpay = ""
		self.holidaypay = ""
		self.cursor = connection.cursor()
		self.cursor.execute("SELECT EmployeeID FROM Employee;")
		results = self.cursor.fetchall()
		for row in results:
			self.idlist.append(str(row[0]))

	def loadEmployee(self, connection = connection):
		try:	
			self.cursor = connection.cursor()
			self.cursor.execute("SELECT * FROM Employee WHERE EmployeeID = "+self.employeeNumberCb.get()+";")
			results = self.cursor.fetchall()
			for row in results:
				self.name  = row[1]+" "+row[2]+" "+row[3]
				self.maritalstatus = row[4]
				self.hourlyrate = row[7]
				self.position = row[8]
				self.overtime = row[9]
				self.sickpay = row[10]
				self.vacaytionpay = row[11]
				self.holidaypay = row[12]
			self.employeeNameValue["text"] = self.name
			self.positionValue["text"] = self.position
			self.hourlyRateValue["text"] = self.hourlyrate
			self.rateValue["text"] = self.hourlyrate

			self.overtimeRate.delete(0, END)
			self.sickpayRate.delete(0, END) 
			self.vacaytionpayRate.delete(0, END)
			self.holidayRate.delete(0, END)

			self.overtimeRate.insert(0, self.overtime)
			self.sickpayRate.insert(0, self.sickpay) 
			self.vacaytionpayRate.insert(0, self.vacaytionpay)
			self.holidayRate.insert(0, self.holidaypay)
		except:
			mb.showerror("Error", "Please choose an ID number.")

	def calculateButtonClickEvent(self):
		try:
			self.straighttimetotal = round((float(self.straighttimeValue.get()) * float(self.rateValue.cget("text"))), 2)
			self.overtimetotal = round((float(self.overtimeValue.get()) * float(self.overtimeRate.get())), 2)
			self.sickpaytotal = round((float(self.sickpayValue.get()) * float(self.sickpayRate.get())), 2)
			self.vacaytionpaytotal = round((float(self.vacaytionpayValue.get()) * float(self.vacaytionpayRate.get())) ,2)
			self.holidaypaytotal = round((float(self.holidayPayValue.get()) * float(self.holidayRate.get())), 2)

			self.rateEarning["text"] = str(self.straighttimetotal)
			self.overtimeEarning["text"] = str(self.overtimetotal)		
			self.sickpayEarning["text"] = str(self.sickpaytotal)
			self.vacaytionpayEarning["text"] = str(self.vacaytionpaytotal)
			self.holidayPayEarning["text"] = str(self.holidaypaytotal)

			self.totalhours = round((float(self.straighttimeInput.get()) + float(self.overtimeValue.get()) + float(self.sickpayValue.get()) + float(self.vacaytionpayValue.get()) + float(self.holidayPayValue.get())), 2)
			self.totalrate = round((float(self.rateValue.cget("text")) + float(self.overtimeRate.get()) + float(self.sickpayRate.get()) + float(self.vacaytionpayRate.get()) + float(self.holidayRate.get())), 2)
			
			self.totalTime["text"] = str(self.totalhours)
			self.totalRate["text"] = str(self.totalrate)

			self.totalearning = round((self.straighttimetotal + self.overtimetotal + self.sickpaytotal + self.vacaytionpaytotal + self.holidaypaytotal), 2)

			self.totalEarning["text"] = str(self.totalearning)

			self.withholdingtotal = 0.00

			if (self.maritalstatus == "Single"):
				self.withholdingtotal = self.singleWithholdingTax(self.totalearning)
			elif (self.maritalstatus == "Married"):
				self.withholdingtotal = self.marriedWithholdingTax(self.totalearning)

			self.medicaretotal = self.medicare(self.totalearning)
			self.ssstotal = self.socialsecurity(self.totalearning)

			self.fedWitholdingAmount["text"] = str(round(self.withholdingtotal, 2))
			self.fedMedAmount["text"] = str(round(self.medicaretotal, 2))
			self.fedOASDIEEAmount["text"] = str(round(self.ssstotal, 2))

			self.taxtotal = str(round((self.withholdingtotal + self.medicaretotal + self.ssstotal), 2))

			self.totalAmount["text"] = self.taxtotal

			self.totalGrossAmount["text"] = str(self.totalearning)
			self.totalTaxesAmount["text"] = self.taxtotal
			self.netPayAmount["text"] = str(round((float(self.totalearning) - float(self.taxtotal)), 2))
		except:
			mb.showerror("Invalid", "Please enter the correct values.")

	def saveButtonClickEvent(self):
		if(self.employeeNumberCb.get() == "Select" or self.employeeNameValue.cget("text") == ""):
			mb.showerror("Invalid", "Please choose an ID number.")
		if(self.overtimeRate.get() == "" or self.sickpayRate.get() == "" or self.vacaytionpayRate.get() == "" or self.holidayRate.get() == ""):
			mb.showerror("Invalid", "Please enter a correct value.")
		else:
			try:			
				datetime.datetime.strptime(self.startDateValue.get(), '%m-%d-%Y')
				datetime.datetime.strptime(self.endDateValue.get(), '%m-%d-%Y')
				datetime.datetime.strptime(self.issueDateValue.get(), '%m-%d-%Y')
				self.cursor = connection.cursor()
				self.cursor.execute("UPDATE Employee SET Overtime = \'"+self.overtimeRate.get()+"\', SickPay = \'"+self.sickpayRate.get()+"\', Vacation = \'"+self.vacaytionpayRate.get()+"\', Holiday= \'"+self.holidayRate.get()+"\' WHERE EmployeeID = "+self.employeeNumberCb.get()+";")
				connection.commit()
				self.cursor.execute("INSERT INTO Saves (StartDate, EndDate, IssueDate, EmployeeID, Name, Position, Rate, StraighttimeHours, OvertimeHours, SickPayHours, VacationPayHours, HolidayPayHours, TotalHours, StraighttimeRate, OvertimePayRate, SickPayRate, VacationPayRate, HolidayPayRate, TotalRate, StraighttimeEarning, OvertimeEarning, SickPayEarning, VacationPayEarning, HolidayPayEarning, TotalEarning, Withholding, Medicaid, SSS, TotalTax, NetPay) VALUES (\'"+self.startDateValue.get()+"\', \'"+self.endDateValue.get()+"\', \'"+self.issueDateValue.get()+"\', \'"+self.employeeNumberCb.get()+"\', \'"+self.employeeNameValue.cget("text")+"\', \'"+self.positionValue.cget("text")+"\', \'"+self.rateValue.cget("text")+"\', \'"+self.straighttimeValue.get()+"\', \'"+self.overtimeValue.get()+"\', \'"+self.sickpayValue.get()+"\', \'"+self.vacaytionpayValue.get()+"\', \'"+self.holidayPayValue.get()+"\', \'"+self.totalTime.cget("text")+"\', \'"+self.rateValue.cget("text")+"\', \'"+self.overtimeRate.get()+"\', \'"+self.sickpayRate.get()+"\', \'"+self.vacaytionpayRate.get()+"\', \'"+self.holidayRate.get()+"\', \'"+self.totalRate.cget("text")+"\', \'"+self.rateEarning.cget("text")+"\', \'"+self.overtimeEarning.cget("text")+"\', \'"+self.sickpayEarning.cget("text")+"\', \'"+self.vacaytionpayEarning.cget("text")+"\', \'"+self.holidayPayEarning.cget("text")+"\', \'"+self.totalEarning.cget("text")+"\', \'"+self.fedWitholdingAmount.cget("text")+"\', \'"+self.fedMedAmount.cget("text")+"\', \'"+self.fedOASDIEEAmount.cget("text")+"\', \'"+self.totalAmount.cget("text")+"\', \'"+self.netPayAmount.cget("text")+"\');")
				connection.commit()
				mb.showinfo("Success", "Successfully saved.")
			except:
				mb.showerror("Invalid", "Invalid Entries or Dates")		

	def clearButtonClickEvent(self):
		
		self.overtimeRate.delete(0, END)
		self.sickpayRate.delete(0, END) 
		self.vacaytionpayRate.delete(0, END)
		self.holidayRate.delete(0, END)

		self.overtimeRate.insert(0, "0.00")
		self.sickpayRate.insert(0, "0.00") 
		self.vacaytionpayRate.insert(0, "0.00")
		self.holidayRate.insert(0, "0.00")

		self.startDateValue.delete(0,END)
		self.endDateValue.delete(0, END)
		self.issueDateValue.delete(0, END)

		self.startDateValue.insert(0, "")
		self.endDateValue.insert(0, "")
		self.issueDateValue.insert(0, "")

		self.straighttimeValue.delete(0, END)
		self.overtimeValue.delete(0, END)
		self.sickpayValue.delete(0, END) 
		self.vacaytionpayValue.delete(0, END)
		self.holidayPayValue.delete(0, END)

		self.straighttimeValue.insert(0, "0.00")
		self.overtimeValue.insert(0, "0.00")
		self.sickpayValue.insert(0, "0.00") 
		self.vacaytionpayValue.insert(0, "0.00")
		self.holidayPayValue.insert(0, "0.00")

		self.rateEarning["text"] = "0.00"
		self.overtimeEarning["text"] = "0.00"
		self.sickpayEarning["text"] = "0.00"
		self.vacaytionpayEarning["text"] = "0.00"
		self.holidayPayEarning["text"]  = "0.00"

		self.totalRate["text"] = "0.00"
		self.totalTime["text"] = "0.00"
		self.totalEarning["text"] = "0.00"

		self.fedWitholdingAmount["text"] = "0.00"
		self.fedMedAmount["text"] = "0.00"
		self.fedOASDIEEAmount["text"] = "0.00"
		self.totalAmount["text"] = "0.00"

		self.totalGrossAmount["text"] = "0.00"
		self.totalTaxesAmount["text"] = "0.00"
		self.netPayAmount["text"] = "0.00"

	def backButtonClickEvent(self):
		self.window.destroy()
		MainMenuAdmin()

	def singleWithholdingTax(self, wage):
		if (wage > 0 and wage <= 142):
			return 0
		elif (wage > 142 and wage <= 509):
			excess = wage - 142
			percent = excess * .10
			tax = 0 + percent
			return tax
		elif (wage > 509 and wage <= 1631):
			excess = wage - 509
			percent = excess * .12
			tax = 36.70 + percent
			return tax
		elif (wage > 1631 and wage <= 3315):
			excess = wage - 1631
			percent = excess * .22
			tax = 171.34 + percent
			return tax
		elif (wage > 3315 and wage <= 6200):
			excess = wage - 3315
			percent = excess * .24
			tax = 541.82 + percent
			return tax
		elif (wage > 6200 and wage <= 7835):
			excess = wage - 6200
			percent = excess * .32
			tax = 1234.22 + percent
			return tax
		elif (wage > 7835 and wage <= 19373):
			excess = wage - 7835
			percent = excess * .35
			tax = 1757.42 + percent
			return tax
		elif (wage > 19373):
			excess = wage - 19373
			percent = excess * .37
			tax = 5795.72 + percent
			return tax

	def marriedWithholdingTax(self, wage):
		if (wage > 0 and wage <= 444):
			return 0
		elif (wage > 444 and wage <= 1177):
			excess = wage - 444
			percent = excess * .10
			tax = 0 + percent
			return tax
		elif (wage > 1177 and wage <= 3421):
			excess = wage - 1177
			percent = excess * .12
			tax = 73.30 + percent
			return tax
		elif (wage > 3421 and wage <= 6790):
			excess = wage - 3421
			percent = excess * .22
			tax = 342.58 + percent
			return tax
		elif (wage > 6790 and wage <= 12560):
			excess = wage - 6790
			percent = excess * .24
			tax = 1083.76 + percent
			return tax
		elif (wage > 12560 and wage <= 15829):
			excess = wage - 12560
			percent = excess * .32
			tax = 2468.56 + percent
			return tax
		elif (wage > 15829 and wage <= 23521):
			excess = wage - 15829
			percent = excess * .35
			tax = 3514.64 + percent
			return tax
		elif (wage > 23521):
			excess = wage - 23521
			percent = excess * .37
			tax = 6206.84 + percent
			return tax

	def medicare(self, wage):
		tax = wage * .0145
		return tax

	def socialsecurity(self, wage):
		tax = wage *  .062
		return tax

class Saves:
	def __init__(self):
		self.window = Tk()
		self.window.title("Payroll - Saved Payrolls")
		self.window.geometry("650x600+425+100")
		self.window.configure(bg = "white")

		self.mainFrame = Frame(self.window, bg = "white")		
		self.mainFrame.pack()

		self.payrollidLabel = Label(self.mainFrame, text = "PAY ID#", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.startLabel = Label(self.mainFrame, text = "START DATE", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.endLabel = Label(self.mainFrame, text = "END DATE", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.issueLabel = Label(self.mainFrame, text = "ISSUE DATE", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.idLabel = Label(self.mainFrame, text = "ID#", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.nameLabel = Label(self.mainFrame, text = "NAME", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.positionLabel = Label(self.mainFrame, text = "POSITION", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.listbox = Listbox(self.mainFrame, height = 16, width = 75, font = ("calibri", 12), bg = "#ededed", relief = FLAT)		
		self.loadEmployees(connection)

		self.showButton = Button(self.mainFrame, text = "SHOW", width = 25, relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.showButtonClickEvent)
		self.deleteButton = Button(self.mainFrame, text = "DELETE", width = 25, relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.deleteButtonClickEvent)
		self.backButton = Button(self.mainFrame, text = "BACK", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.backButtonClickEvent)

		self.payrollidLabel.grid(row = 1, column = 1, pady = (30,0), sticky = W)
		self.startLabel.grid(row = 1, column = 1, padx = (90,0), sticky = SW)
		self.endLabel.grid(row = 1, column = 1, padx = (190,0), sticky = SW)
		self.issueLabel.grid(row = 1, column = 1, padx = (290,0), sticky = SW)
		self.idLabel.grid(row = 1, column = 1, padx = (400,0), sticky = SW)
		self.nameLabel.grid(row = 1, column = 1, padx = (470,0), sticky = SW)
		self.positionLabel.grid(row = 1, column = 1, sticky = SE)
		self.listbox.grid(row = 2, column = 1)
		self.showButton.grid(row = 3, column = 1, padx = (60,0), pady = 20, sticky = W)
		self.deleteButton.grid(row = 3, column =1, padx = (0,60), pady = 20, sticky = E)
		self.backButton.grid(row = 4, column = 1, columnspan = 2, pady = 120)

	def loadEmployees(self, connection):
		self.idlist = []
		self.cursor = connection.cursor()
		self.cursor.execute("SELECT * FROM Saves;")
		results = self.cursor.fetchall()
		for row in results:
			self.payrolllist = [row[0],row[1],row[2],row[3],row[4],row[5],row[6]]
			self.listbox.insert(END, (str(self.payrolllist)).strip("[]").replace(",","|").replace("'",""))
			self.idlist.append(str(self.payrolllist[0]))

	def showButtonClickEvent(self):
		self.payid = ""
		self.payid = str([self.idlist[index] for index in self.listbox.curselection()]).strip("[]").replace(",","").replace("'","")
		if (self.payid == ""):
			mb.showerror("Invalid", "Please select from the list.")
		else:
			self.window.destroy()
			showSavedPayroll(self.payid)

	def deleteButtonClickEvent(self, connection = connection):
		self.payid = str([self.idlist[index] for index in self.listbox.curselection()]).strip("[]").replace(",","").replace("'","")
		if (self.payid == ""):
			mb.showerror("Invalid", "Please select from the list.")
		else:
			self.cursor = connection.cursor()
			self.cursor.execute("DELETE FROM Saves WHERE PayID = "+self.payid+";")
			connection.commit()
			mb.showinfo("Success", "Successfully deleted.")
			self.window.destroy()
			Saves()

	def backButtonClickEvent(self):
		self.window.destroy()
		MainMenuAdmin()

class showSavedPayroll:
	def __init__(self, payid):
		self.payid = payid
		self.window = Tk()
		self.window.title("Payroll - Saved Payroll")
		self.window.geometry("1000x700+250+70")
		self.window.configure(bg = "white")
		## main frame
		self.mainFrame = Frame(self.window, bg = "white")		
		self.mainFrame.pack()
		## frames
		self.employeeFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1, height = 103, width = 541)
		self.payDatesFrame = Frame(self.mainFrame, bg  = "white", highlightbackground = "#e0e0e0", highlightthickness = 1)
		self.earningsFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1, height = 218, width = 541)
		self.taxesFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1)
		self.totalFrame = Frame(self.mainFrame, bg = "white", highlightbackground = "#e0e0e0", highlightthickness = 1)

		## employee frame 
		self.loadPayroll()

		self.employeeNumberLabel = Label(self.employeeFrame, text = "Employee ID:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.employeeNameLabel = Label(self.employeeFrame, text = "Name:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.positionLabel = Label(self.employeeFrame, text = "Job Title:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.hourlyRateLabel = Label(self.employeeFrame, text = "Pay Rate:", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.employeeNumber = Label(self.employeeFrame, text = self.employeeid, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.employeeNameValue = Label(self.employeeFrame, text = self.name, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.positionValue = Label(self.employeeFrame, text = self.position, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.hourlyRateValue = Label(self.employeeFrame, text = self.rate, font = ("calibri", 12), bg = "white", fg = "#383838")
		# employee frame grids
		self.employeeFrame.grid(row =1, column = 1, pady = (130,0), sticky = W)
		self.employeeFrame.grid_propagate(False)
		self.employeeNumberLabel.grid(row = 1, column = 1, sticky = W)
		self.employeeNumber.grid(row = 1, column = 2, padx = (40,0), sticky = W)
		self.employeeNameLabel.grid(row = 2, column = 1, sticky = W)
		self.employeeNameValue.grid(row = 2, column = 2, padx = (40,278), sticky = W)
		self.positionLabel.grid(row = 3, column = 1, sticky = W)
		self.positionValue.grid(row = 3, column = 2, padx = (40,278), sticky = W)
		self.hourlyRateLabel.grid(row = 4, column = 1, sticky = W)
		self.hourlyRateValue.grid(row = 4, column = 2, padx = (40,278), sticky = W)

		## pay date frame 
		self.payIDLabel = Label(self.payDatesFrame, text = "Pay ID:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.startDateLabel = Label(self.payDatesFrame, text = "Start Date:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.endDateLabel = Label(self.payDatesFrame, text = "End Date:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.issueDateLabel = Label(self.payDatesFrame, text = "Issue Date:", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.payIDValue = Label(self.payDatesFrame, text = self.id, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.startDateValue = Label(self.payDatesFrame, text = self.startdate, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.endDateValue =  Label(self.payDatesFrame, text = self.enddate, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.issueDateValue = Label(self.payDatesFrame, text = self.issuedate, font = ("calibri", 12), bg = "white", fg = "#383838")
		# pay date frame grids
		self.payDatesFrame.grid(row =1, column = 2, pady = (130,0), sticky = E)
		self.payIDLabel.grid(row = 1, column = 1, sticky = W)
		self.payIDValue.grid(row = 1, column = 2, padx = (100,0), sticky = W)
		self.startDateLabel.grid(row = 2, column = 1, sticky = W)
		self.startDateValue.grid(row = 2, column = 2, padx = (100,0), sticky = W)
		self.endDateLabel.grid(row = 3, column = 1, sticky = W)
		self.endDateValue.grid(row = 3, column = 2, padx = (100,0), sticky = W)
		self.issueDateLabel.grid(row = 4, column = 1, sticky = W)
		self.issueDateValue.grid(row = 4, column = 2, padx = (100,0), sticky = W)

		## earnings frame 
		self.typeHeaderLabel = Label(self.earningsFrame, text = "Type", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.straighttimeLabel = Label(self.earningsFrame, text = "Straight Time:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.overtimeLabel = Label(self.earningsFrame, text = "Overtime:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.sickpayLabel = Label(self.earningsFrame, text = "Sick Pay:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.vacaytionpayLabel = Label(self.earningsFrame, text = "Vacation Pay:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.holidayPayLabel = Label(self.earningsFrame, text= "Holiday Pay:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalLabel = Label(self.earningsFrame, text = "Total:", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.hoursHeaderLabel = Label(self.earningsFrame, text = "Hours", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.straighttimeValue = Label(self.earningsFrame, text = self.straighttimehours, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.overtimeValue = Label(self.earningsFrame, text = self.overtimehours, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.sickpayValue = Label(self.earningsFrame, text = self.sickpayhours, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.vacaytionpayValue = Label(self.earningsFrame, text = self.vacationpayhours, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.holidayPayValue = Label(self.earningsFrame, text = self.holidaypayhours, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.totalTime = Label(self.earningsFrame, text = self.totalhours, font = ("calibri", 12), bg = "white", fg = "#383838")

		self.rateHeaderLabel = Label(self.earningsFrame, text = "Rates", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.rateValue = Label(self.earningsFrame, text = self.straighttimerate, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.overtimeRate =Label(self.earningsFrame, text = self.overtimepayrate, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.sickpayRate = Label(self.earningsFrame, text = self.sickpayrate, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.vacaytionpayRate = Label(self.earningsFrame, text = self.vacationpayrate, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.holidayRate = Label(self.earningsFrame, text = self.holidaypayrate, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.totalRate = Label(self.earningsFrame, text = self.totalrate, font = ("calibri", 12), bg = "white", fg = "#383838")

		self.earningsHeaderLabel = Label(self.earningsFrame, text = "Earnings", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.rateEarning = Label(self.earningsFrame, text = self.straighttimeearning, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.overtimeEarning = Label(self.earningsFrame, text = self.overtimeearning, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.sickpayEarning = Label(self.earningsFrame, text = self.sickpayearning, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.vacaytionpayEarning = Label(self.earningsFrame, text = self.vacationpayearning, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.holidayPayEarning = Label(self.earningsFrame, text = self.holidaypayearning, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		self.totalEarning = Label(self.earningsFrame, text = self.totalearning, font = ("calibri", 12), bg = "white", fg = "#383838", justify = RIGHT)
		# earnings frame grids
		self.earningsFrame.grid(row = 2, column = 1, pady = (10,0), sticky = W)
		self.typeHeaderLabel.grid(row = 1, column = 1, sticky = W)
		self.straighttimeLabel.grid(row = 2, column = 1, pady = (20,0), sticky = W)
		self.overtimeLabel.grid(row = 3, column = 1, sticky = W)
		self.sickpayLabel.grid(row = 4, column = 1, sticky = W)
		self.vacaytionpayLabel.grid(row = 5, column = 1, sticky = W)
		self.holidayPayLabel.grid(row = 6, column = 1, sticky = W)
		self.totalLabel.grid(row = 7, column = 1, pady = (20,0), sticky = W)

		self.hoursHeaderLabel.grid(row = 1, column = 2, padx = (80,30), sticky = E)
		self.straighttimeValue.grid(row = 2, column = 2, pady = (20,0), padx = (80,30), sticky = E)
		self.overtimeValue.grid(row = 3, column = 2, padx = (80,30), sticky = E)
		self.sickpayValue.grid(row = 4, column = 2, padx = (80,30), sticky = E)
		self.vacaytionpayValue.grid(row = 5, column = 2, padx = (80,30), sticky = E)
		self.holidayPayValue.grid(row = 6, column = 2, padx = (80,30), sticky = E)
		self.totalTime.grid(row = 7, column = 2, pady = (20,0), padx = (80,30), sticky = E)

		self.rateHeaderLabel.grid(row = 1, column = 3, padx = (90,80), sticky = E)
		self.rateValue.grid(row = 2, column = 3, pady = (20,0), padx = (30,80), sticky = E)
		self.overtimeRate.grid(row = 3, column = 3, padx = (30,80), sticky = E)
		self.sickpayRate.grid(row = 4, column = 3, padx = (30,80), sticky = E)
		self.vacaytionpayRate.grid(row = 5, column = 3, padx = (30,80), sticky = E)
		self.holidayRate.grid(row = 6, column = 3, padx = (30,80), sticky = E)
		self.totalRate.grid(row = 7, column = 3, pady = (20,0), padx = (30,80), sticky = E)

		self.earningsHeaderLabel.grid(row = 1, column = 4, padx=(14,0), sticky = E)
		self.rateEarning.grid(row = 2, column = 4, pady = (20,0), sticky = E)
		self.overtimeEarning.grid(row = 3, column = 4, sticky = E)
		self.sickpayEarning.grid(row = 4, column = 4, sticky = E)
		self.vacaytionpayEarning.grid(row = 5, column = 4, sticky = E)
		self.holidayPayEarning.grid(row = 6, column = 4, sticky = E)
		self.totalEarning.grid(row = 7, column = 4, pady = (20,0), sticky = E)

		## taxes frame 
		self.taxesHeadingLabel = Label(self.taxesFrame, text = "TAXES", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.descriptionLabel = Label(self.taxesFrame, text = "Description", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedWitholdingLabel = Label(self.taxesFrame, text = "Fed Withholding", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedMedLabel = Label(self.taxesFrame, text = "Fed Med/EE", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedOASDIEELabel = Label(self.taxesFrame, text = "Fed OASDI/EE", font = ("calibri", 12), bg = "white", fg = "#383838")

		self.amountLabel = Label(self.taxesFrame, text = "Amount", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedWitholdingAmount = Label(self.taxesFrame, text = self.withholding, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedMedAmount = Label(self.taxesFrame, text = self.medicaid, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.fedOASDIEEAmount = Label(self.taxesFrame, text = self.sss, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.taxesTotalLabel = Label(self.taxesFrame, text = "Total:", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalAmount = Label(self.taxesFrame, text = self.totaltax, font = ("calibri", 12), bg = "white", fg = "#383838")
		# taxes frame grids
		self.taxesFrame.grid(row = 2, column = 2, pady = (10,0), padx = (10,0), sticky = N)
		self.taxesHeadingLabel.grid(row = 1, column = 2, sticky = W)
		self.descriptionLabel.grid(row = 2, column = 1, pady = (20,0), sticky = W)
		self.fedWitholdingLabel.grid(row = 3, column = 1, pady = (10,0), sticky = W)
		self.fedMedLabel.grid(row = 4, column = 1, sticky = W)
		self.fedOASDIEELabel.grid(row = 5, column = 1, sticky = W)

		self.amountLabel.grid(row = 2, column = 3, pady = (20,0), padx = (50,0), sticky = E)
		self.fedWitholdingAmount.grid(row = 3, column = 3, pady = (10,0), sticky = E)
		self.fedMedAmount.grid(row = 4, column = 3, sticky = E)
		self.fedOASDIEEAmount.grid(row = 5, column = 3, sticky = E)

		self.taxesTotalLabel.grid(row = 6, column = 1, pady = (35,0), sticky = W)
		self.totalAmount.grid(row = 6, column = 3, pady = (35,0), sticky = E)

		## total frame
		self.totalGrossLabel = Label(self.totalFrame, text = "TOTAL GROSS", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalGrossAmount = Label(self.totalFrame, text = self.totalearning, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalTaxesLabel = Label(self.totalFrame, text = "TOTAL TAXES", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.totalTaxesAmount = Label(self.totalFrame, text = self.totaltax, font = ("calibri", 12), bg = "white", fg = "#383838")
		self.netPayLabel = Label(self.totalFrame, text = "NET PAY", font = ("calibri", 12), bg = "white", fg = "#383838")
		self.netPayAmount = Label(self.totalFrame, text = self.netpay, font = ("calibri", 12), bg = "white", fg = "#383838")
		#total frame grids
		self.totalFrame.grid(row = 3, column = 1, pady = (10,0),sticky = W)
		self.totalGrossLabel.grid(row = 1, column = 1, sticky = W)
		self.totalGrossAmount.grid(row = 2, column = 1, pady = (20,0), sticky = W)
		self.totalTaxesLabel.grid(row = 1, column = 2, padx = (144,0), sticky = E)
		self.totalTaxesAmount.grid(row = 2, column = 2, pady = (20,0), sticky = E)
		self.netPayLabel.grid(row = 1, column = 3, padx = (144,0), sticky = E)
		self.netPayAmount.grid(row = 2, column = 3, pady = (20,0), sticky = E)

		##back button
		self.backButton = Button(self.mainFrame, width = 10, text = "BACK", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.backButtonClickEvent)
		self.backButton.grid(row = 4, column = 1, columnspan = 2, pady = 125)

	def loadPayroll(self, connection = connection):
		self.cursor = connection.cursor()
		self.cursor.execute("SELECT * FROM Saves WHERE PayID = "+self.payid+";")
		results = self.cursor.fetchall()
		for row in results:
			self.id = row[0]
			self.startdate = row[1]
			self.enddate = row[2]
			self.issuedate = row[3]
			self.employeeid = row[4]
			self.name = row[5]
			self.position = row[6]
			self.rate = row[7]
			self.straighttimehours = row[8]
			self.overtimehours = row[9]
			self.sickpayhours = row[10]
			self.vacationpayhours = row[11]
			self.holidaypayhours = row[12]
			self.totalhours = row[13]
			self.straighttimerate = row[14]
			self.overtimepayrate = row[15]
			self.sickpayrate = row[16]
			self.vacationpayrate = row[17]
			self.holidaypayrate = row[18]
			self.totalrate = row[19]
			self.straighttimeearning = row[20]
			self.overtimeearning = row[21]
			self.sickpayearning = row[22]
			self.vacationpayearning = row[23]
			self.holidaypayearning = row[24]
			self.totalearning = row[25]
			self.withholding = row[26]
			self.medicaid = row[27]
			self.sss = row[28]
			self.totaltax = row[29]
			self.netpay = row[30]

	def backButtonClickEvent(self):
		self.window.destroy()
		Saves()

class Employees:
	def __init__(self):
		self.window = Tk()
		self.window.title("Payroll - Employees")
		self.window.geometry("650x600+425+100")
		self.window.configure(bg = "white")

		self.mainFrame = Frame(self.window, bg = "white")		
		self.mainFrame.pack()

		self.idLabel = Label(self.mainFrame, text = "ID#", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.nameLabel = Label(self.mainFrame, text = "NAME", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.statusLabel = Label(self.mainFrame, text = "STATUS", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.emailLabel = Label(self.mainFrame, text = "EMAIL", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.phonenumberLabel = Label(self.mainFrame, text = "PHONE#", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.hourlyrateLabel = Label(self.mainFrame, text = "HOURLY", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.positionLabel = Label(self.mainFrame, text = "POSITION", font = ("calibri", 10), bg = "white", fg = "#383838")
		self.listbox = Listbox(self.mainFrame, height = 16, width = 75, font = ("calibri", 12), bg = "#ededed", relief = FLAT)		
		self.loadEmployees(connection)

		self.addButton = Button(self.mainFrame, text = "ADD", width = 25, relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.addButtonClickEvent)
		self.deleteButton = Button(self.mainFrame, text = "DELETE", width = 25, relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.deleteButtonClickEvent)
		self.backButton = Button(self.mainFrame, text = "BACK", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.backButtonClickEvent)

		self.idLabel.grid(row = 1, column = 1, pady = (30,0), sticky = W)
		self.nameLabel.grid(row = 1, column = 1, padx = (70,0), sticky = SW)
		self.statusLabel.grid(row = 1, column = 1, padx = (150,0), sticky = SW)
		self.emailLabel.grid(row = 1, column = 1, padx = (250,0), sticky = SW)
		self.phonenumberLabel.grid(row = 1, column = 1, padx = (350,0), sticky = SW)
		self.hourlyrateLabel.grid(row = 1, column = 1, padx = (450,0), sticky = SW)
		self.positionLabel.grid(row = 1, column = 1, sticky = SE)
		self.listbox.grid(row = 2, column = 1)
		self.addButton.grid(row = 3, column = 1, padx = (60,0), pady = 20, sticky = W)
		self.deleteButton.grid(row = 3, column =1, padx = (0,60), pady = 20, sticky = E)
		self.backButton.grid(row = 4, column = 1, columnspan = 2, pady = 120)

	def loadEmployees(self, connection):
		self.idlist = []
		self.cursor = connection.cursor()
		self.cursor.execute("SELECT * FROM Employee;")
		results = self.cursor.fetchall()
		for row in results:
			self.employeelist = [row[0],row[1]+" "+row[2]+" "+row[3],row[4],row[5],row[6],row[7],row[8]]
			self.listbox.insert(END, (str(self.employeelist)).strip("[]").replace(",","|").replace("'",""))
			self.idlist.append(str(self.employeelist[0]))

	def deleteButtonClickEvent(self, connection = connection):
		self.employee_id = str([self.idlist[index] for index in self.listbox.curselection()]).strip("[]").replace(",","").replace("'","")
		if (self.employee_id == ""):
			mb.showerror("Invalid", "Please select from the list.")
		else:
			self.cursor = connection.cursor()
			self.cursor.execute("DELETE FROM Employee WHERE EmployeeId = \'"+self.employee_id+"\';")
			connection.commit()
			mb.showinfo("Success", "Successfully deleted.")
			self.window.destroy()
			Employees()

	def backButtonClickEvent(self):
		self.window.destroy()
		MainMenuAdmin()

	def addButtonClickEvent(self):
		self.window.destroy()
		AddEmployee()

class AddEmployee:
	def __init__(self):
		self.window = Tk()
		self.window.title("Payroll - Add Employee")
		self.window.geometry("650x600+430+80")
		self.window.configure(bg = "white")
		self.frame = Frame(self.window, bg = "white")
		self.frame.pack(padx = (0,85))

		self.firstNameInput = StringVar()
		self.middleNameInput = StringVar()
		self.lastNameInput = StringVar()
		self.emailInput = StringVar()
		self.phoneNumberInput = StringVar()
		self.passwordInput = StringVar()
		self.positionInput = StringVar()
		self.hourlyRateInput = StringVar()
		self.statusInput = StringVar()	

		self.firstNameLabel = Label(self.frame, text = "First Name:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.firstNameTextBox = Entry(self.frame, textvariable = self.firstNameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.middleNameLabel = Label(self.frame, text = "Middle Name:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.middleNameTextBox = Entry(self.frame, textvariable = self.middleNameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.lastNameLabel = Label(self.frame, text = "Last Name:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.lastNameTextBox = Entry(self.frame, textvariable = self.lastNameInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.maritalstatusLabel = Label(self.frame, text = "Marital Status:", font = ("calibri", 11), bg = "white", fg = "#383838", justify = RIGHT)
		self.maritalstatus = ttk.Combobox(self.frame, font = ("calibri", 11), textvariable = self.statusInput)
		self.maritalstatus['values']= ('Single','Married')
		self.maritalstatus.set('Select')
		self.emailLabel = Label(self.frame, text = "Email:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.emailTextBox = Entry(self.frame, textvariable = self.emailInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.phoneNumberLabel = Label(self.frame, text = "Phone Number:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.phoneNumberTextBox = Entry(self.frame, textvariable = self.phoneNumberInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.hourlyRateLabel = Label(self.frame, text = "Hourly Rate:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.hourlyRateTextBox = Entry(self.frame, textvariable = self.hourlyRateInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.positionLabel = Label(self.frame, text = "Position:", font = ("calibri", 11), bg = "white", fg = "#383838")
		self.positionTextBox = Entry(self.frame, textvariable = self.positionInput, width = 30, font = ("calibri", 12), bg = "#ededed", relief = FLAT)
		self.addButton = Button(self.frame, width = 30, text = "ADD EMPLOYEE", relief = FLAT, font = ("calibri", 11, "bold"), bg = "#a260f7", fg = "white", command = self.addButtonClickEvent) 
		self.backButton = Button(self.frame, width = 10, text = "BACK", relief = FLAT, font = ("calibri", 11), bg = "white", fg = "#383838", command = self.backButtonClickEvent)

		self.firstNameLabel.grid(row = 1, column = 1, pady = (110, 0), sticky = E)
		self.firstNameTextBox.grid(row = 1, column = 2, pady = (110, 0))
		self.middleNameLabel.grid(row = 2, column = 1, pady = (10, 0), sticky = E)
		self.middleNameTextBox.grid(row = 2, column = 2, pady = (10, 0))
		self.lastNameLabel.grid(row = 3, column = 1, pady = (10, 0), sticky = E)
		self.lastNameTextBox.grid(row = 3, column = 2, pady = (10, 0))
		self.maritalstatusLabel.grid(row = 4, column = 1, pady = (10, 0), sticky = E)
		self.maritalstatus.grid(row = 4, column = 2, pady = (10, 0), padx = (3,0), sticky = W)
		self.emailLabel.grid(row = 5, column = 1, pady = (10, 0), sticky = E)
		self.emailTextBox.grid(row = 5, column = 2, pady = (10, 0))
		self.phoneNumberLabel.grid(row = 6, column = 1, pady = (10, 0), sticky = E)
		self.phoneNumberTextBox.grid(row = 6, column = 2, pady = (10, 0))
		self.hourlyRateLabel.grid(row = 7, column = 1, pady = (10, 0), sticky = E)
		self.hourlyRateTextBox.grid(row = 7, column = 2, pady = (10, 0))
		self.positionLabel.grid(row = 8, column = 1, pady = (10, 0), sticky = E)
		self.positionTextBox.grid(row = 8, column = 2, pady = (10, 0))
		self.addButton.grid(row = 9, column = 2, pady = (30, 0), sticky = E)
		self.backButton.grid(row = 10, column = 2, pady = (130, 0))

	def addButtonClickEvent(self):
		if (self.firstNameTextBox.get() == "" or self.middleNameTextBox.get() == "" or self.lastNameTextBox.get() == "" or self.maritalstatus.get() == "Select" or self.emailTextBox.get() == "" or self.phoneNumberTextBox.get() == "" or self.hourlyRateTextBox.get() == "" or self.positionTextBox.get() == ""):
			mb.showerror("Invalid", "Please fill out all the forms.")
		else:
			d.AddEmployee(connection, self.firstNameTextBox.get(), self.middleNameTextBox.get(), self.lastNameTextBox.get(), self.maritalstatus.get(), self.emailTextBox.get(), self.phoneNumberTextBox.get(), self.hourlyRateTextBox.get(), self.positionTextBox.get(), "0.00", "0.00", "0.00","0.00")
			mb.showinfo("Success", "Successfully added a new employee.")
			self.window.destroy()
			Employees()

	def backButtonClickEvent(self):
		self.window.destroy()
		Employees()

Login()