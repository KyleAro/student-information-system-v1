import os
from Student_Info import Student_info

def clear_screen():  # Clear screen function for pizazz
    os.system('cls')

def add_student_detail(prompt, setter_method, student):
    """Helper function to streamline input and setter calls."""
    print("========================")
    print("===== ADD STUDENT =====")
    print("========================\n")
    detail = input(prompt)
    setter_method(detail)  # Call the appropriate setter method
    clear_screen()
def Add_student(student):
    student_list = student.allstudents

    # Collect student details without asking for the role
    add_student_detail("Enter first name: ", student.setFName, student)
    add_student_detail("Enter last name: ", student.setLName, student)
    add_student_detail("Enter age: ", student.setAge, student)
    add_student_detail("Enter ID number: ", student.setIDNum, student)
    add_student_detail("Enter email: ", student.setEmail, student)
    add_student_detail("Enter phone number: ", student.setPhone, student)
    
    # After gathering all the information, add the student
    student.plus_student()
    print(f"\nStudent {student.getFName()} {student.getLName()} has been added to the list and saved in the students.txt.\n")
