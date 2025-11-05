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

([Тут](MY_OOP_COD.md) детальніше розбираємо приклади розглянуті на парі(по темі функціонального та ООП стилях програмування)

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

