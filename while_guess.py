import random

n = random.randint(1,30)   #1~30 사이에 있는 임의의 수를 뽑습니다.

while True:
    x = input("숫자를 맞춰보세요")
    g = int(x)             #입력된 값을 비교할 수 있도록 정수로 변환
    if(g == n):
        print("정답")
        break
    if(g < n):
        print("작아요.")
    if(g > n):
        print("커요.")
