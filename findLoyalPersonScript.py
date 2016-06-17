from createPathsScript import eventlog
from createPeopleScript import persons
from loyalPersonScript import LoyalPerson
import csv

loyalpersons = []
rowNumber = 0

def findLoyal(personId):
    global rowNumber
    event = [each for each in eventlog if each.nameID == personId] # select the event of the person
    j = 0
    for i in reversed(event):
        j += 1
        if i.state == 's6'or i.state == 's4':
            #print (event)
            eventNext = event[j] #get next event
            #print (eventNext)
            if eventNext.state == 's2':
                loyalpersons.append(LoyalPerson(rowNumber, personId, 'Loyal'))
                rowNumber += 1
        

# go through all persons
for pId in range(len(persons)): 
    findLoyal(pId)

# loyal persons to csv
lcsv = csv.writer(open("OutputCSV/loyalpersons.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
lcsv.writerow(loyalpersons)