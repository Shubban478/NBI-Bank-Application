class Bank:

    customers = []

    def __init__(self):
        self.name = None
        self.pnr = None

    def _load(self):
        pass  # Laddar in från fil

    def get_customers(self):
        print(Bank.customers)

    def add_customer(self, pnr, name):
        self.name = name
        self.pnr = pnr

        if pnr in Bank.customers:
            print(f'{self.pnr} is already a customer. Did you type in the wrong personnummer?')
        else:
            Bank.customers.extend([self.pnr, self.name])
            print(f'{self.name}  was added to customers')

    def get_customer(self, pnr):
        pass

    def change_customer_name(self, name, pnr):
        pass

    def remove_customer(self, pnr):
        pass

    def add_account(self, pnr):
        pass

    def get_account(self, pnr, account_id):
        pass

    def deposit(self, pnr, account_id, amount):
        pass

    def withdraw(self, pnr, account_id, amount):
        pass

    def close_account(self, pnr, account_id):
        pass

    def get_all_transactions_by_pnr_acc_nr(self, pnr, acc_nr):
        pass


b = Bank()

b.add_customer(199305257975, 'Sebastian Lundgren')
b.add_customer(199205257975, 'Sluta Nu')
b.add_customer(199305257975, 'Sebastian Lundgren')

b.get_customers()