import turtle
import math

width=int(input('Введите ширину узора '))
height=int(input('Введите высоту узора '))

angle_radianA=math.atan(height/width)
angle_degreeA=(angle_radianA*180)/3.14

angle_radianB=math.atan(width/height)
angle_degreeB=(angle_radianB*180)/3.14
color='black'

diagonal=math.sqrt(width**2+height**2)


def main():
    turtle.hideturtle()
    drawPattern(width,height)
    

def drawPattern(x,y):
    #внешний прямоугольник
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.pendown()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    #диагонали
    turtle.left(90+angle_degreeA)
    turtle.forward(diagonal)
    turtle.left(90+angle_degreeB)
    turtle.penup()
    turtle.forward(x)
    turtle.pendown()
    turtle.left(90+angle_degreeB)
    turtle.forward(diagonal)
    turtle.left(90+angle_degreeA)
    #деление внешнего пряумоугольника на 4 равных прямоугольника
    turtle.penup()
    turtle.forward(y/2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(x)
    turtle.right(90)
    turtle.penup()
    turtle.forward(y/2)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(y)
    #незакрашенный внутренний прямоугольник
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.left(90+angle_degreeA)
    turtle.forward(diagonal/8)
    turtle.pendown()
    turtle.right(angle_degreeA)
    turtle.forward(3*x/4)
    turtle.left(90)
    turtle.forward(3*y/4)
    turtle.left(90)
    turtle.forward(3*x/4)
    turtle.left(90)
    turtle.forward(3*y/4)
    #закрашенный внутренний прямоугольник
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.left(90+angle_degreeA)
    turtle.forward(diagonal/4)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(angle_degreeA)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(y/2)
    turtle.left(90)
    turtle.forward(y/2)
    turtle.left(90)
    turtle.forward(y/2)
    turtle.end_fill()
    
    
    
    
    
main()
