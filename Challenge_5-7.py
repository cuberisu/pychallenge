# turtle graphics: 입력받은 도형을 그리기

import turtle
t = turtle.Pen()
t.shape("turtle")

s = turtle.textinput("거북이가 도형을 그린다!","어떤 도형?")    
# 마찬가지로 textinput() 얘도 str로 받는다

if s == "사각형" or s == "네모":
    s = turtle.textinput("거북이가 네모를 그린다!","가로 길이:")
    w = int(s)
    s = turtle.textinput("거북이가 네모를 그린다!","세로 길이:")
    h = int(s)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
elif s == "삼각형" or s == "세모":
    s = turtle.textinput("거북이가 세모를 그린다!","한 변 길이:")
    s = int(s)
    t.fd(s)
    t.lt(120)
    t.fd(s)
    t.lt(120)
    t.fd(s)
elif s == "원" or s == "동그라미":
    s = turtle.textinput("거북이가 동그라미를 그린다!","반지름 길이:")
    r = int(s)
    t.circle(r)

t.hideturtle()
t._screen.exitonclick()