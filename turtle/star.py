import turtle
a=turtle.Screen()
a.setup(500,500)
s=turtle.Turtle()
for i in range(3):
    s.forward(100)
    s.left(120)
s.penup()
s.left(90)
s.forward(50)
s.right(90)
s.pendown()
for i in range(3):
    s.forward(100)
    s.right(1200)
turtle.done()
