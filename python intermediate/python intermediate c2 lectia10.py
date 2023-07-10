# def ran=Nonenerator(start, stop):
#     current_value = start
#     while current_value < stop:
#         yield current_value
#         current_value += 1
#
# if __name__ == "__main__":
#
#     my_range = range_generator(1, 10) # range(1, 10)
#     print(next(my_range))
#     print(next(my_range))
#
#     for i in my_range:
#         print(i)
#
#
#
#         def prime_generator(n):
#     number = 2
#     generated_numbers = 0
#     while generated_numbers != n:
#         if is_prime(number):
#             yield number #return ,dar ruleaza mai departe pana la sf codului
#             generated_numbers += 1
#         number += 1
#
# if __name__ == "__main__":
#
#     my_generator = prime_generator(3)
#     # print(next(my_generator))
#     # print(next(my_generator))
#     # print(next(my_generator))
#     # print(next(my_generator))
#
#      i in my_generator:
#         print(i)
#
#
#
#     #0,1,1,2,3,5,8,13,21 ....# sirul lui Fibonacci

def fib_generator
    numbers = 0,1
    generated_numbers = 0
    while generated_numbers != n:
        if is_n(number):
            generated_numbers += numbers
            numbers = numbers + generated_numbers
            yield generated_numbers

    generated_numbers + n = fib_generator(0)

if __name__ == "__main__"

    my_generator = fib_generator()

    print(fib_generator()_generator()) #ex meu





    def Fib_generator
    numbers = n
    generated_numbers = 0
    while generated_numbers != n:
        if is_n(number):
            generated_numbers += numbers
            numbers = numbers + generated_numbers


    generated_numbers + n = Fib_generator()

if __name__ == "__main__"

    my_generator = Fib_generator()

    print(Fib_generator()_generator())




class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class MyContext: #context manager(in fisiere)
    # # with open("file.txt", "w") as f:  in loc de ce ie jos
    # in loc de inchidere fisier classic
    #     f.write("Hello world")

    def __enter__(self):
        print("INCEPUT")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("SFARSIT")

if __name__ == "__main__":

    # with open("file.txt", "w") as f:
    #     f.write("Hello world")
    #
    # f = open("file.txt", "w") #se inchide fisierul automat, ruleaza in open si exit
    # try:
    #     f.write("Hello world")
    # except IOError:
    #     print("error")
    # finally:
    #     f.close()

    # with FileManager("my_file.txt", "w") as f:
    #     f.write("EXEMPLU")

    with MyContext(): #context manager

        print("SE EXECUTA IN MIJLOC")
        print("TOT IN MIJLOC")

    with MyContext():

        print(2 + 5)

