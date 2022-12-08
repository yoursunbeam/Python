import turtle

TOP_X1=-100
TOP_Y1=100
TOP_X2=0
TOP_Y2=100
TOP_X3=100
TOP_Y3=100

MIDDLE_X=0
MIDDLE_Y=0

BOTTOM_X1=-100
BOTTOM_Y1=-100
BOTTOM_X2=0
BOTTOM_Y2=-100
BOTTOM_X3=100
BOTTOM_Y3=-100


def main():
    turtle.hideturtle()
    triangle(BOTTOM_X1,BOTTOM_Y1,BOTTOM_X2,BOTTOM_Y2,MIDDLE_X,MIDDLE_Y,'red')
    triangle(BOTTOM_X2,BOTTOM_Y2,BOTTOM_X3,BOTTOM_Y3,MIDDLE_X,MIDDLE_Y,'blue')
    triangle(MIDDLE_X,MIDDLE_Y,TOP_X1,TOP_Y1,TOP_X2,TOP_Y2,'yellow')
    triangle(MIDDLE_X,MIDDLE_Y,TOP_X2,TOP_Y2,TOP_X3,TOP_Y3,'green')
    
    
   
    
def triangle(x1,y1,x2,y2,x3,y3,color):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x1,y1)
    turtle.end_fill()

main()
