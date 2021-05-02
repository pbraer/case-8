# Case-study #8-2
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)

import turtle
# squares function
def square_draw(a):
    if a < 5:
        return
    turtle.up()
    turtle.right(15)
    turtle.forward(a/8)
    turtle.down()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.up()
    return square(a*0.9)


def square(a):
    turtle.up()
    turtle.goto(-50, 50)
    turtle.down()
    square_draw(a)


# Koch's curve
def koch_curve_draw(ln):
    if ln > 6:
        ln //= 3
        koch_curve_draw(ln)
        turtle.left(60)
        koch_curve_draw(ln)
        turtle.right(120)
        koch_curve_draw(ln)
        turtle.left(60)
        koch_curve_draw(ln)
    else:
        turtle.fd(ln)
        turtle.left(60)
        turtle.fd(ln)
        turtle.right(120)
        turtle.fd(ln)
        turtle.left(60)
        turtle.fd(ln)


def koch_curve(ln):
    turtle.up()
    turtle.goto(-ln * 1.2, 0)
    turtle.down()
    koch_curve_draw(ln)


# Koch's snowflake function
def koch_step(ln):
    if ln > 6:
        ln //= 3
        koch_step(ln)
        turtle.left(60)
        koch_step(ln)
        turtle.right(120)
        koch_step(ln)
        turtle.left(60)
        koch_step(ln)
    else:
        turtle.fd(ln)
        turtle.left(60)
        turtle.fd(ln)
        turtle.right(120)
        turtle.fd(ln)
        turtle.left(60)
        turtle.fd(ln)


def koch(ln):
    turtle.home()
    turtle.up()
    turtle.goto(-200, 120)
    turtle.down()
    koch_step(ln)
    turtle.right(120)
    koch_step(ln)
    turtle.right(120)
    koch_step(ln)


# Minkovsky's curve
# ?
def mink(m):
    if m < 5:
        return
    else:
        turtle.forward(m)
        turtle.left(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(2 * m)
        turtle.left(90)
        turtle.forward(m)
        turtle.left(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)


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


# Levi's curve function
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

def ice(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        ice(order-1, size / 3)
        turtle.left(90)
        ice(order - 1, size / 3)
        turtle.right(180)
        ice(order - 1, size / 3)
        turtle.left(90)
        ice(order - 1, size / 3)
        ice(order - 1, size / 3)
        turtle.right(90)
        ice(order - 1, size / 3)
        turtle .left(90)



turtle.done()
