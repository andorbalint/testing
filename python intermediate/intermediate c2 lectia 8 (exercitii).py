# album, year, US_peak_chart_post
# The White Stripes, 1999, -
# De Stijl, 2000, -
# White Blood Cells, 2001, 61
# Elephant, 2003, 6
# Get Behind Me Satan, 2005, 3
# Icky Thump, 2007, 2
# Under Great White Northern Lights, 2010, 11
# Live in Mississippi, 2011, -
# Live at the Gold Dollar, 2012, -
# Nine Miles from the White City, 2013, -


  # in_file = open("my_csv.csv", "r")
  #   reader = csv.reader(in_file)
  #   next(reader)
  #   my_list = []
  #   for row in reader:
  #       row_dictionary = dict()
  #       ...
  #
  #   in_file.close()



class Person:
        ...

if __name__=="__main__":

#         iterable,iterator,generator

    a = [1,2,3,4]

    list_iterator = a.__iter__()

    print(list_iterator.__next__())
    print(list_iterator.__next__())
    print(list_iterator.__next__())
    print(list_iterator.__next__())
    # print(list_iterator.__next__())

#      un obiect este iterabil daca implementeaza metoda __iter__()
#      aceasta returneaza un iterator

#  un iterator este un obiect care implementeaza metoda __next__()
#  net ridica StopIteration

    it2 = iter(a)

    print(next(it2))

