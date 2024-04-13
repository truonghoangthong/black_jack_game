from random import shuffle 
from itertools import product 

class Card :
    def __init__ (self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'] 
        self.suits = ["clubs", "hearts", 
                "diamonds", "spades"] 
        self.card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'jack': 10, 'queen': 10, 'king': 10, 'ace': 11
        }
        
    def deck(self):
        deck = []
        deck_image = []
        deck_values = []
        for i in self.ranks:
            for j in self.suits:
                deck.append(i+j)
                image = (f"{i}_of_{j}.png")
                deck_image.append(image)
                value = self.card_values[i]  # Lấy giá trị tương ứng với rank từ card_values
                deck_values.append(value)
        shuffle(deck_image)
        return deck_image