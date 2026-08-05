class BankRecord:
    def __init__(self, customer_name, amount):
        self.customer_name = customer_name
        self.__amount = amount      # Encapsulation

    def check_amount(self):
        return self.__amount

    def show_info(self):
        print("Customer Name :", self.customer_name)
        print("Account Amount:", self.__amount)

class SavingPlan(BankRecord):
    def __init__(self, customer_name, amount, rate):
        super().__init__(customer_name, amount)
        self.rate = rate

    def show_info(self):
        super().show_info()
        print("Interest Rate :", self.rate, "%")

class CurrentPlan(BankRecord):
    def __init__(self, customer_name, amount, limit):
        super().__init__(customer_name, amount)
        self.limit = limit

    def show_info(self):
        super().show_info()
        print("Overdraft Limit :", self.limit)


print("====== Saving Plan ======")
saving_acc = SavingPlan("Amit", 50000, 6.5)
saving_acc.show_info()

print("\n====== Current Plan ======")
current_acc = CurrentPlan("Neha", 80000, 25000)
current_acc.show_info()

print("\nSaving Plan Amount :", saving_acc.check_amount())
'''
output:
====== Saving Plan ======
Customer Name : Amit
Account Amount: 50000
Interest Rate : 6.5 %

====== Current Plan ======
Customer Name : Neha
Account Amount: 80000
Overdraft Limit : 25000

Saving Plan Amount : 50000
'''