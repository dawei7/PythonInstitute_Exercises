"""
Estimated time
30-60 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in operating with the getter, setter, and deleter methods;
improving the student's skills in creating their own exceptions.
Scenario
Implement a class representing an account exception,
Implement a class representing a single bank account,
This class should control access to the account number and account balance attributes by implementing the properties:
it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
it should not be possible to delete an account as long as the balance is not zero;
test your class behavior by:
setting the balance to 1000;
trying to set the balance to -200;
trying to set a new value for the account number;
trying to deposit 1.000.000;
trying to delete the account attribute containing a non-zero balance.
"""

class AccountException(Exception):
    pass

class BankAccount:
    
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self,account_number):
        try:
            raise AccountException("It's not allowed to change the account number.")
        except AccountException as e:
            print(e)
    
    @account_number.deleter
    def account_number(self):
        if self.__account_number == 0:
            del self.__account_number
        else:
            try:
                raise AccountException("It's not possible to delete an account, which has a non-zero balance.")
            except AccountException as e:
                print(e)

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        try:
            if amount < 0:
                raise AccountException("It's not possible to set the balance below 0.")
            else:
                self.__balance = amount
        except AccountException as e:
            print(e)
    
    def deposit(self,amount):
        self.__balance += amount
        try:
            if amount > 100000:
                raise AccountException("An employee will contact you for auditing purposes because of an unusual high deposit.")
        except AccountException as e:
            print(e)

    def withdraw(self,amount):
        self.__balance -= amount
        try:
            if amount > 100000:
                raise AccountException("An employee will contact you for auditing purposes because of an unusual high withdrawal.")
        except AccountException as e:
            print(e)


"""
test your class behavior by:
setting the balance to 1000;
trying to set the balance to -200;
trying to set a new value for the account number;
trying to deposit 1.000.000;
trying to delete the account attribute containing a non-zero balance.
"""

my_bank_account = BankAccount("777-777-777",100)
my_bank_account.balance = 1000
my_bank_account.balance = -200
my_bank_account.account_number = '888-888-888'
my_bank_account.deposit(1000000)
del my_bank_account.account_number
print(my_bank_account.account_number) # 777-777-777
print(my_bank_account.balance) # 1001000