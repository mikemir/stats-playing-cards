import collections
from deck import Deck

def print_cards(cards):
    for card in cards:
        print(f'{card.get_type()}:{card.get_value()}')

def main(tamano_mano, intentos):
    hand_samples = []
    my_deck = Deck()

    for _ in range(intentos):
        hand_cards = my_deck.get_hand(tamano_mano)
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

    pair_probability = pairs / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {pair_probability}')

if __name__ == "__main__":
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)