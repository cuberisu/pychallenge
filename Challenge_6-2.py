# 2 turtle graphics: forward(len)(변수?)을 활용하여 n각형 그리기
# 모양, 한 변의 크기를 입력받기

import turtle
t = turtle.Pen()
t.shape("turtle")

n = int(turtle.textinput("귀여운 거북이", "몇각형을 그릴까요?"))
side = int(turtle.textinput("귀여운 거북이", "한 변의 길이는요?"))
for i in range(n):
    t.fd(side)
    t.lt(360/n)

t._screen.exitonclick()