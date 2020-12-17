data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print("atpos : " ,atpos)

sppos = data.find(" ", atpos)
print("sppos : ",sppos)

host = data[atpos+1:sppos]
print("host :",host)


#The Double Split Pattern
words = data.split()
email = words[1]
pieces = email.split("@")
print("pieces : ", pieces[1])

#정규식 구별
import re
y = re.findall('@([^ ]*)',data)
print("y : " , y)
