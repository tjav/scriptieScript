import random
import csv
from createPeopleScript import persons
from eventlogScript import Eventlog

eventlog = []
rowNumber = 0

### various states; with its eventlog creation ###
def stateOne(person):
    #add event
    createEvent(person.nr, 's1')
    #determine next step
    r = random.randint(0,100)
    if r < 60: stateTwo(person)
    else: stateEight(person)

def stateTwo(person):
    createEvent(person.nr, 's2')
    #determine next step
    r = random.randint(0,100)
    if r < 26: stateTwo(person)
    elif r < 76: stateThree(person)
    else: stateEight(person)

def stateThree(person):
    createEvent(person.nr, 's3')
    #determine next step
    r = random.randint(0,100)
    if r <= 50: stateTwo(person)
    elif r <= 60: stateFive(person)
    elif r <= 75: stateFour(person)
    else: stateEight(person)

def stateFour(person):
    createEvent(person.nr, 's4')
    #determine next step
    r = random.randint(0,100)
    if r <= 5: stateTwo(person)
    elif r <= 15: stateSeven(person)
    elif r <= 95: stateSix(person)
    else: stateEight(person)


def stateFive(person):
    createEvent(person.nr, 's5')
    #determine next step
    r = random.randint(0,100)
    if r <= 20: stateThree(person)
    elif r <= 50: stateFive(person)
    elif r <= 95: stateFour(person)
    else: stateEight(person)

def stateSix(person):
    createEvent(person.nr, 's6')
    #determine next step
    r = random.randint(0,100)
    if r <= 10: stateTwo(person)
    else: stateEight(person)

def stateSeven(person):
    createEvent(person.nr, 's7')
    #determine next step
    r = random.randint(0,100)
    if r <= 5: stateSeven(person)
    elif r <= 95: stateSix(person)
    else: stateEight(person)

def stateEight(person):
    createEvent(person.nr, 's8')
    
#adding event to eventlog 
def createEvent(personnumber, state):
    global rowNumber
    rowNumber += 1
    eventlog.append(Eventlog(rowNumber, personnumber, state))
     
# put all persons through the stages    
for each in persons:
    stateOne(each)

# eventlog to csv
wcsv = csv.writer(open("OutputCSV/eventlogs.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
wcsv.writerow(eventlog)

 
