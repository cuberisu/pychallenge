# 나뭇가지
import turtle, random
def tree(length):
    angle = (random.randint(-20,20))
    if length > 5: 
        t.fd(length)
        t.rt(20 + angle)
        tree(length-15 *(random.random()+0.4))
        t.lt(40 + (angle * 2))
        tree(length-15 *(random.random()+0.4))
        t.rt(20 + angle)
        t.bk(length)
    
t = turtle.Pen()
t.lt(90)
t.color("green")
t.speed(1)
tree(90)