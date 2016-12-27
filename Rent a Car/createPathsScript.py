import random
import csv
from createPeopleScript import persons

#global variables
objects = 0
rowNumber = 0
quoterowNumber = 0
revrowNumber = 0
issuesrowNumber = 0
loyalrowNumber = 0
evaluationrowNumber = 0
totalprice = 0

#Open files and write the header
event = open("OutputCSV/eventlog.csv", "w")
event.write("rowNumber,PersonId,State \n")

quote = open("OutputCSV/quote.csv", "w")
quote.write("rowNumber,PersonId,Price,PriceType \n")

rev = open("OutputCSV/revenue.csv", "w")
rev.write("rowNumber,PersonId,Price,Objects \n")

issues = open("OutputCSV/issues.csv", "w")
issues.write("rowNumber,PersonId,Solved \n")

loyal = open("OutputCSV/loyal.csv", "w")
loyal.write("rowNumber,PersonId,Loyal \n")

evaluation = open("OutputCSV/evaluation.csv", "w")
evaluation.write("rowNumber, personId, score, scoreName \n")

### various states; with its eventlog creation ###
def stateOne(person):
    #add event
    createEvent(person.nr, 's1')
    #determine next step
    r = random.randint(0,100)
    if(person.gender == "female"):
        if (r <= 70): stateTwo(person, False)
        else: stateEleven(person, False)
    else: 
        if r <= 45: stateTwo(person, False)
        else: stateEleven(person, False)
        

def stateTwo(person, loyal):
    createEvent(person.nr, 's2')
    #determine next step
    r = random.randint(0,100)
    if(r < 11):
         makeEvaluation(person,loyal,'site experience', 's2', False)
    if(person.gender == 'female'):
        if r <= 90: stateThree(person, loyal)
        else: stateEleven(person, loyal)
    else: 
        if r <= 80: stateThree(person, loyal)
        else: stateEleven(person, loyal)

def stateThree(person, loyal ):
    createEvent(person.nr, 's3')
    makeEvaluation(person,loyal,'CES', 's3', False)
    makePrice(person,loyal, 's3')
    #determine next step
    r = random.randint(0,100)
    if person.gender == 'female':
        if r <= 20: stateThree(person, loyal)
        elif r <= 60: stateFive(person,loyal)
        elif r <= 90: stateFour(person, loyal)
        else: stateEleven(person, loyal)
    else:
        if r <= 20: stateThree(person, loyal)
        elif r <= 30: stateFive(person,loyal)
        elif r <= 70: stateFour(person, loyal)
        else: stateEleven(person, loyal)

def stateFour(person,loyal):
    createEvent(person.nr, 's4')
    makePrice(person, loyal, 's4')
    #determine next step
    r = random.randint(0,100)
    if person.gender == 'male' or loyal or person.company is not None:
       
        if r <= 30: stateThree(person, loyal)
        elif r <= 45: stateFour(person, loyal)
        elif r <= 85: stateFive(person, loyal)
        else: stateEleven(person, loyal)
    else:
        if r <= 30: stateThree(person, loyal)
        elif r <= 40: stateFour(person, loyal)
        elif r <= 80: stateFive(person, loyal)
        else: stateEleven(person, loyal)


def stateFive(person, loyal):
    global totalprice
    global objects
    createEvent(person.nr, 's5')
    createRev(person.nr, totalprice, objects)
    #determine next step
    r = random.randint(0,100)
    if person.gender == 'female' or loyal or person.company is not None:
        if r <= 20: stateTwo(person, True)
        elif r <= 97: stateSeven(person, loyal)
        else: stateSix(person, loyal)
    else:
        if r <= 10: stateTwo(person, True)
        elif r <= 95: stateSeven(person, loyal)
        else: stateSix(person, loyal)

def stateSix(person,loyal):
    global totalprice
    global objects
    createEvent(person.nr, 's6')
    createRev(person.nr, -1 * totalprice, objects)
    #determine next step
    stateEleven(person, loyal)

def stateSeven(person, loyal):
    createEvent(person.nr, 's7')
    makeEvaluation(person,loyal,'CES', 's7', loyal)
    #determine next step
    r = random.randint(0,100)
    if r <= 5: stateSix(person, loyal)
    elif r <= 95: stateNine(person, loyal, False)
    else: stateEight(person, loyal, 's7')

def stateEight(person, loyal, state):
    createEvent(person.nr, 's8')
    r = random.randint(0,1)
    if r == 0:
        makeEvaluation(person, loyal, 'CES', 's8', False)
        makeEvaluation(person, loyal, 'NPS', 's8', False)
        createIssue(person.nr, 'Not Solved')
        if state == 's7':
            stateSix(person,loyal)
        else: stateEleven(person,loyal)
    else: 
        makeEvaluation(person, loyal, 'CES', 's8', True)
        makeEvaluation(person, loyal, 'NPS', 's8', True)
        createIssue(person.nr, 'Solved')
        if state == 's7' or state == 's9':
            stateNine(person,loyal,True)
        else: stateEleven(person,loyal)

    
   
def stateNine(person,loyal, issue):
    createEvent(person.nr, 's9')
    r = random.randint(0,100)
    #determine next step
    if person.age <= 25:
        if r <= 15:
            stateEight(person, loyal, 's9')
        else: stateTen(person, loyal, issue)
    else:
        if r<= 5:
            stateEight(person, loyal, 's9')
        else: stateTen(person, loyal, issue)

def stateTen(person, loyal, issue):
    createEvent(person.nr, 's10')
    makeEvaluation(person, loyal, 'CES', 's10', issue)
    makeEvaluation(person, loyal, 'NPS', 's10', issue)
    #determine next step
    r = random.randint(0,100)
    if person.gender == 'female' or loyal or person.company is not None:
        if r <= 20: stateTwo(person, True)
        else: stateEleven(person, loyal)
    else:
        if r <= 10: stateTwo(person, True)
        else: stateEleven(person, loyal)

def stateEleven(person, loyal):
    createEvent(person.nr, 's11')
    if loyal: createLoyal(person.nr)

#Make an evaluation
def makeEvaluation(person, loyal, scoreName, state, solved):
    rc = random.randint(0,3)
    r = random.randint(1,10)
    rnps = r 
    rces = r 
    re = r
    
    if person.age <= 25:
        rnps    -= 1
        rces    -= 2
        re      -= 1
    
    if person.gender == 'female':
        rnps    += 2
        rces    += 1
        re      += 1

    if person.company is not None:
        rces    += 2
    
    if loyal:
        rnps    += 4
        rces    += 4
        re      += 3  
   
        
    if state == 's8' and solved:
        rnps    += 2
        rces    += 1
    elif state == 's8':
        rnps    -= 3
        rces    -= 1
    
    if rnps > 10: rnps = 10
    elif rnps < 1: rnps = 1
    
    if rces > 10: rces = 10
    elif rces < 1: rces = 1
    
    if re > 10: re = 10
    elif re < 1: re = 1
        
    if scoreName == 'site experience':
        score = re
    elif scoreName == 'CES':
        score = rces
    else:
        score = rnps

    createEvaluation(person.nr, state, score, scoreName , rc)

# create a price
def makePrice(person,loyal, state):
    global totalprice
    global objects
    if state == 's3':
        if person.age <= 25:
            r = random.randint(50,200)
        elif person.company is not None:
            r = random.randint(200, 1000)
        elif loyal or person.gender == 'female':
            r = random.randint(100,800)
        else:
            r = random.randint(75,600)

        totalprice = r
        objects = 1
        createQuote(person.nr, r, 'Car')
    else:
        s = random.randint(0,3)
        if s == 0:
            createQuote(person.nr, '200', 'Insurance')
            totalprice += 200
        elif s == 1:
            createQuote(person.nr, '50', 'Navigation')
            totalprice += 50
        elif s == 2:
            createQuote(person.nr, '60', 'Baby-seat')
            totalprice += 60
        else:
            createQuote(person.nr, '100', 'Extra driver')
            totalprice += 100
         
        objects += 1
        

#adding event to eventlog 
def createEvent(personnumber, state):
    global rowNumber
    rowNumber += 1
    event.write(str(rowNumber) + "," + str(personnumber) + "," + state + "\n")

#adding quote
def createQuote(personnumber, price, pricetype):
    global quoterowNumber
    quoterowNumber += 1
    quote.write(str(quoterowNumber) + "," + str(personnumber) + "," + str(price) + "," + pricetype+ "\n")

#adding revenue
def createRev(PersonId,Price,Objects):
    global revrowNumber
    revrowNumber += 1
    rev.write(str(revrowNumber) + "," + str(PersonId) + "," + str(Price) + "," + str(Objects)+ "\n")

#adding Evaluations
def createEvaluation(personnumber,state,score, scoreName, channel ):
    global evaluationrowNumber
    evaluationrowNumber += 1
    evaluation.write(str(evaluationrowNumber) + "," + str(personnumber) + "," + state + "," + str(score) + "," +scoreName + "," + str(channel) + "\n")

#adding Loyal
def createLoyal(personnumber):
    global loyalrowNumber
    loyalrowNumber += 1
    loyal.write(str(loyalrowNumber) + "," + str(personnumber) + ",Loyal" + "\n")

#adding issues
def createIssue(personnumber, solved):
    global issuesrowNumber
    issuesrowNumber += 1
    issues.write(str(evaluationrowNumber) + "," + str(personnumber) + solved + "\n")
     
# put all persons through the stages    
for each in persons:
    
    stateOne(each)

# close csv
event.close()
quote.close()
rev.close()
issues.close()
loyal.close()
evaluation.close()

 
