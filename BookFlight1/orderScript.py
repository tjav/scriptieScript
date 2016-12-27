class Order:
    def __init__(self, nr, nameID, state, price, orderType):
        self.nr = nr
        self.nameID = nameID
        self.state = state
        self.price = price
        self.orderType = orderType
    
    def __str__(self):
        return str(self.nr) + "," + str(self.nameID) + "," + self.state + "," + str(self.price) + "," + self.orderType
    
    def __getitem__(self):
        return self
    