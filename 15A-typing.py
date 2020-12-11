import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "sanke", "wolf"]
n = 1


print("[타자게임] 준비되면 엔터!")
input()             
start = time.time()   #시작 시간을 기록합니다.


q = random.choice(w)  #단어 리스트에서 아무것이나 하나 뽑습니다.

while n<=5:
    print("※문제",n)
    print(q)
    ans = input()

    if q==ans:
        print("통과")
        n=n+1
        q=random.choice(w)
    else:
        print("오타! 다시도전")

end = time.time()
et = end - start
et = format(et, ".2f")    #소수점 둘째자리까지만 표기
print("타자 시간 : ",et , "초")

 
