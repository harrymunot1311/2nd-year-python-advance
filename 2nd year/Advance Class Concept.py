class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance      # Encapsulation

    def get_balance(self):
        return self.__balance

    def display(self):
        print("Account Holder :", self.holder)
        print("Balance        :", self.__balance)


# Child Class
class SavingsAccount(Account):
    def __init__(self, holder, balance, interest):
        super().__init__(holder, balance)
        self.interest = interest

    # Method Overriding
    def display(self):
        super().display()
        print("Interest Rate :", self.interest, "%")


# Another Child Class
class CurrentAccount(Account):
    def __init__(self, holder, balance, overdraft):
        super().__init__(holder, balance)
        self.overdraft = overdraft

    # Method Overriding
    def display(self):
        super().display()
        print("Overdraft Limit :", self.overdraft)


# -------- Main Program --------

print("====== Savings Account ======")
s1 = SavingsAccount("Jyotsna", 50000, 6.5)
s1.display()

print("\n====== Current Account ======")
c1 = CurrentAccount("Joy", 80000, 25000)
c1.display()

print("\nSavings Account Balance :", s1.get_balance())


#Balance        : 50000
#Interest Rate : 6.5 %

#====== Current Account ======
#Account Holder : Joy
#Balance        : 80000
#Overdraft Limit : 25000

#Savings Account Balance : 50000
