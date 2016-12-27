import random
import csv
from createPeopleScript import persons

#global variables

rowNumber = 0

books = 0

#Open files and write the header
event = open("C:/Users/Tim/Documents/GitHub/scriptieScript/Ebicus/OutputCSV/eventlog.csv", "w")
event.write("rowNumber,PersonId,State,LifeCycle,Loyal,NoB,Issue,Fine,Score,ScoreName,NPS-score\n")



### various states; with its eventlog creation ###
def stateOne(person):
    #add event
    createEvent(person, 's1','Awareness',None,None,None,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if (r <= 30): stateTwo(person, False, False)
    else: stateEleven(person, None, None)
    

def stateTwo(person, loyal, issue):
    global books
    books = 1
    S = random.randint(0,100)
    if(S < 11):
         makeEvaluation(person, 's2','Awareness',None,None,None,None,None,'NPS',None)
    else:
        createEvent(person, 's2','Awareness',None,None,None,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if (r < 20): stateThree(person, loyal, issue)
    elif (r < 80): stateFour(person, loyal, issue, 's2')
    else: stateEleven(person, loyal, issue)

def stateThree(person, loyal, issue):
    createEvent(person, 's3','Evaluation',None,None,None,None,None,None,None)
    #determine next step
    stateFour(person,loyal,issue, 's3')
    
def stateFour(person,loyal,issue,state):
    
    S = random.randint(0,100)
    if(S < 20):
        makeEvaluation(person, 's4','Evaluation',None,None,None,None,None,'CES',None)
        makeEvaluation(person, 's4','Evaluation',None,None,None,None,None,'NPS',None)
    else:
        createEvent(person, 's4','Evaluation',None,None,None,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if (state == 's3'):
        if r <= 40: stateFive(person, loyal, issue)
        else: stateEleven(person,loyal,issue)
    elif (state == 's5'):
        if r <= 50: stateSix(person, loyal, issue)
        else: stateFive(person, loyal,  issue)
    else:
        if r <= 30: stateThree(person, loyal, issue)
        elif r <= 70: stateFive(person, loyal,  issue)
        else: stateEleven(person,loyal,issue)

def stateFive(person, loyal, issue):
    global books
    books += 1
    S = random.randint(0,100)
    if(S < 30):
        makeEvaluation(person, 's5','Evaluation',None,None,None,None,None,'CES',None)
        makeEvaluation(person, 's5','Evaluation',None,None,None,None,None,'NPS',None)
    else:
        createEvent(person, 's5','Evaluation',None,None,None,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if (r < 40): stateFour(person, loyal,issue, 's5')
    elif (r<80): stateSix(person,loyal,issue)
    else: stateEleven(person,loyal,issue)

def stateSix(person,loyal,issue):
    global books
    S = random.randint(0,100)
    if(S < 20):
        makeEvaluation(person, 's6','Purchase',None,books,None,None,None,'CES',None)
        makeEvaluation(person, 's6','Purchase',None,books,None,None,None,'NPS',None)
    
    createEvent(person, 's6','Purchase',None,books,None,None,None,None,None)
    #determine next step
    stateSeven(person, loyal, issue)

def stateSeven(person, loyal, issue):
    global books
    S = random.randint(0,100)
    if(S < 40):
        makeEvaluation(person, 's7','Use',None,books,None,None,None,'CES',None)
        makeEvaluation(person, 's7','Use',None,books,None,None,None,'NPS',None)
    else:
        createEvent(person, 's7','Use',None,books,None,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if r <= 10: 
        stateTwo(person, True, issue)
    elif r <= 90: stateNine(person, loyal, issue)
    else: stateEight(person, loyal, issue)

def stateEight(person, loyal, issue):
    global books
    S = random.randint(0,100)
    if S < 40:
        makeEvaluation(person, 's8','Use',None,books,None,None,None,'CES',None)
        makeEvaluation(person, 's8','Use',None,books,None,None,None,'NPS',None)
    else:
        createEvent(person, 's8','Use',None,books,None,None,None,None,None)
    stateTen(person,loyal,True)

    
   
def stateNine(person,loyal, practice, PracticeName, issue):
    global books
    S = random.randint(0,100)
    if(S < 35):
        makeEvaluation(person,'s9', practice, PracticeName, 'Use',loyal, issue, None, 'CES', None, None,None,None,None,None)
        makeEvaluation(person,'s9', practice, PracticeName, 'Use',loyal, issue, None, 'NPS', None, None,None,None,None,None)
    else:
        createEvent(person, 's9', practice, PracticeName, 'Use', loyal, issue, None,None,None,None,None,None,None,None)
    r = random.randint(0,100)
    #determine next step
    if issue:
        stateTen(person,loyal,practice,PracticeName,issue)
    else:
        if r <= 40:
            stateFour(person,True,practice,PracticeName,issue)
        else:
            stateTen(person,loyal,practice,PracticeName,issue)
def stateTen(person,loyal,issue):
    global books
    S = random.randint(0,100)
    if S < 40:
        makeEvaluation(person, 's8','Use',None,books,None,None,None,'CES',None)
        makeEvaluation(person, 's8','Use',None,books,None,None,None,'NPS',None)
    else:
        createEvent(person, 's8','Use',None,books,None,None,None,None,None)
    stateEleven(person,loyal, True)

def stateEleven(person, loyal, issue):
    createEvent(person, 's10','End',None,books,None,None,None,None,None)

#Make an evaluation
def makeEvaluation(person,state, practice, PracticeName,stateName,loyal, issue, score, scoreName, NPSscore, channel,quotePrice,quoteType,revPrice,revObjects):
    rc = random.randint(0,3)
    r = random.randint(2,10)
    rnps = r 
    rces = r 
    
    if practice == 0 and person.location == 'nl' or practice == 5 and person.location == 'nl':
        rnps    += 4
        rces    += 4
    elif practice == 0 or practice == 5:
        rnps    += 3
        rces    += 3
    elif practice == 1 and person.location == 'de':
        rnps    -= 2
        rces    -= 2
    elif practice == 1:
        rnps    -= 4
        rces    -= 4
    elif practice == 4 and person.location == 'be':
        rnps    -= 3
        rces    -= 3
    elif practice == 3 and person.location == 'se':
        rnps    -= 3
        rces    -= 3
    elif practice == 4:
        rnps    += 3
        rces    += 3
    
    if loyal:
        rnps    += 4
        rces    += 4 
    if person.location == 'nl':
        rnps    += 2
        rces    += 2
   
        
    if issue == 'Solved':
        rnps    += 2
        rces    += 1
    elif issue == 'Not Solved':
        rnps    -= 3
        rces    -= 3
    
    if rnps > 10: rnps = 10
    elif rnps < 1: rnps = 1
    
    if rces > 10: rces = 10
    elif rces < 1: rces = 1
    
        
    if scoreName == 'CES':
        score = rces
    else:
        score = rnps
        if score < 7:
            NPSscore = -1
        elif score > 8 :
            NPSscore = 1
        else:
            NPSscore = 0

    createEvent(person, state, practice, PracticeName, stateName, loyal, issue, score,scoreName,NPSscore,None,None,None,None,None)

# create a price
def makePrice(person,state, practice, PracticeName,stateName,loyal, issue, score, scoreName, NPSscore, channel,quotePrice,quoteType,revPrice,revObjects):
    global totalprice
    
    if loyal:
        r = random.randint(50000,100000)
    elif practice == 0 and person.location == 'nl' or practice == 5 and person.location == 'nl':
        r = random.randint(70000,90000)
    elif practice == 0 or practice == 5:
        r = random.randint(10000,30000)
    elif practice == 1 and person.location == 'de':
        r = random.randint(40000, 80000)
    elif practice == 1:
        r = random.randint(5000, 15000)
    elif practice == 3 and person.location == 'se':
        r = random.randint(50000,75000)
    elif practice == 3:
        r = random.randint(10000,50000)
    elif practice == 4:
        r = random.randint(8000,40000)
    else:
        r = random.randint(5000,60000)

    totalprice = r
    createEvent(person, state, practice, PracticeName, stateName, loyal, issue, score,scoreName,NPSscore,None, r,'Consultant',None,None)
    
        

#adding event to eventlog 
def createEvent(person,state, practice, PracticeName,stateName,loyal, issue, score, scoreName, NPSscore, channel,quotePrice,quoteType,revPrice,revObjects):
    personnumber = person.nr
    if practice == None:
         practice = ''
    else: practice = str(practice)
    if PracticeName == None:
         PracticeName = ''
    if loyal:
         loyal = 'Loyal'
    else: loyal = ''
    if issue == None:
        issue = ''
    elif issue == False:
        issue = 'Not Solved'
    elif issue == True:
        issue = 'Solved'
    if score == None:
         score = ''
    else: score = str(score)
    if scoreName == None:
         scoreName = ''
    if NPSscore == None:
         NPSscore = ''
    else: NPSscore = str(NPSscore)
    if channel == None:
         channel = ''
    else: channel = str(channel)
    if quotePrice == None:
         quotePrice = ''
    else: quotePrice = str(quotePrice)
    if quoteType == None:
         quoteType = ''
    if revPrice == None:
         revPrice = ''
    else: revPrice = str(revPrice)
    if revObjects == None:
         revObjects = ''
    else: revObjects = str(revObjects)

    global rowNumber
    rowNumber += 1
    event.write(str(rowNumber) + "," + str(personnumber) + "," + state  + "," + practice + "," + PracticeName + "," + stateName + "," + loyal + "," + issue + "," + score + "," + scoreName + "," + NPSscore + "," + channel + "," + quotePrice + "," + quoteType + "," + revPrice + "," + revObjects +  "\n")


     
# put all persons through the stages    
for each in persons:
    
    stateOne(each)

# close csv
event.close()


 
