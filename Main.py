from Bank import *

if __name__ == '__main__':
    b = Bank()
    ans = True
    while ans:
        print("""
        1. Show all customers
        2. New customer
        3. Customer search
        4. Change name of customer
        5. Remove customer
        6. Account search
        7. Deposit
        8. Withdraw
        9. Close account
        10. Exit application
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            b.get_customers()
        elif ans == "2":
            b.add_customer(input("Enter name of new customer: "), input("Enter social security number of new customer: "))
        elif ans == "3":
            b.get_customer(input("Enter social security number of customer: "))
        elif ans == "4":
            b.change_customer_name(input("Enter social security number of the customer you want to change: "), input("Enter the new name of the customer: "))
        elif ans == "5":
            b.remove_customer(input("Enter social security number of the customer you want to delete: "))
        elif ans == "6":
            b.get_account(input("Enter account number of the account you wish to see information about: "))
        elif ans == "7":
            b.deposit(input("Enter a social security number: "), input("Enter customers account number: "), input("How much do you want to deposit? "))
        elif ans == "8":
            b.withdraw(input("Enter a social security number: "), input("Enter customers account number: "), input("How much do you want to withdraw? "))
        elif ans == "9":
            b.close_account(input("Enter customers account number that will be deleted: "))
        elif ans == "10":
            print("Thanks for using the NBI Bank Application. See you soon!")
            quit()
        else:
            print("Invalid input")
            ans = True