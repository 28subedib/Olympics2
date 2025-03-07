import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('Tan')
t = turtle.Turtle()

#circle
t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor('blue')
t.circle(35)
#circle
t.penup()
t.goto(0,15)
t.pendown()
t.pencolor('black')
t.circle(35)
#circle
t.penup()
t.goto(80,15)
t.pendown()
t.pencolor('red')
t.circle(35)
#circle
t.penup()
t.goto(-40,-15)
t.pendown()
t.pencolor('yellow')
t.circle(35)
#circle
t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor('green')
t.circle(35)
#text on the screen
t.penup()
t.goto(-150,100)
t.pendown()
t.pencolor("purple")
t.write("Winter Olympics", font=("Arial",30,"bold"))
#text on the screen
t.penup()
t.goto(-40,-100)
t.pendown()
t.pencolor("purple")
t.write("2026", font=("Arial",30,"bold"))
#This is the last line of code
turtle.done()






