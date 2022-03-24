import random

class Card:
    suits = ['clubs', 'hearts', 'diamonds', 'spades']

    # values = {
    #     'Two': 2,
    #     'Three': 3,
    #     'Four': 4,
    #     'Five': 5,
    #     'Six': 6,
    #     'Seven': 7,
    #     'Eight': 8,
    #     'Nine': 9,
    #     'Ten': 10,
    #     'Jack': 11,
    #     'Queen': 12,
    #     'King': 13,
    #     'Ace': 14
    # }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value} of {self.suit}'

    @classmethod
    def compare_cards(cls, card_1, card_2):
        """compares values to see which card is higher and prints the winner"""
        if card_1.value > card_2.value:
            print(f'{card_1.value} of {card_1.suit} wins!')
        elif card_1.value < card_2.value:
            print(f'{card_2.value} of {card_2.suit} wins!')
        else:
            print('Draw!')

class Deck:

    def __init__(self):
        self.cards = []

    def build(self):
        for suit in Card.suits:
            for value in range(2, 15):
                self.cards.append(Card(value, suit))
        return

    def show(self, position_in_deck):
        print(self.cards[position_in_deck])

    def pick_card(self):
        card = random.randint(0, 51)
        self.show(card)

    def num_of_cards_remaining(self):
        cards_in_deck = len(self.cards)
        return cards_in_deck

    def remove_random_card(self):
        card_idx = random.randint(0, len(self.cards) - 1)
        card_to_remove = self.cards[card_idx]
        self.cards.remove(card_to_remove)
        cards_left = self.num_of_cards_remaining()
        print(f'{card_to_remove} was removed from the deck.')
        print(f'There are {cards_left} cards remaining in the deck.')


deck = Deck()
print(deck.cards)
deck.build()






