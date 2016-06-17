from createPathsScript import eventlog
from createPathsScript import persons
import csv

loyalpersons = []

for i in range(len(persons)):
    pRecord = persons[i]
    pId = pRecord.nr
    findLoyal(pId)

def findLoyal(personId):
    rowNumber = 1
    event = [each for each in eventlog if eventlog.nameID == personId]
    
    for i in reversed(event):
        if event.state == 's6' and event[i+1] is not 's8':
            loyalpersons.append(loyalpersons(rowNumber, personId, 'Loyal'))

# loyal persons to csv
lcsv = csv.writer(open("OutputCSV/loyalpersons.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
lcsv.writerow(loyalpersons)