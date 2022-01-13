from uuid import uuid4


class Customer:

    def __init__(self, pnr, name, surname):
        self.uid = uuid4()
        self.pnr = pnr
        self.name = name
        self.surname = surname
