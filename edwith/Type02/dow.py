han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    wds  = line.split()
    print("Line : " , line)
    print("Words :" , wds)
    #Guadian Start
    if(line == "" or len(wds) < 1):
        print("Skip Blank")
        continue
    #Guadian End
    if(wds[0] != 'From'):
        print("Ignore")
        continue
    print(wds[2])
