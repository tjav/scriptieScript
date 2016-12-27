class Eventlog:
    def __init__(self, nr, nameID, state):
        self.nr         = nr
        self.nameID     = nameID
        self.state      = state

    def __str__(self):
        return str(self.nr) + ","  + str(self.nameID) + "," +  self.state 
    
    def __getitem__(self):
        return self