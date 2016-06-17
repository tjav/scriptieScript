import csv
from orderScript import Order
from createPeopleScript import persons
from createPathsScript import eventlog
from createQuoteScript import quotes

orders = []
rowNumber = 0

def calcTotal(personId):
    
    event = [each for each in eventlog if each.nameID == personId]
    quoteEvent = [each for each in quotes if each.nameID == personId]
    flightPrice = 0
    extraprice = 0

    for i in reversed(event):
        if i.state == 's4':
            a = 0
            l = 0
            for i in event:
                if i.state == 's3':
                    if extraprice is not 0:
                        extraprice = 0
                    flightPrice = [quote.price for quote in quoteEvent if quote.state == 's3']
                    flightPrice = flightPrice[a]
                    print (flightPrice)
                    a += 1
                elif i.state == 's5':
                    ep = [quote.price for quote in quoteEvent if quote.state == 's5']
                    extraprice += ep[l] 
                    print (extraprice)
                    l += 1
                elif i.state == 's4':
                    orderPrice = flightPrice + extraprice
                    if orderPrice is not 0:
                        print (orderPrice)
                        appendToOrders(personId, orderPrice)
                
    

def appendToOrders(personId, orderPrice):
    global rowNumber
    orders.append(Order(rowNumber, personId, 's4', orderPrice, 'Total'))
    rowNumber += 1

for i in range(0,len(persons)):
    pRecord = persons[i]
    pId = pRecord.nr
    print ('pid')
    print (pId)
    calcTotal(pId)
    

# loyal persons to csv
ocsv = csv.writer(open("OutputCSV/orders.csv","w"), delimiter='\n',quoting=csv.QUOTE_MINIMAL)
ocsv.writerow(orders)