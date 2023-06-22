# #clase abstacte - pot fi vazute ca niste matrite ptr clase
#
#
# from abc import ABC , abstractmethod # abstact base class
#
# class Figure(ABC):
#
#     @abstractmethod  #decorator
#     def area(self):
#         pass
#
# class Rectangle(Figure):
#
#     def __init__(self, l, L):
#             self.l = l
#             self.L = L
#
#     def area(self):
#             return self.l *self.L
#
# if __name__ == "__main__":  # ne asiguram ca codul nu este rulat decit cind rulam scriptul(scop de organizare)
#
#     my_rectangle = Rectangle(10, 20)
#
#     print(my_rectangle.area())

class Animal:
    def __init__(self, name , speed , position=0):
        self.name ...


    """
    metode abstracte:
     - make sound() - print(#animal#sound)
     - move() - position + speed ( metoda va actualiza membrul position)
     - get_position() - return position
     
     """
    #class tiger , class Deer


if __name__ == "__main__":

    my_tiger = Tiger("Tiger_name" , 5)
    my_deer = Deer("Deer_name" , 7)

    my_tiger.move()
    my_deer.move()

print(my_deer.get_position(),
my_tiger.get_position
