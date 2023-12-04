class Test:
    staticVariable = 0
    instanceVariable = 0

    def __init__(self):
        self.instanceVariable += 1
        Test.staticVariable += 1

t1 = Test()
print("instance variable t1: ", t1.instanceVariable)
print("static variable t1:", t1.staticVariable)

t2 = Test()
print("instance variable t1: ", t2.instanceVariable)
print("static variable t1:", t2.staticVariable)

print ("static variable from class: ", Test.staticVariable)

print("static variable from t1 after t2 is created: ", t1.staticVariable)


