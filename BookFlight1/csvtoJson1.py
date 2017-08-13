import csv
import json
import pandas as pd

 
filter = []
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
    file = open('C:/Users/tivanbee/Source/Repos/scriptie/scriptieScript/BookFlight1/OutputCSV/FlightFemale.json', 'w')
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
    global personCounter 
    global source
    global target
    global filter
    global filterrunner
#set target and source
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
        
# count link
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


#load csv to dataframe
persons = pd.read_csv('C:/Users/tivanbee/Source/Repos/scriptie/scriptieScript/BookFlight1/OutputCSV/persons.csv', names=['PersonID','Email','Name','Company','Gender','Country','Age'], index_col = 'PersonID') #for setting index to colnumber add , index_col='rownumber'
events = pd.read_csv('C:/Users/tivanbee/Source/Repos/scriptie/scriptieScript/BookFlight1/OutputCSV/eventlog.csv', names=['Rownumber','PersonID','State','StateName','LifeCycle','Channel','Loyal','FlightPrice','Upsell','totalPrice','Issue','ScoreName','Score','NPS-score'], index_col = 'Rownumber' ) # for specifying the column names add , names=['name1','name2','etc']

#filter on male for example
persons_female = persons.filter(like='female' , axis=1) #compares the string 'male' in the 5th column

#an inner join on the filter
events_female = pd.merge(events, persons_female, on='PersonID', how='inner')

#go through the rows
for i in range(0,100000):
    event = events_male.filter(like=i, axis=0)
    for line in event:
            findLink(line[1],Line[2])

addLinks()



