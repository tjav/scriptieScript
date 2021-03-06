import random
import csv
from personScript import Person
from dataScript import companies, firstnames, lastnames

emails = ['@gmail.com','@xs4all.com','@planet.nl', '@live.com', '@me.com', '@hotmail.com', '@outlook.com', '@icloud.com']
locations = ['nl']
gender = ['male','female']

persons = []

def giveRandom(x):
    return x[random.randint(0,len(x)-1)]

def compRandom(x):
    y = random.randint(0,2)
    if y == 0: return giveRandom(x)
    else: return None

def makePeople(number):
    #people = InstanceList[Person for i in range(number)]:
        
    for each in range(number):
        f = giveRandom(firstnames)
        l = giveRandom(lastnames)
        e = giveRandom(emails)
        c = giveRandom(companies)
        a = random.randint(18,80)
        if not c:
           c = 'NULL'
        persons.append(Person(each, f + " " + l, f + "." + l + e ,c,giveRandom(gender),giveRandom(locations), a))
makePeople(100000)
print (len(persons))

## evaluations to csv
wcsv = csv.writer(open("C:/Users/Tim/Documents/GitHub/scriptieScript/Hire a Book/OutputCSV/persons.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
wcsv.writerow(persons)


