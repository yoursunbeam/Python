import turtle
import random

def main():
    turtle.hideturtle()
    #здания
    buildings('grey')
    turtle.goto(200,-200)
    turtle.goto(-200,-200)
    turtle.goto(-200,-100)
    turtle.end_fill()
    #небо
    buildings('black')
    turtle.goto(200,200)
    turtle.goto(-200,200)
    turtle.goto(-200,-100)
    turtle.end_fill()

    #окна   
    window(-110,-100)
    window(-80,10)
    window(-50,80)
    window(0,-50)
    window(0,110)
    window(85,0)
    window(85,-120)
    window(120,-90)

    stars1()
    stars2()
    stars3()
    stars4()
    stars5()
    stars6()
    stars7()
    stars1()
    stars2()
    stars3()
    stars4()
    stars5()
    stars6()
    stars7()

def buildings(color):
    turtle.penup()
    turtle.goto(-200,-100)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(190)
    turtle.right(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(85)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(20)

def window(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for col in range(4):      
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

def stars1():
    x=random.randint(-198,-152)
    y=random.randint(-98,198)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.dot()

def stars2():
    x=random.randint(-150,-92)
    y=random.randint(-48,198)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.dot()

def stars3():
    x=random.randint(-90,30)
    y=random.randint(142,198)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.dot()

def stars4():
    x=random.randint(32,67)
    y=random.randint(-58,198)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.dot()

def stars5():
    x=random.randint(72,138)
    y=random.randint(27,198)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.dot()

def stars6():
    x=random.randint(142,178)
    y=random.randint(-44,198)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.dot()

def stars7():
    x=random.randint(182,198)
    y=random.randint(-118,198)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.dot()    




main()
    
    
