import turtle, time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Lights
def draw_light(color, y):
    t = turtle.Turtle()
    t.penup()
    t.goto(-80, y)
    t.shape("circle")
    t.color(color)
    return t

red = draw_light("red", 70)
yellow = draw_light("grey", 40)
green = draw_light("grey", 10)

# Robot
robot = turtle.Turtle()
robot.shape("square")
robot.color("blue")
robot.penup()
robot.goto(-200, -50)

# Light sequence
def traffic_sequence():
    red.color("red")
    time.sleep(2)
    red.color("grey"); yellow.color("yellow")
    time.sleep(1)
    yellow.color("grey"); green.color("green")
    time.sleep(0.5)
    for _ in range(50):
        robot.forward(5)
        time.sleep(0.05)

traffic_sequence()
turtle.done()
