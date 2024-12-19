from tkinter import *
from tkinter import messagebox
from functools import partial
from main import *
from Student_Info import *  # Import the Student_info class
from search_student import * # Import the search_student class



# Initialize Tkinter window
win = Tk()
student_logged_in = None
# Create an instance of Student_info
student = Student_info()

# Load students from file when GUI starts
student.load_students_from_file()

# Function Definitions
def viewinfo(content_contain):
    """ Clear and show student information. """
    for widget in content_contain.winfo_children():
        widget.destroy()  # Remove any previous widgets in content_contain

    # Display the student's information
    Label(content_contain, text="=================\nYour Information\n=================\n", font=("Century Gothic", 20), bg="#2CA6A4").pack(pady=20)

    if student_logged_in:
        details = [
            f"Name:  {student_logged_in[0]} {student_logged_in[1]}",
            f"Age:   {student_logged_in[2]}",
            f"ID:    {student_logged_in[3]}",
            f"Email: {student_logged_in[4]}",
            f"Phone: {student_logged_in[5]}",
        ]
        
        for detail in details:
            # Create a frame to make each detail section stand out with borders
            detail_frame = Frame(content_contain, bg="#FFFFFF", padx=10, pady=10, relief="solid", borderwidth=2)
            detail_frame.pack(pady=5, fill="x", padx=20)  # Added padding and fill for better spacing
            
            # Add the detail label inside the frame with custom font and color
            Label(detail_frame, text=detail, font=("Century Gothic", 16), bg="#FFFFFF", fg="#333333", anchor="w").pack()
    else:
        messagebox.showerror("Error", "No student information available!")


def search_stud(content_contain):
    """ Search student by ID and recreate the search GUI each time. """
    # Create the search section only once (do not recreate every time)
    for widget in content_contain.winfo_children():
        widget.destroy()  # Clear the frame first

    # Create the search header
    Label(content_contain, text="====================\nSearch Student\n====================", font=("Century Gothic", 20), bg="#2CA6A4", fg="white").pack(pady=20)

    # Add the student ID input label and entry field
    Label(content_contain, text="Enter Student ID:", font=("Century Gothic", 16), bg="#2CA6A4", fg="white").pack(pady=10)
    student_id_entry = Entry(content_contain, font=("Century Gothic", 16))
    student_id_entry.pack(pady=10)

    # Function to search and display student details
    def search_and_display():
        student_id = student_id_entry.get().strip()  # Get the student ID entered by the user
        student_found = None

        # Loop through all students to find the matching ID
        for s in student.allstudents:
            if student_id == s[3]:  # Assuming s[3] is the student ID
                student_found = s
                break

        # Clear the previous result frames before displaying new results
        for widget in content_contain.winfo_children():
            if isinstance(widget, Frame):  # Only clear the frames (previous student details)
                widget.destroy()

        # If student found, display their information
        if student_found:
            details = [
                f"Name:  {student_found[0]} {student_found[1]}",
                f"Age:   {student_found[2]}",
                f"ID:    {student_found[3]}",
                f"Email: {student_found[4]}",
                f"Phone: {student_found[5]}",
            ]
            
            # Create the same styled frame for displaying the student details
            for detail in details:
                detail_frame = Frame(content_contain, bg="#FFFFFF", padx=10, pady=10, relief="solid", borderwidth=2)
                detail_frame.pack(pady=5, fill="x", padx=20)  # Added padding and fill for better spacing
                
                # Add the detail label inside the frame with custom font and color
                Label(detail_frame, text=detail, font=("Century Gothic", 16), bg="#FFFFFF", fg="#333333", anchor="w").pack()

        else:
            # If student not found, show an error message
            messagebox.showerror("Student Not Found", "No student found with this ID!")

    # Add the search button to the GUI
    search_button = Button(content_contain, text="Search", font=("Century Gothic", 16), command=search_and_display)
    search_button.pack(pady=20)


def addstud():
    # Clear the content_contain frame first
    for widget in content_contain.winfo_children():
        widget.destroy()

    # Create a form for adding student details
    Label(content_contain, text="====================\nAdd New Student\n====================", 
          font=("Century Gothic", 20), bg="#2CA6A4", fg="white").pack(pady=10)

    # Fields and their respective error labels
    fields = ["First Name", "Last Name", "Age", "ID", "Email", "Phone"]
    entries = {}
    error_labels = {}

    # Create entry widgets dynamically for each field
    for field in fields:
        Label(content_contain, text=field, font=("Century Gothic", 16), bg="#2CA6A4", fg="white").pack(pady=5)
        entry = Entry(content_contain, font=("Century Gothic", 14))
        entry.pack(pady=3)

        # Error label (hidden initially)
        error_label = Label(content_contain, text="", font=("Century Gothic", 12), fg="red", bg="#2CA6A4")
        error_label.pack(pady=2)

        entries[field] = entry
        error_labels[field] = error_label

    # Function to handle form submission
    def submit_student():
    # Clear all previous error messages
        for label in error_labels.values():
            label.config(text="")

        # Collect data from fields and validate
        data = {field: entry.get().strip() for field, entry in entries.items()}
        valid = True  # To check if all validations pass

        # Validation checks
        for field, value in data.items():
            if not value:  # Empty field
                error_labels[field].config(text=f"{field} is required!")
                valid = False

        if not valid:
            return  # Stop submission if there are errors

        # Set the student attributes
        student.setFName(data["First Name"])
        student.setLName(data["Last Name"])
        student.setAge(data["Age"])
        student.setIDNum(data["ID"])
        student.setEmail(data["Email"])
        student.setPhone(data["Phone"])

        # Add the student and save
        student.plus_student()

        # Show success message
        messagebox.showinfo("Success", f"Student {data['First Name']} {data['Last Name']} added successfully!")

        # Clear the textboxes after showing the success message
        for entry in entries.values():
            entry.delete(1, Tk.END)  # Clear each text field

    submit_button = Button(content_contain, text="Add Student", font=("Century Gothic", 14), command=submit_student)
    submit_button.pack(pady=15)


def viewall(content_contain):
    # Clear the content_contain frame first
    for widget in content_contain.winfo_children():
        widget.destroy()

    # Create a Canvas widget to hold all the content
    canvas = Canvas(content_contain, bg="#2CA6A4")  # Set background color of the canvas
    canvas.pack(side="left", fill="both", expand=True)

    # Create a Scrollbar and link it to the canvas
    scrollbar = Scrollbar(content_contain, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas to hold all student information
    frame = Frame(canvas, bg="#2CA6A4")  # Set background color of the frame to match the canvas
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Display a label indicating that we are viewing all students
    Label(frame, text="====================\nAll Students\n====================", font=("Century Gothic", 20), bg="#2CA6A4", fg="white").pack(pady=20)

    if student.allstudents:
        for student_info in student.allstudents:
            details = [
                ("Name", f"{student_info[0]} {student_info[1]}"),
                ("Age", f"{student_info[2]}"),
                ("ID", f"{student_info[3]}"),
                ("Email", f"{student_info[4]}"),
                ("Phone", f"{student_info[5]}"),
            ]

            # Create a frame for each student's details (styled box)
            student_frame = Frame(frame, bg="#FFFFFF", padx=20, pady=10, relief="solid", borderwidth=2)
            student_frame.pack(pady=10, fill="x", padx=200)  # Added padding and fill for better spacing

            # Create a grid layout to neatly align the fields in rows and columns
            for idx, (label, value) in enumerate(details):
                # Label for the field name (e.g., "Name", "Age", etc.)
                label_widget = Label(student_frame, text=label, font=("Century Gothic", 14, "bold"), bg="#FFFFFF", fg="#333333", anchor="w")
                label_widget.grid(row=idx, column=0, sticky="w", padx=10, pady=5)

                # Value for the field (e.g., "John Doe", "25", etc.)
                value_widget = Label(student_frame, text=value, font=("Century Gothic", 14), bg="#FFFFFF", fg="#333333", anchor="w")
                value_widget.grid(row=idx, column=1, sticky="w", padx=10, pady=5)

            # Add a separator between students
            Label(frame, text="=============================", font=("Century Gothic", 16), bg="#2CA6A4", fg="white").pack(pady=10)

        # Update the scroll region to include all the content
        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    else:
        messagebox.showinfo("No Students", "There are no students in the system.")
def logout():
    """ Clear the current window and go back to the login page. """
    for widget in win.winfo_children():
        widget.destroy()  # Destroy all current widgets
    create_login_frame()  # Recreate the login page

def clear_and_create_new_frame():
    """ Clear and create the new GUI screen. """
    for widget in win.winfo_children():
        widget.destroy()
    create_new_gui()  # Call function to create the new GUI screen

def create_login_frame():
    """ Create the login page for the application. """
    menu_contain = Frame(win, bg="#31263E")
    menu_contain.pack(side="left", fill="y", anchor="nw")

    welcome_label = Label(menu_contain,text="Welcome!",font=("Bookman Old Style", 40),bg="#31263E",fg="white",padx=20,width=15,anchor="w")
    welcome_label.grid(row=1, column=0, sticky="w")
    Label(menu_contain, text="", pady=120, bg="#31263E").grid(row=0, column=0, sticky='w')
    Label(menu_contain, text="        Student", font=("Bookman Old Style", 40), padx=20, width=15, bg="#31263E", fg="white", anchor="w").grid(row=2, column=0, sticky='w')
    Label(menu_contain, text="        Information", font=("Bookman Old Style", 40), padx=20, width=15, bg="#31263E", fg="white", anchor="w").grid(row=3, column=0, sticky='w')
    Label(menu_contain, text="        System", font=("Bookman Old Style", 40), padx=20, width=15, bg="#31263E", fg="white", anchor="w").grid(row=4, column=0, sticky='w')

    def update_label():
        texts = ["        Welcome!", "        Willkommen!", "        Bienvenue!", "        환영합니다!"]
        welcome_label.config(text=texts[update_label.counter % len(texts)])
        update_label.counter += 1
        win.after(1000, update_label)

    update_label.counter = 0
    update_label()

    log_contain = Frame(win, bg="#2CA6A4")
    log_contain.pack(side="left", fill="both", expand=True)

    log_label = Label(log_contain, text="Log-In", font=("Bookman Old Style", 30), bg="#2CA6A4")
    log_label.place(relx=0.1, rely=0.3, anchor="center")

    global txtbox1
    txtbox1 = Entry(log_contain, width=15, font=("Bookman Old Style", 20), relief="flat")
    txtbox1_title = Label(log_contain, text="  Student ID:", bg="#2CA6A4", font=("Bookman Old Style", 20))

    txtbox1_title.place(relx=0.1, rely=0.5, anchor="w")
    txtbox1.place(relx=0.4, rely=0.5, anchor="w")

    login_button = Button(
        log_contain, width=5, height=1, text="Login", font=("Bookman Old Style", 20), cursor="hand2", command=login_button_func)
    login_button.place(relx=0.4, rely=0.6, anchor="w")

def create_new_gui():
    """ Create the main interface for logged-in users. """
    new_frame = Frame(win, bg="#4A4063")
    new_frame.pack(fill="both", expand=True)

    menu_contain = Frame(new_frame, borderwidth=1, bg="#31263E", relief="sunken")
    menu_contain.pack(side="right", fill="y")

    global content_contain
    content_contain = Frame(new_frame, borderwidth=1, bg="#2CA6A4")
    content_contain.pack(side="left", fill="both", expand=True)

    Label(menu_contain, text="Main Menu", font=("Century Gothic", 20), fg="white", bg="#31263E", padx=20).grid(row=0, column=0, pady=10)

    btn_txt = ["View Your Student Info", "Search Student", "Add Student", "View All Students", "Logout"]
    btn_funcs = [
        partial(viewinfo, content_contain),
        partial(search_stud, content_contain),  # Pass content_contain to search_stud
        addstud,
        partial(viewall, content_contain),
        logout
    ]

    for i, txt in enumerate(btn_txt):
        btn = Button(menu_contain, text=txt, width=40, font=("Century Gothic", 14), padx=10, pady=15, relief="flat", command=btn_funcs[i])
        btn.grid(row=i + 1, column=0, pady=5)

def login_button_func():
    """ Handle the login process by verifying the student ID. """
    student_id = txtbox1.get()

    student_found = student.verify_id(student_id)

    if student_found:
        global student_logged_in
        student_logged_in = student_found
        messagebox.showinfo("Login Successful", f"Welcome, {student_found[0]}!")
        clear_and_create_new_frame()
    else:
        messagebox.showerror("Login Failed", "Invalid Student ID!")

# Tkinter Window Setup
win.configure(bg="#4A4063")
win.title("Student Information System")
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")
win.resizable(False, False)

# Initialize the login page on application start
create_login_frame()

# Start the Tkinter main loop
win.mainloop()
