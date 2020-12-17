fname = input("Enter File : ")
if len(fname) < 1 :
    fname = "clown.txt"

hand = open(fname, encoding='UTF8')

di = dict()
for line in hand:
    line = line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for w in words:
        # if the key is not there the count is zero
        # print("**", w,di.get(w,-99))
        # oldCount = di.get(w,0)
        # print(w,"old",oldCount)
        # newCount = oldCount + 1
        #di[w] = di.get(w,0) + 1
        #print(w,"new",di[w])
        if w in di:
            di[w] = di[w] + 1
            #print("***Existing***")
        else:
            di[w] = 1
            #print("***NEW***")
        #print(w , di[w])
    largest = -1
    theword = None
    for k,v in di.items():
        print(k,v)
        if v > largest:
            largest = v
            theword = k
    print("Max Key   : " , theword)
    print("Max Value : " , largest)
