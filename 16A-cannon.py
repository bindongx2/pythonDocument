import turtle as t
import random
import time

def turn_up():
    t.left(2)


def turn_down():
    t.right(2)


def fire():
    ang = t.heading()      # 현재 거북이가 바라보는 각도를 기억합니다.
    while t.ycor() >0 :    # 거북이가 땅 위에 있는 동안 반복합니다.
        t.fd(15)           # 15만큼 전진
        t.right(5)         # 5도만큼 회전

    #while 반복문을 빠져나오면 거북이가 땅에 닿은 상태입니다.

    d = t.distance(target, 0)      #거북이와 목표 지점과의 거리를 구합니다.
    t.sety(random.randint(10,100)) #성공 또는 실패를 표시할 위치를 지정합니다.

    if d < 25 :    #거리 차이가 25보다 작으면 목표 지점에 명중한 것으로 처리
        t.color("blue")
        t.write("Good!", False, "center", ("",15))
        t.color("black")
        t.goto(-200,10)   # 거북이 위치를 처음 발사했던 곳으로 되돌립니다.
        t.setheading(0)
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("",15))
        t.color("black")  # 거북이 색을 검은색으로 되돌립니다.
        t.goto(-200,10)   # 거북이 위치를 처음 발사했던 곳으로 되돌립니다.
        t.setheading(ang) # 각도도 처음 기억해 둔 각도로 되돌립니다.


################## def fire() end ##################

#땅을 그립니다.
t.goto(-300,0)
t.down()
t.goto(300,0)



#목표 지점을 설정하고 그립니다.
target = random.randint(50,150)   # 목표 지점을 50~150 사이에 있는 임의의 수로 지정
t.pensize(4)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

#거북이 색을 검은색으로 지정하고 처음 발사했던 곳으로 되돌립니다.
t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)

#거북이가 동작하는데 필요한 설정을 합니다.
t.onkeypress(turn_up,"Up")      # 
t.onkeypress(turn_down,"Down")  # 
t.onkeypress(fire,"space")      # 스페이스바를 누르면 fire함수 실행
t.listen()  # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.








        

    
    
    
