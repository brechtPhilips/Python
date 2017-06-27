import random

from BankAccount.BackEnd import Database



class Account:

    def __init__(self,first_name,last_name,address,amount):
       self.first_name = first_name
       self.last_name = last_name
       self.amount = amount
       self.address = address
       self.database = Database.Database()
       self.account_number = self.get_account_number()

    def get_account_number(self):
        account_number = ""
        while account_number.__len__() < 12:
            account_number += str(random.randrange(0, 13))

        for account_numbers in self.database.get_account_number():
            if account_number == str(account_numbers[0]):
                self.get_account_number()
        return int(account_number)
