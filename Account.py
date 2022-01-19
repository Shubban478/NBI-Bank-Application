class Account:

    def __init__(self, name, pnr, acc_nr, balance, acc_type = "Debit Account"):
        self.name = name
        self.pnr = pnr
        self.acc_nr = acc_nr
        self.balance = float(balance)
        self.acc_type = acc_type
