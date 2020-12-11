import turtle as t
t.shape("turtle")
d=200 #변수d에 100값 셋팅

#삼각형 그리기
t.color("red")
t.fd(d)
t.left(120)
t.fd(d)
t.left(120)
t.fd(d)
t.left(120)

#사각형 그리기
t.color("green")
t.pensize(3)    #펜 굵기를 3으로 지정
for x in range(4):
    t.fd(100)
    t.lt(90)


#원 그리기
t.color("blue")
t.circle(50)    #반지름이 50인 원을 그린다.
