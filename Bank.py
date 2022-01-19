import Customer as ctr
import Account as act


class Bank:

    proc_customers = []
    accounts = []

    def _load(self):
        customers = []
        with open('Customers.txt') as customer:
            for line in customer:
                customers.append(line.strip().split(':'))
            for line in customers:
                Bank.proc_customers.append(ctr.Customer(line[0], line[1], line[2]))
                Bank.accounts.append(act.Account(line[1], line[2], line[3], line[4]))

    def get_customers(self):
        for c in Bank.proc_customers:
            print(f'ID: {c.cust_id}, {c.name}, {c.pnr}')

    def add_customer(self, name, pnr):
        for x in Bank.proc_customers:
            if x.pnr == pnr:
                print(f'{name} is already a customer. Did you mean to add someone else?')
                break
            else:
                gen_id = len(Bank.proc_customers) + 1000
                Bank.proc_customers.append(ctr.Customer(gen_id, name, pnr))
                print(f'{gen_id} {name} {pnr} was added to customers. Welcome to NBI Bank!')
                break

    def get_customer(self, pnr):
        for x in Bank.proc_customers:
            if pnr == "":
                print("Invalid input")
                break
            elif x.pnr == pnr:
                print(f'{x.cust_id}, {x.name}, {x.pnr}')
                break
        else:
            print(f'Did not find social security number {pnr}. Did you type it correctly?')

        for x in Bank.accounts:
            if pnr == "":
                break
            elif x.pnr == pnr:
                print(f'Found accounts for {x.name}: {x.acc_nr}, {x.acc_type}, {x.balance}')
                break
        else:
            print(f'No accounts found for {pnr}')

    def change_customer_name(self, pnr, name):
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
        for x in Bank.proc_customers:
            if x.pnr == pnr:
                Bank.proc_customers.remove(x)
                break
            else:
                print(f'Did not find social security number {pnr}. Did you type it correctly?')
                break

        for x in Bank.accounts:
            if x.pnr == pnr:
                Bank.accounts.remove(x)
                print(f'Customer {x.name} was removed.\nAccount: {x.acc_nr}, {x.acc_type} was also removed. Balance to be refunded: {x.balance}')
                break

    # TODO
    def add_account(self):
        pass

    def get_account(self, acc_nr):
        for x in Bank.accounts:
            if x.acc_nr == acc_nr:
                print(f'Owner: {x.name}, {x.pnr}\nAccount: {x.acc_nr}, {x.acc_type}, {x.balance}')
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def deposit(self, pnr, acc_nr, amount):
        for x in Bank.accounts:
            if x.pnr == pnr and x.acc_nr == acc_nr:
                new_balance = x.balance + float(amount)
                x.balance = new_balance
                print(f'Deposit successful. New balance is: {x.balance}')
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def withdraw(self, pnr, acc_nr, amount):
        for x in Bank.accounts:
            if x.pnr == pnr and x.acc_nr == acc_nr:
                new_balance = x.balance - float(amount)
                if new_balance < 0:
                    print(f'Withdrawal denied. Not enough balance on account {acc_nr}.\nCurrent balance is: {x.balance}')
                else:
                    x.balance = new_balance
                    print(f'Withdrawal successful. New balance is: {x.balance}')
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def close_account(self, acc_nr):
        for x in Bank.accounts:
            if x.acc_nr == acc_nr:
                print(f"{x.name}'s {x.acc_type} {acc_nr} with balance: {x.balance} was terminated successfully")
                Bank.accounts.remove(x)
                break
        else:
            print(f'Did not find account {acc_nr}. Did you type it correctly?')

    # TODO
    def get_all_transactions_by_pnr_acc_nr(self, pnr, acc_nr):
        pass


b = Bank()
b._load()