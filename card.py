from random import shuffle 
from itertools import product 

class Card :
    def __init__ (self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'] 
        self.suits = ["clubs", "hearts", 
                "diamonds", "spades"] 
    def deck(self):
        deck = []
        deck_image = []
        deck_values = []
        for i in self.ranks:
            for j in self.suits:
                deck.append(i+j)
                image = (f"{i}_of_{j}.png")
                deck_image.append(image)
        shuffle(deck_image)
        return deck_image