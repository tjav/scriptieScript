import csv

#Open files and write the header
NPS = open("C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/nps.csv", "w")
NPS.write("PersonID,State,Score, NPS \n")

def makeNPS(person,state, score, nps):
    if score > '8': newscore = '1'
    elif score < '7': newscore = '-1'
    else: newscore = '0'
    NPS.write(person + "," + state + "," + newscore + ","+nps +"\n")





with open('C:/Users/Tim/Documents/GitHub/scriptieScript/ComputerHelp/OutputCSV/evaluation.csv', newline='') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
       for row in spamreader:
           if len(row)-1:
                if row[4] == 'NPS':
                    makeNPS(row[1],row[2],row[3],row[4])

NPS.close()