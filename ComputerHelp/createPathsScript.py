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
event = open("C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/eventlog.csv", "w")
event.write("rowNumber,PersonId,State \n")

quote = open("C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/quote.csv", "w")
quote.write("rowNumber,PersonId,Price,PriceType, State \n")

rev = open("C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/revenue.csv", "w")
rev.write("rowNumber,PersonId,Price,Objects, State \n")

issues = open("C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/issues.csv", "w")
issues.write("rowNumber,PersonId,Solved ,State \n")

loyal = open("C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/loyal.csv", "w")
loyal.write("rowNumber,PersonId,Loyal \n")

evaluation = open("C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/evaluation.csv", "w")
evaluation.write("rowNumber, PersonId, State, score, scoreName, Channel \n")

### various states; with its eventlog creation ###
def stateOne(person):
    #add event
    createEvent(person.nr, 's1')
    #determine next step
    r = random.randint(0,100)
    if(person.age >= 50):
        if (r <= 50): stateThree(person, False)
        elif (r <= 60): stateTwo(person, False)
        else: stateNine(person, False)
    else: 
        if (r <= 10): stateThree(person, False)
        elif (r <= 60): stateTwo(person, False)
        else: stateNine(person, False)
        

def stateTwo(person, loyal):
    createEvent(person.nr, 's2')
    #determine next step
    r = random.randint(0,100)
    s = random.randint(0, 80)
    if(s < 20):
         makeEvaluation(person,loyal,'CES', 's2', False)
         makeEvaluation(person,loyal,'NPS', 's2', False)
    if(person.gender == 'female'):
        if r <= 65: stateFour(person, loyal)
        else: stateNine(person, loyal)
    else: 
        if r <= 55: stateFour(person, loyal)
        else: stateNine(person, loyal)

def stateThree(person, loyal ):
    createEvent(person.nr, 's3')
    s = random.randint(0, 80)
    if(s < 20):
         makeEvaluation(person,loyal,'CES', 's3', False)
         makeEvaluation(person,loyal,'NPS', 's3', False)
    #determine next step
    stateFour(person, loyal)

def stateFour(person,loyal):
    createEvent(person.nr, 's4')
    makePrice(person, loyal, 's4')
    #determine next step
    r = random.randint(0,100)
    if person.gender == 'female' or loyal:
       
        if r <= 45: stateFive(person, loyal)
        elif r <= 85: stateFour(person, loyal)
        else: stateNine(person, loyal)
    else:
        if r <= 30: stateFive(person, loyal)
        elif r <= 70: stateFour(person, loyal)
        else: stateNine(person, loyal)


def stateFive(person, loyal):
    global totalprice
    global objects
    createEvent(person.nr, 's5')
    createRev(person.nr, totalprice, objects)
    s = random.randint(0, 80)
    if(s < 20):
         makeEvaluation(person,loyal,'CES', 's5', False)
         makeEvaluation(person,loyal,'NPS', 's5', False)
    #determine next step
    r = random.randint(0,100)
    if loyal:
        if r <= 10: 
            stateFive(person, loyal)
            objects += 1
        elif r <= 97: stateSix(person, loyal, False)
        else: stateNine(person, loyal)
    elif person.age >= 50:
        if r <= 10: 
            stateFive(person, loyal)
            objects += 1
        elif r <= 80: stateSix(person, loyal, False)
        else: stateNine(person, loyal)
    else:
        if r <= 10: 
            stateFive(person, loyal)
            objects += 1
        elif r <= 60: stateSix(person, loyal, False)
        else: stateNine(person, loyal)

def stateSix(person,loyal, issue):
    global totalprice
    global objects
    createEvent(person.nr, 's6')
    createRev(person.nr, -1 * totalprice, objects)
    objects = 0
    #determine next step
    r = random.randint(0,100)
    if issue:
        stateEight(person, loyal, issue)
    else:
        if r <= 60: stateEight(person, loyal, issue)
        else: stateSeven(person, loyal)

def stateSeven(person, loyal):
    createEvent(person.nr, 's7')
    s = random.randint(0, 80)
    
    #determine next step
    s = random.randint(0,1)
    r = random.randint(0,100)
    if s == 0:
        makeEvaluation(person, loyal, 'CES', 's7', False)
        makeEvaluation(person, loyal, 'NPS', 's7', False)
        createIssue(person.nr, 'Not Solved')
        if r <= 10: stateNine(person, loyal)
        elif r <= 60: stateFive(person, loyal)
        else: stateSix(person, loyal,False)
    else: 
        makeEvaluation(person, loyal, 'CES', 's7', True)
        makeEvaluation(person, loyal, 'NPS', 's7', True)
        createIssue(person.nr, 'Solved') 
        stateSix(person, loyal,True)


def stateEight(person, loyal, issue):
    createEvent(person.nr, 's8')
    s = random.randint(0,80)
    if(s < 20):
         makeEvaluation(person,loyal,'CES', 's8', issue)
         makeEvaluation(person,loyal,'NPS', 's8', issue)
    if issue:
        stateNine(person, loyal)
    elif loyal:
        r = random.randint(0,100) 
        if r <= 5: stateThree(person, True)
        elif r <= 10: stateTwo(person, True)
        else: stateNine(person, loyal)
    elif person.age >= 50:
        r = random.randint(0,100) 
        if r <= 15: stateThree(person, True)
        elif r <= 18: stateTwo(person, True)
        else: stateNine(person, loyal)
    else:
        r = random.randint(0,100) 
        if r <= 5: stateThree(person, True)
        elif r <= 15: stateTwo(person, True)
        else: stateNine(person, loyal)
    
    
   
def stateNine(person,loyal):
    global objects
    objects = 0
    createEvent(person.nr, 's9')
    if loyal: createLoyal(person.nr)



#Make an evaluation
def makeEvaluation(person, loyal, scoreName, state, solved):
    rc = random.randint(0,3)
    r = random.randint(1,10)
    rnps = r 
    rces = r 
    re = r
    
    if person.age >= 50:
        rnps    += 3
        rces    += 2
        re      += 2

    elif person.age >= 25 and person.age < 50:
        rnps    += 2
        rces    += 2
        re      += 2
    
    if person.gender == 'female':
        rnps    += 2
        rces    += 1
        re      += 1

    if person.company is not None:
        rces    -= 2
    
    if loyal:
        rnps    += 4
        rces    += 4
        re      += 3  
   
    
        
    if state == 's7' and solved:
        rnps    += 2
        rces    += 1
    elif state == 's7':
        rnps    -= 3
        rces    -= 1
    elif state == 's3':
        rnps    += 3
        rces    += 3
    elif state == 's2':
        rnps -= 2
        rnps -= 2
    
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
    if loyal:
         r = random.randint(60,500)
    elif person.age <= 25 :
        r = random.randint(10,100)
    elif person.age > 25 and person.age < 50 and person.gender == 'female':
        r = random.randint(20,150)
    elif person.age > 25 and person.age < 50 and person.company is not None:
        r = random.randint(150,1000)
    elif person.age > 25 and person.age < 50:
        r = random.randint(10,50)
    else:
        r = random.randint(75,600)

        totalprice = r
        objects += 1
        createQuote(person.nr, r, 'ComputerQuote')
   
         
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
    quote.write(str(quoterowNumber) + "," + str(personnumber) + "," + str(price) + "," + pricetype+ ",s4" + "\n")

#adding revenue
def createRev(PersonId,Price,Objects):
    global revrowNumber
    revrowNumber += 1
    rev.write(str(revrowNumber) + "," + str(PersonId) + "," + str(Price) + "," + str(Objects)+ ",s5" + "\n")

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
    issues.write(str(evaluationrowNumber) + "," + str(personnumber) + solved + ",s7" + "\n")
     
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

 
