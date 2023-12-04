class Employee:

    def __init__(self, empno, name, salary, dept):
        self.Empno = empno
        self.Name = name
        self.Salary = salary
        self.Dept = dept


    def showEmployee(self):
        print("Empno: {}\nName: {}\nSalary: {}\nDept: {}\n".format(self.Empno, self.Name, self.Salary, self.Dept))


class SalesMan (Employee):
    def __init__(self, empno, name, salary, dept, comm):
        self.commission = comm
        super().__init__(empno, name, salary, dept)


sm1 = SalesMan(101, 'Ajith', 100000, 'ABC', 100)
sm1.showEmployee()
print("Commission: ", sm1.commission )
