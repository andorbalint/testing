# def TypeError
#
#     def TypeError(self):
#         [...]
#
#
# def factorial(n):
#     prod = 1
#     for i in range(1, n + 1):
#         prod = prod * i # prod *= i
#
#     print(prod)
#
# if __name__ == "__main__":
#
#     n = 8.2
#     if not isinstance(n, int):
#         raise TypeError("n should be int")
#
#     factorial(7)


from functools import reduce
from dataclasses import dataclass
def multiply(x):
    return 2 * x


@dataclass
class Student:
    nota: int


if __name__ == "__main__":

    # map

    my_list = [10, 1, 2, 3, 4, 5]

    # new_list = list(map(multiply, my_list)) # --> [mulitply(1), multiply(2), ..., multiply(5)]
    #
    # print(new_list)
    #
    # # filter
    #
    # new_list = list(filter(lambda x: x % 2 == 0, my_list))
    #
    # print(new_list)

    # reduce
    new_list = reduce(lambda x, y: x + y, my_list)

    print(new_list)

    # sorted, max, min

    tuple_list = [(10, 2), (5, 9), (7, 8)]

    print(sorted(tuple_list, key=lambda x: x[1] - x[0]))

    print(min(tuple_list, key=lambda x: x[1] - x[0]))

    studenti = [Student(10), Student(8), Student(1)]

    d1 = {"varsta": 25, "nume": "Ion"}
    d2 = {"varsta": 18, "nume": "Alex"}

    people = [d1, d2]

    print(min(studenti, key=lambda s: s.nota))

    print(sorted(people, key=lambda x: x["varsta"]))
