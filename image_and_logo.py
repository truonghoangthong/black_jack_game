import pygame 
class Image:
    def __init__(self):
        # Define logo
        self.icon1 = pygame.image.load(r'image\poker-chips.png')
        self.icon2 = pygame.image.load(r"image\casino.png")
        self.icon3 = pygame.image.load(r"image\Online-Casino-1-1.jpeg")
        
        # button for menu
        self.start = pygame.image.load(r'image\start.png').convert_alpha()
        self.history = pygame.image.load(r'image\history.png').convert_alpha()
        self.quit = pygame.image.load(r'image\exit.png').convert_alpha()
        self.back = pygame.image.load(r'image\back.png').convert_alpha()
        
        ## button for game
        self.stand = pygame.image.load(r'image\stand.png').convert_alpha()
        self.deal = pygame.image.load(r'image\deal.png').convert_alpha()
        self.new = pygame.image.load(r'image\new.png').convert_alpha()
    
        # Define size of logo 
        self.size_of_logo_for_menu = (200, 100)
        self.size_of_logo_for_menu2 = (700, 350)
        self.size_of_desk = (1000,700)
        self.size_of_deck = (180,120)
        self.size_of_card = (130,150)
        self.size_of_history =(1200,600)
        
        ## Define image for game play:
        self.desk = pygame.image.load(r"image\desk.jpg")
        self.history_background = pygame.image.load(r"image\history_background.jpg")
        self.match = pygame.image.load(r"match.png")
        
        ## Define cards for game play :
        self.deck = pygame.image.load(r"card_image\back.png")
                
    def icon(self, icon):
        if icon == 1:
            return self.icon1
        elif icon == 2 :
            return self.icon2
        elif icon == 3 :
            return self.icon3
        else:
            return None
    def image(self,image):
        if image == 1 :
            return self.desk
        elif image == 2 :
            return self.history_background 
        elif image == 3 :
            return self.match
        else : 
            return None
        
    def button(self,button):
        if button == 1 :
            return self.start
        elif button == 2 : 
            return self.history
        elif button == 3 :
            return self.quit
        elif button == 4 :
            return self.back
        elif button == 5:
            return self.deal
        elif button == 6:
            return self.stand
        elif button == 7:
            return self.new
        else :
            return None
        
    def size(self, size):
        if size == 1:
            return self.size_of_logo_for_menu
        if size == 2:
            return self.size_of_logo_for_menu2
        if size == 3 :
            return self.size_of_desk
        if size == 4 :
            return self.size_of_deck
        if size == 5 :
            return self.size_of_card
        if size == 6 :
            return self.size_of_history
        else:
            return None

    def card_image(self,index):
        if index == 0 :
            return self.deck
        else :
            return None 
