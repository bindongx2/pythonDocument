import random

def make_question():
    a = random.randint(1,40)
    b = random.randint(1,40)
    op = random.randint(1,3)

    p = str(a)

    if op==1:
        p = p + "+"
    if op==2:
        p = p + "-"
    if op==3:
        p = p + "*"

    p = p + str(b)
    return p


sc1 = 0
sc2 = 0

for x in range(5):
     p = make_question()
     print(p)
     ans = input("=")
     result = int(ans)

     if eval(p) == result:
         print("정답!")
         sc1 = sc1 + 1
     else:
         print("오답!")
         sc2 = sc2 + 1



print("정답 : ", sc1, "오답 : " ,sc2)

if sc2==0:
    print("모두 정답입니다.!")
         
          
