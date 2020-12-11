import random

a = random.randint(1,30)
b = random.randint(1,30)

print(a, "+",b , "=")    #문제를 출력합니다.
x = input()
c = int(x)


if a+b==c:
    print("정답")
else:
    print("오답")
    
