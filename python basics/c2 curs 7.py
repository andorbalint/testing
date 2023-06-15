# programare orientata pe obiecte "OP"
#
# class BankAccount:
#     def __init__(self, account_number , balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     def depozit(self , amount):
#         self.balance += amount #self.balance = self.balance +amount
#
#     def withdraw(self ,amount):
#
#         if self.balance <= amount:
#             print("fonduri insuficiente!")
#         else:
#             self.balance -= amount #self_balane =self.balance - amount


my_bank_account_1 = BankAccount("RO1234" , 5000 )
print(f"Numarul tau de cont este: {my_bank_account_1.account_number}")
print(f"Suma ta de pe cont este:{my_bank_account_1.balance}")
my_bank_account_1.depozit(2500)
print(f"Suma ta dupa depozit  este:{my_bank_account_1.balance}")
my_bank_account_1.withdraw(4000)
print(f"Suma ta dupa retragere este:{my_bank_account_1.balance}")
my_bank_account_1.withdraw(4000)
# print(f"Suma ta dupa retragere este:")




