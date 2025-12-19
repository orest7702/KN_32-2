import turtle

# Налаштування вікна
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Весела черепашка")

# Створення черепашки
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

# Функція для малювання кола
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Панцир (тіло)
draw_circle("#228B22", 100, 0, -100)

# Голова
draw_circle("#006400", 30, 0, 60)

# Очі
draw_circle("white", 8, -10, 90)
draw_circle("white", 8, 10, 90)
draw_circle("black", 3, -10, 97)
draw_circle("black", 3, 10, 97)

# Верхні лапки
draw_circle("#006400", 20, -85, 20)   # Ліва
draw_circle("#006400", 20, 85, 20)    # Права

# Нижні лапки (підняті вище)
draw_circle("#006400", 20, -65, -110)  # Ліва
draw_circle("#006400", 20, 65, -110)   # Права

# Хвостик (також піднятий)
draw_circle("#006400", 10, 0, -110)

# Завершення
t.hideturtle()
screen.mainloop()
