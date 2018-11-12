import random

class Card:
    def __init__(self, card_face, card_suit):
        self.card_face = card_face
        self.card_suit = card_suit


    card_face = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_suit = ['H','S','C','D']

    def new_card(self):
        for i in Card.card_suit:
            for j in Card.card_face:
                return(random.pop(self.card_face,self.card_suit))




class Deck(Card):
    new_deck = []
    length = len(new_deck) #testing purposes

    for i in Card.card_suit:
        for j in Card.card_face:
            new_deck.append(i + j)

    def new_card(self):
        # instead of return, use yield?
        return (self.new_deck[randint(0, len(self.new_deck) - 1)])



    #def new_card(self):
     #   return (self.new_deck[random.choice(self.card_face, self.card_suit)])
