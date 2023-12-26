import random
from game_set_up import Card

class Pile:
    types = ["draw pile", "stock"]
    piles = []
    def __init__(self, pile_type, initial_cards):
        self.pile_type = pile_type
        self.card_list = initial_cards
        Pile.piles.append(self)

    def display_cards(self):
        for card, i in enumerate(self.card_list):
            card.display(self.location, i)


    @classmethod
    def display_cards_manager(cls):
        for i, pile in enumerate(cls.piles):
            print(f"\n{pile.card_list}: {i}: {pile.pile_type}:")


    def insert_into_stock(self, stock):
        if self.type != "draw cards":
            print('wrong type')
            return
        
        if self.card_list:
            stock.card_list.append(self.card_list.pop())



 
    def insert(self, other_pile):
        other_pile.card_list.append(self.card_list.pop())

    def can_insert(self, other_pile):
        print(f"{self.pile_type = } { other_pile.pile_type = }")
        if other_pile.pile_type == "tableau":
            top_card_is_one_less = self.card_list[-1] == other_pile.card_list[-1]-1
            if top_card_is_one_less:
                return True
        
            top_card = self.card_list[-1]
            if top_card == 13 and not other_pile.card_list:
                return True
        
        if self.pile_type == 'draw pile' and other_pile.pile_type == 'stock':
            return True
        
        return False
        


all_cards = list(range(1, 14))
for i in range(2):
    all_cards.extend(all_cards)
    random.shuffle(all_cards)

start_index, end_index = 0, 8
for i in range(5):
    Pile("tableau", all_cards[start_index:end_index])
    del all_cards[start_index:end_index]

Pile("draw pile", all_cards)
Pile("stock", [])


while True:
    Pile.display_cards()

    top_draw_card = Pile.piles[5].card_list[-1]
    if top_draw_card == 1:
        Pile(Pile.piles[5].card_list.pop(), "discard pile")
        continue

    pile1 = int(input("pile1: "))
    pile2 = int(input("pile2: "))
    if Pile.piles[pile1].can_insert(Pile.piles[pile2]):
        Pile.piles[pile1].insert(Pile.piles[pile2])

    else:
        print("move not allowed")
