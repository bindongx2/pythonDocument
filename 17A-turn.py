import turtle as t
import time
import random

te = t.Turtle()    #악당 거북이 te를 새로 만듭니다.
te.shape("turtle")
te.color("red")    #빨간색으로 지정
te.speed(0)
te.up()
te.goto(0,200)


ts = t.Turtle()    #먹이로 사용할 거북이
ts.shape("circle") #모양을 원으로 지정
ts.color("green")  #초록색으로 지정
ts.speed(0)
ts.up()
ts.goto(0,-200)

#t  : 주인공 거북이
#te : 악당거북이
#ts : 먹이

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def turn_right():
    t.setheading(0)

global score

def play():
    t.fd(10)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(9)

    if t.distance(ts) < 12:
       star_x = random.randint(-230,230)
       star_y = random.randint(-230,230)
       ts.goto(star_x,star_y)  # 먹이를 다른 곳으로 옮깁니다.
       t.write("+100", False, "center")

    if t.distance(te) >= 12:   # 주인공과 악당의 거리가 12 이상일 경우
       t.ontimer(play,100)     # 0.1초 후 play함수를 실행합니다.




t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_right, "Right")
t.listen()    #거북이 그래픽 창이 키보드 입력을 받도록 합니다.
play()







