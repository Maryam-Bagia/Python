import turtle

def draw_snake_body(color, x, y, width, height, radius, direction):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.setheading(direction)
    for _ in range(2):
        turtle.forward(width - radius * 2)
        turtle.circle(radius, 90)
        turtle.forward(height - radius * 2)
        turtle.circle(radius, 90)
    turtle.end_fill()

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_python_logo():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Python Logo")
    screen.bgcolor("white")

    # Draw the top snake body (yellow)
    draw_snake_body("gold", -100, 100, 200, 150, 50, 0)

    # Draw the bottom snake body (blue)
    draw_snake_body("blue", -100, -50, 200, 150, 50, 0)

    # Draw the top eye
    draw_circle("white", -60, 140, 10)

    # Draw the bottom eye
    draw_circle("white", 60, -10, 10)

    # Draw the dividing mouth line
    turtle.penup()
    turtle.goto(-100, 50)
    turtle.setheading(0)
    turtle.pendown()
    turtle.width(5)
    turtle.color("white")
    turtle.forward(200)

    # Finish up
    turtle.hideturtle()
    screen.mainloop()

# Call the function to draw the Python logo
draw_python_logo()
