class Grandparents:
    def PropertyLand(self):
        print('Land for farming from GPs')

class Parents (Grandparents):
    def PropertyHome(self):
        print('Home from parents')

class Child (Parents):
    def PropertyCar(self):
        super().PropertyLand()
        super().PropertyHome()
        print('Car bought by me')

    def PropertyLand(self): #method overriding
        print('Land for farming from GPs, But I will use for construction')

c1 = Child()
c1.PropertyCar()
c1.PropertyLand()
