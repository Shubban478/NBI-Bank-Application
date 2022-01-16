import Customer as ctr

customers = []

class Bank:

    def __init__(self):
        self.name = None
        self.pnr = None

    def _load(self):
        with open('Customers.txt') as customer:
            for line in customer:
                customers.append(line.strip().split(':'))

    def process_customer(self, data):
        proc_customers = []
        for student in customers:
            proc_customers.append(ctr.Customer(student[0], student[1], student[2]))
        return proc_customers

    def get_customers(self):
        for s in b.process_customer(customers):
            print(s.name, s.pnr)

    def add_customer(self, pnr, name):
        self.pnr = pnr
        self.name = name

        if any(self.pnr in cust for cust in customers):
            print(f'{self.pnr} is already a customer. Did you type in the wrong social security number?')
        else:
            customers.append([self.name, self.pnr])
            print(f'{self.name}  was added to customers')

    def change_customer_name(self, pnr):
        if any(pnr in inner_list for inner_list in customers):
            for sub_list in customers:
                if pnr in sub_list:
                    indx = customers.index(sub_list)
                    customers[indx][1] = input('Set new name: ')

    def get_customer(self, name):
        if any(name in inner_list for inner_list in customers):
            for sub_list in customers:
                if name in sub_list:
                    indx = customers.index(sub_list)
                    print(customers[indx])
        else:
            print(f'No customer {name} exists')

    def remove_customer(self, pnr):
        if any(pnr in inner_list for inner_list in customers):
            for sub_list in customers:
                if pnr in sub_list:
                    indx = customers.index(sub_list)
                    print(f'{customers[indx]} was removed from customers.')
                    del customers[indx]
        else:
            print(f'No customer {pnr} exists')
        # Tar bort kund med personnumret som angetts ur banken, alla kundens eventuella konton
        # tas också bort och resultatet returneras. Listan som returneras ska innehålla information
        # om alla konton som togs bort, saldot som kunden får tillbaka.

    def get_account(self, pnr):
        if any(pnr in inner_list for inner_list in customers):
            for sub_list in customers:
                if pnr in sub_list:
                    indx = customers.index(sub_list)
                    print(customers[indx][3:])
        else:
            print(f'No customer {pnr} exists')

    def deposit(self, pnr, account_nr):
        # Gör en insättning på kontot, returnerar True om det gick bra annars False.
        pass

    def withdraw(self, pnr, account_nr, amount):
        # Gör ett uttag på kontot, returnerar True om det gick bra annars False.
        pass

    def close_account(self, acc_nr):
        if any(acc_nr in inner_list for inner_list in customers):
            for sub_list in customers:
                if acc_nr in sub_list:
                    indx = customers.index(sub_list)
                    print(f'Account {customers[indx][3]} was terminated and check with balance was sent. Balance left on account: {customers[indx][5]}')
                    del customers[indx][3:]
        else:
            print(f'No customer with account: {acc_nr} exists')

b = Bank()
b._load()
b.get_customers()
