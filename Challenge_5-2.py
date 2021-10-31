# turtle graphics: 입력에 따른 거북이 움직이기

import turtle
t = turtle.Pen()
t.shape("turtle")

t.width(3)  # 선 두께 3픽셀
t.shapesize(3,3)    # 거북이 3배 확대

flag = True     # 루프 제어 변수 flag
while flag:     # True일 때 반복하는 문장. 즉 무한루프. False일 때 종료됨
    command = turtle.textinput("lrq", "명령을 입력하세요.: ")   # 팝업창으로 커맨드 입력시키기
    if command == "l" or command == "left":     # 문자열이니까 따옴표 꼭 붙여라....
        t.lt(90)
        t.fd(100)
    if command == "r" or command == "right":
        t.rt(90)
        t.fd(100)
    if command == "q" or command =="quit":
        flag = False    # 종료 코드
