import turtle as t

def polygon(n):
    for x in range(n):
        t.fd(50)
        t.left(360/n)


def polygon2(n,a):
    for x in range(n):
        t.fd(a)
        t.left(360/n)


polygon(3)   # 삼각형을 그립니다.
polygon(5)   # 오각형을 그립니다.

#그림을 그리지 않고 거북이를 100만큼 이동시킵니다.

t.up()
t.fd(100)
t.down()


polygon2(3,75)    #한 변이 75인 삼각형을 그립니다.
polygon2(5,100)   #한 변이 100인 오각형을 그립니다.



a = t.distance(3000,3000)   # 현재위치에서 (x,y) 좌표까지의 거리
b = t.heading()             # 현재 바라보고 있는 각도를 구함
c = t.towards(3000,3000)    # 현재 위치에서 (x,y) 위치까지 바라보는 각도를 구함

print("distince : " ,a )
print("angele   : " ,b )
print("angeleC   : " ,c )

t.setheading(90)  # 거북이가 화면 위쪽(90도)을 바라봅니다.
t.home()          # 거북이가 화면 가운데인 (0,0)에서 오른쪽(0도)로 초기화 됩니다.

def up():
    print("up function In")
    t.setheading(90)
    t.forward(10)
    
def down():
    print("down function In")
    t.setheading(270)
    t.forward(10)


t.onkeypress(up, "Up")
t.onkeypress(down, "Down")     
t.onscreenclick(t.goto)   # 마우스 버튼을 누르면 (goto함수는 거북이를 마우스 버튼을 누른위치로 이동)
#t.ontimer(f, 1000)        # 1초 있다가 f함수 실행

t.listen()  #사용자 입력이 잘 처리되도록 거북이 그래픽창에 포커스를 줍니다.
t.title("Test") # 제목 설정
t.write("Hello")
t.write("Hi",False, "center", ("", 20))

