"""Создайте класс Bicycle с атрибутами brand (бренд велосипеда), model (модель) и year (год выпуска).
Добавьте метод get_age, который вычисляет возраст велосипеда как разницу между текущим годом и годом выпуска."""

class Bicycle:
    def __init__(self, brand=None, model="ahmedpro", year="2024"):
        self.brand = brand
        self.model = model
        self.year = year
    def get_age(self):
        return 2024 - self.year

"""Создайте классы Doctor и Patient. Класс Doctor должен иметь атрибут `name`,
 а класс Patient — метод `introduce_doctor`, который будет выводить имя врача, переданного в качестве аргумента."""


class Doctor:
    def __init__(self, name="vasya"):
        self.name = name
class Patient:
    def introduce_doctor(self, name):
     return self.name

patient2 = Patient("sanya")
doctor2 = Doctor("vasya")
patient2.introduce_doctor(doctor2)

#Создайте классы Vehicle и Car. Vehicle должен иметь метод `move`, выводящий на экран "Vehicle moves".
# Car должен наследовать Vehicle и переопределять метод `move`, выводя "Car drives". Создайте объект Car и вызовите метод `move`.

class Vehicle:
 def move(self):
     print("vehicle moves")

class car(Vehicle):
    def move(self):
        print("car drives")

car1 = car()
car1.move()

"""Создайте классы Pen и Highlighter. Pen должен иметь метод `write`, 
который выводит "Writing". Highlighter должен иметь метод `highlight`, который выводит "Highlighting". 
Создайте класс Marker, который наследует оба класса, и вызовите оба метода."""

class Pen:
    def write(self):
        print("writing")
class Highlighter:
    def highlight(self):
        print("highlighting")
class Marker(Pen, Highlighter):
    pass

marker1 = Marker()
marker1.write()
marker1.highlight()
