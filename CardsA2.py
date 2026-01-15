class Player():
    def __init__(self,name):
        self.name = name
        self.deck = None 

    def pickupDeck():
        number = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
        suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        Deck = Card(suit,number)
    def shuffleDeck():
        pass
    def dealCard():
        pass

class Deck():
    def __init__(self):
        for suit in suit:
            for number in number:
                []

class Card():
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number

player_one = Player('Keira')
player_two = Player('Pedro')

player_one.pickupDeck()
player_one.shuffleDeck()
player_one.dealCard()
