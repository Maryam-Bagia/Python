import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_spokes(x, y, radius, num_spokes):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(num_spokes):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.left(360 / num_spokes)

def indian_flag():
    screen = turtle.Screen()
    screen.title("Indian Flag")
    screen.bgcolor("white")
    turtle.speed(3)

    # Saffron Rectangle
    draw_rectangle("orange", -180, 100, 360, 50)

    # White Rectangle
    draw_rectangle("white", -180, 50, 360, 50)

    # Green Rectangle
    draw_rectangle("green", -180, 0, 360, 50)

    # Blue Ashoka Chakra
    draw_circle("blue", 0, 50, 20)
    draw_spokes(0, 50, 20, 24)

    turtle.hideturtle()
    screen.mainloop()

indian_flag()
