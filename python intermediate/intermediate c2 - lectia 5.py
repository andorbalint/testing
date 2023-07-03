# # # from copy import deepcopy
# # #
# # # from dataclasses import dataclass
# # #
# # # @dataclass
# # # class Rectangle:
# # #     a : int
# # #     b : int
# # #
# # # if __name__=="__main__":
# #
# #     # my_rectangle = Rectangle(3, 4)
# #     # new_r = deepcopy(my_rectangle)
# #     # my_list = [8,9,10]
# #     # x = [1,2,3, my_rectangle]
# #     # y = deepcopy(x) #deepcoppy copiaza toate valorile din x
# #     # y[3].a = 99
# #     # new_r.b = 222
# #     #
# #     # print(x ,y, my_rectangle)
# #
# #
# #
# #
# # #
# # # def add(a,b):
# # #     return a+b
# # #
# # #
# # # def do_operations(a ,b,f):
# # #
# # #     def additional_print()
# # #         print("additional print")
# # #         print(f(a,b))
# # #     return additional_print()
# # #
# # # if __name__ == "__main__:":
# # #
# # #     do_operations(10,15, add)
# #
# # from datetime import datetime
# #
# # def disable_at_night(func):#dar param funct decorata
# #     def wrapper(*args ,**kwargs):
# #         if 12 <= datetime.now().hour <= 22:
# #             func(*args, **kwargs)#args (argumente) lista
# #
# #     return wrapper
# #
# # @disable_at_night
# # def trigger_water(water_presure):
# #     print("sistemul a fost pornit")
# #
# # def my_function(*args ,**kwargs):
# #     for argument in args:
# #         print(argument)
# #
# #     for key , value in **kwargs
#
# #
# # if __name__ == "__main__":
# #
# #     trigger_water = disable_at_night(trigger_water) # rand 50 = coment linia 57
# #     trigger_water()
# #
#
# # from datetime import datetime
# #
# # def run_between(start, end): #functie parametru
# #     def disable_at_night(func): #-> decorator
# #         def wrapper(*args, **kwargs):#args= lista, *kwargs =dictionar
# #             if 12 <= datetime.now().hour <= 20:
# #                 print("S-a apelat functia decorata")
# #                 func(*args, **kwargs)
# #
# #         return wrapper
# #     return disable_at_night
# #
# #
# # @run_between(10,20)
# # def trigger_water(**kwargs):
# #     print(f"Sistemul a fost pornit cu {kwargs['pressure']}")
# #
# #
# # #@disable_at_night
# # def my_function():
# #     print("not decorated")
# #
# #
# # def my_function(*args, **kwargs):
# #     for argument in args:
# #         print(argument)
# #
# #     for key, value in kwargs.items():
# #         print(f"{key}: {value}")
# #
# # if __name__ == "__main__":
# #
# #     # trigger_water = disable_at_night(trigger_water)
# #     # trigger_water(3)
# #
# #     trigger_water(pressure=3)
# #
# #     # my_function()
# #
# #     # print(datetime.now().hour, datetime.now().minute)
#
# def majuscula(func):
#     def wrapper(self, *args):
#         result = func(self, *args)
#         return result[0].upper() + result[1:]
#
#     return wrapper
#
#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#
#     @majuscula
#     def get_name(self):
#         return self.name
#
#
# if __name__ == "__main__":
#     s = Student("ion")
#     print(f"Salut, {s.get_name()}")
