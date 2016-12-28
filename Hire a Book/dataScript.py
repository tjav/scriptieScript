import csv

companies   = []
firstnames  = []
lastnames   = []

with open("C:/Users/Tim/Documents/GitHub/scriptieScript/Hire a Book/InputCSV/company.csv", 'r') as comp:
    data_iter = csv.reader(comp, delimiter = " ",  quotechar = '|' )
    for row in data_iter:
        companies.append(', '.join(row))       


with open("C:/Users/Tim/Documents/GitHub/scriptieScript/Hire a Book/InputCSV/firstnames.csv",'r') as fn:
    data_iter = csv.reader(fn, delimiter = " ",  quotechar = '|' )
    for row in data_iter:
        firstnames.append(', '.join(row)) 

with open("C:/Users/Tim/Documents/GitHub/scriptieScript/Hire a Book/InputCSV/lastnames.csv",'r') as ln:
    data_iter = csv.reader(ln, delimiter = " ",  quotechar = '|' )
    for row in data_iter:
        lastnames.append(', '.join(row))

        