class Person:
    def __init__(self, nr, name, email, company, gender, location):
        self.nr         = nr
        self.email      = email
        self.name       = name
        self.company    = company
        self.gender     = gender
        self.location   = location

    def __str__(self):
        return str(self.nr) + "," + str(self.email) + "," + str(self.name) + "," + str(self.company) + "," + self.gender + "," + self.location
    
    def __getitem__(self):
        return self
    
