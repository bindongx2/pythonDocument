import re
x = "My 2 favorite numbers are 19 and 42"
x1 = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('[0-9]+',x)
print("y : " ,y)

z = re.findall("[AEIOU]+", x)
print("z : " ,z)

z1 = re.findall("\S+@\S+",x1)
print("z1 : " ,z1)

z2 = re.findall("^From (\S+@\S+)", x1)
print("z2 : " ,z2)
