class Transactions:
    
    def __init__(self, pnr, trans_id, cust_id, acc_nr, date, amount):
        self.pnr = int(pnr)
        self.trans_id = int(trans_id)
        self.cust_id = int(cust_id)
        self.acc_nr = int(acc_nr)
        self.date = date
        self.amount = amount
