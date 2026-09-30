import csv
import re

FILE_NAME = "customers.csv"

def read_customers():
    customers = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                customers.append(row)

    except FileNotFoundError:
        print("Error: customers.csv file not found.")

    return customers


def display_customers(customers):
    if not customers:
        print("No customer records found.")
        return

    print("\nCustomer Records")

    for customer in customers:
        print("\nAccount Number :", customer["AccountNumber"])
        print("Name           :", customer["Name"])
        print("Address        :", customer["Address"])
        print("Phone          :", customer["Phone"])
        print("Balance        :", customer["Balance"])


def search_customer(customers):
    account_number = input("Enter Account Number: ")

    pattern = r"^ACC\d{4}$"

    if not re.match(pattern, account_number):
        print("Invalid account number format.")
        print("Expected format: ACC1001")
        return

    found = False

    for customer in customers:
        if customer["AccountNumber"].upper() == account_number.upper():
            print("\nCustomer Found")
            print("Account Number :", customer["AccountNumber"])
            print("Name           :", customer["Name"])
            print("Address        :", customer["Address"])
            print("Phone          :", customer["Phone"])
            print("Balance        :", customer["Balance"])

            found = True
            break

    if not found:
        print("Customer not found.")


def main():
    customers = read_customers()

    while True:
        print("\nBank Customer Record System")
        print("1. Display all customer details")
        print("2. Search customer by Account Number")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_customers(customers)

        elif choice == "2":
            search_customer(customers)

        elif choice == "3":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
