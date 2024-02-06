from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pickle as pk


class user:
    def __init__(self, userID, password, name, securityQ, securityA, incorrectAttempts = 0):
        self.userID = userID
        self.password = password
        self.name = name
        self.securityQ = securityQ
        self.securityA = securityA
        self.incorrectAttempts = incorrectAttempts

class teacher(user):
    def __init__(self, userID, password, name, securityQ, securityA, incorrectAttempts, department = None, courses = None, officeAddress = None):
        super().__init__(userID, password, name, securityQ, securityA, incorrectAttempts)
        self.department = department
        self.courses = courses
        self.officeAddress = officeAddress
        
class student(user):
    def __init__(self, userID, password, name, securityQ, securityA, incorrectAttempts, year, degree, department = None, courses = None, cgpa = None, address = None, phoneNo = None):
        super().__init__(userID, password, name, securityQ, securityA, incorrectAttempts)
        self.year = year
        self.degree = degree
        self.department = department
        self.courses = courses
        self.cgpa = cgpa
        self.address = address
        self.phoneNo = phoneNo
         
class UGs(student):
    def __init__(self, userID, password, name, securityQ, securityA, incorrectAttempts, year, degree, department, courses, cgpa, address, phoneNo, minorCourses = None, majorCourses = None):
        super().__init__(userID, password, name, securityQ, securityA, incorrectAttempts, year, degree, department, courses, cgpa, address, phoneNo)
        self.minorCourses = minorCourses
        self.majorCourses = majorCourses
                
class PGs(student):
    def __init__(self, userID, password, name, securityQ, securityA, incorrectAttempts, year, degree, department, courses, cgpa, address, phoneNo, specialization = None):
        super().__init__(userID, password, name, securityQ, securityA, incorrectAttempts, year, degree, department, courses, cgpa, address, phoneNo)
        self.specialization = specialization
     
     
def checkUserID(userID):
    if "@" not in userID:
        return False
    if "." not in userID:
        return False
    return True

def checkPassword(password):
    #Password: A valid password should satisfy the following:
        #a) It should be within 8-12 character long.
        #b) It should contain at least one upper case, one digit, and one lower case.
        #c) It should contains one or more special character(s) from the list [! @ # $ % & *]
        #d) No blank space will be allowed.
    if len(password) < 8 or len(password) > 12:
        return False
    upper = False
    lower = False
    digit = False
    special = False
    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
        elif i in "!@#$%&*":
            special = True
        else:
            return False
    if upper and lower and digit and special:
        return True
    return False

def showPassword(passwordEntry, showPasswordVar):
    if showPasswordVar:
        passwordEntry.config(show="")
    else:
        passwordEntry.config(show="*")
     
#inactive windows     
register_window = registerTeacher_window = registerStudent_window = login_window = None
   
def home():   
    global root 
    root = Tk()  
    root.title("Home Page")  
    root.geometry("700x600")
    root.configure(bg='#b3b3ff', highlightthickness=4)
    
    homePageLabel = Label(root, text="Welcome to\nEnterprise Resource Planning\n[E.R.P.]", fg='#000033', font=('Batang', 18, 'bold'), bg='#b3b3ff', width=30, height=3, borderwidth=5, relief="groove", padx=10, pady=15, highlightbackground="black", highlightcolor="black")
    homePageLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
    
    registerButton = Button(root, text="Register", command=register, bg='#6666ff', font=('Fira Sans', 12), width=15, activebackground='lightblue', fg='white')
    loginButton = Button(root, text="Login", command=login, bg='#6666ff', font=('Helvetica', 12), width=15, activebackground='lightblue', fg='white')
    registerButton.place(relx=0.5, rely=0.45, anchor=CENTER)
    loginButton.place(relx=0.5, rely=0.55, anchor=CENTER)
    
    quitButton = Button(root, text="Quit", command=quit, bg='black', fg = 'white', font=('Helvetica', 12, 'bold'), width=10, height=1, activebackground='white', activeforeground='black')
    quitButton.place(relx=0.5, rely=0.9, anchor=CENTER)
    
    root.mainloop()

def quit():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()   


def register():  
    #if register window is already open, lift it to the top
    global register_window
    if register_window is not None:
        register_window.lift()
        return
    
    #if register window is not open, open it
    global root
    register_window =Toplevel(root)
    #The Toplevel() function takes one optional argument, which is the parent of the new window. In your code, root is the parent of register_window. This means that if root is closed, register_window will also be closed.
    register_window.title("Register")
    register_window.geometry("700x600")
    register_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    registerTeacherButton = Button(register_window, text="Register as a teacher", command=registerTeacher, bg='#6666ff', font=('Helvetica', 12, 'bold'), width=25, activebackground='lightblue', fg='white')
    registerStudentButton = Button(register_window, text="Register as a student", command=registerStudent, bg='#6666ff', font=('Helvetica', 12, 'bold'), width=25, activebackground='lightblue', fg='white')
    
    registerTeacherButton.place(relx=0.5, rely=0.20, anchor=CENTER)
    registerStudentButton.place(relx=0.5, rely=0.30, anchor=CENTER)
    
    #go to login
    loginLabel = Label(register_window, text="Already registered?", bg='#b3b3ff', fg='black', font=('Helvetica', 12, 'bold'))
    loginLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
    loginButton = Button(register_window, text="Login", command=login, bg='#8080ff', font=('Helvetica', 12, 'bold'), width=15, activebackground='lightblue', fg='white')
    loginButton.place(relx=0.5, rely=0.75, anchor=CENTER)
    
    homepagebutton = Button(register_window, text = "Close", command= on_register_window_closed, bg='black', fg = 'white', font=('Helvetica', 12, 'bold'), width=10, height=1, activebackground='white', activeforeground='black')
    homepagebutton.place(relx=0.5, rely=0.9, anchor=CENTER)
      
def on_register_window_closed():
    global register_window
    register_window.destroy()
    register_window = None
    #register_window = None is important to make sure that register_window is set to None when the window is closed. This way, the next time register() is called, it will open a new window instead of just lifting the old one.
    
    
def registerTeacher():
    global registerTeacher_window
    if registerTeacher_window is not None:
        registerTeacher_window.lift()
        return
    
    global register_window
    registerTeacher_window = Toplevel(register_window)
    registerTeacher_window.title("Register as a teacher")
    registerTeacher_window.geometry("700x600")
    registerTeacher_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    #userID
    userIDLabel = Label(registerTeacher_window, text="Enter your userID", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
    userIDEntry = Entry(registerTeacher_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    userIDEntry.place(relx=0.5, rely=0.13, anchor=CENTER)

    #password
    passwordLabel = Label(registerTeacher_window, text="Enter your password", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    passwordLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
    passwordEntry = Entry(registerTeacher_window, width=50, show="*", bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    passwordEntry.place(relx=0.5, rely=0.23, anchor=CENTER)
    showPasswordVar = BooleanVar()
    showPasswordCheckbutton = Checkbutton(registerTeacher_window, text="Show password", variable=showPasswordVar, command= lambda: showPassword(passwordEntry, showPasswordVar.get()), bg='#b3b3ff', fg='black', font=('Helvetica', 9), activebackground='#b3b3ff', activeforeground='black')
    showPasswordCheckbutton.place(relx=0.80, rely=0.23, anchor=W)
    
    #name
    nameLabel = Label(registerTeacher_window, text="Enter your name", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    nameLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
    nameEntry = Entry(registerTeacher_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    nameEntry.place(relx=0.5, rely=0.33, anchor=CENTER)
    
    #security question
    securityQLabel = Label(registerTeacher_window, text="Select your security question", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    securityQLabel.place(relx=0.5, rely=0.42, anchor=CENTER)
    securityQs = [
        "What is your favourite color?",
        "What is your favourite food?",
        "What is your favourite movie?",
        "What is your favourite book?",
        "What is your favourite song?"
    ]
    securityQCombobox = ttk.Combobox(registerTeacher_window, values=securityQs, state="readonly")
    securityQCombobox.set(securityQs[0])  # Set the default value to the first security question
    securityQCombobox.config(width=47, font=('Helvetica', 9), background='#e6e6ff', foreground='black')
    securityQCombobox.place(relx=0.5, rely=0.47, anchor=CENTER)
    
    #security answer
    securityALabel = Label(registerTeacher_window, text="Enter your security answer", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    securityALabel.place(relx=0.5, rely=0.52, anchor=CENTER)
    securityAEntry = Entry(registerTeacher_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    securityAEntry.place(relx=0.5, rely=0.55, anchor=CENTER)    
    
    #department
    departments = [
        "Aerospace Engineering",
        "Agricultural and Food Engineering",
        "Architecture and Regional Planning",
        "Centre of Excellence in Artificial Intelligence (AI)",
        "Chemical Engineering",
        "Civil Engineering",
        "Computer Science and Engineering",
        "Electrical Engineering",
        "Electronics and Electrical Communication Engg.",
        "Mechanical Engineering",
        "Metallurgical and Materials Engineering",
        "Mining Engineering",
        "Ocean Engg and Naval Architecture"
    ]
    
    #combobox for department
    departmentLabel = Label(registerTeacher_window, text="Select your department", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    departmentLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
    departmentCombobox = ttk.Combobox(registerTeacher_window, values=departments, state="readonly")
    departmentCombobox.set(departments[6])  # Set the default value to the first department
    departmentCombobox.config(width=47, font=('Helvetica', 9), background='#e6e6ff', foreground='black')
    departmentCombobox.place(relx=0.5, rely=0.63, anchor=CENTER)
    
    
    #security Key, so that a verified teacher can register
    securityKeyLabel = Label(registerTeacher_window, text="Enter Teacher security key", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    securityKeyLabel.place(relx=0.5, rely=0.75, anchor=CENTER)
    securityKeyEntry = Entry(registerTeacher_window, width=50,show="*", bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    securityKeyEntry.place(relx=0.5, rely=0.78, anchor=CENTER)
    showSecurityKeyVar = BooleanVar()
    showSecurityKeyCheckbutton = Checkbutton(registerTeacher_window, text="Show security key", variable=showSecurityKeyVar, command= lambda: showPassword(securityKeyEntry, showSecurityKeyVar.get()), bg='#b3b3ff', fg='black', font=('Helvetica', 9), activebackground='#b3b3ff', activeforeground='black')
    showSecurityKeyCheckbutton.place(relx=0.80, rely=0.78, anchor=W)
    
    
    #department to be edited later
    #courses to be edited later 
    
    #register button
    registerButton = Button(registerTeacher_window, text="Register Teacher", command=lambda: registerTeacherButtonClicked(userIDEntry.get(), passwordEntry.get(), departmentCombobox.get(), securityKeyEntry.get(), nameEntry.get(), securityQCombobox.get(), securityAEntry.get()), bg='#6666ff', font=('Helvetica', 12, 'bold'), width=15, activebackground='lightblue', fg='white')
    registerButton.place(relx=0.5, rely=0.85, anchor=CENTER)
    
    #go back to register window
    homepagebutton = Button(registerTeacher_window, text = "Go back to register", command= on_registerTeacher_window_closed, bg='black', fg = 'white', font=('Helvetica', 12, 'bold'),activebackground='white', activeforeground='black')
    homepagebutton.place(relx=0.5, rely=0.95, anchor=CENTER)
        
def on_registerTeacher_window_closed():
    global registerTeacher_window
    registerTeacher_window.destroy()
    registerTeacher_window = None
    
def registerTeacherButtonClicked(userID, password, department, securityKey, name, securityQ, securityA):
    #no input can be empty
    #check if userID is already taken
    #if yes, show error message
    #if no, register
    #then go back to register window
    global registerTeacher_window
    if userID == "" or password == "":
        messagebox.showerror("Error", "No input can be empty")
        on_registerTeacher_window_closed()
        return 
    if not checkUserID(userID):
        messagebox.showerror("Error", "Invalid userID\n Enter valid Email address")
        on_registerTeacher_window_closed()
        return
    if not checkPassword(password):
        messagebox.showerror("Error", "Invalid password")
        on_registerTeacher_window_closed()
        return
    if securityKey != "SEL@30012024":
        messagebox.showerror("Error", "Incorrect security key\nYou are not a verified teacher")
        on_registerTeacher_window_closed()
        return
    
    try:
        with open("users.pk", "rb") as f:
            teachers = pk.load(f)
    except:
        teachers = {}
    if userID in teachers:
        messagebox.showerror("Error", "This userID is already taken")
        return
    teachers[userID] = teacher(userID, password, name, securityQ, securityA, 0, department, None, None)
    with open("users.pk", "wb") as f:
        pk.dump(teachers, f)
    messagebox.showinfo("Success", "You have been registered as a teacher")
    on_registerTeacher_window_closed()
    

def registerStudent():
        # give dropdown for UG/PG
        # if UG is selected, give entry for minor and major courses
        # if PG is selected, give entry for specialization

        global registerStudent_window
        if registerStudent_window is not None:
            registerStudent_window.lift()
            return

        global register_window
        registerStudent_window = Toplevel(register_window)
        registerStudent_window.title("Register as a student")
        registerStudent_window.geometry("700x600")
        registerStudent_window.configure(bg='#b3b3ff', highlightthickness=4)

        # dropdown menu
        options = ["UG", "PG"]
        #combobox for degree
        degreeLabel = Label(registerStudent_window, text="Select your degree", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        degreeLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
        clicked = StringVar()
        clicked.set(options[0])  # Set the default value to the first degree
        degreeCombobox = ttk.Combobox(registerStudent_window, values=options, state="readonly")
        degreeCombobox.config(width=47, font=('Helvetica', 9), background='#e6e6ff', foreground='black')
        degreeCombobox.place(relx=0.5, rely=0.13, anchor=CENTER)

        # userID
        userIDLabel = Label(registerStudent_window, text="Enter your userID", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        userIDLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
        userIDEntry = Entry(registerStudent_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
        userIDEntry.place(relx=0.5, rely=0.25, anchor=CENTER)

        # password
        passwordLabel = Label(registerStudent_window, text="Enter your password", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        passwordLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
        passwordEntry = Entry(registerStudent_window, width=50, show="*", bg='#e6e6ff', fg='black', font=('Helvetica', 9))
        passwordEntry.place(relx=0.5, rely=0.35, anchor=CENTER)
        showPasswordVar = BooleanVar()
        showPasswordCheckbutton = Checkbutton(registerStudent_window, text="Show password", variable=showPasswordVar, command= lambda: showPassword(passwordEntry, showPasswordVar.get()), bg='#b3b3ff', fg='black', font=('Helvetica', 9), activebackground='#b3b3ff', activeforeground='black')
        showPasswordCheckbutton.place(relx=0.80, rely=0.35, anchor=W)

        # name
        nameLabel = Label(registerStudent_window, text="Enter your name", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        nameLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        nameEntry = Entry(registerStudent_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
        nameEntry.place(relx=0.5, rely=0.45, anchor=CENTER)

        # security question
        securityQLabel = Label(registerStudent_window, text="Select your security question", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        securityQLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        securityQs = [
            "What is your favourite color?",
            "What is your favourite food?",
            "What is your favourite movie?",
            "What is your favourite book?",
            "What is your favourite song?"
        ]
        #combobox for security question
        selected_securityQ = StringVar(registerStudent_window)
        selected_securityQ.set(securityQs[0])  # Set the default value to the first security question
        securityQCombobox = ttk.Combobox(registerStudent_window, values=securityQs, state="readonly")
        securityQCombobox.config(width=47, font=('Helvetica', 9), background='#e6e6ff', foreground='black')
        securityQCombobox.place(relx=0.5, rely=0.53, anchor=CENTER)
        
        # security answer
        securityALabel = Label(registerStudent_window, text="Enter your security answer", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        securityALabel.place(relx=0.5, rely=0.6, anchor=CENTER)
        securityAEntry = Entry(registerStudent_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
        securityAEntry.place(relx=0.5, rely=0.65, anchor=CENTER)

        # year
        yearLabel = Label(registerStudent_window, text="Enter your enrollment year", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        yearLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
        # dropdown for year
        years = [
            "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024",
        ]
        #combobox for year
        selected_year = StringVar(registerStudent_window)
        selected_year.set(years[0])  # Set the default value to the first year
        yearCombobox = ttk.Combobox(registerStudent_window, values=years, state="readonly")
        yearCombobox.config(width=47, font=('Helvetica', 9), background='#e6e6ff', foreground='black')
        yearCombobox.place(relx=0.5, rely=0.73, anchor=CENTER)
        
        # department dropdown menu
        departments = [
            "Aerospace Engineering",
            "Agricultural and Food Engineering",
            "Architecture and Regional Planning",
            "Centre of Excellence in Artificial Intelligence (AI)",
            "Chemical Engineering",
            "Civil Engineering",
            "Computer Science and Engineering",
            "Electrical Engineering",
            "Electronics and Electrical Communication Engg.",
            "Mechanical Engineering",
            "Metallurgical and Materials Engineering",
            "Mining Engineering",
            "Ocean Engg and Naval Architecture"
        ]

        #combobox for department
        departmentLabel = Label(registerStudent_window, text="Select your department", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        departmentLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
        selected_department = StringVar(registerStudent_window)
        selected_department.set(departments[6])  # Set the default value to the first department
        departmentCombobox = ttk.Combobox(registerStudent_window, values=departments, state="readonly")
        departmentCombobox.config(width=47, font=('Helvetica', 9), background='#e6e6ff', foreground='black')
        departmentCombobox.place(relx=0.5, rely=0.83, anchor=CENTER)

        # register button
        registerButton = Button(registerStudent_window, text="Register Student", command=lambda: registerStudentButtonClicked(userIDEntry.get(), passwordEntry.get(), yearCombobox.get(), degreeCombobox.get(), departmentCombobox.get(), nameEntry.get(), securityQCombobox.get(), securityAEntry.get()), bg='#6666ff', font=('Helvetica', 12, 'bold'), width=15, activebackground='lightblue', fg='white')
        registerButton.place(relx=0.5, rely=0.90, anchor=CENTER)

        # go back to register window
        homepagebutton = Button(registerStudent_window, text="Go back to register", command=on_registerStudent_window_closed, bg='black', fg='white', font=('Helvetica', 12, 'bold'), activebackground='white', activeforeground='black')
        homepagebutton.place(relx=0.5, rely=0.95, anchor=CENTER)

def on_registerStudent_window_closed():
    global registerStudent_window
    registerStudent_window.destroy()
    registerStudent_window = None

def registerStudentButtonClicked(userID, password, year, degree, department, name, securityQ, securityA):
    #no input can be empty
    #check if userID is already taken
    #if yes, show error message
    #if no, register
    #then go back to register window
    global registerStudent_window
    if userID == "" or password == "" or year == "":
        messagebox.showerror("Error", "No input can be empty")
        on_registerStudent_window_closed()
        return 
    if not checkUserID(userID):
        messagebox.showerror("Error", "Invalid userID\n Enter valid Email address")
        on_registerStudent_window_closed()
        return
    if not checkPassword(password):
        messagebox.showerror("Error", "Invalid password")
        on_registerStudent_window_closed()
        return
    try:
        with open("users.pk", "rb") as f:
            students = pk.load(f)
    except:
        students = {}
    if userID in students:
        messagebox.showerror("Error", "This userID is already taken")
        return
    if degree == "UG":
        students[userID] = UGs(userID, password, name, securityQ, securityA, 0, year, degree, department, None, None, None, None, None, None)
    else:
        students[userID] = PGs(userID, password, name, securityQ, securityA, 0, year, degree, department, None, None, None, None, None)
        
    with open("users.pk", "wb") as f:
        pk.dump(students, f)
    messagebox.showinfo("Success", "You have been registered as a student")
    on_registerStudent_window_closed()
  

def login():
    global login_window
    if login_window is not None:
        login_window.lift()
        return
    
    global root
    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.geometry("700x600")
    login_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    #userID
    userIDLabel = Label(login_window, text="Enter your userID", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
    userIDEntry = Entry(login_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    userIDEntry.place(relx=0.5, rely=0.13, anchor=CENTER)

    #password
    passwordLabel = Label(login_window, text="Enter your password", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    passwordLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
    passwordEntry = Entry(login_window, width=50, show="*", bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    passwordEntry.place(relx=0.5, rely=0.23, anchor=CENTER)
    showPasswordVar = BooleanVar()
    showPasswordCheckbutton = Checkbutton(login_window, text="Show password", variable=showPasswordVar, command= lambda: showPassword(passwordEntry, showPasswordVar.get()), bg='#b3b3ff', fg='black', font=('Helvetica', 9), activebackground='#b3b3ff', activeforeground='black')
    showPasswordCheckbutton.place(relx=0.80, rely=0.23, anchor=W)
    
    #login button
    loginButton = Button(login_window, text="Login", command=lambda: loginButtonClicked(userIDEntry.get(), passwordEntry.get()), bg='#6666ff', font=('Helvetica', 12, 'bold'), width=15, activebackground='lightblue', fg='white')
    loginButton.place(relx=0.5, rely=0.3, anchor=CENTER)
    
    #go to register
    registerLabel = Label(login_window, text="Not registered yet?", bg='#b3b3ff', fg='black', font=('Helvetica', 12, 'bold'))
    registerLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
    registerButton = Button(login_window, text="Register", command=register, bg='#8080ff', font=('Helvetica', 12, 'bold'), width=15, activebackground='lightblue', fg='white')
    registerButton.place(relx=0.5, rely=0.75, anchor=CENTER)
    
    #go back to home window
    homepagebutton = Button(login_window, text = "Close", command= on_login_window_closed, bg='black', fg = 'white', font=('Helvetica', 12, 'bold'),activebackground='white', activeforeground='black')
    homepagebutton.place(relx=0.5, rely=0.9, anchor=CENTER)
    
def on_login_window_closed():
    global login_window
    login_window.destroy()
    login_window = None
    
def loginButtonClicked(userID, password):
    global login_window
    if userID == "" or password == "":
        messagebox.showerror("Error", "No input can be empty")
        on_login_window_closed()
        return
    if not checkUserID(userID):
        messagebox.showerror("Error", "Invalid userID\n Enter valid Email address")
        on_login_window_closed()
        return
    if not checkPassword(password):
        messagebox.showerror("Error", "Invalid password")
        on_login_window_closed()
        return
    try:
        with open("users.pk", "rb") as f:
            users = pk.load(f)
    except:
        users = {}
    if userID not in users:
        messagebox.showerror("Error", "This userID is not registered")
        return
    if users[userID].password != password:
        messagebox.showerror("Error", "Incorrect password")
        return
    
    #security check
    securityCheck(userID)
    on_login_window_closed()
    
    
def securityCheck(userID):
    global root
    global securityCheck_window
    securityCheck_window = Toplevel(root)
    securityCheck_window.title("Security Check")
    securityCheck_window.geometry("700x600")
    securityCheck_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    #userID
    userIDLabel = Label(securityCheck_window, text="Your userID is " + userID, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.grid(row=0, column=0)
    
    #security question
    with open("users.pk", "rb") as f:
        users = pk.load(f)
    securityQLabel = Label(securityCheck_window, text="Your security question is " + users[userID].securityQ, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    securityQLabel.grid(row=1, column=0, columnspan=2, sticky=W)
    
    #security answer
    securityALabel = Label(securityCheck_window, text="Enter your security answer", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    securityALabel.grid(row=2, column=0)
    securityAEntry = Entry(securityCheck_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    securityAEntry.grid(row=2, column=1, sticky=W)
    
    #submit button
    submitButton = Button(securityCheck_window, text="Submit", command=lambda: securityCheckButtonClicked(userID, securityAEntry.get()), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    submitButton.grid(row=3, column=0)
    
    #go back to login window
    homepagebutton = Button(securityCheck_window, text = "Close", command= securityCheck_window.destroy, bg='black', fg = 'white', activebackground='white', activeforeground='black')
    homepagebutton.grid(row=4, column=0)
    
def securityCheckButtonClicked(userID, securityA):
    global securityCheck_window
    if securityA == "":
        messagebox.showerror("Error", "No input can be empty")
        return
    with open("users.pk", "rb") as f:
        users = pk.load(f)
        
    if users[userID].securityA != securityA:
        users[userID].incorrectAttempts += 1
        if users[userID].incorrectAttempts >= 3:
            messagebox.showerror("Error", "You have been locked out")
            return
        with open("users.pk", "wb") as f:
            pk.dump(users, f)
        messagebox.showerror("Error", "Incorrect security answer")
        return
    securityCheck_window.destroy()
    securityCheck_window = None
    if users[userID].incorrectAttempts == 3:
        messagebox.showinfo("Error", "You have been locked out")
        return
    if isinstance(users[userID], teacher):
        with open("users.pk", "wb") as f:
            users[userID].incorrectAttempts = 0
            pk.dump(users, f)
        teacherProfile(userID)
        messagebox.showinfo("Success", "You have been logged in as a teacher")
    else:
        with open("users.pk", "wb") as f:
            users[userID].incorrectAttempts = 0
            pk.dump(users, f)
        studentProfile(userID)
        messagebox.showinfo("Success", "You have been logged in as a student")


studentProfile_window  = teacherProfile_window = editUGDetails_window = editPGDetails_window = editStudentDetails_window  = freeLockout_window = deregistration_window = None

def studentProfile(userID):
    #show all its details
    #edit details button, to edit pasword, micro, major, specialization
    #cannot edit cgpa, only teacher can edit/save cgpa
    global studentProfile_window
    if studentProfile_window is not None:
        studentProfile_window.lift()
        return
    
    global root
    studentProfile_window = Toplevel(root)
    studentProfile_window.title("Student Profile")
    studentProfile_window.geometry("700x600")
    studentProfile_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    #show stored details corresponding to userID
    #edit details button, to edit pasword, micro, major, specialization
    #cannot edit cgpa, only teacher can edit/save cgpa
    #check if some detail is None, if yes, show empty string
    
    with open("users.pk", "rb") as f:
        students = pk.load(f)
    student = students[userID]       
    
    #userID
    userIDLabel = Label(studentProfile_window, text="Your userID is " + student.userID, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.grid(row=0, column=0)
    
    #name
    nameLabel = Label(studentProfile_window, text="Name: " + student.name, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    nameLabel.grid(row=1, column=0, sticky=W)
    
    #password
    passwordLabel = Label(studentProfile_window, text="Your password is " + student.password, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    passwordLabel.grid(row=1, column=1, sticky=W)
    
    #year
    yearLabel = Label(studentProfile_window, text="Your enrollment year is " + str(student.year), bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    yearLabel.grid(row=2, column=0, sticky=W)
    
    #degree
    degreeLabel = Label(studentProfile_window, text="Your degree is " + student.degree, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    degreeLabel.grid(row=3, column=0, sticky=W)
    
    #department details
    departmentLabel = Label(studentProfile_window, text="Your department is " + student.department, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    departmentLabel.grid(row=4, column=0, sticky=W)
    
    #courses details may be None
    if student.courses is None:
        coursesLabel = Label(studentProfile_window, text="Your courses are ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    else:
        coursesLabel = Label(studentProfile_window, text="Your courses are: " + ", ".join(student.courses), bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    coursesLabel.grid(row=5, column=0, sticky=W)
        
    #cgpa details may be None
    if student.cgpa is None:
        cgpaLabel = Label(studentProfile_window, text="Your cgpa is ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    else:
        cgpaLabel = Label(studentProfile_window, text="Your cgpa is " + str(student.cgpa), bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    cgpaLabel.grid(row=6, column=0, sticky=W)
    
    
    if student.degree == "UG":
    #minorCourses details may be None
        if student.minorCourses is None or len(student.minorCourses) == 0:
            minorCoursesLabel = Label(studentProfile_window, text="Your minor courses are ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        else:
            minorCoursesLabel = Label(studentProfile_window, text="Your minor courses are: " + ", ".join(student.minorCourses), bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        minorCoursesLabel.grid(row=7, column=0, sticky=W)

        #majorCourses details may be None
        if student.majorCourses is None or len(student.majorCourses) == 0:
            majorCoursesLabel = Label(studentProfile_window, text="Your major courses are ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        else:
            majorCoursesLabel = Label(studentProfile_window, text="Your major courses are: " + ", ".join(student.majorCourses), bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        majorCoursesLabel.grid(row=8, column=0, sticky=W)
        
    else:
        #specialization details may be None
        if student.specialization is None:
            specializationLabel = Label(studentProfile_window, text="Your specialization is ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        else:
            specializationLabel = Label(studentProfile_window, text="Your specialization is " + student.specialization, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        specializationLabel.grid(row=7, column=0, sticky=W)
    
        
    #address details may be None
    if student.address is None:
        addressLabel = Label(studentProfile_window, text="Your address is ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    else:
        addressLabel = Label(studentProfile_window, text="Your address is " + student.address, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    addressLabel.grid(row=9, column=0, sticky=W)
    
    #phoneNo details may be None
    if student.phoneNo is None:
        phoneNoLabel = Label(studentProfile_window, text="Your phone number is ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    else:
        phoneNoLabel = Label(studentProfile_window, text="Your phone number is " + student.phoneNo, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    phoneNoLabel.grid(row=10, column=0, sticky=W)

    #edit details button
    editDetailsButton = Button(studentProfile_window, text="Edit Details", command=lambda: editUGDetails(userID), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    editDetailsButton.grid(row=11, column=0)
    
    #logout
    logoutButton = Button(studentProfile_window, text="Logout", command=on_studentProfile_window_closed, bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    logoutButton.grid(row=12, column=0)
    
    #deregistragtion 
    deregistrationButton = Button(studentProfile_window, text="Deregister", command=lambda: deregistration(userID), bg='#400080', width=15, activebackground='lightblue', fg='white')
    deregistrationButton.grid(row=12, column=1)
    
def on_studentProfile_window_closed():
    global studentProfile_window
    studentProfile_window.destroy()
    studentProfile_window = None
   
      
def editUGDetails(userID):
    #close studentProfile_window
    global studentProfile_window
    studentProfile_window.destroy()
    studentProfile_window = None
    
    #open editUGDetails_window
    global root
    global editUGDetails_window
    editUGDetails_window = Toplevel(root)
    editUGDetails_window.title("Edit UG Details")
    editUGDetails_window.geometry("700x600")
    editUGDetails_window.configure(bg='#b3b3ff', highlightthickness=4)

    #userID is not editable
    #show userID
    userIDLabel = Label(editUGDetails_window, text="Your userID is " + userID, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.grid (row=0, column=0)
    
    #password
    passwordLabel = Label(editUGDetails_window, text="Enter your new password", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    passwordLabel.grid(row=1, column=0)
    passwordEntry = Entry(editUGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    passwordEntry.grid(row=1, column=1)
    
    #courses
    coursesLabel = Label(editUGDetails_window, text="Select your courses", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    coursesLabel.grid(row=2, column=0)
    
    # List of courses
    courses = ["Course 1", "Course 2", "Course 3", "Course 4", "Course 5"]
    # Create the Listbox
    coursesListbox = Listbox(editUGDetails_window, selectmode=MULTIPLE, exportselection=0, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    coursesListbox.grid(row=3, column=0)
    # Add the courses to the Listbox
    for course in courses:
        coursesListbox.insert(END, course)

        
    #minorCourses
    minorCoursesLabel = Label(editUGDetails_window, text="Select your minor courses", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    minorCoursesLabel.grid(row=2, column=1)
    # List of minorCourses
    minorCourses = ["mCourse 1", "mCourse 2", "mCourse 3", "mCourse 4", "mCourse 5"]
    # Create the Listbox
    minorCoursesListbox = Listbox(editUGDetails_window, selectmode=MULTIPLE, exportselection=0, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    minorCoursesListbox.grid(row=3, column=1)
    # Add the minorCourses to the Listbox
    for minorCourse in minorCourses:
        minorCoursesListbox.insert(END, minorCourse)

    #majorCourses
    majorCoursesLabel = Label(editUGDetails_window, text="Select your major courses", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    majorCoursesLabel.grid(row=2, column=2)
    # List of majorCourses
    majorCourses = ["MCourse 1", "MCourse 2", "MCourse 3", "MCourse 4", "MCourse 5"]
    # Create the Listbox
    majorCoursesListbox = Listbox(editUGDetails_window, selectmode=MULTIPLE, exportselection=0, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    majorCoursesListbox.grid(row=3, column=2)
    # Add the minorCourses to the Listbox
    for majorCourse in majorCourses:
        majorCoursesListbox.insert(END, majorCourse)
        
        
    with open("users.pk", "rb") as f:
        students = pk.load(f)
    student = students[userID]
        
    if student.courses is not None:
        for i in range(len(courses)):
            if courses[i] in student.courses:
                coursesListbox.select_set(i)
    if student.minorCourses is not None:
        for i in range(len(minorCourses)):
            if minorCourses[i] in student.minorCourses:
                minorCoursesListbox.select_set(i)
    if student.majorCourses is not None:
        for i in range(len(majorCourses)):
            if majorCourses[i] in student.majorCourses:
                majorCoursesListbox.select_set(i)
                

    #address
    addressLabel = Label(editUGDetails_window, text="Enter your new address", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    addressLabel.grid(row=5, column=0)
    if student.address is None:
        addressEntry = Entry(editUGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    else:
        addressEntry = Entry(editUGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9), textvariable=student.address)
    addressEntry.grid(row=5, column=1)
    
    #phoneNo
    phoneNoLabel = Label(editUGDetails_window, text="Enter your new phone number", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    phoneNoLabel.grid(row=6, column=0)
    if student.phoneNo is None:
        phoneNoEntry = Entry(editUGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    else:
        phoneNoEntry = Entry(editUGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9), textvariable=student.phoneNo)
    phoneNoEntry.grid(row=6, column=1)
    
    #save button
    saveButton = Button(editUGDetails_window, text="Save", command=lambda: saveUGDetails(userID, passwordEntry.get(), coursesListbox.curselection(), minorCoursesListbox.curselection(), majorCoursesListbox.curselection(), addressEntry.get(), phoneNoEntry.get()), bg='#6666ff', width=15, activebackground='lightblue', fg='white')  
    saveButton.grid(row=7, column=0)
    
    #go back to student profile
    backToStudentProfileButton = Button(editUGDetails_window, text="Go back to profile", command = lambda: back_to_UGprofile(userID), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    backToStudentProfileButton.grid(row=8, column=0)
         
def saveUGDetails(userID, password, courses, minorCourses, majorCourses, address, phoneNo):
    if password !="" and (not checkPassword(password)):
        messagebox.showerror("Error", "Invalid password")
        return
    
    slected_courses_indices = courses
    selected_courses = ["Course " + str(i+1) for i in slected_courses_indices]
    
    selected_minor_indices = minorCourses
    selected_minorCourses = ["mCourse " + str(i+1) for i in selected_minor_indices]
    
    selected_major_indices = majorCourses
    selected_majorCourses = ["MCourse " + str(i+1) for i in selected_major_indices]


    try:
        with open("users.pk", "rb") as f:
            students = pk.load(f)
    except:
        students = {}
    student = students[userID]
    if password != "":
        student.password = password
    if courses != []:
        student.courses = selected_courses
    if minorCourses != []:
        student.minorCourses = selected_minorCourses
    if majorCourses != []:
        student.majorCourses = selected_majorCourses
    if address != "":
        student.address = address
    if phoneNo != "":
        student.phoneNo = phoneNo
    
    students[userID] = student
    with open("users.pk", "wb") as f:
        pk.dump(students, f)
    messagebox.showinfo("Success", "Your details have been saved")
    back_to_UGprofile(userID)
    
def back_to_UGprofile(userID):
    global editUGDetails_window
    editUGDetails_window.destroy()
    editUGDetails_window = None
    studentProfile(userID)


def editPGDetails(userID):
    
    #close studentProfile_window
    global studentProfile_window
    studentProfile_window.destroy()
    studentProfile_window = None
    
    #open editPGDetails_window
    global root
    global editPGDetails_window
    editPGDetails_window = Toplevel(root)
    editPGDetails_window.title("Edit PG Details")
    editPGDetails_window.geometry("700x600")
    editPGDetails_window.configure(bg='#b3b3ff', highlightthickness=4)

    #userID is not editable
    #show userID
    userIDLabel = Label(editPGDetails_window, text="Your userID is " + userID, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.grid (row=0, column=0)
    
    #password
    passwordLabel = Label(editPGDetails_window, text="Enter your new password", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    passwordLabel.grid(row=1, column=0)
    passwordEntry = Entry(editPGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    passwordEntry.grid(row=1, column=1)
    
    #courses
    coursesLabel = Label(editPGDetails_window, text="Select your courses", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    coursesLabel.grid(row=2, column=0)
    
    # List of courses
    courses = ["Course 1", "Course 2", "Course 3", "Course 4", "Course 5"]
    # Create the Listbox
    coursesListbox = Listbox(editPGDetails_window, selectmode=MULTIPLE, exportselection=0, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    coursesListbox.grid(row=3, column=0)
    # Add the courses to the Listbox
    for course in courses:
        coursesListbox.insert(END, course)

    #specialization
    specializationLabel = Label(editPGDetails_window, text="Enter your new specialization", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    specializationLabel.grid(row=4, column=0)
    specializationEntry = Entry(editPGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    specializationEntry.grid(row=4, column=1)
    

    with open("users.pk", "rb") as f:
        students = pk.load(f)
    student = students[userID]
    
    if student.courses is not None:
        for i in range(len(courses)):
            if courses[i] in student.courses:
                coursesListbox.select_set(i)
    if student.specialization is not None:
        specializationEntry.insert(0, student.specialization)
        
    
    #address
    addressLabel = Label(editPGDetails_window, text="Enter your new address", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    addressLabel.grid(row=5, column=0)
    if student.address is None:
        addressEntry = Entry(editPGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    else:
        addressEntry = Entry(editPGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9), textvariable=student.address)
    addressEntry.grid(row=5, column=1)
    
    
    #phoneNo
    phoneNoLabel = Label(editPGDetails_window, text="Enter your new phone number", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    phoneNoLabel.grid(row=6, column=0)
    if student.phoneNo is None:
        phoneNoEntry = Entry(editPGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    else:
        phoneNoEntry = Entry(editPGDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9), textvariable=student.phoneNo)
    phoneNoEntry.grid(row=6, column=1)
    
    
    #save button
    saveButton = Button(editPGDetails_window, text="Save", command=lambda: savePGDetails(userID, passwordEntry.get(), coursesListbox.curselection(), specializationEntry.get(), addressEntry.get(), phoneNoEntry.get()), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    saveButton.grid(row=7, column=0)
    
    #go back to student profile
    backToStudentProfileButton = Button(editPGDetails_window, text="Go back to profile", command = lambda: back_to_PGprofile(userID), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    backToStudentProfileButton.grid(row=8, column=0)
        
def savePGDetails(userID, password, courses, specialization, address, phoneNo):
    if password !="" and (not checkPassword(password)):
        messagebox.showerror("Error", "Invalid password")
        return
    
    slected_courses_indices = courses
    selected_courses = ["Course " + str(i+1) for i in slected_courses_indices]
    
    try:
        with open("users.pk", "rb") as f:
            students = pk.load(f)
    except:
        students = {}
    student = students[userID]
    if password != "":
        student.password = password
    if courses != []:
        student.courses = selected_courses
    if specialization != "":
        student.specialization = specialization
    if address != "":
        student.address = address
    if phoneNo != "":
        student.phoneNo = phoneNo
    
    
    students[userID] = student
    with open("users.pk", "wb") as f:
        pk.dump(students, f)
    messagebox.showinfo("Success", "Your details have been saved")
    back_to_PGprofile(userID)
      
def back_to_PGprofile(userID):
    global editPGDetails_window
    editPGDetails_window.destroy()
    editPGDetails_window = None
    studentProfile(userID)

    
def teacherProfile(userID):
    #show all its details
    #edit details button, to edit pasword, micro, major, specialization
    #cannot edit cgpa, only teacher can edit/save cgpa
    global teacherProfile_window
    if teacherProfile_window is not None:
        teacherProfile_window.lift()
        return
    
    global root
    teacherProfile_window = Toplevel(root)
    teacherProfile_window.title("Teacher Profile")
    teacherProfile_window.geometry("700x600")
    teacherProfile_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    #show stored details corresponding to userID
    #edit details button, to edit pasword, micro, major, specialization
    #cannot edit cgpa, only teacher can edit/save cgpa
    #check if some detail is None, if yes, show empty string
    
    with open("users.pk", "rb") as f:
        teachers = pk.load(f)
    teacher = teachers[userID]       
    
    #userID
    userIDLabel = Label(teacherProfile_window, text="Your userID is " + teacher.userID, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.grid(row=0, column=0)
    
    #name 
    nameLabel = Label(teacherProfile_window, text="Name: " + teacher.name, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    nameLabel.grid(row=1, column=0, sticky=W)
    
    #password
    passwordLabel = Label(teacherProfile_window, text="Your password is " + teacher.password, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    passwordLabel.grid(row=1, column=1, sticky=W)
    
    #department details
    departmentLabel = Label(teacherProfile_window, text="Your department is " + teacher.department, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    departmentLabel.grid(row=2, column=0, sticky=W)
    
    #courses details may be None
    if teacher.courses is None:
        coursesLabel = Label(teacherProfile_window, text="Your courses are ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    else:
        coursesLabel = Label(teacherProfile_window, text="Your courses are " + ", ".join(teacher.courses), bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    coursesLabel.grid(row=3, column=0, sticky=W)
        
    #officeAddress details may be None
    if teacher.officeAddress is None:
        officeAddressLabel = Label(teacherProfile_window, text="Your office address is ----", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    else:
        officeAddressLabel = Label(teacherProfile_window, text="Your office address is " + teacher.officeAddress, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    officeAddressLabel.grid(row=4, column=0, sticky=W)
    
    #edit details button
    editDetailsButton = Button(teacherProfile_window, text="Edit my Details", command=lambda: editTeacherDetails(userID), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    editDetailsButton.grid(row=5, column=0)
    
    #edit stugents details button
    editStudentDetailsButton = Button(teacherProfile_window, text="Edit students details", command= editStudentDetails, bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    editStudentDetailsButton.grid(row=5, column=1)
    
    #free lockout
    freeLockoutButton = Button(teacherProfile_window, text="Free lockout", command= freeLockout, bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    freeLockoutButton.grid(row=5, column=2)
    
    #logout
    logoutButton = Button(teacherProfile_window, text="Logout", command=on_teacherProfile_window_closed, bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    logoutButton.grid(row=7, column=0)
    
    #deregisration
    deregistrationButton = Button(teacherProfile_window, text="Deregister", command=lambda: deregistration(userID), bg='#400080', width=15, activebackground='lightblue', fg='white')
    deregistrationButton.grid(row=7, column=1)
    
    
def on_teacherProfile_window_closed():
    global teacherProfile_window
    teacherProfile_window.destroy()
    teacherProfile_window = None
    
def editTeacherDetails(userID):
        
        #close teacherProfile_window
        global teacherProfile_window
        teacherProfile_window.destroy()
        teacherProfile_window = None
        
        #open editTeacherDetails_window
        global root
        global editTeacherDetails_window
        editTeacherDetails_window = Toplevel(root)
        editTeacherDetails_window.title("Edit Teacher Details")
        editTeacherDetails_window.geometry("700x600")
        editTeacherDetails_window.configure(bg='#b3b3ff', highlightthickness=4)
    
        #userID is not editable
        #show userID
        userIDLabel = Label(editTeacherDetails_window, text="Your userID is " + userID, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        userIDLabel.grid (row=0, column=0)
        
        #password
        passwordLabel = Label(editTeacherDetails_window, text="Enter your new password", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        passwordLabel.grid(row=1, column=0)
        passwordEntry = Entry(editTeacherDetails_window, width=50, borderwidth=5, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
        passwordEntry.grid(row=1, column=1)
        
        with open("users.pk", "rb") as f:
            teachers = pk.load(f)
        teacher = teachers[userID]
        
        #courses
        coursesLabel = Label(editTeacherDetails_window, text="Select your courses", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        coursesLabel.grid(row=2, column=0)
        
        # List of courses
        courses = ["Course 1", "Course 2", "Course 3", "Course 4", "Course 5"]
        # Create the Listbox
        coursesListbox = Listbox(editTeacherDetails_window, selectmode=MULTIPLE, exportselection=0, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
        coursesListbox.grid(row=3, column=0)
        # Add the courses to the Listbox
        for course in courses:
            coursesListbox.insert(END, course)
    
        if teacher.courses is not None:
            for i in range(len(courses)):
                if courses[i] in teacher.courses:
                    coursesListbox.select_set(i)
                    
    
        #officeAddress
        officeAddressLabel = Label(editTeacherDetails_window, text="Enter your new office address", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
        officeAddressLabel.grid(row=4, column=0)
        if teacher.officeAddress is None:
            officeAddressEntry = Entry(editTeacherDetails_window, width=50, borderwidth=5, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
        else:
            officeAddressEntry = Entry(editTeacherDetails_window, width=50, borderwidth=5, bg='#e6e6ff', fg='black', font=('Helvetica', 9), textvariable=teacher.officeAddress)
        officeAddressEntry.grid(row=4, column=1)
        
        #save button
        saveButton = Button(editTeacherDetails_window, text="Save", command=lambda: saveTeacherDetails(userID, passwordEntry.get(), coursesListbox.curselection(), officeAddressEntry.get()), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
        saveButton.grid(row=5, column=0)
        
        #go back to teacher profile
        backToTeacherProfileButton = Button(editTeacherDetails_window, text="Go back to profile", command = lambda: back_to_Teacherprofile(userID), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
        backToTeacherProfileButton.grid(row=6, column=0)
        
def saveTeacherDetails(userID, password, courses, officeAddress):
    if password !="" and (not checkPassword(password)):
        messagebox.showerror("Error", "Invalid password")
        return
    
    slected_courses_indices = courses
    selected_courses = ["Course " + str(i+1) for i in slected_courses_indices]
    
    try:
        with open("users.pk", "rb") as f:
            teachers = pk.load(f)
    except:
        teachers = {}
    teacher = teachers[userID]
    if password != "":
        teacher.password = password
    if courses != []:
        teacher.courses = selected_courses
    if officeAddress != "":
        teacher.officeAddress = officeAddress
    
    teachers[userID] = teacher
    with open("users.pk", "wb") as f:
        pk.dump(teachers, f)
    messagebox.showinfo("Success", "Your details have been saved")
    back_to_Teacherprofile(userID)
    
def back_to_Teacherprofile(userID):
    global editTeacherDetails_window
    editTeacherDetails_window.destroy()
    editTeacherDetails_window = None
    teacherProfile(userID)

def editStudentDetails():
    #give a list of all students
    #select a student
    #techer can edit the cgpa of that student
    
    global editStudentDetails_window
    if editStudentDetails_window is not None:
        editStudentDetails_window.lift()
        return
    
    global root
    editStudentDetails_window = Toplevel(root)
    editStudentDetails_window.title("Edit Student Details")
    editStudentDetails_window.geometry("700x600")
    editStudentDetails_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    #give a list of all students
    #select a student
    #techer can edit the cgpa of that student
    
    # List of students
    with open("users.pk", "rb") as f:
        allUsers = pk.load(f)
        
    #out of all users, if its is a UGs, PGs, then add it to the list of students
    students = []
    for user in allUsers:
        if isinstance(allUsers[user], UGs) or isinstance(allUsers[user], PGs):
            students.append(user)
            
    if len(students) == 0:
        messagebox.showerror("Error", "There are no students registered")
        editStudentDetails_window.destroy()
        return
            
    # Variable to store the selected student
    selected_student = StringVar(editStudentDetails_window)
    selected_student.set(students[0])  # Set the default value to the first student
    
    # Create the dropdown menu
    studentMenu = OptionMenu(editStudentDetails_window, selected_student, *students)
    studentMenu.configure(bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    studentMenu.place(relx=0.5, rely=0.25, anchor=CENTER)
    
    #cgpa
    cgpaLabel = Label(editStudentDetails_window, text="Enter the new cgpa", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    cgpaLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
    if allUsers[selected_student.get()].cgpa is None:
        cgpaEntry = Entry(editStudentDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    else:
        cgpaEntry = Entry(editStudentDetails_window, width=50, bg='#e6e6ff', fg='black', font=('Helvetica', 9), textvariable=allUsers[selected_student.get()].cgpa)
    cgpaEntry.place(relx=0.5, rely=0.55, anchor=CENTER)
    
    
    #save button
    saveButton = Button(editStudentDetails_window, text="Save", command=lambda: saveStudentDetails(selected_student.get(), cgpaEntry.get()), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    saveButton.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    #go back to teacher profile
    backToTeacherProfileButton = Button(editStudentDetails_window, text="Close", command = editStudentDetails_window.destroy, bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    backToTeacherProfileButton.place(relx=0.5, rely=0.9, anchor=CENTER)
    
def saveStudentDetails(userID, cgpa):
    if cgpa !="" and (not checkCGPA(cgpa)):
        messagebox.showerror("Error", "Invalid cgpa")
        return
    
    try:
        with open("users.pk", "rb") as f:
            students = pk.load(f)
    except:
        students = {}
    student = students[userID]
    if cgpa != "":
        student.cgpa = cgpa
    
    students[userID] = student
    with open("users.pk", "wb") as f:
        pk.dump(students, f)
    messagebox.showinfo("Success", "Student's cgpa has been updated")
    editStudentDetails_window.destroy()
    
def checkCGPA(cgpa):
    try:
        cgpa = float(cgpa)
    except:
        return False
    if cgpa < 0 or cgpa > 10:
        return False
    return True
    
def freeLockout():
    #dropdown list of users, select it and free
    global freeLockout_window
    
    if freeLockout_window is not None:
        freeLockout_window.lift()
        return
    
    global root
    freeLockout_window = Toplevel(root)
    freeLockout_window.title("Free Lockout")
    freeLockout_window.geometry("700x600")
    freeLockout_window.configure(bg='#b3b3ff', highlightthickness=4)

    
    # List of students
    with open("users.pk", "rb") as f:
        allUsers = pk.load(f)
            
    #make list of all users
    users = []
    for user in allUsers:
        users.append(user)
        
            
    if len(users) == 0:
        messagebox.showerror("Error", "There are no users registered")
        freeLockout_window.destroy()
        return
            
    # Variable to store the selected student
    selected_user = StringVar(freeLockout_window)
    selected_user.set(user[0])  # Set the default value to the first student
    
    # Create the dropdown menu
    usersMenu = OptionMenu(freeLockout_window, selected_user, *users)
    usersMenu.configure(bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    usersMenu.place(relx=0.5, rely=0.25, anchor=CENTER)
    
    #free button
    freeButton = Button(freeLockout_window, text="Free", command=lambda: freeButtonClicked(selected_user.get()), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    freeButton.place(relx=0.5, rely=0.55, anchor=CENTER)
    
    #go back to teacher profile
    backToTeacherProfileButton = Button(freeLockout_window, text="Close", command = freeLockout_window.destroy, bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    backToTeacherProfileButton.place(relx=0.5, rely=0.9, anchor=CENTER)
    
def freeButtonClicked(userID):
    try:
        with open("users.pk", "rb") as f:
            users = pk.load(f)
    except:
        users = {}
    users[userID].incorrectAttempts = 0
    with open("users.pk", "wb") as f:
        pk.dump(users, f)
    messagebox.showinfo("Success", "User has been freed")
    freeLockout_window.destroy()
    
def deregistration(userID):
    global deregistration_window
    if deregistration_window is not None:
        deregistration_window.lift()
        return
    
    global root
    deregistration_window = Toplevel(root)
    deregistration_window.title("Deregistration")
    deregistration_window.geometry("700x600")
    deregistration_window.configure(bg='#b3b3ff', highlightthickness=4)
    
    #userID
    userIDLabel = Label(deregistration_window, text="Your userID is " + userID, bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    userIDLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    #password
    passwordLabel = Label(deregistration_window, text="Enter your password", bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    passwordLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
    passwordEntry = Entry(deregistration_window, width=50, borderwidth=5, show="*", bg='#e6e6ff', fg='black', font=('Helvetica', 9))
    passwordEntry.place(relx=0.5, rely=0.25, anchor=CENTER)
    showPasswordVar = BooleanVar()
    showPasswordCheckbutton = Checkbutton(deregistration_window, text="Show password", variable=showPasswordVar, command= lambda: showPassword(passwordEntry, showPasswordVar.get()), bg='#b3b3ff', fg='black', font=('Helvetica', 9))
    showPasswordCheckbutton.place(relx=0.75, rely=0.25, anchor=W)
    
    #deregister button
    deregisterButton = Button(deregistration_window, text="Deregister", command=lambda: deregisterButtonClicked(userID, passwordEntry.get()), bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    deregisterButton.place(relx=0.5, rely=0.3, anchor=CENTER)
    
    #go back to student profile
    backToStudentProfileButton = Button(deregistration_window, text="Close", command = deregistration_window.destroy, bg='#6666ff', width=15, activebackground='lightblue', fg='white')
    backToStudentProfileButton.place(relx=0.5, rely=0.9, anchor=CENTER)
    
def deregisterButtonClicked(userID, password):
    if password == "":
        messagebox.showerror("Error", "No input can be empty")
        return
    if not checkPassword(password):
        messagebox.showerror("Error", "Invalid password")
        return
    try:
        with open("users.pk", "rb") as f:
            users = pk.load(f)
    except:
        users = {}
    if userID not in users:
        messagebox.showerror("Error", "This userID is not registered")
        return
    if users[userID].password != password:
        messagebox.showerror("Error", "Incorrect password")
        return
    
    if isinstance(users[userID], teacher):
        teacherProfile_window.destroy()
    else:
        studentProfile_window.destroy()
    users.pop(userID)
    with open("users.pk", "wb") as f:
        pk.dump(users, f)
    messagebox.showinfo("Success", "You have been deregistered")
    deregistration_window.destroy()
    

home()