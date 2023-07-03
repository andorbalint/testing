#
#
# #scrieti un decorator care permite apelul metodei get_name
# # doar daca Userul este logat (self.logged_in == True)
# # daca nu este logat, in loc de nume
# # se va afisa un string care se va furniza ca parametru la decorator
#
#
# def custom_check(my_text):
#
#     def auth_check(func):
#         def wrapper(self):
#             if not self.logged_in:
#                 print("userul nu este logat")
#             else:
#                 func(self,*args)
#         return wrapper
#     return auth_check
#
# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.logged_in = False
#
#     @auth_check("userul nu este logat")
#     def get_name(self):
#         print(self.name)
#
#     def login(self):
#         self.logged_in = True
#
#
# if __name__ == "__main__":
#
#     _____
#
#     @decorator("Userul nu este logat!")
#     def get_name(self):
#         [...]
#
#     '''
#
#
#     ion = User("Ion")
#     ion.get_name() # Userul nu este logat!
#     ion.login()
#     ion.get_name() # Ion

#
# def custom_check(my_text):
#     def auth_check(func):
#         def wrapper(self, *args):
#             if not self.logged_in:
#                 print(my_text)
#             else:
#                 func(self, *args)
#         return wrapper
#     return auth_check
#
# class User:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.logged_in = False
#         self.age = age
#
#     @custom_check("USERUL NU ESTE LOGAT!!")
#     def get_name(self):
#         print(self.name)
#
#     def login(self):
#         self.logged_in = True
#
#     @custom_check("Inainte de a afisa varsta, logati-va!")
#     def get_age(self):
#         print(f"Varsta lui {self.name} este {self.age}")
#
#
# if __name__ == "__main__":
#
#     '''
#     scrieti un decorator care permite apelul metodei get_name doar daca Userul este logat (self.logged_in == True)
#     daca nu este logat, in loc de nume se va afisa un string care se va furniza ca parametru la decorator
#     _____
#
#     @decorator("Userul nu este logat!")
#     def get_name(self):
#         [...]
#
#     '''
#
#     ion = User("Ion", 19)
#     ion.get_name() # Userul nu este logat!
#     ion.get_age()
#     ion.login()
#     ion.get_name() # Ion
#     ion.get_age()

#
# from datetime import datetime
# import time
#
#
# def my_function():
#     time.sleep(2)
#
# if __name__=="__main__":
#
#     now =datetime.now()
#     print(now.hour, now.minute, now.second)
#
#     start = time.time()
#     my_function()
#     end = time.time()
#
#     print(f"Executia functiei a durat {end - start} secunde")

import time


def calculate(n):
    def

def my_function():
    print("Acum")
    time.sleep(5)
    print("Peste 5 secunde")

def calculate(n):




    if __name__=="__main__":

     """
    # def calculate(n):
    # -> calculeaza suma primelor n numere(1+2+ ....+n) si afiseaza
    # 
    # creati 2 decoratoare:
    # 1) Afisati ora executiei inainte de executie
    # 
    # 2) Afiseaza timpul de executie dupa ce a fost executata
    # 
    # """

