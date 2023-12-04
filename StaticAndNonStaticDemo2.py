class Employee:
    TotalEmployees = 0
    def __init__(self, empno, name, salary, dept):
        self.Empno = empno
        self.Name = name
        self.Salary = salary
        self.Dept = dept
        Employee.TotalEmployees += 1

    def showEmployee(self):
        print("Empno: {}\nName: {}\nSalary: {}\nDept: {}\nTotal Employees: {}\n".format(self.Empno, self.Name, self.Salary, self.Dept, self.TotalEmployees))



emp1 = Employee(101, 'Ajith', 100000, 'ABC')
emp2 = Employee(102, 'Anay', 200000, 'DEF')

emp1.showEmployee()
emp2.showEmployee()


