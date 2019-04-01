from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
ranks_to_values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}
chips = 100
bet = 0


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        print(f'{self.rank} of {self.suit}')


class Deck:
    def __init__(self):
        global suits
        global ranks

        self.cards_deck = []
        for suit in suits:
            for rank in ranks:
                self.cards_deck.append(Card(suit, rank))

    def shuffle(self):
        shuffle(self.cards_deck)

    def __str__(self):
        print(self.cards_deck)

    def draw_card(self):
        self.cards_deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += ranks_to_values[card.rank]

        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        for card in self.cards:
            print(f'{card.rank} of {card.suit}')

        print(f"Your hand's value is {self.value}")


def place_bet():
    global bet
    global chips

    while True:
        try:
            bet = int(input('Place your bet: '))
        except ValueError:
            print("That's not an integer. Try again.")
        else:
            if bet > chips:
                print("Sorry, you don't have that many chips. Try again.")
            elif bet < 0:
                print('Bet has to be a positive number')
            else:
                break


def hit(deck, hand):
    card = deck.draw_card()
    hand.add_card(card)


def hit_or_stand(deck, hand):
    playing = True

    while playing:
        player_input = input('Do you want to hit or stand? h/s: ').lower()

        if player_input == 'h':
            hit(deck, hand)
        elif player_input == 's':
            playing = False
        else:
            print("That's not a valid input. Try again")





