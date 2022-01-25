import os
from Bank import *


def clear_console():
    """Clears screen from the previous prints and prompts"""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

if __name__ == '__main__':
    b = Bank()
    clear_console()

    ans = True
    while ans:
        print("""
NBI Bank Application
        
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
        
        If you wish to return here, press CTRL + C to get you back.
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            b.get_customers()
            input("Press enter to continue")
            clear_console()

        elif ans == "2":
            while True:
                try:
                    name = input("Enter name of new customer: ")
                    pnr = int(input("Enter social security number of new customer: "))
                    b.add_customer(name, pnr)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers to specify social security number")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "3":
            while True:
                try:
                    pnr = int(input("Enter social security number of the customer you want to search for: "))
                    b.get_customer(pnr)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers to specify social security number")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "4":
            while True:
                try:
                    pnr = int(input("Enter social security number of the customer you want to change: "))
                    name = input("Enter the new name of the customer: ")
                    b.change_customer_name(pnr, name)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers to specify social security number")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "5":
            while True:
                try:
                    pnr = int(input("Enter social security number of the customer you want to delete: "))
                    b.remove_customer(pnr)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers to specify social security number")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "6":
            while True:
                try:
                    pnr = int(input("Enter customers social security number: "))
                    b.add_account(pnr)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers to specify social security number")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "7":
            while True:
                try:
                    acc_nr = int(input("Enter account number of the account you wish to see information about: "))
                    b.get_account(acc_nr)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers to specify account number")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "8":
            while True:
                try:
                    pnr = int(input("Enter a social security number: "))
                    acc_nr = int(input("Enter customers account number: "))
                    amount = float(input("How much do you want to deposit? "))
                    b.deposit(pnr, acc_nr, amount)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers for all fields")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "9":
            while True:
                try:
                    pnr = int(input("Enter a social security number: "))
                    acc_nr = int(input("Enter customers account number: "))
                    amount = float(input("How much do you want to withdraw? "))
                    b.withdraw(pnr, acc_nr, amount)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers for all fields")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "10":
            while True:
                try:
                    acc_nr = int(input("Enter customers account number that will be deleted: "))
                    b.close_account(acc_nr)
                    input("Press enter to continue")
                    clear_console()
                    break
                except ValueError:
                    print("Please use numbers for all fields")
                except KeyboardInterrupt:
                    print("\nReturning to menu")
                    input("Press enter to continue")
                    clear_console()
                    break

        elif ans == "11":
            print("Thanks for using the NBI Bank Application. See you soon!")
            quit()

        else:
            clear_console()
            ans = True
