class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

colors = ["S", "C", "H", "D"]

values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [Card(value, color) for value in range(1, 14) for color in colors]

print(deck)

