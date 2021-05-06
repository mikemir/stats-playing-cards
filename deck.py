import random
from card import Card

CARD_TYPES = ['Espada', 'Trebol', 'Corazon', 'Diamante']
CARD_VALUES = ['AS', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JOTA', 'REINA', 'REY']

class Deck:

    def __init__(self):
        self.__items = self._generate_deck()

    def _generate_deck(self):
        cards = []

        for type in CARD_TYPES:
            for value in CARD_VALUES:
                cards.append(Card(type, value))

        return cards

    def get_hand(self, quantify = 5):
        return random.sample(self.__items, k = quantify)

    def get_items(self):
        return self.__items

    def shuffle(self):
        random.shuffle(self.__items)