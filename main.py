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


import turtle as t

# квадрат
def square(a):
    t.pensize(0.02)
    t.pencolor('purple')
    if a < 5:
        return
    t.up()
    t.right(15)
    t.forward(a/8)
    t.down()
    for i in range(4):
        t.forward(a)
        t.right(90)
    t.up()
    return square(a*0.9)
#square(100)

# кривая Коха
def koch(ln):
    if ln > 6:
        ln //= 3
        koch(ln)
        t.left(60)
        koch(ln)
        t.right(120)
        koch(ln)
        t.left(60)
        koch(ln)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)

# снежинка Коха
t.home()
t.up()
t.goto(-200, 0)
t.down()
def koch2(ln):
    if ln > 6:
        ln //= 3
        koch2(ln)
        t.left(60)
        koch2(ln)
        t.right(120)
        koch2(ln)
        t.left(60)
        koch2(ln)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)

t.speed(1000)

koch2(150)
t.right(120)
koch2(150)
t.right(120)
koch2(150)

# кривая Минковского

def mink(order, size):
    if order == 0:
        t.forward(size)
    else:
        mink(order - 1, size / 4)
        t.left(90)
        mink(order - 1, size / 4)
        t.right(90)
        mink(order - 1, size / 4)
        t.right(90)
        mink(order - 1, size / 4)
        t.left(0)
        mink(order - 1, size / 4)
        t.left(90)
        mink(order - 1, size / 4)
        t.left(90)
        mink(order - 1, size / 4)
        t.right(90)
        mink(order - 1, size / 4)


t.done()
