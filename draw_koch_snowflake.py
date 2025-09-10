import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_koch_snowflake(level):
    window = turtle.Screen()
    window.bgcolor("lightblue")
    t = turtle.Turtle()
    t.color("midnightblue")
    t.pensize(2)
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_curve(t, 300, level)
        t.right(120)

    window.mainloop()

# Введення рівня рекурсії
try:
    level = int(input("Введіть рівень рекурсії (наприклад, 3): "))
    draw_koch_snowflake(level)
except ValueError:
    print("Будь ласка, введіть ціле число.")