class Student:
    def __init__(self,name,roll_number,cgpa):
        self.name=name
        self.roll_number=roll_number
        self.cgpa=cgpa

def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    return sorted_students
students=[
    Student("guru","2k22431",7.1),
    Student("jeyakrishnan","2k22415",8.9),
    Student("abi","2k22401",9.1),
    Student("sanjay","2k22460",9.8)
    ]
sorted_students=sort_students(students)
for student in sorted_students:
    print("Name:{}. Roll Number:{}. CGPA:{}".format(student.name,student.roll_number,student.cgpa))
    

        
