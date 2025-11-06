# Звіт до лабораторної роботи №2
# ***Тема***: Знайомство з ООП
# ***Мета роботи*** : Навчитись використовувати основні принципи ООП, розглянути кострукції побудови класу та створення обєктів та навчитись працювати з ними

[Даний](OOP.py) код вивів такі результати 
```plaintext
Розпочинаємо створювати обєкти!
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x763217d291f0> 
This is object attribute: Bohdan / 1
This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua
This is <class 'method'> call: Bohdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone! 
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x763217d29220> 
This is object attribute: Marta / 2
This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
This is <class 'method'> call: Marta@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone! 
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x763217d29250> 
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone! 
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
We are done. We create 4 names! ??? Why 4?
```

([Тутоньки](MY_OOP_COD.md) детальніше розбираємо приклади розглянуті на парі(по темі функціонального та ООП стилях програмування)

---


Для додавання свого імя в список достатньо вказати його тут 
```python
names = ("Bohdan", "Marta", "Orest", None)
```
---


Тому що виконується цей код 
```python 
self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
```
Це свого роду "запасний", "Дефолтний" варіант
---


Для зміни тексту достатньо змінити текст у лапках "Hello to everyone!" та "You say"

```python
def say_hello(message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message}"
```
---


Функція яка буде підраховувати кількість букв у імені 
```python

def count_letters(self) -> int:
        """Instance method
        return: кількість букв у імені
        """
        return len(self.name)
```
---


Різна кількість імен із за того що присутній "дефолтний" варіант None

```python

MyName.total_names += 1 # modify class variable

```
```plaintext

 MyName("Bohdan") → total_names = 1
 MyName("Marta") → total_names = 2
 MyName(None)
  - викликає MyName("Anonymous") → total_names = 3
  - потім завершує MyName(None) → total_names = 4

```
---


Щоб зробити ім'я з великої літери нам просто імена треба передавати в метод capitalize()

```python
def __init__(self, name=None) -> None:
    """Ініціалізація класу
    """
    if name is None:
        self.name = "Anonymous"
    else:
        # Робимо першу літеру великою, а решту залишаємо як є
        self.name = name.capitalize()
    MyName.total_names += 1
    self.my_id = self.total_names

```
---

Для того щоб можна було модифікувати запис після @ ми будем передавати наш запис і просто вставляти його після @
```python
def create_email(self, domain="itcollege.lviv.ua") -> str:
    """Instance method
    Створює e-mail з можливістю змінювати домен.
    """
    return f"{self.name}@{domain}"

```
---


Для перевірки імені на літери так щоб були лише вони ми теж скористаємось методом, а саме "isalpha()"
```python

if not name.isalpha():
        raise ValueError("Ім'я може містити лише літери!")
```
---

Ось як зробити нову функцію для повернення  
```txt   
"User #<id>: <name> (<email>)"
```
```python
@property
def full_name(self) -> str:
"""Class property
return: повна інформація про користувача
"""
return f"User #{self.my_id}: {self.name} ({self.my_email})"
```
---

Такий вигляд буде мати функція для збереження інформації про user в файл 'users.txt'
```python
def save_to_file(self, filename="users.txt") -> None:
"""Instance method — зберігає інформацію про користувача у файл."""
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")
```
---

# Після проведених операцій наш клас буде мати такий вигляд 

```python
class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        if name is None:
            self.name = "Anonymous"
        else:
            # Робимо першу літеру великою
            name = name.capitalize()

            # Перевіряємо, щоб ім’я містило лише літери
            if not name.isalpha():
                raise ValueError("Ім'я може містити лише літери!")

            self.name = name

        MyName.total_names += 1
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
        """Class property"""
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property"""
        return self.create_email()
    
    def create_email(self, domain="itcollege.lviv.ua") -> str:
        """Instance method — створює e-mail з можливістю змінювати домен."""
        return f"{self.name}@{domain}"

    @property
    def full_name(self) -> str:
        """Class property — повна інформація про користувача."""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def save_to_file(self, filename="users.txt") -> None:
        """Instance method — зберігає інформацію про користувача у файл."""
        with open(filename, "a", encoding="utf-8") as file:
            file.write(self.full_name + "\n")
            print("Все готово")

    @classmethod
    def anonymous_user(cls):
        """Class method"""
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method"""
        return f"You say: {message}"

```
---

## Для того щоб перевірити чи все працює ми зараз викличемо кожну функцію (метод) та виведем результат [сюда](OOP.ipynb)

