import random
import csv
from createPathsScript import eventlog
from createPeopleScript import persons
from evaluationScript import Evaluation
from issuesScript import Issues
from createQuoteScript import quotes

evaluation = []
issues = []
rowNumber = 0
issueNumber = 0


#creation of evaluations
def createEvaluation(personID, state, work, gender, issue):
    takes = random.randint(0,99)
    rc = random.randint(0,3)
    r = random.randint(1,10)
    rnps = r 
    rces = r 
    re = r
    
    if work:
        rnps -= 1
        rces += 2
        re += 1
    
    if gender == 'female':
        rnps += 2
        rces += 1
        re += 1
        
    if rc == 0:
        rnps += 1
        rces += 2
        re += 1
    elif rc == 1:
        rces -= 2
        
    if state == 's7' and issue:
        rnps += 2
        rces += 1
    elif state == 's7':
        rnps -= 3
        rces -= 1
    
    
    if rnps > 10: rnps = 10
    elif rnps < 1: rnps = 1
    
    if rces > 10: rces = 10
    elif rces < 1: rces = 1
    
    if re > 10: re = 10
    elif re < 1: re = 1
        
    if state == 's2':
        if takes < 10:
            createEvaluationLog(personID, state, re, 'site experience' , rc)
    
    elif state == 's7':
        if takes < 40:
            createEvaluationLog(personID, state, rnps, 'NPS' , rc)    
    elif takes < 60:
        if state == 's6':
            createEvaluationLog(personID, state, rces, 'CES' , rc)
            createEvaluationLog(personID, state, rnps, 'NPS' , rc)
        else:
            createEvaluationLog(personID, state, rces, 'CES' , rc)

def createEvaluationLog(personID,state, score, scorename, channel):
    global rowNumber
    rowNumber += 1
    evaluation.append(Evaluation(rowNumber,personID, state, score, scorename, channel))

#search through list
def searchEventlog(state):
    name = [events.nameID for events in eventlog if events.state == state]
    for each in name:
        if state == 's7':
            r = random.randint(0,1)
            if r == 0:
                searchPersons(each, state, True)
                createIssueLog(each, True)
            else:
                searchPersons(each, state, False)
                createIssueLog(each, False)  
        else:
            searchPersons(each,state, None)

# search through persons
def searchPersons(nr, state, issue):
    person = persons[nr]
    comp = person.company
    gender = person.gender
    if comp and gender == 'male': createEvaluation(nr, state, True, gender, issue)
    else: createEvaluation(nr, state, False, gender,issue)


def createIssueLog(name, issue):
    global issueNumber
    issueNumber += 1
    if issue:
        issues.append(Issues(issueNumber, name,'solved'))
    else:
        issues.append(Issues(issueNumber, name, 'not solved'))

i = ['s2', 's4', 's5', 's6', 's7']
#get persons state
for item in i:
    searchEventlog(item)
    
# evaluations to csv
wcsv = csv.writer(open("OutputCSV/evaluations.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
wcsv.writerow(evaluation)

# Issues to csv
icsv = csv.writer(open("OutputCSV/issues.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
icsv.writerow(issues)
