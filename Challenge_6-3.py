# 3 turtle graphics: 지멋대로 가는 거북이
# 거북이가 90도로만 움직이게 하기
# (90, 180, 270, 360도 중 하나를 선택)

import turtle, random
t = turtle.Pen()
t.shape("turtle")

for i in range(30):  # 30번 이동
    angle = random.randrange(90, 361, 90)   
            # 90에서 시작, 360까지 90 간격으로 증감
    length = random.randint(0, 100)
    t.fd(length)
    t.lt(angle)

t._screen.exitonclick()