c = {"a":10,"b":1,"c":22}
tmp = list()

for k,v in c.items():
    tmp.append( (v,k) )
print("tmp : " , tmp)

tmp = sorted(tmp)
print("Sorted : " , tmp)

tmp = sorted(tmp, reverse=True)
print("Sroted Reverse" , tmp)
