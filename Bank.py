import Customer as ctr
import Account as act
import Transactions as tcs
import datetime as dt


class Bank:

    proc_customers = []
    accounts = []
    transactions = []
    custid_count = 1000
    custacc_count = 2000
    transaction_id = 1

    def _load(self):
        """Load existing customers and accounts from text file"""

        customers = []

        with open('Customers.txt') as customer:
            for line in customer:
                customers.append(line.strip().split(':'))
            for line in customers:
                Bank.proc_customers.append(ctr.Customer(line[0], line[1], line[2]))
                Bank.accounts.append(act.Account(line[0], line[1], line[2], line[3], line[4]))
                Bank.custid_count += 1
                Bank.custacc_count += 1

    def get_customers(self):
        """Prints all customers currently registered at the bank"""

        if not Bank.proc_customers:
            print("No customers registered")
        else:
            for c in Bank.proc_customers:
                print(f'ID: {c.cust_id}, {c.name}, {c.pnr}')

    def add_customer(self, name, pnr):
        """Register a new customer"""

        for x in Bank.proc_customers:
            if x.pnr == pnr:
                print(f'{name} is already a customer. Did you mean to add someone else?')
                break
            else:
                Bank.proc_customers.append(ctr.Customer(Bank.custid_count, name, pnr))
                print(f'{Bank.custid_count} {name} {pnr} was added to customers. Welcome to NBI Bank!')
                Bank.custid_count += 1
                break

    def get_customer(self, pnr):
        """Search for a customer by using the customers social security number"""

        for x in Bank.proc_customers:
            if x.pnr == pnr:
                print(f'{x.cust_id}, {x.name}, {x.pnr}')
                break
            elif pnr == "":
                print("Invalid input")
                break
        else:
            print(f'Did not find social security number {pnr}. Did you type it correctly?')

        for x in Bank.accounts:
            if x.pnr == pnr:
                print(f'Found accounts for {x.name}: {x.acc_nr}, {x.acc_type}, {x.balance}')

    def change_customer_name(self, pnr, name):
        """Search for a customer by using the social security number and enter a new name of the customer"""

        for x in Bank.proc_customers:
            if pnr == "":
                print("Invalid input")
                break
            elif x.pnr == pnr:
                x.name = name
                print(f'Name of {x.pnr} was changed to: {name}')
                break
        else:
            print(f'{pnr} is not a customer. Did you mean to change name of someone else?')

    def remove_customer(self, pnr):
        """Search for a customer by using the social security number and removes that customer"""

        for x in Bank.proc_customers:
            if x.pnr == pnr:
                Bank.proc_customers.remove(x)
                print(f'Customer {x.name} was removed.')
                break
        else:
            print(f'Did not find social security number {pnr}. Did you type it correctly?')

        for x in Bank.accounts:
            if x.pnr == pnr:
                print(f'Account for {x.name}: {x.acc_nr}, {x.acc_type} was removed. Balance: {x.balance} was refunded')
            if pnr == "":
                print('Invalid input')
                break

    def add_account(self, pnr):
        """Create a new account for the social security number that is entered. Account information will be printed"""

        for x in Bank.proc_customers:
            if x.pnr == pnr:
                Bank.accounts.append(act.Account(Bank.custid_count, x.name, pnr, Bank.custacc_count))
                print(f'Account {Bank.custacc_count} for {x.name} {pnr} was successfully created')
                Bank.custacc_count += 1
                break
        else:
            print(f'{pnr} is not a customer. Register as customer first')

    def get_account(self, acc_nr):
        """Search for a specific account and prints the owner and information about that account"""

        for x in Bank.accounts:
            if x.acc_nr == acc_nr:
                print(f'Owner: {x.name}, {x.pnr}\nAccount: {x.acc_nr}, {x.acc_type}, {x.balance}')
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def deposit(self, pnr, acc_nr, amount):
        """Make a deposit to a customers account by using social security number and account number"""

        for x in Bank.accounts:
            if x.pnr == pnr and x.acc_nr == acc_nr:
                new_balance = x.balance + float(amount)
                x.balance = new_balance
                date = dt.datetime.now()
                print(f'Deposit successful. New balance is: {x.balance}')
                Bank.transactions.append(tcs.Transactions(pnr, Bank.transaction_id, x.cust_id ,x.acc_nr, date.strftime("%d/%m/%Y %H:%M:%S"), amount))
                Bank.transaction_id += 1
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def withdraw(self, pnr, acc_nr, amount):
        """Try to withdraw from a customers account by using social security number and account number"""

        for x in Bank.accounts:
            if x.pnr == pnr and x.acc_nr == acc_nr:
                new_balance = x.balance - float(amount)
                if new_balance < 0:
                    print(f'Withdrawal denied. Not enough balance on account {acc_nr}.\nCurrent balance is: {x.balance}')
                else:
                    x.balance = new_balance
                    date = dt.datetime.now()
                    print(f'Withdrawal successful. New balance is: {x.balance}')
                    Bank.transactions.append(tcs.Transactions(pnr, Bank.transaction_id, x.cust_id, x.acc_nr, date.strftime("%d/%m/%Y %H:%M:%S"), str(f'-{amount}')))
                    Bank.transaction_id += 1
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def close_account(self, acc_nr):
        """Closes the account with the specified account number and prints information about the account"""

        for x in Bank.accounts:
            if x.acc_nr == acc_nr:
                print(f"{x.name}'s {x.acc_type} {acc_nr} with balance: {x.balance} was terminated successfully")
                Bank.accounts.remove(x)
                break
        else:
            print(f'Did not find account {acc_nr}. Did you type it correctly?')

    def get_all_transactions_by_pnr_acc_nr(self, pnr, acc_nr):
        """Get all transactions with the specified social security number and account number"""

        for x in Bank.transactions:
            if x.pnr == pnr and x.acc_nr == acc_nr:
                print(f'ID: {x.trans_id}, Customer ID: {x.cust_id}, Account number: {x.acc_nr}, Date: {x.date}, Amount: {x.amount}')
            else:
                print("No transactions found with credentials.")
        if not Bank.transactions:
            print("There are no transactions yet.")



b = Bank()
b._load()