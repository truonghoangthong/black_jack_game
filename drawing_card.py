import pygame
from card import Card
from random import shuffle
import random
deck = Card()
screen = pygame.display.set_mode((1000, 700))
class Draw:
    def __init__(self, image_path, width, height): # take url of cards
        self.image = pygame.image.load(f'card_image\{image_path}')
        self.image = pygame.transform.scale(self.image, (width, height)) 
        self.rect = self.image.get_rect()
class play:
    def __init__(self): # set all things that are necessary
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700))
        self.player_cards = []
        self.opponent_cards = []
        self.player_values = []
        self.opponent_values = []
        self.deck_game = Card().deck()

    def draw_cards(self): # draw cards in the beginning
        if not self.player_cards:
            self.player_cards = random.sample(self.deck_game, 2)
            for value in self.player_cards:
                self.deck_game.remove(value)
        if not self.opponent_cards:
            self.opponent_cards = random.sample(self.deck_game, 2)
            for value2 in self.opponent_cards:
                self.deck_game.remove(value2)
        self.player = [Draw(image_pack, 130, 180) for image_pack in self.player_cards]
        self.opponent = [Draw(image_pack, 130, 180) for image_pack in self.opponent_cards]
        return self.player, self.opponent, self.deck_game


    def show_card(self): # show card, replace show_first() function after pressing stand
        x = (1000 - (100 * 2 + 10)) // 2
        y_opponent = 50  
        y_player = 700 - 200 - 50
        for card in self.opponent:
            card.rect.topleft = (x, y_opponent)
            self.screen.blit(card.image, card.rect)
            x += 60
        x = (1000 - (100 * 2 + 10)) // 2
        for card in self.player:
            card.rect.topleft = (x, y_player)
            self.screen.blit(card.image, card.rect)
            x += 60
    def show_first(self): # Hide opponent's cards, it will be deleted after pressing stand button
        x = (1000 - (100 * 2 + 10)) // 2
        y_opponent = 50  
        y_player = 700 - 200 - 50
        hide_card = [Draw("back.png", 130, 180)]
        for i in range(len(self.opponent)):
            for card in hide_card :
                card.rect.topleft = (x, y_opponent)
                self.screen.blit(card.image, card.rect)
                x += 60
        x = (1000 - (100 * 2 + 10)) // 2
        for card in self.player:
            card.rect.topleft = (x, y_player)
            self.screen.blit(card.image, card.rect)
            x += 60

    def add_card(self): # this one for deal button, draw card
        add_card = random.sample(self.deck_game, 1)
        self.player_cards.extend(add_card)
        self.deck_game.remove(add_card[0])

    def add_card_opp(self): #Add a card to the opponents ( but i set the percentage of cards that will be added )
        while True: 
            random_integer = random.randint(1, 11)
            if self.opp_score() < 16 :
                add_card = random.sample(self.deck_game, 1)
                self.opponent_cards.extend(add_card)
                self.deck_game.remove(add_card[0])
            elif self.opp_score() == 16 and random_integer <= 2 :
                add_card = random.sample(self.deck_game, 1)
                self.opponent_cards.extend(add_card)
                self.deck_game.remove(add_card[0])
            elif self.opp_score() == 17 and random_integer <= 2 :
                add_card = random.sample(self.deck_game, 1)
                self.opponent_cards.extend(add_card)
                self.deck_game.remove(add_card[0])
            elif self.opp_score() == 18 and random_integer <= 3 :
                add_card = random.sample(self.deck_game, 1)
                self.opponent_cards.extend(add_card)
                self.deck_game.remove(add_card[0])
            elif self.opp_score() == 19 and random_integer <= 3:
                add_card = random.sample(self.deck_game, 1)
                self.opponent_cards.extend(add_card)
                self.deck_game.remove(add_card[0])
            else:
                break

    def total_card_you(self):
        return len(self.player_values)

    def card_value(self, check_rank): # set the value of a card based on its rank
        if check_rank.isdigit():
            return int(check_rank)
        elif check_rank in ['king', 'queen', 'jack']:
            return 10
        elif check_rank == 'ace' and len(self.player_cards) >= 4 :
            return 1
        elif check_rank == 'ace' and len(self.player_cards) < 4 :
            return 11
        elif check_rank == 'ace' and len(self.opponent_cards) >= 4 :
            return 1
        elif check_rank == 'ace' and len(self.opponent_cards) < 4 :
            return 11

    def your_score(self): # sum of values of cards that you have played
        self.player_values = [self.card_value(card.split('_')[0]) for card in self.player_cards]
        total = sum(self.player_values)
        return total

    def opp_score(self): # sum of opponents cards values
        self.opponent_values = [self.card_value(card.split('_')[0]) for card in self.opponent_cards]
        total = sum(self.opponent_values)
        return total

    def update_cards(self): # reset 
        self.player_cards = []
        self.opponent_cards = []
        self.player_values = []
        self.opponent_values = []
        self.deck_game = Card().deck()
        self.draw_cards()

