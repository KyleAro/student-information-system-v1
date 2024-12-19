import os

class Student_info:
    def __init__(self):
        self.allstudents = []
    
    # Setters
    def setFName(self, fname):
        self.fname = fname

    def setLName(self, lname):
        self.lname = lname

    def setAge(self, age):
        self.age = age

    def setIDNum(self, idnum):
        self.idnum = idnum

    def setEmail(self, email):
        self.email = email

    def setPhone(self, phone):
        self.phone = phone

    # Getters
    def getFName(self):
        return self.fname

    def getLName(self):
        return self.lname

    def getAge(self):
        return self.age

    def getIDNum(self):
        return self.idnum

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def verify_id(self, student_id):
        # Check if the student ID exists in the allstudents list
        for student in self.allstudents:
            if student[3] == str(student_id):  # student[3] is where the student ID is stored
                return student  
        return None
    def plus_student(self):
        self.allstudents.append([self.fname, self.lname, self.age, self.idnum, self.email, self.phone])

        # Write the new student to the file
        with open("students.txt", "a") as file:
            file.write(f"{self.fname},{self.lname},{self.age},{self.idnum},{self.email},{self.phone}\n")

    def load_students_from_file(self):
        #Load student data from students.txt into the allstudents list.
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as file:
                for line in file:
                    line = line.strip()  # Remove any extra whitespace or newlines
                    if line:  # Make sure the line is not empty
                        parts = line.split(",")  # Split the line into individual student details
                        if len(parts) == 6:  # Ensure that there are exactly 6 parts (fname, lname, age, id, email, phone)
                            self.allstudents.append([parts[0], parts[1], int(parts[2]), parts[3], parts[4], parts[5]])
        else:
            print("students.txt file not found.")
    def __str__(self):
        if not self.allstudents:
            return "No students in the list."
        return "\n".join([f"===============================================================================================================\nName: {s[0]} {s[1]}, Age: {s[2]}, ID: {s[3]}, Email: {s[4]}, Phone: {s[5]}\n===============================================================================================================\n" for s in self.allstudents])
