from uuid import uuid4


class Customer:

    def __init__(self, cust_id, name, pnr):
        self.uid = uuid4()
        self.cust_id = cust_id
        self.name = name
        self.pnr = pnr
