from abc import ABC, abstractmethod

class Institute(ABC):
    def __init__(self):
        print(type(self).__name__, "details: ")

    def coursesOffered(self):
        print("c#., SQL, .NET")

    @abstractmethod
    def Address(self): pass

class TechnoAcademy (Institute):
    #method overriding
    def coursesOffered(self):
        print("AI, ML, Python")
    def Address(self):
        print("Address @ Seattle")

class OnlineAcademy (Institute):
    def Address(self):
        print("Address @Online")

ta = TechnoAcademy()
ta.coursesOffered()
ta.Address()

oa = OnlineAcademy()
oa.coursesOffered()
oa.Address()