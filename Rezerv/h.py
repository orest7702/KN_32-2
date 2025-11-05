import random
names = ["Мечик", "Шпага", "Сокирка", "Спис"]
magic_types = ["Вогонь", "Земля", "Вода", "Вітер"]

def draw_card():
    item = {
        "name": random.choice(names),
        "attack_power": random.randint(4, 8),
        "durability": random.randint(30, 60),
        "magic_attribute": f"Магія: {random.choice(magic_types)}"
    }
    return item

player_1 = list()
player_2 = list()


for move in range(3):
    print("Гравець 1 робить хід:")
    player_1.append(draw_card())
    print("Гравець 2 робить хід:")
    player_2.append(draw_card())

print(f"""Карти у руці гравця 1:
        {player_1}
    Карти у руці гравця 2:
        {player_2}
      """)

def check_if_player_has_cards(list_of_cards: list) -> bool:
    return True if len(list_of_cards) >= 1 else False


for move in range(3):
    if check_if_player_has_cards(player_1):
        card_on_board_1 = player_1.pop()
    else:
        print("У гравця 1 не залишилось карт")
    
    if check_if_player_has_cards(player_2):
        card_on_board_2 = player_2.pop()
    else:
        print("У гравця 2 не залишилось карт")

    while card_on_board_1['durability'] > 0 or card_on_board_2['durability'] > 0:
        card_on_board_1['durability'] -= card_on_board_2["attack_power"]
        card_on_board_2['durability'] -= card_on_board_1["attack_power"]

        print(f"""
        у гравця 1 залишилось витривалості: {card_on_board_1['durability']}
        у гравця 2 залишилось витривалості: {card_on_board_2['durability']}
        """)
    # перевіряємо яка з карт програла
    if card_on_board_1['durability'] <= 0 and check_if_player_has_cards(player_1):
        print("Карта гравця 1 Вибуває, гравець витягує нову карту")
        card_on_board_1 = player_1.pop()
    elif card_on_board_2['durability'] <= 0 and check_if_player_has_cards(player_2):
        print("Карта гравця 2 Вибуває, гравець витягує нову карту")
        card_on_board_2 = player_2.pop()
    else:
        print("У гравців закінчились карти")