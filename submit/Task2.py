#finding the longest duration spent on phone 
import csv
with open('../texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def calculateMaxDuration(phoneNumber,phoneDurations,maxDuration,phoneNumberHavingMaxDuration): 
    if phoneNumber in phoneDurations.keys():
        phoneDurations[phoneNumber]+=int(entry[3]) 
    else:
        phoneDurations[phoneNumber] = int(entry[3]) 
    if(maxDuration<phoneDurations[phoneNumber]):
            maxDuration = phoneDurations[phoneNumber] 
            phoneNumberHavingMaxDuration = phoneNumber 
    return (maxDuration,phoneNumberHavingMaxDuration)

phoneDurations = { } 
maxDuration = 0  
phoneNumberHavingMaxDuration = '';
for entry in calls: 
    maxDuration,phoneNumberHavingMaxDuration = calculateMaxDuration(entry[0],phoneDurations,maxDuration,phoneNumberHavingMaxDuration); 
    maxDuration,phoneNumberHavingMaxDuration = calculateMaxDuration(entry[1],phoneDurations,maxDuration,phoneNumberHavingMaxDuration);
    
   
print(phoneNumberHavingMaxDuration,"spent the longest time,", maxDuration, "seconds, on the phone during September 2016.")