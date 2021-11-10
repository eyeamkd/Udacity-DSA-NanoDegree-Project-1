import csv
with open('../texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader) 

def findUniquePhoneNumbers(listOfEntries,phoneNumberSet):
    for entry in listOfEntries:
        phoneNumberSet.add(entry[0]) 
        phoneNumberSet.add(entry[1])


phoneNumberSet = set()
findUniquePhoneNumbers(texts,phoneNumberSet);
findUniquePhoneNumbers(calls,phoneNumberSet); 
print("There are", len(phoneNumberSet), "different telephone numbers in the records")

