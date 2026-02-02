import random

numbers = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.description = self.number + ' of ' + self.suit


class Deck():
    def __init__(self):
        self.cards = []
        numbers = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        for suit in suits:
            for number in numbers:
                self.cards.append(Card(suit, number))


class Player():
    def __init__(self, name):
        self.name = name
        self.deck = None

    def pickupDeck(self):
        self.deck = Deck()
        
    def shuffleDeck(self):
        random.shuffle(self.deck.cards)

    def dealCard(self):
        card = self.deck.cards.pop()
        print(card.description)

    def printCardsLeft(self):
        print(len(self.deck.cards))

    def hand(self):
        self.hand = player_one.deck()
        player_one.dealCard()
        for cards in self.hand:
            print(self.hand)

        

player_one = Player('Keira')
#player_two = Player('Pedro')

player_one.pickupDeck()
player_one.shuffleDeck()
player_one.printCardsLeft()
player_one.dealCard()
player_one.dealCard()
player_one.hand()




