suits = ('C', 'S', 'H', 'D')
faces = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
cards = [suit+face for face in faces for suit in suits]
print (cards)

