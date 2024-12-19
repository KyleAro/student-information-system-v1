from Student_Info import Student_info

class StudentIDSearcher:
    def __init__(self, student_info):  # Accepts a Student_info object
        self.student_info = student_info  # Use the provided Student_info object
        student_info = Student_info()

    def get_student_id(self):
        print("==========================")
        print(" STUDENT SEARCHER SECTION ")
        print("==========================\n")

        search_query = input("Enter Student ID: ").strip()

        for s in self.student_info.allstudents:
            if search_query == s[3]:  # Assuming s[3] is the student ID
                print("=========================================")
                print(f"======= {s[0]} Information Table =======")
                print("=========================================")
                print(f"Name:  {s[0]} {s[1]}")
                print(f"Age:   {s[2]}")
                print(f"ID:    {s[3]}")
                print(f"Email: {s[4]}")
                print(f"Phone: {s[5]}")
                print("=========================================")
                break
        else:
            print("STUDENT NOT FOUND. TRY AGAIN!")
