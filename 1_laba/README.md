# Звіт до роботи
## Тема: _робота з Python_ 
### Мета роботи: Навчитись кодити на Python з використанням опису на Markdown

---
### Виконання роботи
* Результати виконання завдання *1 лабораторної роботи*
    1. Зробив студент 3 курсу Михайлів Орест Михайлович
    2. Програма вивела значення:
    ```
    PS D:\KN_32-2> & C:/Users/SystemX/AppData/Local/Programs/Python/Python313/python.exe d:/KN_32-2/1_laba/first_progect.py     
    Orest start programming at 2025-09-11 18:32:45.611241. Lviv is the best city!
    ```
    3. Отримані дані точного часу 
    4. Здобув практичні навички роботи з *GitHub*, *Markdown* та *Visual Code*
   

![alt text](image.png)
    

   
 - Ось цей код з можливістю копіювати

    ```python
    from datetime import datetime
    name = "Orest"
    location = "Lviv"

    print(f"{name} start programming at {datetime.now()}. {location} is the best city!")
    ```
- також ось __PYTHON__ код який за допомогою бібліотеки Turtle малює  

![](/1_laba/turtle.png)

    
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


## Висновок:
> у висновку потрібно відповісти на запитання:

- Дана робота була зроблена для демокстрації набутих навичок;
- Мета роботи було воконана так як освоїв програми для роботи в сфері IT;
- Отримані навички в розробленні свого рипозиторія і т.д.;
- вдалось виконати усі поставлені завдання перед собою;
- Звісно виникили проблеми але вони досить легко були виправлені;
- Точно сказати не можу але впринципі може бути;
- Немаю;
