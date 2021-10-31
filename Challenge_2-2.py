# turtle graphics: 움직이는 길이를 변수로 지정

import turtle
t = turtle.Pen()
t.shape("turtle")
radius = 50 # 반지름
x = 30  # 거리

t.circle(radius)
t.fd(x)
t.circle(radius)
x = 50  # 변수를 지정하였으므로 거리 바꾸는 게 편리하다
t.fd(x)
t.circle(radius)

t._screen.exitonclick()