import random

#print('Hello ')
#name = 'K'
#print(name)
#Linear.py


#def write_hello():
  #  print('hello')

#def write_name(name):
 #   print(name)

#write_hello()
#write_name('K') 
#Functional.py


def card_number(number):
     if number == 1:
         return("Ace")
     elif number == 11:
         return("Jack")
     elif number == 12:
       return("Queen")
     elif number == 13:
         return("King")
     else:
         return(str(number))
    

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

random_number = random.randint(1,13)
random_suit = random.choice(suits)
random_card = print(card_number(random_number), 'of', random_suit)



#now using classes:

class Cards:
    suits = ""
    number = ""
    def function(self):
        self.suits = []
        self.number = ()


    
    
