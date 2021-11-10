
import csv

with open('../texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def getAreaCode(phoneNumber):
    if(" " in phoneNumber):
        return phoneNumber[:4] 
    elif('('==phoneNumber[0]):
        return phoneNumber[:(phoneNumber.index(")")+1)]
        

areaCodes = set()
bangloreCalls = 0


for entry in calls: 
    areaCode = entry[0][1:4] 
    receiverAreaCode = getAreaCode(entry[1])
    if(areaCode=='080'):
        areaCodes.add(receiverAreaCode) 
        if(receiverAreaCode[1:4]=='080'):
            bangloreCalls+=1   

percentage = bangloreCalls*100/(len(calls))
print("The numbers called by people in Bangalore have codes:")
for code in sorted(areaCodes,key=str):
    print(code,end="\n") 

print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."%percentage)