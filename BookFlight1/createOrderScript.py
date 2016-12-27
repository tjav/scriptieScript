import csv
from orderScript import Order
from createPeopleScript import persons
from createPathsScript import eventlog
from createQuoteScript import quotes


orders = []
rowNumber = 0

# calculate the total order of a person
def calcTotal(personId):
    
    event = [each for each in eventlog if each.nameID == personId] #get only the event of the person
    quoteEvent = [each for each in quotes if each.nameID == personId] #get the quotes of the person
    flightPrice = 0
    extraprice = 0
    
    #go backwards through the event
    for i in reversed(event):
        if i.state == 's4':
            a = 0
            l = 0
            for i in event:
                if i.state == 's3': 
                    if extraprice is not 0:   #if there was a previous extra price, it will not be added to the new quote
                        extraprice = 0
                    flightPrice = [quote.price for quote in quoteEvent if quote.state == 's3']
                    flightPrice = flightPrice[a] #there is only on flightPrice
                    #print (flightPrice)
                    a += 1
                elif i.state == 's5':
                    ep = [quote.price for quote in quoteEvent if quote.state == 's5']
                    extraprice += ep[l]  #there could be multiple additional prices
                    #print (extraprice)
                    l += 1
                elif i.state == 's4': #the quote is payed
                    orderPrice = flightPrice + extraprice
                    if orderPrice is not 0:
                        #print (orderPrice)
                        appendToOrders(personId, orderPrice) # there is no break, because there could be an extra payed ticket in the event.
                
    

def appendToOrders(personId, orderPrice):
    global rowNumber
    orders.append(Order(rowNumber, personId, 's4', orderPrice, 'Total'))
    rowNumber += 1

# go through all record of the person file and take the person
for pId in range(len(persons)):
    #print ('pid')
    #print (pId)
    calcTotal(pId)
    

# loyal persons to csv
ocsv = csv.writer(open("OutputCSV/orders.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
ocsv.writerow(orders)