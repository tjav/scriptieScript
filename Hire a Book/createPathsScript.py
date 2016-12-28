import random
import csv
from createPeopleScript import persons

#global variables

rowNumber = 0

books = 0

#Open files and write the header
event = open("C:/Users/Tim/Documents/GitHub/scriptieScript/Hire a Book/OutputCSV/eventlog.csv", "w")
event.write("rowNumber,PersonId,State,StateName,Loyal,Books,Issue,Fine,ScoreName,Score, NPS-score\n")



### various states; with its eventlog creation ###
def stateOne(person):
    #add event
    createEvent(person, 's1','Awareness',None,None,None,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if (r <= 30): stateTwo(person, None, None)
    else: stateEleven(person, None, None,None)
    

def stateTwo(person, loyal, issue):
    global books
    books = 1
    S = random.randint(0,100)
    
    if(S < 11):
         makeEvaluation(person, 's2','Awareness',loyal,books,issue,None,'NPS',None,None)
    else:
        createEvent(person, 's2','Awareness',loyal,books,issue,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if person.age <= 25 and person.gender == 'male':
        if (r < 5): stateThree(person, loyal, issue)
        elif (r < 40): stateFour(person, loyal, issue, 's2')
        else: stateEleven(person, loyal, issue,books)
    else:
        if (r < 20): stateThree(person, loyal, issue)
        elif (r < 80): stateFour(person, loyal, issue, 's2')
        else: stateEleven(person, loyal, issue,books)

def stateThree(person, loyal, issue):
    createEvent(person, 's3','Evaluation',loyal,books,issue,None,None,None,None)
    #determine next step
    stateFour(person,loyal,issue, 's3')
    
def stateFour(person,loyal,issue,state):
    global books
    S = random.randint(0,100)
    if(S < 20):
        makeEvaluation(person, 's4','Evaluation',loyal,books,issue,None,'CES',None,None)
        makeEvaluation(person, 's4','Evaluation',loyal,books,issue,None,'NPS',None,None)
    else:
        createEvent(person, 's4','Evaluation',loyal,books,issue,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if (state == 's3'):
        if person.gender == 'female':
            if r <= 70: stateFive(person, loyal, issue)
            else: stateEleven(person,loyal,issue,books)
        else:
            if r <= 40: stateFive(person, loyal, issue)
            else: stateEleven(person,loyal,issue,books)
    elif (state == 's5'):
        if r <= 50: stateSix(person, loyal, issue)
        else: stateFive(person, loyal,  issue)
    else:
        if person.age <= 25 and person.gender == 'male':
            if r <= 5: stateThree(person, loyal, issue)
            elif r <= 30: stateFive(person, loyal,  issue)
            else: stateEleven(person,loyal,issue, books)
        elif person.age >= 50 and person.gender == 'female':
            if r <= 40: stateThree(person, loyal, issue)
            elif r <= 90: stateFive(person, loyal,  issue)
            else: stateEleven(person,loyal,issue, books)


def stateFive(person, loyal, issue):
    global books
    books += 1
    S = random.randint(0,100)
    if(S < 30):
        makeEvaluation(person, 's5','Evaluation',loyal,books,issue,None,'CES',None,None)
        makeEvaluation(person, 's5','Evaluation',loyal,books,issue,None,'NPS',None,None)
    else:
        createEvent(person, 's5','Evaluation',loyal,books,issue,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if (r < 40): stateFour(person, loyal,issue, 's5')
    elif (r<80): stateSix(person,loyal,issue)
    else: stateEleven(person,loyal,issue,books)

def stateSix(person,loyal,issue):
    global books
    S = random.randint(0,100)
    if(S < 20):
        makeEvaluation(person, 's6','Purchase',loyal,books,issue,None,'CES',None,None)
        makeEvaluation(person, 's6','Purchase',loyal,books,issue,None,'NPS',None,None)
    
    createEvent(person, 's6','Purchase',loyal,books,issue,None,None,None,None)
    #determine next step
    stateSeven(person, loyal, issue)

def stateSeven(person, loyal, issue):
    global books
    S = random.randint(0,100)
    if(S < 40):
        makeEvaluation(person, 's7','Use',loyal,books,issue,None,'CES',None,None)
        makeEvaluation(person, 's7','Use',loyal,books,issue,None,'NPS',None,None)
    else:
        createEvent(person, 's7','Use',loyal,books,issue,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if person.age >= 50 and person.gender == 'female':
        if r <= 30: 
            stateTwo(person, True, issue)
        elif r <= 90: stateNine(person, loyal, issue)
        else: stateEight(person, loyal, issue)
    else:
        if r <= 10: 
            stateTwo(person, True, issue)
        elif r <= 90: stateNine(person, loyal, issue)
        else: stateEight(person, loyal, issue)

def stateEight(person, loyal, issue):
    global books
    S = random.randint(0,100)
    if S < 40:
        makeEvaluation(person, 's8','Use',loyal,books,issue,None,'CES',None,None)
        makeEvaluation(person, 's8','Use',loyal,books,issue,None,'NPS',None,None)
    else:
        createEvent(person, 's8','Use',loyal,books,issue,None,None,None,None)
    stateTen(person,loyal,True)

    
   
def stateNine(person,loyal, issue):
    global books
    S = random.randint(0,100)
    if(S < 35):
        makeEvaluation(person, 's9','Use',loyal,books,issue,None,'CES',None,None)
        makeEvaluation(person, 's9','Use',loyal,books,issue,None,'NPS',None,None)
    else:
        createEvent(person, 's9','Use',loyal,books,issue,None,None,None,None)
    r = random.randint(0,100)
    #determine next step

    if issue:
        stateEleven(person,loyal, issue, books)
    else:
        if person.age >= 50 and person.gender == 'female':
            if r <= 40:
                stateTwo(person,True, issue)
            else:
                stateEleven(person,loyal, issue, books)
        else:
            if r <= 10:
                stateTwo(person,True, issue)
            else:
                stateEleven(person,loyal, issue, books)


def stateTen(person,loyal,issue):
    global books
    makeFine(person, 's10','Use',loyal,books,issue,None,None,None,None)
    S = random.randint(0,100)
    if S < 40:
        makeEvaluation(person, 's10','Use',loyal,books,issue,None,'CES',None,None)
        makeEvaluation(person, 's10','Use',loyal,books,issue,None,'NPS',None,None)
    else:
        createEvent(person, 's10','Use',loyal,books,issue,None,None,None,None)
    r = random.randint(0,100)
    if r < 5:
        stateNine(person, loyal, True)
    else:
        stateEleven(person,loyal, True,books)

def stateEleven(person, loyal, issue, books):
    createEvent(person, 's11','End', loyal, books, issue, None, None, None, None)

#Make an evaluation
def makeEvaluation(person, state, stateName, loyal, books, issue, fine, scoreName, score, NPS):
    rc = random.randint(0,3)
    r = random.randint(1,10)
    rnps = r 
    rces = r 
    
    if person.age >= 50 and person.gender == 'female' or person.age >= 30 and person.age <= 40 and person.gender == 'male' and person.company == None:
        rnps    += 4
        rces    += 4
    elif person.gender == 'female' and person.company is not None:
        rnps    -= 3
        rces    -= 3
    elif person.gender == 'male'and person.age <= 25:
        rnps    += 5
        rces    += 5
    elif person.gender == 'male' and person.company is not None:
        rnps    -= 4
        rces    -= 4
    
    if loyal:
        rnps    += 4
        rces    += 4    
        
    if issue:
        rnps    -= 2
        rces    -= 1
    
    
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
        NPS = NPSscore
    
    createEvent(person, state, stateName, loyal, books, issue, fine, scoreName, score, NPS)

# create a price
def makeFine(person, state, stateName, loyal, books, issue, fine, scoreName, score, NPS):
    
    if loyal:
        r = random.randint(1,2)
    elif person.gender == 'female' and person.age >= 50 or person.gender == 'male' and person.age <= 30:
        r = random.randint(1,5)
    elif person.gender == 'male' and person.age <= 25:
        r = random.randint(2,8)
    elif person.gender == 'male' and person.company is not None:
        r = random.randint(1,10)
    elif books >= 6:
        r = random.randint(5, 20)
    else: 
        r = random.randint(2, 15)
    

    fine = r
    createEvent(person, state, stateName, loyal, books,issue, fine ,scoreName,score, NPS)
    
        

#adding event to eventlog 
def createEvent(person, state, stateName, loyal, books, issue, fine, scoreName, score, NPS):
    personnumber = str(person.nr)
    if loyal:
         loyal = 'Loyal'
    else: loyal = ''
    if issue == None:
        issue = ''
    elif issue == False:
        issue = ''
    elif issue == True:
        issue = 'Fine'
    if score == None:
         score = ''
    else: score = str(score)
    if scoreName == None:
         scoreName = ''
    if NPS == None:
         NPS = ''
    else: NPS = str(NPS)  
    if books == None:
         books= ''
    else: books = str(books)
    if fine == None:
         fine = ''
    else: fine = str(fine)
    
    global rowNumber
    rowNumber += 1
    event.write(str(rowNumber) + "," + personnumber + "," + state  + ","+ stateName + "," + loyal + "," + books + "," + issue + "," + fine + "," + scoreName + "," + score + "," + NPS +  "\n")


     
# put all persons through the stages    
for each in persons:
    
    stateOne(each)

# close csv
event.close()


 
