"""
GAME: Hit the Target
Description:    Modified the exercise in Chapter 3 of
                Starting Out with Python, 5th Edition
                by Tony Gaddis
"""

import math
import random
import turtle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
target_play = True

while target_play:
    TARGET_LLEFT_X = random.choice([100, 250, 300])
    TARGET_LLEFT_Y = random.choice([200, 250, 350])

    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()

    turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
    turtle.pensize(3)

    turtle.pendown()
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()

    turtle.goto(0, 0)
    turtle.pensize(1)
    turtle.setheading(EAST)
    turtle.showturtle()
    turtle.speed(PROJECTILE_SPEED)

    angle = turtle.numinput("Angle", "Enter the Angle: ")
    force = turtle.numinput("Projectile", "Enter a value in the range 1-15", default=7.5, minval=1, maxval=15)

    distance = force * FORCE_FACTOR

    turtle.setheading(angle)

    turtle.pendown()
    turtle.forward(distance)

    target_hit = True

    if (TARGET_LLEFT_X <= turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH)
            and TARGET_LLEFT_Y <= turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        target_hit = True
        turtle.color("green")
        turtle.write('Target hit!', font=("Arial", 12, "normal"))
    else:
        target_hit = False
        turtle.color("red")
        turtle.write('You missed the Target.', font=("Arial", 12, "bold"))
        actual_angle = math.degrees(math.atan(TARGET_LLEFT_Y / TARGET_LLEFT_X))
        actual_distance = math.sqrt((TARGET_LLEFT_Y * TARGET_LLEFT_Y + TARGET_LLEFT_X * TARGET_LLEFT_X))
        force_actual = actual_distance / FORCE_FACTOR

        turtle.hideturtle()
        turtle.penup()

        turtle.color("blue")

        turtle.goto(-250, 25)

        if angle > actual_angle:
            turtle.write(f'Choose a smaller angle than {angle}', font=("Arial", 12, "normal"))
        elif angle == actual_angle:
            turtle.write('Correct angle')
        else:
            turtle.write(f'Choose a bigger angle than {angle}', font=("Arial", 12, "normal"))

        turtle.goto(-250, 0)

        if force > force_actual:
            turtle.write(f'Choose a smaller force than {force}', font=("Arial", 12, "normal"))
        elif force == force_actual:
            turtle.write('Correct force')
        else:
            turtle.write(f'Choose a bigger force than {force}', font=("Arial", 12, "normal"))

    play = turtle.numinput('Play again?', 'Enter 1 for yes or 2 to exit', default=1, minval=1, maxval=2)

    if play == 1:
        target_play = True
        turtle.reset()
    else:
        target_play = False

turtle.done()
