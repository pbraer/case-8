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


def choose_fractal():
    print('''
    1. Spiral of squares 
    2. Binary tree 
    3. Branch 
    4. Koch's curve 
    5. Koch Snowflake 
    6. Minkowski Curve 
    7. Ice Fractal 1 
    8. Ice Fractal 2 
    9. Levi's Curve 
    10. Harter-Haythaway Dragon Fractal
    ''')
    choice = int(input('Select a fractal: '))
    return choice


def main():
    turtle.speed(999999)
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.Screen().bgcolor('black')
    choice = choose_fractal()
    if choice == 1:
        return square(150)
    if choice == 2:
        return
    if choice == 3:
        return
    if choice == 4:
        return koch_curve(200)
    if choice == 5:
        return koch(150)
    if choice == 6:
        return
    if choice == 7:
        return
    if choice == 8:
        return
    if choice == 9:
        return levi(7, 10)
    if choice == 10:
        return dragon(12, 5)


main()
turtle.done()
