class Name:
    def __init__(self, firstName, middleName, lastName):
        self.FirstName = firstName
        self.MiddleName = middleName
        self.LastName = lastName

class Student:
    def __init__(self, rollNo, sName, course):
        self.RollNo = rollNo
        self.StudentName = sName
        self.Course = course

student1 = Student('101', Name('Ajith','K','Devadas'), 'OOP with Python')
student2 = Student('102', Name('Seema','M','Archana'), 'OOP with Python')
student3 = Student('103', Name('Anay','A','Ajith'), 'OOP with Python')

students = [student1, student2, student3]

for student in students:
    print("Roll Number : {}\nStudentName : {} {} {}\nCourse Enrolled: {}\n".format(student.RollNo,
                                                                                   student.StudentName.FirstName, student.StudentName.MiddleName,
                                                                                   student.StudentName.LastName, student.Course))