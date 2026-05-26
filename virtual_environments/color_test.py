from colorama import Fore, Back, Style, init

# Ініціалізація colorama
init(autoreset=True)

print(Fore.GREEN + "🟢 Цей текст виведено зеленим кольором!")
print(Back.YELLOW + Fore.BLACK + "🟡 Цей текст має жовтий фон та чорні літери!")
print(Style.BRIGHT + Fore.CYAN + "🔵 Цей текст є яскраво-блакитним!")