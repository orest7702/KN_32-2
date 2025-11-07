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


user1 = MyName("bohdan")
user2 = MyName("marta")
user3 = MyName()

user1.save_to_file()
user2.save_to_file()
user3.save_to_file()

print(user1.whoami)