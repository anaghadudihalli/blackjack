from random import shuffle
from time import sleep

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
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


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
        cards_str = ''
        for card in self.cards_deck:
            cards_str += '\n' + card.__str__()
        return cards_str

    def draw_card(self):
        return self.cards_deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += ranks_to_values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def place_bet():
    global bet, chips

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


def hit(deck_, hand):
    card = deck_.draw_card()
    hand.add_card(card)


def hit_or_stand(deck_, hand):
    global playing
    playing = True

    while True:
        player_input = input('Do you want to hit or stand? h/s: ').lower()

        if player_input == 'h':
            hit(deck_, hand)
        elif player_input == 's':
            playing = False
        else:
            print("That's not a valid input. Try again")
            continue
        break


def show_some_cards(player_, dealer_):
    print("Dealer:")
    for index, card in enumerate(dealer_.cards):
        if index == 1:
            print('Face Down')
        else:
            print(card)

    print("You:")
    for card in player_.cards:
        print(card)
    print("Your hand value: " + str(player_.value))


def show_all_cards(player_, dealer_):
    print("Dealer:")
    for card in dealer_.cards:
        print(card)
    print("Dealer's hand value: " + str(dealer_.value))

    print("You:")
    for card in player_.cards:
        print(card)
    print("Your hand value: " + str(player_.value))


def player_busts():
    global chips, bet
    print("Player busts!")
    chips -= bet


def player_wins():
    global chips, bet
    print("Player wins!")
    chips += bet


def dealer_busts():
    global chips, bet
    print("Dealer busts!")
    chips += bet


def dealer_wins():
    global chips, bet
    print("Dealer wins!")
    chips -= bet


def tie():
    print("Dealer and Player tie!")


def replay():
    global chips, bet, playing

    replay_choice = input("Do you want to play again? y/n?").lower()

    if replay_choice == 'y':
        if chips > 0:
            playing = True
            while True:
                chips_choice = input("Do you want to continue with same number of chips or renew them? s/r? ").lower()
                if chips_choice == 's':
                    bet = 0
                    return True
                elif chips_choice == 'r':
                    chips = 0
                    bet = 0
                    return True
                else:
                    print("Invalid input. Please try again.")
                    continue
        else:
            print("Sorry, you don't have any coins.")


if __name__ == '__main__':
    print('\nWelcome to BlackJack! Get ready to play!! ')
    while True:
        print('\nShuffling the deck ... Gimme a min')
        deck = Deck()
        deck.shuffle()
        sleep(2)
        print(f'Alrighty! You have {chips} chips.')
        place_bet()
        print('Dealing cards ..')
        player = Hand()
        dealer = Hand()
        for _ in range(0, 2):
            hit(deck, player)
            hit(deck, dealer)
        show_some_cards(player, dealer)

        while playing:
            hit_or_stand(deck, player)
            show_some_cards(player, dealer)

            if player.value > 21:
                player_busts()
                break

        if player.value <= 21:

            while dealer.value < 17:
                hit(deck, dealer)

            show_all_cards(player, dealer)

            if dealer.value > 21:
                dealer_busts()

            elif dealer.value > player.value:
                dealer_wins()

            elif dealer.value < player.value:
                player_wins()

            else:
                tie()

        print(f"\nPlayer's winnings stand at {chips}")

        if not replay():
            print("Thanks for playing!")
            break
