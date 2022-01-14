from Account import Account as a

class Bank:

    customers = []

    def __init__(self):
        self.pnr = ''
        self.name = ''

    def _load(self):
        with open('Customers.txt') as customer:
            for line in customer:
                Bank.customers.append(line.strip().split(':'))

    def get_customers(self):
        for customer in Bank.customers:
            print(customer)

    def add_customer(self, pnr, name):
        self.pnr = pnr
        self.name = name

        if any(self.pnr in cust for cust in Bank.customers):
            print(f'{self.pnr} is already a customer. Did you type in the wrong social security number?')
        else:
            Bank.customers.append([self.name, self.pnr])
            print(f'{self.name}  was added to customers')

    def change_customer_name(self, pnr):
        if any(pnr in inner_list for inner_list in Bank.customers):
            for sub_list in Bank.customers:
                if pnr in sub_list:
                    indx = Bank.customers.index(sub_list)
                    Bank.customers[indx][1] = input('Set new name: ')

    def get_customer(self, name):
        if any(name in inner_list for inner_list in Bank.customers):
            for sub_list in Bank.customers:
                if name in sub_list:
                    indx = Bank.customers.index(sub_list)
                    print(Bank.customers[indx])
        else:
            print(f'No customer {name} exists')

    def remove_customer(self, pnr):
        if any(pnr in inner_list for inner_list in Bank.customers):
            for sub_list in Bank.customers:
                if pnr in sub_list:
                    indx = Bank.customers.index(sub_list)
                    print(f'{Bank.customers[indx]} was removed from customers.')
                    del Bank.customers[indx]
        else:
            print(f'No customer {pnr} exists')
        # Tar bort kund med personnumret som angetts ur banken, alla kundens eventuella konton
        # tas också bort och resultatet returneras. Listan som returneras ska innehålla information
        # om alla konton som togs bort, saldot som kunden får tillbaka.

    def get_account(self, pnr, account_id):
        # Returnerar Textuell presentation av kontot med kontonummer som tillhör
        # kunden (kontonummer, saldo, kontotyp).
        pass

    def deposit(self, amount):
        a.saldo = a.saldo + int(amount)
        print(a.saldo)
        # Gör en insättning på kontot, returnerar True om det gick bra annars False.
        pass

    def withdraw(self, amount):
        a.saldo = a.saldo - int(amount)
        print(a.saldo)
        # Gör ett uttag på kontot, returnerar True om det gick bra annars False.

    def close_account(self, pnr, account_id):
        # Avslutar ett konto. Textuell presentation av kontots saldo ska genereras och returneras.
        pass
