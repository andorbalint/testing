# recapitulare (leetcode.com)


# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal
# to or lower than 1000, else return their sum.


number1 = 20
number2 = 30

def caclulate_product_or_sum(number1, number2):
     product = 20 * 30
     if product <= 1000:
         return product
     else:
         return 20 + 30


