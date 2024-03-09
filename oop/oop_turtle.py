from turtle import Turtle, Screen
my_screen = Screen()
donatello = Turtle()
donatello.shape('turtle')
donatello.color('red')
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(200)
donatello.home()

raphael = Turtle()
raphael.shape('turtle')
raphael.color('green')
raphael.penup()
raphael.goto(-150, 200)
raphael.pendown()
raphael.pencolor('blue')

x = 10
while x <= 50:
    raphael.circle(x)
    donatello.circle(x + 5)
    x += 10

my_screen.exitonclick()