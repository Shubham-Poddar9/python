import turtle
import random
a=turtle.Screen()
a.setup(400,500)
s=turtle.Turtle()
w=["red","orange","yellow","purple","silver"]
for i in range(100):
    s.pencolor(random.choice(w))
    s.forward(i*5)
    s.left(90)
s.done()