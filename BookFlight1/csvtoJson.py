import csv
import json
from eventlogScript import Eventlog
 
eventlog = []
personCounter = -1
source = " "
target = " "
counter = 0
an = 0
ae = 0
en = 0
ep = 0
pn = 0
pa = 0
pu = 0
un = 0
ua = 0
adn = 0

def writeJson(jsonText):
    file = open('OutputCSV/data.json', 'w')
    file.write(jsonText)
    file.close()

def addLinks():
   global an, ae, en, ep, pn, pa, pu, un, ua, adn
   en = ae-ep
   text = '{"source": "Awareness","target": "End","value":"'+ str(an) +'.0"}, \n'
   text = text + '{"source": "Awareness","target": "Evaluation","value":"'+ str(ae) +'.0"}, \n'
   text = text + '{"source": "Evaluation","target": "End","value":"'+ str(en) +'.0"}, \n'
   text = text + '{"source": "Evaluation","target": "Purchase","value":"'+ str(ep) +'.0"}, \n'
   text = text + '{"source": "Purchase","target": "End","value":"'+ str(pn) +'.0"}, \n'
   text = text + '{"source": "Purchase","target": "Advocate","value":"'+ str(pa) +'.0"}, \n'
   text = text + '{"source": "Purchase","target": "Use","value":"'+ str(pu) +'.0"}, \n'
   text = text + '{"source": "Use","target": "End","value":"'+ str(un) +'.0"}, \n'
   text = text + '{"source": "Use","target": "Advocate","value":"'+ str(ua) +'.0"}, \n'
   text = text + '{"source": "Advocate","target": "End","value":"'+ str(adn) +'.0"} \n'
   jsonText = '{ "links" : [ \n' + text + ' \n], "nodes" : [ \n {"name":"Awareness"}, \n {"name":"Evaluation"}, \n {"name":"Purchase"}, \n {"name":"Use"}, \n {"name":"Advocate"}, \n {"name":"End"} ] }'
   writeJson(jsonText)
   

def findLink(person,state):
    global personCounter
    global source
    global target
    global an, ae, en, ep, pn, pa, pu, un, ua, adn
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
            target = '"Purchase"'
        elif (state == "s6" or state == "s7"):
            target = '"Use"'
        elif (state == "s8"):
            target = '"End"'
        

        if (source is not target):
            if(source == '"Awareness"'):
                if(target == '"End"'):
                    an += 1
                elif(target == '"Evaluation"'):
                    ae += 1
            if(source == '"Evaluation"'):
                if(target == '"End"'):
                    en += 1
                elif(target == '"Purchase"'):
                    ep += 1
            if(source == '"Purchase"'):
                if(target == '"End"'):
                    pn += 1
                elif(target == '"Use"'):
                    pu += 1
                elif(target == '"Advocate"'):
                    pa += 1
            if(source == '"Use"'):
                if(target == '"End"'):
                    un += 1
                elif(target == '"Advocate"'):
                    ua += 1
            if(source == '"Advocate"'):
                if(target == '"End"'):
                    adn += 1
                
                               
    else:
        target = " "
        personCounter += 1
        if (state == "s1" or "s2"):
           target = '"Awareness"'

with open('OutputCSV/previous output/eventlogs.csv', newline='') as csvfile:
   spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in spamreader:
       if len(row):
        findLink(int(row[1]),row[2])

addLinks()


