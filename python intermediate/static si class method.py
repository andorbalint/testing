# # metoda statice si de clasa
# import Matematica
#
# class Matematica: #exemplu static metod
#
#     @staticmethod
#     def add_2(a, b):
#         return a + b
#
#     @staticmethod
#     def custom_math_function(a,b):
#         return 3 * (a - b)
#
#from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, speed, position=0):
        self.name = name
        self.speed = speed
        self.position = position

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def get_position(self):
        pass


class Tiger(Animal):

    def __init__(self, name, speed, position=0):
        super().__init__(name, speed, position)

    def make_sound(self):
        print("tiger sound")

    def move(self):
        self.position += self.speed # self.position = self.position + self.speed

    def get_position(self):
        return self.position

    @staticmethod
    def clip_tiger_speed(speed):
        """
        daca speed > 20, functia va returna20.Altfel va returna parametrii initiali

        """

    if my_tiger_speed >20
        return 20
    else return speed

    @classmethod
    def create_from_string(cls, custom_string):

        """
        exemplu tiger = Tiger create from string('Tigername-28'), altul cu 18
        :param custom_string:
        :return:
        """

class Deer(Animal):

    def __init__(self, name, speed, position=0):
        super().__init__(name, speed, position)

    def make_sound(self):
        print("deer sound")

    def move(self):
        self.position += self.speed

    def get_position(self):
        return self.position


if __name__ == "__main__":

    my_tiger = Tiger("Tiger_name", 5, 100)
    my_deer = Deer("Deer_name", 7)

    my_tiger.move()
    my_deer.move()
    my_tiger.move()

    my_deer.move()

    print(my_deer.get_position(), my_tiger.get_position())

    my_deer.make_sound()
    my_tiger.make_sound()

#
# class Person:
#     # init - constructor initializeaza membrul din clasa
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # str -metoda care returneaza stringul care vrem sal printam
#     def __str__(self):
#         return f"Sunt {self.name} si am {self.age} de ani"
#
#
# class Employee(Person):
#     def __init__(self, name, age, working_hours, rate):
#         super().__init__(self, name, age)
#         self.rate = rate
#         self.working_hours = working_hours
#
#     def show_finance(self):
#         return self.rate * self.working_hours
#
#
# class Student(Person):
#     def __init__(self, name, age, scholarship):
#         Person.__init__(self, name, age)
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#     @staticmethod  # metoda statica scrisa in clasa si apeleaza de acolo
#     def is_name_correct(name):  # tine de logica clasei(metoda statica def in clasa
#         print("Am apelat o functie")
#         if name[0].isupper() and len(name) > 3:
#             return True
#         return False
#
#     @classmethod
#     def create_from_string(cls, input_string):
#         name, age , scholarship = input_string.split()
#         age, scholarship = int(age), int(scholarship)
#
#         return cls (name, age , scholarship)
#
#
#
#     if __name__ == "__main__":
#
#         x = 2
#         y = 10
#
#         print (Matematica.add_2(x,y))
#         print (Matematica.custom_math_function(x,y))
#
#         my_student =Student("num", 12 , 222)
#         my_student2 = Student("num2" , 1222, 23345)
#
#         new_student = Student.create_from_string("ion 20 9000")
#         print(new_student.show_finance)
#         print("ana are mere".split("-"))
#
#         db_string = "ion 20 9000"
#
# class WorkingStudent(Employee, Student):
#     def __init__(self, name, age, rate, working_hours, scholarship):
#         Employee.__init__(self, name, age, rate, working_hours)
#         Student.__init__(self, name, age, scholarship)
#
#     def show_finance(self):
#         return self.rate * self.working_hours + self.scholarship
#
#
# if __name__ == "__main__":
#     pers = Person("Ion", 23)
#     pers2 = Person("Alex", 18)
#     print(pers.name, pers.age)
#
#     student = Student("Ion", 20, 2000)
#
#     print(student)
#     print(student.show_finance())
#
#     w_student = WorkingStudent("Ion", 20, 50, 100, 1000)


class Rectangle:

    def __init__(self, lungime , latime):
        self.lungime = lungime
        self.latime = latime

    def __eq__(self, other):
        if isinstance(other, Rectangle) and (self.lungime , self.latime) == (other.lungime , other.latime)
            return True
        return False

    def__str__(self):
        return f"Rectangle({self.lungime}, {self.latime})"

@dataclass # echivalent cu ce este mai sus# creezi obiecte cu el simple
class Rectangle2:
    lungime: int
    latime: int


@dataclass
class Sfera:
    raza: int #type hint
    diametru:int

    def area(self)
        ...

if __name__ == "__main":

    d1 = Rectangle(10, 21)
    d2 = Rectangle(10 , 21)

    print(d1 ==  d2)

# class Rectangle(Figure):
#         def __init__(self, a: int, b: int):
#             self.a = a
#             self.b = b
#
#         def __str__(self):
#             return f"Rectangle(a={self.a}, b={self.b})"
#
#         def __eq__(self, other):
#             return isinstance(other, Rectangle) and (self.a, self.b) == (other.a, other.b)


@dataclass
class Persoana:
    cnp: str


