from math import sqrt
def is_prime(n):
    # 2 ... sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i = i + 1 # i += 1

    return primes


if __name__ == "__main__":

    my_list = get_n_primes(50)
    print(my_list)




    from math import sqrt


def is_prime(n):
    # 2 ... sqrt(n)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class PrimeIterator:

    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()

if __name__ == "__main__":

    my_it = PrimeIterator(2)
    # for number in my_it:
    #     print(number, end=" ")
    print(next(my_it))
    print(next(my_it))
    print(next(my_it))



    class EvenNumbers:
    ...

if __name__ == "__main__":


    #primele n numere pare
    my_iterator = EvenNumbers(5) #-> 2 4 6 8 10
    for i in my_iterator:
        ...




    class Student:

    def __init__(self, name, grades, bonus):
        self.name = name
        self.grades = grades
        self.bonus = bonus

    def get_average(self):
        return sum(self.grades) / len(self.grades)

    def get_total_score(self):
        return self.get_average() + self.bonus

    def __repr__(self):
        return self.name



    Andra Aurora Ghita
  8:49 PM
class Student:
    def __init__(self, nume, note):
        self.nume = nume
        self.note = note
        self.generated_note = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.generated_note >= len(self.note):
            raise StopIteration
        else:
            current_index = self.generated_note
            self.generated_note += 1
            return self.note[current_index]



if __name__ == "__main__":



    s1 = Student("Ion", [10, 8, 7, 5, 6])
    for i in s1:
        print(i)



        def __iter__(self):
        return iter(self.grades)
