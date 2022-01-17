class Account:

    def __init__(self, name, pnr, acc_nr, acc_type, balance):
        self.name = name
        self.pnr = int(pnr)
        self.acc_nr = int(acc_nr)
        self.acc_type = acc_type
        self.balance = float(balance)
