import turtle as t

def turn_right():
    t.setheading(0)
    t.fd(10)


def turn_up():
    t.setheading(90)
    t.fd(10)


def turn_left():
    t.setheading(180)
    t.fd(10)

def turn_down():
    t.setheading(270)
    t.fd(10)

def blank():
    t.clear()

t.shape("turtle")        # 거북이 모양을 사용합니다.
t.speed(0)               # 거북이 속도를 가장 빠르게 지정합니다.
t.onkeypress(turn_right, "Right") 
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")   
t.onkeypress(blank, "Escape")     # ESC를 누르면 blank함수를 실행
t.listen()                        # 그래픽 창이 키보드 입력을 받습니다.  
