def square(a):   #a의 제곱근을 구하는 함수
    c = a*a
    return c

def triangle(a,h): #밑변이 a이고 높이가 h인 삼각형의 넓이를 구하는 함수
    c = a*h/2
    return c


s1 = 4
s2 = square(s1)
print(s1,s2)

print(triangle(3,4))

