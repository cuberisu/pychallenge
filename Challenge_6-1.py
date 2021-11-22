# 1 turtle graphics: 반복을 사용하여 정육각형 그리기
import turtle
t = turtle.Pen()
t.shape("turtle")

for i in range(6):  # 6번 반복
    t.fd(100)
    t.lt(60)

t._screen.exitonclick()