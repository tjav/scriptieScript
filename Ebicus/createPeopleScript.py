import random
import csv
from personScript import Person
from dataScript import companies, firstnames, lastnames

emails = ['@gmail.com','@xs4all.com','@planet.nl', '@live.com', '@me.com', '@hotmail.com', '@outlook.com', '@icloud.com']
locations = ['nl','be','de', 'se']
gender = ['male','female']

persons = []

def giveRandom(x):
    return x[random.randint(0,len(x)-1)]

def makePeople(number):
    #people = InstanceList[Person for i in range(number)]:
        
    for each in range(number):
        f = giveRandom(firstnames)
        l = giveRandom(lastnames)
        e = giveRandom(emails)
        c = giveRandom(companies)
        a = random.randint(18,80)
        persons.append(Person(each, f + " " + l, f + "." + l + e ,c,giveRandom(gender),giveRandom(locations), a))

makePeople(1000)
print (len(persons))

## evaluations to csv
wcsv = csv.writer(open("C:/Users/Tim/Documents/GitHub/scriptieScript/Ebicus/OutputCSV/persons.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
wcsv.writerow(persons)


