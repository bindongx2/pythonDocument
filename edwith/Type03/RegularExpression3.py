import re
hand  = open('mbox-short.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1:  # stuff =1이면 밑에 작업은 수행하지 않는다.
        continue
    num = float(stuff[0])
    numlist.append(num)

print("Maximum : ", max(numlist))
