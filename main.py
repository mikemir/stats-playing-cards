import collections
from deck import Deck


def print_cards(cards):
    for card in cards:
        print(card)


def main(size_hand, intents):
    hand_samples = []
    my_deck = Deck()

    for _ in range(intents):
        hand_cards = my_deck.get_hand(size_hand)
        hand_samples.append(hand_cards)
        print_cards(hand_cards)
        print('=' * 50)

    pairs = 0
    for hand in hand_samples:
        card_values = []
        for card in hand:
            card_values.append(card.get_value())

        counter = dict(collections.Counter(card_values))
        for val in counter.values():
            if val == 2:
                pairs += 1
                break

    pair_probability = pairs / intents
    print(f'La probabilidad de obtener un par en una mano de {size_hand} cartas es {pair_probability}')


if __name__ == "__main__":
    size_hand = int(input('De cuantas cartas sera la mano: '))
    intents = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(size_hand, intents)
