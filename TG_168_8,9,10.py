if turtle.heading()>=0 and turtle.heading()<=45:
    turtle.penup()


if turtle.pencolor()=='red' or turtle.pencolor()=='blue':
   turtle.pensize(5)


if (turtle.xcor()>=100 and turtle.xcor()<=200
    turtle.ycor()>=100 and turtle.ycor()<=200):
    turtle.hideturtle()
