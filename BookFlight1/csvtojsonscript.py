import csv
import json
from eventlogScript import Eventlog
 
eventlog = []
personCounter = -1
source = " "
target = " "
text = " "
counter = 0

def addLink(source, target):
   global text
   global counter
   global personCounter
   counter += 1
   text = text + '{"source": ' + source +  ',"target": ' + target + ',"value":"1.0"}, \n'
   if(counter % 30000 == 0):
       print (str(counter) + " " + str(personCounter))
   

def findLink(person,state):
    global personCounter
    global source
    global target
    if (target is not " "):
        source = target
    if (personCounter == person):
        if (source == '"Advocate"' or source == '"End"'):
            target = '"End"'
        elif (state == 's1'):
            target = '"Awareness"'
        elif (state == 's2'):
            if(source == '"Purchase"' or source == '"Use"'):
                target = '"Advocate"'
            else:
                target = '"Awareness"'
        elif (state == "s3" or state == "s5"):
            target = '"Evaluation"'
        elif (state == "s4"):
            target == '"Purchase"'
        elif (state == "s6" or state == "s7"):
            target = '"Use"'
        elif (state == "s8"):
            target = '"End"'
        


        if (source is not target):
            if(source is not '"Evaluation"' and target is not '"Awareness"'):
                addLink(source, target)
    else:
        target = " "
        personCounter += 1
        if (state == "s1" or "s2"):
           target = '"Awareness"'

with open('OutputCSV/previous output/eventlogs.csv', newline='') as csvfile:
   spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in spamreader:
       personNr = int(row[1])
       if( personNr < 99998):
            findLink(personNr,row[2])

def writeJson(jsonText):
    with open('OutputCSV/data.txt', 'w') as outfile:
        json.dump(jsonText, outfile)

def finalizeText():
    global text
    jsonText = '{ "links" : [ \n' + text + ' \n "nodes" : [ \n {"name":"Awareness"}, \n {"name":"Evaluation"}, \n {"name":"Purchase"}, \n {"name":"Use"}, \n {"name":"Advocate"}, \n {"name":"End"} ] }'
    writeJson(jsonText)

finalizeText()