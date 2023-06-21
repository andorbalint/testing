# mostenire_multipla (super -metoda care apeleaza din clasa parinte)
# class Animal:
#
#     def make_a_sound(self):
#         pass
#
# class Tiger(Animal):
#
#     def make_a_sound(self):
#         print("Tiger sound")
#
#
# class Lion(Animal):
#
#     def make_a_sound(self):
#         print("Lion sound")
#
#
# if __name__=="__main__":
#
#     lion = Lion()
#     tiger = Tiger()
#     animal_list = [lion, tiger]
#

# class Person:
#     # init - constructor initializeaza membrul din clasa
#     def __init__(self ,name , age):
#         self.name = name
#         self.age = age
#
#     # str -metoda care returneaza stringul care vrem sal printam
#     def __str__(self):
#         return f"Sunt {self.name} si am {self.age} de ani"
#
# class Employee(Person):
#     def __init__(self, name ,age, working_hours ,rate):
#         super().__init__(self ,name , age)
#         self.rate = rate
#         self.working_hours = working_hours
#
#
#     def show_finance(self):
#         return self.rate * self.working_hours
#
# class Student(Person):
#     def __init__(self, name ,age ,scholarship):
#         Person.__init__(self , name, age )
#         self.scholarship = scholarship
#
#     def show_finance(self):
#         return self.scholarship
#
#
#
# class WorkingStudent(Employee , Student):
#     def __init__(self, name, age , rate , working_hours , scholarship):
#         Employee.__init__(self, name, age, rate, working_hours)
#         Student.__init__(self, name, age, scholarship)
#
#     def show_finance(self):
#         return self.rate * self.working_hours + self.scholarship
#
#
# if __name__=="__main__":
#
#     pers = Person("Ion" , 23)
#     pers2 = Person("Alex", 18)
#     print(pers.name , pers.age)
#
#     student = Student( "Ion" , 20, 2000)
#
#     print(student)
#     print(student.show_finance())
#
#     w_student = WorkingStudent("Ion", 20 , 50, 100, 1000)


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age: {self.age}")


class Student(Person):  # student_id
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        Person.__init__(self,age, name)


    def display_info(self):
        super().display_info()
        print(f"student_id: {self.student_id}")


class Teacher(Person):  # subject
    def __init__(self, subject, name, age):
        self.subject = subject
        super().__init__(age, name)

    def display_info(self):
        super().display_info()
        print(f"subject: {self.subject}")


class StudentTeacher(Student , Teacher):
    def __init__(self, name , age , student_id, subject):
        Student.__init__(self, age, name , student_id)
        Teacher.__init__(self , age , name , subject)

    def display_info(self):
        super().display_info()

if __name__ == "__main__": # locul unde python cauta rularea programului

    student_teacher = StudentTeacher ( 25 , "andrei" , 1122 , "programare")
    student_teacher.display_info()
    p = Person(19, "adi")
    p.display_info()
    p1 = Person(22, "doc")
    p1.display_info()
    s = Student(20 , "vlad", 2222)
    s.display_info()
    t = Teacher("english" , 41 , "gratiela"  )
    t.display_info()


#polimorfism- mai multe obiecte cu clasa parinte comuna

s = Student(19 ,"Student_name" , 12345)
t = Teacher(30 ,"teacher name" , "python")
s2 = Student(20, "student_2", 5678)

person_list = [s, t, s2]

for x in person_list:
    x.display_info()
    print("==========")
