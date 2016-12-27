class LoyalPerson:
    def __init__(self, rowID, personID, loyalState):
        self.rowID = rowID
        self.personID = personID
        self.loyalState = loyalState

    def __str__(self):
        return str(self.rowID) + "," + str(self.personID) + "," + self.loyalState

    def __getitem__(self):
        return self