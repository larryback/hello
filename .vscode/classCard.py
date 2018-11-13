class Card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "The {} of {}".format(self.value, self.suit)

    def intValue(self):
        if self.value.isdigit():
            return int(self.value)
        elif self.value == 'a':
            return 1
        else:
            return 10
