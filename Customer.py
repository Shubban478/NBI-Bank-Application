from uuid import uuid4


class Customer:

    def __init__(self, name, pnr, acc_nr):
        self.uid = uuid4()
        self.name = name
        self.pnr = pnr
        self.acc_nr = acc_nr
