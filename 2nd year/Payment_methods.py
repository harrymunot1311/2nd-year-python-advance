from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"\nPayment of ₹{amount} successful using Credit Card.")

class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"\nPayment of ₹{amount} successful using Debit Card.")

class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"\nPayment of ₹{amount} successful using UPI.")

class NetBankingPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"\nPayment of ₹{amount} successful using Net Banking.")

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"\nPayment of ₹{amount} successful using Cash.")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)

print("====== PAYMENT PROCESSING SYSTEM ======")

amount = float(input("Enter Payment Amount: ₹"))

print("\nChoose Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")
print("4. Net Banking")
print("5. Cash")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = DebitCardPayment()
elif choice == 3:
    strategy = UpiPayment()
elif choice == 4:
    strategy = NetBankingPayment()
elif choice == 5:
    strategy = CashPayment()
else:
    print("Invalid Choice!")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)

print("\nThank you for using our Payment Processing System!")