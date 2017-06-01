import random
import csv
from createPeopleScript import persons

#global variables

rowNumber = 0
totalprice = 0
Upsell = 0

#Open files and write the header
event = open("C:/Users/Tim/Documents/GitHub/scriptieScript/BookFlight1/OutputCSV/eventlog.csv", "w")
event.write("rowNumber,PersonId,State,StateName,LifeCycle,Channel,Loyal,FlightPrice,Upsell, totalPrice,Issue,ScoreName,Score, NPS-score\n")



### various states; with its eventlog creation ###
def stateOne(person):
    #create the channel
    c = random.randint(0,2)
    if c == 0:
        Channel = 'Mobile'
    elif c == 1:
        Channel = 'Computer'
    elif c == 2:
        Channel = 'Tablet'
    #add event
    createEvent(person, 's1', 'Start', 'Awareness',Channel,None,None,None,None,None,None,None,None)
    #determine next step
    r = random.randint(0,100)
    if r < 60: stateTwo(person,Channel)
    else: stateEight(person, Channel)

def stateTwo(person,Channel):
     #add event
    createEvent(person, 's2', 'Ticket-Website', 'Awareness',Channel,None,None,None,None,None,None,None,None)
    #add Evaluation
    e = random.randint(0,100)
    if e <= 30: 
        makeEvaluation(person, 's2', 'Ticket-Website', 'Awareness',Channel,None,None,None,None,None,'CES',None,None)
        makeEvaluation(person, 's2', 'Ticket-Website', 'Awareness',Channel,None,None,None,None,None,'NPS',None,None)
    #determine next step
    r = random.randint(0,100)
    if r < 26: stateTwo(person,Channel)
    elif r < 76: stateThree(person, Channel)
    else: stateEight(person,Channel)

def stateThree(person,Channel):
     #add event
    createEvent(person, 's3', 'Select-Flight', 'Evaluation',Channel,None,None,None,None,None,None,None,None)
    #make price
    makePrice(person, 's3', 'Select-Flight', 'Evaluation',Channel,None,None,None,None,None,None,None,None)
    #add Evaluation
    e = random.randint(0,100)
    if e <= 30: 
        makeEvaluation(person, 's3', 'Select-Flight', 'Evaluation',Channel,None,None,None,None,None,'CES',None,None)
        makeEvaluation(person, 's3', 'Select-Flight', 'Evaluation',Channel,None,None,None,None,None,'NPS',None,None)
     #determine next step
    r = random.randint(0,100)
    if person.gender == 'female':
        if r <= 20: stateTwo(person,Channel)
        elif r <= 55: stateFive(person,Channel)
        elif r <= 90: stateFour(person,Channel)
        else: stateEight(person,Channel)
    elif Channel == 'Tablet':
        if r <= 30: stateTwo(person,Channel)
        elif r <= 40: stateFive(person,Channel)
        elif r <= 45: stateFour(person,Channel)
        else: stateEight(person,Channel)
    else:
        if r <= 50: stateTwo(person,Channel)
        elif r <= 60: stateFive(person,Channel)
        elif r <= 75: stateFour(person,Channel)
        else: stateEight(person,Channel)

def stateFour(person,Channel):
    global totalprice 
    #add event
    createEvent(person, 's4', 'Pay-Flight', 'Purchase', Channel,None,None,None, totalprice,None,None,None, None)
    
    #add Evaluation
    e = random.randint(0,100)
    if e <= 30: 
        makeEvaluation(person, 's4', 'Pay-Flight', 'Purchase',Channel,None,None,None,None,None,'CES',None,None)
        makeEvaluation(person, 's4', 'Pay-Flight', 'Purchase',Channel,None,None,None,None,None,'NPS',None,None)
    #determine next step
    r = random.randint(0,100)
    if r <= 5: stateTwo(person,Channel)
    elif r <= 15: stateSeven(person,Channel)
    elif r <= 95: stateSix(person,Channel)
    else: stateEight(person, Channel)


def stateFive(person,Channel):
     #add event
    createEvent(person, 's5', 'Cross/Up-sell', 'Evaluation',Channel,None,None,None,None,None,None,None,None)
    #makeprice
    makePrice(person, 's5', 'Cross/Up-sell', 'Evaluation',Channel,None,None,None,None,None,None,None,None)
    #add Evaluation
    e = random.randint(0,100)
    if e <= 30: 
        makeEvaluation(person, 's5', 'Cross/Up-sell', 'Evaluation',Channel,None,None,None,None,None,'CES',None,None)
        makeEvaluation(person, 's5', 'Cross/Up-sell', 'Evaluation',Channel,None,None,None,None,None,'NPS',None,None)
    #determine next step
    r = random.randint(0,100)
    if person.gender == 'female':
        if r <= 20: stateThree(person,Channel)
        elif r <= 55: stateFive(person,Channel)
        elif r <= 90: stateFour(person,Channel)
        else: stateEight(person,Channel)
    elif Channel == 'Tablet':
        if r <= 30: stateThree(person,Channel)
        elif r <= 40: stateFive(person,Channel)
        elif r <= 45: stateFour(person,Channel)
        else: stateEight(person,Channel)
    else:
        if r <= 50: stateThree(person,Channel)
        elif r <= 60: stateFive(person,Channel)
        elif r <= 75: stateFour(person,Channel)
        else: stateEight(person,Channel)

def stateSix(person,Channel):
    global totalprice
     #add event with the total price
    createEvent(person, 's6', 'Trip', 'Use', Channel,None,None,None, None,None,None,None, None)
    #add Evaluation
    e = random.randint(0,100)
    if e <= 30: 
        makeEvaluation(person, 's6', 'Trip', 'Use',Channel,None,None,None,None,None,'CES',None,None)
        makeEvaluation(person, 's6', 'Trip', 'Use',Channel,None,None,None,None,None,'NPS',None,None)
    #determine next step
    r = random.randint(0,100)
    if person.gender == 'female':
        if r <= 40: stateTwo(person,Channel)
        else: stateEight(person,Channel)
    else:
        if r <= 5: stateTwo(person,Channel)
        else: stateEight(person,Channel)

def stateSeven(person,Channel):
     #add event
    createEvent(person, 's7', 'Issue', 'Use',Channel,None,None,None,None,None,None,None,None)
    #add Evaluation
    e = random.randint(0,100)
    if e <= 30: 
        makeEvaluation(person, 's7', 'Issue', 'Use',Channel,None,None,None,None,None,'CES',None,None)
        makeEvaluation(person, 's7', 'Issue', 'Use',Channel,None,None,None,None,None,'NPS',None,None)
    #determine next step
    r = random.randint(0,100)
    if r <= 5: stateSeven(person,Channel)
    elif r <= 95: stateSix(person,Channel)
    else: stateEight(person,Channel)

def stateEight(person,Channel):
     #add event
    createEvent(person, 's8', 'End', 'End',Channel,None,None,None,None,None,None,None,None)
    
#Make an evaluation
def makeEvaluation(person,State,StateName,LifeCycle,Channel,Loyal,FlightPrice,Upsell, totalPrice,Issue,ScoreName,Score, NPSscore):
    rc = random.randint(0,3)
    r = random.randint(2,10)
    rnps = r 
    rces = r 
    
    if person.gender == 'female':
        rnps    += 5
        rces    += 5

    if person.company is not 'NULL' and Channel == 'Computer':
        rnps    += 4
        rces    += 4
    elif person.company is not 'NULL' and Channel == 'Mobile':
        rnps    -= 4
        rces    -= 4
    elif person.gender == 'male' and person.age > 50 and Channel == 'Computer':
        rnps    -= 4
        rces    -= 4
    elif person.gender == 'male' and Channel == 'Tablet':
        rnps    += 3
        rces    += 3
    elif Channel == 'Mobile':
        rnps    -= 5
        rces    -= 5

     
   
    
    if rnps > 10: rnps = 10
    elif rnps < 1: rnps = 1
    
    if rces > 10: rces = 10
    elif rces < 1: rces = 1
    
        
    if ScoreName == 'CES':
        Score = rces
    else:
        Score = rnps
        if Score < 7:
            NPSscore = -1
        elif Score > 8 :
            NPSscore = 1
        else:
            NPSscore = 0

    createEvent(person,State,StateName,LifeCycle,Channel,Loyal,FlightPrice,Upsell, totalPrice,Issue,ScoreName,Score, NPSscore)

# create a price
def makePrice(person,State,StateName,LifeCycle,Channel,Loyal,FlightPrice,Upsell, totalPrice,Issue,ScoreName,Score, NPSscore):
    global totalprice
    r = None
    Upsell = None
    if State == 's3':
        totalprice = 0
        if person.gender == 'female':
            r = random.randint(300,1200)

        if person.company is not 'NULL' and Channel == 'Computer':
            r = random.randint(300,1000)
        elif person.company is not 'NULL' and Channel == 'Mobile':
            r = random.randint(300,1000)
        elif person.gender == 'male' and person.age > 50 and Channel == 'Computer':
            r = random.randint(500,1000)
        elif person.gender == 'male' and Channel == 'Tablet':
            r = random.randint(60,200)
        elif Channel == 'Mobile':
            r = random.randint(60,200)    
        else: r = random.randint(100,800)
        totalprice += r
    else:
        sell = random.randint(0,2)
        if sell == 0:
            Upsell = 50
            totalprice += 50
        elif sell == 1:
            Upsell = 80
            totalprice += 80
        elif sell == 2:
            Upsell = 40
            totalprice += 40
    createEvent(person,State,StateName,LifeCycle,Channel,Loyal,r,Upsell, None,Issue,ScoreName,Score, NPSscore)
    


#adding event to eventlog
def createEvent(person,State,StateName,LifeCycle,Channel,Loyal,FlightPrice,Upsell,totalPrice,Issue,ScoreName,Score, NPSscore):
    PersonId = person.nr
    
    if Loyal == None:
        Loyal = '' 
    if Issue == None:
        Issue = ''
    elif Issue == False:
        Issue = 'Not Solved'
    elif Issue == True:
        Issue = 'Solved'
    if Score == None:
         Score = ''
    else: Score = str(Score)
    if ScoreName == None:
         ScoreName = ''
    if NPSscore == None:
         NPSscore = ''
    else: NPSscore = str(NPSscore)
    if Channel == None:
         Channel = ''
    else: Channel = str(Channel)
    if FlightPrice == None:
         FlightPrice = ''
    else: FlightPrice = str(FlightPrice)
    if Upsell == None:
         Upsell = ''
    else: Upsell = str(Upsell)
    if totalPrice == None:
         totalPrice = ''
    else: totalPrice = str(totalPrice)

    global rowNumber
    rowNumber += 1
    event.write(str(rowNumber) + "," + str(PersonId) + "," + State  + "," + StateName + "," + LifeCycle + "," + Channel + "," + Loyal + "," + FlightPrice + "," + Upsell + "," + totalPrice + "," + Issue + "," + ScoreName + "," + Score + "," + NPSscore  +  "\n")



# put all persons through the stages    
for each in persons:
    
    stateOne(each)

# close csv
event.close()


 
