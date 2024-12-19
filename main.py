import os
from Student_Info import Student_info
from add_student import Add_student
from search_student import StudentIDSearcher as searchstud

# Clear screen function (for CLI, but not necessary for GUI)
def clear_screen():
    os.system('cls')

# Function to verify student by ID
def verify_id(student):
    attempts = 0
    max_attempts = 3

    # Load student data from file before verifying ID
    student.load_students_from_file()

    while attempts < max_attempts:
        user_id = input("Enter your ID: ")

        # Check if the entered ID exists in the loaded list of students
        for s in student.allstudents:
            if s[3] == user_id:  # Compare user ID with the ID in the list
                clear_screen()
                print("================================")
                print(f"    Welcome, {s[0]} {s[1]}!")
                print("================================\n")
                return s  # Return the student data that matched the ID
            
        attempts += 1
        print(f"Access denied. ID not found. You have {max_attempts - attempts} attempt(s) left.")

    print("Maximum attempts reached. Please try again later.")
    clear_screen()
    return verify_id(student)  # Recursively call again after max attempts

def main():
    student = Student_info() 
    student.allstudents.append(("Student","Default","23","1234","Email User","Phone User"))
    student.allstudents.append(("Admin","Default","23","12345","Email User","Phone User"))

    while True:
        student_logged_in = verify_id(student)  # will put the verify id to student id variable
        print("_______________________________________________________\n\nWelcome to Student Portal Access!\n\n1. View your Student Information\n2. Search for other Student Info\n3. Add New Student\n4. View All Students\n5. Exit\n_______________________________________________________ ")
                     

        choice = input("\n\n\nEnter the Task you want to Do (1-5): ")

        #View your student info
        if choice == "1":
                clear_screen()
                print("================================")
                print("======= Your Information =======")
                print("================================")
                print(f"Name:  {student_logged_in[0]} {student_logged_in[1]}")
                print(f"Age:   {student_logged_in[2]}")
                print(f"ID:    {student_logged_in[3]}")
                print(f"Email: {student_logged_in[4]}")
                print(f"Phone: {student_logged_in[5]}")
                print("================================")
                 # To clear screen for pizazz.
        #Search for student 
        elif choice == "2":
            clear_screen()  # To clear screen for pizazz.
            search_pls = searchstud(student)
            search_pls.get_student_id()
            
        #ADD STUDENT
        elif choice == "3":
            clear_screen()  # To clear screen for pizazz.
            Add_student(student) 
 
        #Will View All students in the list
        elif choice == "4":
            clear_screen()  # To clear screen for pizazz.
            print(student)  # Print the list of all students

        elif choice == "5":
            clear_screen()  # To clear screen for pizazz.
            print("================================\nThanks for using our system\n================================")
            exit() 
        
        else:
            clear_screen()
            print("================================\nThat is Not an Option Try Again.\n================================\n\n")
            continue

        # Ask if the user wants to do another query
        
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=-=-")
        choice1 = input("Do you want to do another task (Yes / No)? ").lower()   
      
        if choice1 == "yes":
            clear_screen()
        else:
            clear_screen()  # To clear screen for pizazz.
            print("================================\nThanks for using our system\n================================")
            exit()   

