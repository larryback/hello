from random import shuffle

suits = ['C', 'S', 'H', 'D']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
cards = [suit+rank for rank in ranks for suit in suits]
print (cards)


def deck():
    return [[rank, suit] for rank in ranks for suit in suits]

d = deck()
shuffle(d)

# boolean variable that indicates whether player has gone bust yet
player_in = True

# issue the player and dealer their first two cards
player_hand = [d.pop(), d.pop()]
dealer_hand = [d.pop(), d.pop()]


#a = 0 

#while len(print(cards)) > 0:


#    random.shuffle(print(cards))

 #   print (random.shuffle(print(cards))

 #   a = a + 1
