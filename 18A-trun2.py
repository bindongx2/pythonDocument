#터틀린2 만들기

import turtle as t
import random
import time

score = 0        # 점수를 저장하는 변수
playing = False  # 현재 게임이 플레이 중인지 확인하는 변수

#악당 거북이(빨간색)
te = t.Turtle()       
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

#먹이(초록색)
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():   # 게임을 시작하는 함수
    global playing
    if playing == False:
        playing = True
        t.clear() # 거북이 선 모두 지우기(초기화)
        play()    # 플레이 함수 실행

def play():
    global score
    global playing
    t.fd(10)
    if random.randint(1,5) == 3:  # 1~5 사이에서 뽑은수가 3이면(20%)
        ang = te.towards(t.pos()) # te 가 t좌표로 바라보는 각도
        te.setheading(ang)

    speed = score + 5 # 점수에 5를 더해서 속도를 올립니다.

    if speed > 15:    # 속도는 15를 넘지않도록 설정
        speed = 15

    te.fd(speed)  # 악당 스피드로 전진

    if(t.distance(te) < 12): # 주인공과 악당의 거리가 12보다 작으면 게임 종료
        text = "Score : " + str(score)
        message("Game Over", text)  # message() 함수 사용
        playing = False
        score = 0

    if(t.distance(ts) < 12): # 주인공과 먹이의 거리가 12보다 작으면 점수올림
        score = score + 1
        t.write(score)       # 점수를 화면에 표시
        star_x = random.randint(-230,230)
        star_y = random.randint(-230,230)
        ts.goto(star_x,star_y)

    if(playing): # 게임 플레이 중이면 0.1초 후 play함수 실행
        t.ontimer(play, 100)

def message(m1,m2):   # message 쓰는 함수
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center", ("",20))
    t.goto(0,-100)
    t.write(m2,False,"center", ("",15))
    t.home()


t.title("Trutle Run")
t.setup(500,500)  #그래픽창 크기 조절
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")
t.listen()  # 거북이 그래픽 창이 키보드 입력을 받도록 합니다.
message("Turtle Run", "[Space]")
