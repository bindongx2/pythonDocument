import turtle as t

n=5  #오각형을 그립니다.(다른 값을 입력하면 다른 도형을 그립니다.)
t.color("purple")
t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()
