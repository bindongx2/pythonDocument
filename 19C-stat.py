# 평균, 분산, 표준편차를 구하는 프로그램

import math

# 자료값 리스트
d = [1,2,3,4,5]
print(d)

# 평균 구하기
mean = sum(d)/len(d)
print("평균 : ", mean)


#분산구하기   분산 = (표본-평균)^2 / 표본의 개수
vsum=0
for x in d:
    vsum = vsum + (x-mean)**2

v = vsum / len(d)
print("분산 : ", v)

#표준편차 구하기  표준편차= 분산의 제곱근
std = math.sqrt(v)  #math.sqrt() : 제곱근 함
print("표준편차 : ", std)
