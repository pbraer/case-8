import turtle

turtle.speed(999999)
turtle.pencolor('white')
turtle.pensize(2)
turtle.Screen().bgcolor('black')



# dragon curve function


def first_step(steps, size):
    if size == 0:
        return
    first_step(steps, size - 1)
    turtle.right(90)
    second_step(steps, size - 1)
    turtle.forward(steps)


def second_step(steps, size):
    if size == 0:
        return
    turtle.forward(steps)
    first_step(steps, size - 1)
    turtle.left(90)
    second_step(steps, size - 1)


def dragon(steps, size):
    turtle.up()
    turtle.goto(-150, -70)
    turtle.down()
    turtle.right(180)
    turtle.forward(size)
    first_step(size, steps)
    turtle.forward(steps)


# Levi curve function

def levi_fun(steps, size):
    if size == 0:
        return turtle.forward(steps)
    turtle.left(45)
    levi_fun(steps, size - 1)
    turtle.right(45)
    turtle.right(45)
    levi_fun(steps, size - 1)
    turtle.left(45)


def levi(steps, size):
    turtle.up()
    turtle.goto(-100, 0)
    turtle.down()
    levi_fun(steps, size)

#dragon(12, 5)
#levi(10, 8)
turtle.done()
