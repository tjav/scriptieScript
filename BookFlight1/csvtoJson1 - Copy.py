import csv
import json
import numpy as np
import pandas as pd


#global Variables

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
 
#create json

def writeJson(jsonText):
    file = open('C:/Users/tivanbee/Source/Repos/scriptie/scriptieScript/BookFlight1/OutputCSV/FlightComputer.json', 'w')
    file.write(jsonText)
    file.close()

     #make txt in json format
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
    
    global source
    global target
    target = state
#set target and source
    global an, ae, en, ep, pn, pa, pu, un, ua, adn
    
    
    
    
# count link
    if (source is not target):
        if(source == 'Awareness'):
            if(target == 'End'):
                an += 1
            elif(target == 'Evaluation'):
                ae += 1
        if(source == 'Evaluation'):
            if(target == 'End'):
                en += 1
            elif(target == 'Purchase'):
                ep += 1
        if(source == 'Purchase'):
            if(target == 'End'):
                pn += 1
            elif(target == 'Use'):
                pu += 1
            elif(target == 'Evaluation'):
                pa += 1
                source = 'Advocate'
        if(source == 'Use'):
            if(target == 'End'):
                un += 1
            elif(target == 'Evaluation'):
                ua += 1
                source = 'Advocate'
        if(source == 'Advocate'):
            if(target == 'End'):
                adn += 1

    source = target       
                               
    


#load csv to dataframe
persons = pd.read_csv('C:/Users/tivanbee/Source/Repos/scriptie/scriptieScript/BookFlight1/OutputCSV/persons.csv', names=['PersonID','Email','Name','Company','Gender','Country','Age']) #for setting index to colnumber add , index_col='rownumber'
events = pd.read_csv('C:/Users/tivanbee/Source/Repos/scriptie/scriptieScript/BookFlight1/OutputCSV/eventlog.csv', names=['Rownumber','PersonID','State','StateName','LifeCycle','Channel','Loyal','FlightPrice','Upsell','totalPrice','Issue','ScoreName','Score','NPS-score'], index_col = 'Rownumber' ) # for specifying the column names add , names=['name1','name2','etc']

#inner Join
join = pd.merge(persons, events, how='inner', on=['PersonID', 'PersonID'])

#select on male for example
select = join[join.Channel == 'Computer']
#select = join


#go through the rows
for i in range(0,10000):
    event = select[select.PersonID == str(i)]
    for index, line in event.iterrows():
            findLink(line.PersonID,line.LifeCycle)
    #target = " "
    #source = " "
addLinks()



