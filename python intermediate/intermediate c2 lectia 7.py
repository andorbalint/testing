# # import pickle
# #
# #
# # if __name__=="__main__":
# #
# #     grades = [10,9,9,8]
# #
# #     my_file = open("grades.pickle", "wb")#write binary
# #     pickle.dump(grades, my_file)
# #     my_file.close()
# #
# #     file = open("grades.pickle", "rb")#read binary
# #     my_new_list = pickle.load(file)
# #     file.close()
# #
# #     # file = open("grades.pickle", "a")#append
# #
# #     print(my_new_list)
# #
#
#
# import json
#
# # class Person:
# #
# #     def __init__(self, name):
# #         self.name = name
#
#
# if __name__ == "__main__":
#
#     my_dict = {
#         "student1": 19,
#         "student2": 29
#     }
#
#     file = open("my_students.txt", "w")
#     json.dump(my_dict, file)
#     file.close()
#
#     file = open("my_students.txt", "r")
#     my_new_dict = json.load(file)
#     file.close()
#
#     print(my_new_dict)


# import json
#
#
# exercises = {
#    "right_side":[
#       3,
#       5,
#       3,
#       6,
#       4,
#       2,
#       3,
#       6,
#       8,
#       4,
#       3,
#       2
#    ],
#    "left_side":[
#       1.2,
#       4.3,
#       5.4,
#       6.9,
#       9.9,
#       7.2
#    ]
# }
#
# # file = open("my_students.txt", "r")
# file = open("json_exercisess.txt","r")
#
# '''
#     media right_side
#     media left_side
#     media totala
# '''
#
# ex = json.load(file)
# file.close()
#
# print(ex["right_side"])
#
# e = sum(ex["right_side"])/len(ex["right_side"])
#
# print(e)
#
#
# print(ex["left_side"])
#
# e = sum(ex["left_side"])/len(ex["left_side"])
#
# print(e)


import csv


if __name__=="__main__":

      # file = open("employees.csv","r")
      # reader = csv.reader(file)
      # next(reader)
      # for row in reader:
      #    print(row)

      file = open("empoyees2.txt","w", newline="")

      writer = csv.writer(file)

      header = ["name", "age"]

      writer.writerow(header)
      writer.writerow(["ion",20])

      for _ in range(3):
          my_input = input("Row:").split()
          writer.writerow(my_input)

      file.close()


