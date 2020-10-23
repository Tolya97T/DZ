# Вариант 10
class car:
    __id = 0
    __marka = " "
    __model = " "
    __year = 0
    __color = " "
    __price = 0
    __num = " "
    __cars = []

    def __init__(self, id, marka, model, year, color, price, num):
        self.__id = id
        self.__marka = marka
        self.__model = model
        self.__year = year
        self.__color = color
        self.__price = price
        self.__num = num

    def get_id(self):
        return self.__id

    def get_marka(self):
        return self.__marka

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_num(self):
        return self.__num

    def add_car(self, newCar):
        if newCar.year() < 2005:
            self.__cars.append(newCar)
            print("Машины которые в эксплуатации более 15 лет:")
        else:
            print("nope")

    def __str__(self):
        return "ID: " + str(self.__id) + " Марка: " + str(self.__marka) + " Модель: " + str(
            self.__model) + " Год выпуска: " + str(self.__year) + " Цвет: " + str(self.__color) + " Цена: " + str(
            self.__price) + " Рег. номер: " + str(self.__num)


newCar = [
    car(0, "Nissan", "almera", 1998, "black", 1250, "5732-IX"),
    car(1, "Honda", "CR-X", 2001, "grey", 1500, "3214-OK"),
    car(2, "Subaru", "Impreza", 1995, "blue", 1000, "8424-KX"),
    car(3, "Audi", "100", 1984, "yellow", 500, "2406-KL"),
    car(4, "Nissan", "Sunny", 2005, "green", 1890, "5789-AB"),
    car(5, "Honda", "Accord", 2009, "white", 2400, "1249-JK"),
    car(6, "Honda", "CR-V", 2007, "red", 3200, "3127-QK")
]

for i in range(len(newCar)):
    2020 - car.get_year(self=newCar[i])
    print(newCar[i], "возраст машины: ", 2020 - car.get_year(self=newCar[i]))

print("Машины старше 15 лет:")
for i in range(len(newCar)):
    if car.get_year(self=newCar[i]) < 2005:
        print(newCar[i])

print("Машины марки Nissan:")
for i in range(len(newCar)):
    if car.get_marka(self=newCar[i]) == "Nissan":
        print(newCar[i])
