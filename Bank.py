import Customer as ctr
import Account as act


class Bank:

    proc_customers = []
    proc_accounts = []
    customers = []
    accounts = []

    def _load(self):
        with open('Customers.txt') as customer:
            for line in customer:
                Bank.customers.append(line.strip().split(':'))
            for line in Bank.customers:
                Bank.proc_customers.append(ctr.Customer(line[0], line[1], line[2]))
                Bank.proc_accounts.append(act.Account(line[1], line[2], line[3], line[4], line[5]))

    def get_customers(self):
        for c in Bank.proc_customers:
            print(f'ID: {c.cust_id}, {c.name}, {c.pnr}')

    def add_customer(self, name, pnr):
        for x in Bank.proc_customers:
            if x.pnr == pnr:
                print(f'{name} is already a customer. Did you mean to add someone else?')
                break
            else:
                Bank.proc_customers.append(ctr.Customer(None, name, pnr))
                break

    def change_customer_name(self, pnr, name):
        for x in Bank.proc_customers:
            if x.pnr == pnr:
                x.name = name
                break
            else:
                print(f'{pnr} is not a customer. Did you mean to change name of someone else?')
                break

    def get_customer(self, pnr):
        for x in Bank.proc_customers:
            if x.pnr == pnr:
                print(x.cust_id, x.name, x.pnr)
                break
        else:
            print(f'Did not find social security number {pnr}. Did you type it correctly?')

    def remove_customer(self, pnr):
        for x in Bank.proc_customers:
            if x.pnr == pnr:
                Bank.proc_customers.remove(x)
                break
            else:
                print(f'Did not find social security number {pnr}. Did you type it correctly?')
                break

        for x in Bank.proc_accounts:
            if x.pnr == pnr:
                Bank.proc_accounts.remove(x)
                print(f'Customer {x.name} was removed.\nAccount: {x.acc_nr}, {x.acc_type} was also removed. Balance to be refunded: {x.balance}')
                break

    def get_account(self, acc_nr):
        for x in Bank.proc_accounts:
            if x.acc_nr == acc_nr:
                print(x.pnr, x.acc_nr, x.acc_type, x.balance)
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def deposit(self, pnr, acc_nr, amount):
        for x in Bank.proc_accounts:
            if x.pnr == pnr and x.acc_nr == acc_nr:
                new_balance = float(x.balance) + float(amount)
                x.balance = new_balance
                print(f'Deposit successful. New balance is: {x.balance}')
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def withdraw(self, pnr, acc_nr, amount):
        for x in Bank.proc_accounts:
            if x.pnr == pnr and x.acc_nr == acc_nr:
                new_balance = float(x.balance) - float(amount)
                if new_balance < 0:
                    print(f'Withdrawal denied. Not enough balance on account {acc_nr}.')
                else:
                    x.balance = new_balance
                    print(f'Withdrawal successful. New balance is: {x.balance}')
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def close_account(self, acc_nr):
        for x in Bank.proc_accounts:
            if x.acc_nr == acc_nr:
                print(f'{x.acc_type} {acc_nr} with balance: {x.balance} was terminated successfully')
                Bank.proc_accounts.remove(x)
                break
        else:
            print(f'Did not find account {acc_nr}. Did you type it correctly?')