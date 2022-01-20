from Bank import *

if __name__ == '__main__':
    b = Bank()
    print("Welcome to NBI Bank Application!")
    ans = True
    while ans:
        print("""
        1. Show all customers
        2. New customer
        3. Customer search
        4. Change name of customer
        5. Remove customer
        6. Open new account
        7. Account search
        8. Deposit
        9. Withdraw
        10. Close account
        11. Exit application
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            b.get_customers()

        elif ans == "2":
            name = input("Enter name of new customer: ")
            while True:
                try:
                    pnr = int(input("Enter social security number of new customer: "))
                    b.add_customer(name, pnr)
                    break
                except:
                    print("Please use numbers to specify social security number")

        elif ans == "3":
            while True:
                try:
                    pnr = int(input("Enter social security number of the customer you want to search for: "))
                    b.get_customer(pnr)
                    break
                except:
                    print("Please use numbers to specify social security number")

        elif ans == "4":
            while True:
                try:
                    pnr = int(input("Enter social security number of the customer you want to change: "))
                    break
                except:
                    print("Please use numbers to specify social security number")
                
            name = input("Enter the new name of the customer: ")
            b.change_customer_name(pnr, name)

        elif ans == "5":
            while True:
                try:
                    pnr = int(input("Enter social security number of the customer you want to delete: "))
                    b.remove_customer(pnr)
                    break
                except:
                    print("Please use numbers to specify social security number")

        elif ans == "6":
            while True:
                try:
                    pnr = int(input("Enter customers social security number: "))
                    b.add_account(pnr)
                    break
                except:
                    print("Please use numbers to specify social security number")

        elif ans == "7":
            while True:
                try:
                    accnr = int(input("Enter account number of the account you wish to see information about: "))
                    b.get_account(accnr)
                    break
                except:
                    print("Please use numbers to specify account number")

        elif ans == "8":
            while True:
                try:
                    pnr = int(input("Enter a social security number: "))
                    accnr = int(input("Enter customers account number: "))
                    amount = int(input("How much do you want to deposit? "))
                    break
                except:
                    print("Please use numbers for all fields")

            b.deposit(pnr, accnr, amount)

        elif ans == "9":
            while True:
                try:
                    pnr = int(input("Enter a social security number: "))
                    accnr = int(input("Enter customers account number: "))
                    amount = int(input("How much do you want to withdraw? "))
                    break
                except:
                    print("Please use numbers for all fields")

            b.withdraw(pnr, accnr, amount)

        elif ans == "10":
            while True:
                try:
                    accnr = int(input("Enter customers account number that will be deleted: "))
                    b.close_account(accnr)
                    break
                except:
                    print("Please use numbers to specify account number")

        elif ans == "11":
            print("Thanks for using the NBI Bank Application. See you soon!")
            quit()

        else:
            print("Invalid input")
            ans = True