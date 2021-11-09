import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)  

# texts format sending receiving timestamp 
# calls format calling reciving start timestamp duration  

firstRecordInTexts = texts[0]
firstRecordInCalls = calls[0] 

(incomingNumberText, answeringNumberText, textTimestamp) = firstRecordInTexts; 
(incomingNumberCall, answeringNumberCall, callTimestamp, duration) = firstRecordInCalls;

print("First record of texts, ",incomingNumberText,"texts ",answeringNumberText," at time ",textTimestamp); 
print("First record of calls, ", incomingNumberCall,"calls ",answeringNumberCall," at time ",callTimestamp, "lasting ",duration, "seconds"); 





