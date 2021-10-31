# turtle graphics: 사각형을 그리고 각변에 출력하기

import turtle
t = turtle.Pen()
t.shape("turtle")

s = turtle.textinput("","이름을 입력하시오.:")  # 입력받기


t.fd(200) # 정사각형
t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다.")
t.lt(90)
t.fd(200)
t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다.")
t.lt(90)
t.fd(200)
t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다.")
t.lt(90)
t.fd(200)
t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다.")

t._screen.exitonclick()