# Decorator
def mobile_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 35)
        print("      MOBILE DETAILS")
        print("=" * 35)
        func(*args, **kwargs)
        print("=" * 35)
    return wrapper


# Mobile Class
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @mobile_header
    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Price :", self.price)

        if self.price >= 50000:
            print("Category : Premium")
        elif self.price >= 20000:
            print("Category : Mid-range")
        else:
            print("Category : Budget")


# Store Class
class Store:
    def add_mobile(self, mobile):
        print("Mobile Added Successfully!\n")

    def display_mobile(self, mobile):
        mobile.display()


# Main Program
m1 = Mobile("Samsung", "Galaxy S24", 75000)

store = Store()
store.add_mobile(m1)
store.display_mobile(m1)

"""
===================================
      MOBILE DETAILS
===================================
Brand : Samsung
Model : Galaxy S24
Price : 75000
Category : Premium
===================================
"""