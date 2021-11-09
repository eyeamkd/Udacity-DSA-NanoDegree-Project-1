
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def isAreaNumber(phoneNumber):
    if(phoneNumber[0]=='('):
        return True 
    else:
        return False

areaCodes = set()
bangloreCalls = 0


for entry in calls: 
    if(isAreaNumber(entry[0])): 
        areaCode = entry[0][1:4]
        if(areaCode=='080'):
            bangloreCalls+=1
        areaCodes.add(entry[0][1:4])     

percentage = bangloreCalls*100/(len(calls))

for code in sorted(areaCodes,key=str):
    print(code,end="\n") 

print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."%percentage)