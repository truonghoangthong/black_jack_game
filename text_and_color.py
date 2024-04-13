import pygame 
class Text:
    def __init__(self):
        # Define fonts
        self.smallfont = pygame.font.SysFont("comicsansms", 25)
        self.medfont = pygame.font.SysFont("comicsansms", 40)
        self.minifont = pygame.font.SysFont("comicsansms",20)
        

        # Define colors
        self.text_color1 = (255, 255, 0)
        self.text_color2 = (230, 230, 0)
        self.text_color3 = (255,255,255)

    def font(self, size):
        if size == "small":
            return self.smallfont
        elif size == "medium":
            return self.medfont
        elif size == "mini":
            return self.minifont
        else:
            return None

    def color(self, option):
        if option == 1:
            return self.text_color1
        elif option == 2:
            return self.text_color2
        elif option == 3 :
            return self.text_color3
        else:
            return None