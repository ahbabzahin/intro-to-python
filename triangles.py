import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

t = turtle.Turtle()
t.pensize(3)
t.speed(1)

def draw_triangle(t, side_length):
    t.color("red")
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

def draw_rectangle(t, width, height):
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_hexagon(t, side_length):
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.color("purple")
    t.begin_fill()
    for _ in range(6):
        t.forward(side_length)
        t.left(60)
    t.end_fill()

draw_triangle(t, 100)
draw_rectangle(t, 150, 80)
draw_hexagon(t, 60)

screen.exitonclick()