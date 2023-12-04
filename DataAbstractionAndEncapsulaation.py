class Product:

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__price = ""

    def setProduct(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def showProduct(self):
        print("id: {}\nname: {}\nprice: {}\n".format(self.__id, self.__name, self.__price))

p1 = Product()
p1.setProduct(101, 'Mic', 150)

p2 = Product()
p2.setProduct(102, 'Speaker', 800)

p1.showProduct()
p2.showProduct()

print(p1.__price)