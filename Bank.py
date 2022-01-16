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
                Bank.proc_accounts.append(act.Account(line[1], line[3], line[4], line[5]))

    def get_customers(self):
        for c in Bank.proc_customers:
            print(c.name, c.pnr)

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
                break
        else:
            print(f'Did not find social security number {pnr}. Did you type it correctly?')
        # Tar bort kund med personnumret som angetts ur banken, alla kundens eventuella konton
        # tas också bort och resultatet returneras. Listan som returneras ska innehålla information
        # om alla konton som togs bort, saldot som kunden får tillbaka.

    def get_account(self, acc_nr):
        for x in Bank.proc_accounts:
            if x.acc_nr == acc_nr:
                print(x.name, x.acc_nr, x.acc_type, x.balance)
                break
        else:
            print(f'Did not find account: {acc_nr}. Did you type it correctly?')

    def deposit(self, pnr, acc_nr):
        # Gör en insättning på kontot, returnerar True om det gick bra annars False.
        pass

    def withdraw(self, pnr, account_nr, amount):
        # Gör ett uttag på kontot, returnerar True om det gick bra annars False.
        pass

    def close_account(self, acc_nr):
        if any(acc_nr in inner_list for inner_list in Bank.customers):
            for sub_list in Bank.customers:
                if acc_nr in sub_list:
                    indx = Bank.customers.index(sub_list)
                    print(f'Account {Bank.customers[indx][3]} was terminated and check with balance was sent. Balance left on account: {Bank.customers[indx][5]}')
                    del Bank.customers[indx][3:]
        else:
            print(f'No customer with account: {acc_nr} exists')

b = Bank()
b._load()