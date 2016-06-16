class Issues:
    def __init__(self, nr, name, issue):
        self.nr = nr
        self.name = name
        self.issue = issue
    
    def __str__(self):
        return str(self.nr) + "," + str(self.name) + "," + self.issue
    
    def __getitem__(self):
        return self
