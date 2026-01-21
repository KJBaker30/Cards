import random

numbers = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

class Player():
    def __init__(self,name):
        self.name = name
        self.deck = None 

    def pickupDeck():
        numbers = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        Deck = Card(suits,numbers)  # Need to number each card (0-52) 
    def shuffleDeck():
        random(Deck)                # shuffle (random) number between 0-52 when each value is assigned a number.
        def dealCard():
            Deal = Deck - random(Card) and player_one or player_two + Card # do I need the 'random' or will shuffle do that for me? (Not sure how to word the 'and' statement.)

class Deck():
    def __init__(self):
        for suit in suits:
            for number in numbers:
                self.cards = (number, 'of', suit)   # Not sure?

class Card():
    def __init__(self,suits,numbers):
        self.suits = suits
        self.numbers = numbers

player_one = Player('Keira')
player_two = Player('Pedro')

player_one.pickupDeck()
player_one.shuffleDeck()
player_one.dealCard()
