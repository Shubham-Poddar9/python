import turtle

def draw_triangle():
    for _ in range(3):
        turtle.forward(100)  
        turtle.left(120)  

def draw_rectangle():
    for _ in range(2):
        turtle.forward(150)  
        turtle.left(90)
        turtle.forward(80) 
        turtle.left(90)

def draw_hexagon():
    for _ in range(6):
        turtle.forward(80)  
        turtle.left(60)  

turtle.setup(500, 500)
turtle.speed(3)  

turtle.penup()
turtle.goto(-200, 100)  
turtle.pendown()
draw_triangle()

turtle.penup()
turtle.goto(100, 100) 
turtle.pendown()
draw_rectangle()

turtle.penup()
turtle.goto(-200, -150)  
turtle.pendown()
draw_hexagon()

turtle.hideturtle()
turtle.done()
