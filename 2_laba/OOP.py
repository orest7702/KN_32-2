import random

class Game():
    def __init__(self, name):
        self.name = name
        self.names =  ["Мечик", "Шпага", "Сокирка", "Спис"]
        self.magic_types =  ["Вогонь", "Земля", "Вода", "Вітер"]
        self.player_cards = {}

    def draw_card (self):  #витягаєм карти
        cards = []
        for move in range(3):
            item = {
                "name": random.choice(self.names),
                "attack_power": random.randint(4, 8),
                "durability": random.randint(30, 60),
                "magic_attribute": f"Магія: {random.choice(self.magic_types)}" 
            }
            cards.append(item)

        self.player_cards[self.name] = cards
        print(self.player_cards)
        return item
    
    def show_cards(self):
        print(f"""Карти у руці гравця {self.name}:
            {self.player_cards[self.name]}
        """)
    
    def fight (self, other):
        for round in range(3):
            card_on_board_1 = self.player_cards[self.name].pop()
            card_on_board_2 = other.player_cards[other.name].pop()
            while card_on_board_1['durability'] > 0 and card_on_board_2['durability'] > 0:
                card_on_board_1['durability'] -= card_on_board_2["attack_power"]
                card_on_board_2['durability'] -= card_on_board_1["attack_power"]
                if card_on_board_1['durability'] <= 0 or card_on_board_2['durability'] <= 0:
                    break
                print(f"""
                у гравця 1 залишилось витривалості: {card_on_board_1['durability']}
                у гравця 2 залишилось витривалості: {card_on_board_2['durability']}
                """)
            print(f"Переміг гравець: {self.name if card_on_board_1['durability'] > card_on_board_2['durability'] else other.name}")
            
   