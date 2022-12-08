import turtle

x=-100
y=-100
width=40


def main():
    turtle.hideturtle()
    square(x,y,width)
                        

def square(x,y,width):
    total=0
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for clas in range(5):#остальные строки
        for row in range(5):#нижняя строка
            for col in range(4):#квадрат
                if total%2==0:#цвет
                    turtle.fillcolor('black')
                    turtle.begin_fill()
                    turtle.forward(width)
                    turtle.left(90)
                    turtle.end_fill()
                else:
                    turtle.forward(width)
                    turtle.left(90)
                total=total+1
            x=x+width
            turtle.goto(x,y)
        y=y+width
        x=-100
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
            
        
        
        
    

main()
    
    
