#finding the longest duration spent on phone 
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


phoneDurations = { } 
maxDuration = 0 
phoneNumberHavingMaxDuration = '';
for entry in calls: 
    phoneNumber = entry[0]
    if phoneNumber in phoneDurations.keys():
        phoneDurations[phoneNumber]+=int(entry[3]) 
    else:
        phoneDurations[phoneNumber] = int(entry[3]) 
    if(maxDuration<phoneDurations[phoneNumber]):
            maxDuration = phoneDurations[phoneNumber] 
            phoneNumberHavingMaxDuration = phoneNumber
print(phoneNumberHavingMaxDuration,"spent the longest time,", maxDuration, "seconds, on the phone during September 2016.")