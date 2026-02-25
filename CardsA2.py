import random

numbers = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


class Card(): # for each card:
    def __init__(self, suit, number): # they will have a suit and a number 
        self.suit = suit
        self.number = number
        self.description = self.number + ' of ' + self.suit  # when a card needs to be defined, it will have the description: number 'of' suit.


class Deck(): # for each deck:
    def __init__(self, empty): # it can hold an item (or items), or it can be empty 
        self.cards = [] # the deck holds 'cards'
        numbers = ('A','2','3','4','5','6','7','8','9','10','J','Q','K') 
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        for suit in suits: # going through each suit for the following:
            for number in numbers: # each suit will be paired with the following numbers
                self.cards.append(Card(suit, number)) # the cards held in 'deck' will all gain an individual suit and number 
         


class Player(): # for each player:
    def __init__(self, empty, name): # the player has to have a name
        self.name = name # players name 
        self.deck = None # player has a deck
        self.hand = Deck(empty=True) # player has a hand 
        for self.hand in Player:  # for said hand..
            if empty == True:  # if the hand is empty..
                self.hand == None  # it holds no cards 
            else: # otherwise 
                self.hand.append(Card) # the hand holds cards


    def pickupDeck(self): # the action to pick up a deck
        self.deck = Deck() # the deck that has been picked up is the same deck as defined in the ClassDeck() (holding all 52 cards)
        
    def shuffleDeck(self): # the action to shuffle the deck held 
        random.shuffle(self.deck.cards) # randomises the order of said deck of cards 

    def dealCard(self): # the action to hand out a card 
        card = self.deck.cards.pop() # the card has to be taken out of the deck to be handed to a player (so no repeated cards as 'pop' removes the card from the deck and doesn't then return it back to the deck (one less card in the deck, plus one card to the player))
        print(card.description) # prints 'number 'of' suit' of the card dealt 

    def printCardsLeft(self):  # how many cards are left
        print(len(self.deck.cards)) # prints how many cards left in the deck

    

    

        

player_one = Player('Keira')
#player_two = Player('Pedro')

player_one.pickupDeck()
player_one.shuffleDeck()
player_one.printCardsLeft()
player_one.dealCard()
player_one.dealCard()
player_one.hand()




