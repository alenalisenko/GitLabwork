import time
import turtle
from random import randrange

BREAK_FLAG = False

# draw a window for the game
screen = turtle.Screen()
screen.title('Snake with turtle module')
screen.bgcolor('orange')
screen.setup(650, 650)
screen.tracer(0)

# draw a game field border
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)

# draw a snake of three segments and
# paint the head of the snake in black
snake = []
for i in range(3):
    snake_segment = turtle.Turtle()
    snake_segment.shape('square')
    snake_segment.penup()
    if i > 0:
        snake_segment.color('gray')
    snake.append(snake_segment)

# draw a food for the snake
food = turtle.Turtle()
food.shape('circle')
food.penup()
food.goto(randrange(-300, 300, 20), randrange(-300, 300, 20))
