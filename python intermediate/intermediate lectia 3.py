#clase abstacte - pot fi vazute ca niste matrite ptr clase


from abc import ABC , abstractmethod # abstact base class

class Figure(ABC):

    @abstractmethod  #decorator
    def area(self):
        pass

class Rectangle(Figure):

    def __init__(self, l, L):
            self.l = l
            self.L = L

    def area(self):
            return self.l *self.L

if __name__ == "__main__":  # ne asiguram ca codul nu este rulat decit cind rulam scriptul(scop de organizare)

    my_rectangle = Rectangle(10, 20)

    print(my_rectangle.area())
