import turtle

BASE_X=0
BASE_Y=-100
BASE_RADIUS=100

MID_X=0
MID_Y=60
MID_RADIUS=60

HEAD_X1=0
HEAD_Y1=150
HEAD_RADIUS1=30
HEAD_X2=10
HEAD_Y2=160
HEAD_RADIUS2=3
HEAD_X3=-10
HEAD_Y3=160
HEAD_RADIUS3=3

MOUTH_X1=-15
MOUTH_Y1=140
MOUTH_X2=15
MOUTH_Y2=140


ARM_LEFT_X1=-60
ARM_LEFT_Y1=60
ARM_LEFT_X2=-100
ARM_LEFT_Y2=75
ARM_LEFT_X3=-110
ARM_LEFT_Y3=120
HAND_LEFT_X1=-100
HAND_LEFT_Y1=130
HAND_LEFT_X2=-120
HAND_LEFT_Y2=130

ARM_RIGHT_X1=60
ARM_RIGHT_Y1=60
ARM_RIGHT_X2=125
ARM_RIGHT_Y2=90
HAND_RIGHT_X1=135
HAND_RIGHT_Y1=80
HAND_RIGHT_X2=130
HAND_RIGHT_Y2=105

HAT_X1=0
HAT_Y1=170
HAT_X2=0
HAT_Y2=170
WIDTH=50

def main():
    turtle.hideturtle()
    drawBase(BASE_X,BASE_Y,BASE_RADIUS)
    drawMidSection(MID_X,MID_Y,MID_RADIUS)
    drawArmLeft(ARM_LEFT_X1,ARM_LEFT_Y1,ARM_LEFT_X2,ARM_LEFT_Y2,ARM_LEFT_X3,ARM_LEFT_Y3,HAND_LEFT_X1,HAND_LEFT_Y1,HAND_LEFT_X2,HAND_LEFT_Y2)
    drawArmRight(ARM_RIGHT_X1,ARM_RIGHT_Y1,ARM_RIGHT_X2,ARM_RIGHT_Y2,HAND_RIGHT_X1,HAND_RIGHT_Y1,HAND_RIGHT_X2,HAND_RIGHT_Y2)
    drawHead(HEAD_X1,HEAD_Y1,HEAD_RADIUS1)
    drawHead(HEAD_X2,HEAD_Y2,HEAD_RADIUS2)
    drawHead(HEAD_X3,HEAD_Y3,HEAD_RADIUS3)
    drawMouth(MOUTH_X1,MOUTH_Y1,MOUTH_X2,MOUTH_Y2)
    drawHat(HAT_X1,HAT_Y1,HAT_X2,HAT_Y2,WIDTH,'black')


def drawBase(x,y,radius):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius)

def drawMidSection(x,y,radius):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius)

def drawHead(x,y,radius):
    turtle.penup()
    turtle.goto(x,y-radius)
    turtle.pendown()
    turtle.circle(radius)

def drawMouth(x1,y1,x2,y2):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    
    
def drawArmLeft(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.goto(x4,y4)
    turtle.penup()
    turtle.goto(x5,y5)
    turtle.pendown()
    turtle.goto(x3,y3)

def drawArmRight(x1,y1,x2,y2,x3,y3,x4,y4):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    turtle.goto(x3,y3)
    turtle.penup()
    turtle.goto(x4,y4)
    turtle.pendown()
    turtle.goto(x2,y2)

def drawHat(x1,y1,x2,y2,width,color):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.goto(x1,y1)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x2-width/2,y2)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    
    
    
    

main()

