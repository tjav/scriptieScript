import random
import csv
from createPathsScript import eventlog
from createPeopleScript import persons
from orderScript import Order

quotes = []
rowNumber = 0

#create the order
def makeOrder(personID, state, company):
    if state == 's3' and company:
        r = random.randint(1000,4000) 
        makeOrderLog(personID, state, r, "Flight") 
    elif state == 's3':
        r = random.randint(50, 1500)
        makeOrderLog(personID, state, r, "Flight")     
    else:
        rn = random.randint(0,3)
        if rn == 0: makeOrderLog(personID, state, 40, 'Luggage')
        elif rn == 1: makeOrderLog(personID, state, 150, 'Car Rental' )
        elif rn == 2: makeOrderLog(personID, state, 120, 'Hotel Booking')
        else: makeOrderLog(personID, state, 40, 'Special check-in')
 
#create order record
def makeOrderLog(person, state, price, orderType):
    global rowNumber
    rowNumber += 1
    quotes.append(Order(rowNumber, person, state, price, orderType))            

#search through list
def searchEventlog(state):
    name = [events.nameID for events in eventlog if events.state == state]
    for each in name:
        searchPersons(each, state)
        

# search through persons
def searchPersons(nr, state):
    person = persons[nr]
    comp = person.company
    if comp: makeOrder(nr, state, True)
    else: makeOrder(nr, state, False)


#get persons state = s3
searchEventlog('s3')

#get persons state = s5
searchEventlog('s5')

## quotes to csv
wcsv = csv.writer(open("OutputCSV/quotes.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
wcsv.writerow(quotes)

