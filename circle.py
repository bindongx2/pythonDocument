import turtle as t

n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)        # 거북이 속도를 가장 빠르게 지정합니다.

for x in range(n):
    t.circle(80)  # 현재 위치에서 반지름이 80인 원을 그립니다.
    t.left(n)     # 거북이가 360/n만큼 왼쪽으로 회전합니다.
