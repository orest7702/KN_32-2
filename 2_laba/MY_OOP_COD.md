# Звіт до роботи
## Тема: Знайомство з ООП
### Мета роботи: Начитись використовувати основні принципи ООП, розглянути кострукції побудови класу та створення обєтів та навчитись працювати з ними

---
### Виконання роботи
* Результати виконання завдання ;
    1. Запустили створення класу з github. Програма вивела значення 
>Розпочинаємо створювати обєкти!
*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x00000227F2F76F90> 
This is object attribute: Bohdan / 1
This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua
This is <class 'method'> call: Bohdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x00000227F31E4B90>
This is object attribute: Marta / 2
This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
This is <class 'method'> call: Marta@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>

>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x00000227F31E4CD0>
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
We are done. We create 4 names! ??? Why 4?

2. не можу
3. +-знаю
4. >*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x0000028EEC6A6F90>
This is object attribute: Орест / 1
This is <class 'property'>: My name is Орест / Орест@itcollege.lviv.ua
This is <class 'method'> call: Орест@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 5 / from object 5
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>

5. 1. Тому що є функція скажем так дефолтних значень і про передавані none робиться дефолтний запис
    > self.name = name if name is not None else self.anonymous_user().name цей рядок перевіряє якщо є none то виводити anonymous
   2. > @staticmethod  
        def say_hello(message="Hello to everyone!") -> str:  
        """Static method
        """  
        return f"You say: {message}"  #тут замість "You say" треба написти свій тип привітання
        
* з використанням URL ![alt text](https://github.com/BobasB/it_college/raw/main/reports/pictures/logo-lit.jpg "ІТ Коледж")
    
* через локальні шляхи ![alt text](./pictures/logo-lit.jpg "ІТ Коледж")

* вставлений код / текстовий або числовий результат / інші результати:
    - так можна вставляти код, або просто вствляйте посилання на файл з програмою;
    ```python
    def simple_function_example():
        pass
    ```
    - якщо потрібно виділити текст, тоді:
    ```text
    << Тут можна писати те що хочемо виокремити >>
    ```

* результати виконання індивідуального завдання (якщо такі є);

---
### Висновок:
> у висновку потрібно відповісти на запитання:

- :question: Що зроблено в роботі;
- :question: Чи досягнуто мети роботи;
- :question: Які нові знання отримано;
- :question: Чи вдалось відповісти на всі питання задані в ході роботи;
- :question: Чи вдалося виконати всі завдання;
- :question: Чи виникли складності у виконанні завдання;
- :question: Чи подобається такий формат здачі роботи (Feedback);
- :question: Побажання для покращення (Suggestions);

---