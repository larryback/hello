import random

suits = ["spade", "club", "heart", "diamond"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

cards = []
for suit in suits:
    for face in faces:
        cards.append((suit, face))



random.shuffle(cards)
card = cards.pop()
