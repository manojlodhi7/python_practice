import sys

class Patel_Bank:
    bankname = "PATEL-BANK"

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposite(self, amount):
        self.balance = self.balance + amount
        print("Current Balance is : ", self.balance)

    def withdrowl(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Current remaining balance is : ", self.balance)
        print("Insufficient balance is : ", self.balance)

print("Welcome to ", Patel_Bank.bankname)

name = input("Please enter your name : \n")
c = Patel_Bank(name)
while True:
    print("Please select from below options")
    user_input = input("d : Deposite \nw : withdrowal \ne : exit\n")
    if user_input.casefold() == "d":
        c.deposite(float(input("Enter amount to deposite : ")))
    elif user_input.casefold() == "w":
        c.withdrowl(float(input("Enter amount to withdowal : ")))
    elif user_input.casefold() == "e":
        print("Thank you for banking with us")
        sys.exit()
    else:
        print("Incorrect option")

