class Evaluation:
    def __init__(self, nr, nameID, state, score, scoreName, channel):
        self.nr         = nr
        self.nameID     = nameID
        self.state      = state
        self.score      = score
        self.scoreName  = scoreName
        self.channel    = channel
        

    def __str__(self):
        return str(self.nr) + "," + str(self.nameID) + "," + str(self.state) + "," + str(self.score) + "," + self.scoreName + "," + str(self.channel)

    def __getitem__(self):
        return self
    