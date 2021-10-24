# (1)
import turtle
t = turtle.Pen()
t.shape("turtle")
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.clear()   # 모든 선 없애기
t.ht()  # 거북이 없애기

# (2)
import turtle
t = turtle.Pen()
t.shape("turtle")
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t._screen.exitonclick()     # 클릭해야 창이 닫히게 하는 코드