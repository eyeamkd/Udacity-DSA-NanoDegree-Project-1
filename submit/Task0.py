import csv
with open('../texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)  

# texts format sending receiving timestamp 
# calls format calling reciving start timestamp duration  

firstRecordInTexts = texts[0]
lastRecordInCalls = calls[-1]  

(incomingNumberText, answeringNumberText, textTimestamp) = firstRecordInTexts; 
(incomingNumberCall, answeringNumberCall, callTimestamp, duration) = lastRecordInCalls;

print("First record of texts, ",incomingNumberText,"texts ",answeringNumberText," at time ",textTimestamp); 
print("Last record of calls, ", incomingNumberCall,"calls ",answeringNumberCall," at time ",callTimestamp, "lasting ",duration, "seconds"); 





"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
