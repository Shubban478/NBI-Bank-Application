class Account:

    def __init__(self, cust_id, name, pnr, acc_nr, balance = 0, acc_type = "Debit Account"):
        self.cust_id = int(cust_id)
        self.name = name
        self.pnr = int(pnr)
        self.acc_nr = int(acc_nr)
        self.balance = float(balance)
        self.acc_type = acc_type
