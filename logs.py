import urllib.request 
import re
from collections import Counter

log = urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','log.txt')

### Monthly log files ###
logs = open("log.txt","r")

octoberlogs = open("octoberlogs.txt","w")
octpattern = re.compile (r"(/[Oct]{3}/[0-9]{4})")

for line in logs:
    if octpattern.search(line) != None:
        octoberlogs.write(line)
    else:
        continue
    
octoberlogs.close()

logs = open("log.txt","r")

novemberlogs = open("novemberlogs.txt","w")
novpattern = re.compile (r"(/[Nov]{3}/[0-9]{4})")

for line in logs:
    if novpattern.search(line) != None:
        novemberlogs.write(line)
    else:
        continue
    
novemberlogs.close()

logs = open("log.txt","r")

decemberlogs = open("decemberlogs.txt","w")
decpattern = re.compile (r"(/[Dec]{3}/[0-9]{4})")

for line in logs:
    if decpattern.search(line) != None:
        decemberlogs.write(line)
    else:
        continue
    
decemberlogs.close()

logs = open("log.txt","r")

januarylogs = open("januarylogs.txt","w")
janpattern = re.compile (r"(/[Jan]{3}/[0-9]{4})")

for line in logs:
    if janpattern.search(line) != None:
        januarylogs.write(line)
    else:
        continue
    
januarylogs.close()

logs = open("log.txt","r")

februarylogs = open("februarylogs.txt","w")
febpattern = re.compile (r"(/[Feb]{3}/[0-9]{4})")

for line in logs:
    if febpattern.search(line) != None:
        februarylogs.write(line)
    else:
        continue
    
februarylogs.close()

logs = open("log.txt","r")

marchlogs = open("marchlogs.txt","w")
marpattern = re.compile (r"(/[Mar]{3}/[0-9]{4})")

for line in logs:
    if marpattern.search(line) != None:
        marchlogs.write(line)
    else:
        continue
    
marchlogs.close()

logs = open("log.txt","r")

aprillogs = open("aprillogs.txt","w")
aprpattern = re.compile (r"(/[Apr]{3}/[0-9]{4})")

for line in logs:
    if aprpattern.search(line) != None:
        aprillogs.write(line)
    else:
        continue
    
aprillogs.close()

logs = open("log.txt","r")

maylogs = open("maylogs.txt","w")
maypattern = re.compile (r"(/[May]{3}/[0-9]{4})")

for line in logs:
    if maypattern.search(line) != None:
        maylogs.write(line)
    else:
        continue
    
maylogs.close()

logs = open("log.txt","r")

junelogs = open("junelogs.txt","w")
junpattern = re.compile (r"(/[Jun]{3}/[0-9]{4})")

for line in logs:
    if junpattern.search(line) != None:
        junelogs.write(line)
    else:
        continue
    
junelogs.close()

logs = open("log.txt","r")

julylogs = open("julylogs.txt","w")
julpattern = re.compile (r"(/[Jul]{3}/[0-9]{4})")

for line in logs:
    if julpattern.search(line) != None:
        julylogs.write(line)
    else:
        continue
    
julylogs.close()

logs = open("log.txt","r")

augustlogs = open("augustlogs.txt","w")
augpattern = re.compile (r"(/[Aug]{3}/[0-9]{4})")

for line in logs:
    if augpattern.search(line) != None:
        augustlogs.write(line)
    else:
        continue
    
augustlogs.close()

logs = open("log.txt","r")

septemberlogs = open("septemberlogs.txt","w")
seppattern = re.compile (r"(/[Sep]{3}/[0-9]{4})")

for line in logs:
    if seppattern.search(line) != None:
        septemberlogs.write(line)
    else:
        continue
    
septemberlogs.close()

### Operations to answer questions ###

with open("novemberlogs.txt", "r") as n:
    novlinecount = 0
    for line in n:
        novlinecount += 1

with open("decemberlogs.txt", "r") as d:
    declinecount = 0
    for line in d:
        declinecount += 1

linecount = ((declinecount + novlinecount) / 2)

dayrequests = []      
for line in open("novemberlogs.txt","r"):
    try:
        file = re.split(r"(\[[0-9]{2}/)", line)
        filename = file[1]
        dayrequests.append(filename)
    except IndexError:
        pass
    continue

daycount = dict(Counter(dayrequests))
numday = []
for key, value in daycount.items():
    numday.append(value)

logs = open("log.txt","r")

numpattern = re.compile (r"(/[a-zA-Z]{3}/[0-9]{4})")
count = 0 

for line in logs:
    if numpattern.search(line) != None:
        count = count + 1
    else:
        continue
    
logs = open("log.txt","r")

badrequest = re.compile(r"(\" [4][0-9]{2} -)")
badcount = 0 

for line in logs:
    if badrequest.search(line) != None:
        badcount = badcount + 1
    else:
        continue
    
logs = open("log.txt","r")

redirectrequest = re.compile(r"(\" [3][0-9]{2} -)")
redirectcount = 0 

for line in logs:
    if redirectrequest.search(line) != None:
        redirectcount = redirectcount + 1
    else:
        continue

logs = open("log.txt","r")
key = re.compile(r"(\ [0-9a-zA-Z.]{5,})")

files = []

for line in open("log.txt","r"):
    try:
        file = re.split(r"(\ [0-9a-zA-Z.]{5,})", line)
        filename = file[1]
        files.append(filename)
    except IndexError:
        pass
    continue

filecount = dict(Counter(files))
leastrequest = []

for key, value in filecount.items():
    if value == 1:
        leastrequest.append(key)

with open("leastrequestedfiles.txt", "w") as file:
    for item in leastrequest:
        file.write("%s\n" % item)

file.close()      
    
filecount = sorted((value, key) for (key, value) in filecount.items())
badcount = round(((badcount / count) * 100), 1)
redirectcount = round(((redirectcount / count) * 100), 1) 
numday = round((sum(numday)/len(numday)),1)
filecount = list(filecount)[-1]
### Answered Questions ###
    
print("How many total requests were made in the time period represented in the log?", count,"requests")

print("How many requests were made on each day? per week? per month? There were on average",numday,"requests per day,",linecount,"requests per month.")

print("What percentage of the requests were not successful (any 4xx status code)?", badcount,"percent")

print("What percentage of the requests were redirected elsewhere (any 3xx codes)?", redirectcount,"percent")

print("What was the most-requested file? The most requested file was",filecount[-1])

print("What was the least-requested file? The list of least requested files is saved in a text file called leastrequestedfiles.txt")

#print(leastrequest)
#pattern = "/[Oct]{3}/[0-9]{4}"


#l = re.findall(pattern, logs)

#print(l)

