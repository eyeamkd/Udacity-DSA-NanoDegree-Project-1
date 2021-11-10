import csv
with open('../texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader) 

possibleTelemarketers = set()

for call in calls:
    possibleTelemarketers.add(call[0]) 
for call in calls:    
    if(call[1] in possibleTelemarketers):
        possibleTelemarketers.remove(call[1]) 

for text in texts:
    if(text[0] in possibleTelemarketers):
        possibleTelemarketers.remove(text[0])
    if(text[1] in possibleTelemarketers):
        possibleTelemarketers.remove(text[1]) 

print('These numbers could be telemarketers:') 


for number in sorted(possibleTelemarketers,key=str):
    print(number,end="\n")
