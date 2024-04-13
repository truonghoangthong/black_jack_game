import pygame
from text_and_color import Text
from image_and_logo import Image
import button
from drawing_card import play
from random import shuffle
from game_note import NoteDAO
from draw_chart import draw
pygame.init()

#create the screen
screen = pygame.display.set_mode((1000, 700))

# load music
pygame.mixer.music.load("music\gamble.mp3")
pygame.mixer.music.play(-1)
# Pause 
game_pause = False  
menu_state = "main"

#call class from another library
run_text = Text()
run_image = Image()

#Title and icon
pygame.display.set_caption("Serious Business")
pygame.display.set_icon(run_image.icon(1))

def draw_text (text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

start_button = button.Button(380,280,run_image.button(1),0.6)
exit_button = button.Button(390,520,run_image.button(3),0.6)
history_button = button.Button(390,400,run_image.button(2),0.6)
back_button = button.Button(20,-20,run_image.button(4),0.6)
deal_button = button.Button(20,500,run_image.button(5),0.4)
stand_button = button.Button(20,600,run_image.button(6),0.4)
new_button = button.Button(400,300,run_image.button(7),0.5)

record = [0,0,0]


#Game loop
game = play()
player, opponent, deck_game = game.draw_cards()
back = True
running = True
cards_drawn = 0
set = game.show_first()
while running :
    if game_pause == True:
        screen.fill((180,0,0))
        if menu_state == "main" :
            max_clicks = 3
            click_stand = 0
            click_count = 0
            result = False
            play = False
            draw_text("YOU PLAY, YOU WIN",run_text.font("medium"), run_text.color(1),310,130)
            draw_text("Serious Business", run_text.font("small"), run_text.color(2), 410, 200)
            scaled_logo1 = pygame.transform.scale(run_image.icon(1), run_image.size(1))
            scaled_logo2 = pygame.transform.scale(run_image.icon(2), run_image.size(1))
            screen.blit(scaled_logo1, (710, 130)) 
            screen.blit(scaled_logo2, (110, 130)) 
            something1 = False
            opp_score = False ##Not done yet, handle later
            if start_button.draw(screen) :
                menu_state = "start"
            if history_button.draw(screen):
                menu_state = "history"
            if exit_button.draw(screen) :
                running = False
        elif menu_state == "start" :       
            scaled_image = pygame.transform.scale(run_image.image(1), run_image.size(3))
            background = screen.blit(scaled_image, (0, 0))
            scaled_deck = pygame.transform.scale(run_image.card_image(0), run_image.size(4))
            deck = pygame.transform.rotate(scaled_deck, -90)
            if not opp_score:
                opp_score_text =draw_text(f'Opponent score: ?',run_text.font("mini"), run_text.color(3),400,10)
            if opp_score:
                opp_score_text =draw_text(f'Opponent score: {game.opp_score()}',run_text.font("mini"), run_text.color(3),400,10)
            if result :
                if game.opp_score() <= 21 and game.your_score() > 21:
                    lose = draw_text('SEE YOU LATER, LOSER.',run_text.font("medium"), run_text.color(3),300,270)
                    new_button.draw(screen)
                    if update_record :
                        record[1] += 1
                        update_record = False
                if game.opp_score() > 21 and game.your_score() <= 21:
                    win = draw_text('Incredible how lucky some assholes get. ',run_text.font("medium"), run_text.color(3),230,270)
                    new_button.draw(screen)
                    if update_record :
                        record[0] += 1
                        update_record = False
                if game.opp_score() > 21 and game.your_score() > 21:
                    if game.opp_score() < game.your_score() :
                        lose = draw_text('Man! You are one pathetic loser.',run_text.font("medium"), run_text.color(3),300,270)
                        new_button.draw(screen)
                        if update_record :
                            record[1] += 1
                            update_record = False

                    elif game.opp_score() > game.your_score() :
                        win = draw_text('You are fucking lucky.',run_text.font("medium"), run_text.color(3),300,270)
                        new_button.draw(screen)
                        if update_record :
                            record[0] += 1
                            update_record = False

                if game.opp_score() == game.your_score():
                    tie = draw_text('Tie game?! - What the hell?!',run_text.font("medium"), run_text.color(3),300,270)
                    new_button.draw(screen)
                    if update_record :
                            record[2] += 1
                            update_record = False
                if game.your_score() == 16 and game.opp_score() <= 21 :
                    lose = draw_text('Sounds like a loser.',run_text.font("medium"), run_text.color(3),300,270)
                    new_button.draw(screen)
                    if update_record :
                        record[1] += 1
                        update_record = False
                if game.your_score() <= 21 and game.opp_score() <= 21 and game.total_card_you() == 5:
                    win = draw_text('WHAT THE F*CK ?',run_text.font("medium"), run_text.color(3),300,270)
                    new_button.draw(screen)
                    if update_record :
                            record[0] += 1
                            update_record = False
                if game.your_score() < 16 and game.opp_score() <= 21 :
                    lose = draw_text('First time ? huh',run_text.font("medium"), run_text.color(3),300,270)
                    new_button.draw(screen)
                    if update_record :
                        record[1] += 1
                        update_record = False
                if 16< game.your_score() <= 21 and game.opp_score() <= 21 and game.your_score() > game.opp_score() and game.total_card_you() != 5:
                    win = draw_text('OK OK, You win',run_text.font("medium"), run_text.color(3),350,270)
                    new_button.draw(screen)
                    if update_record :
                            record[0] += 1
                            update_record = False
                if 16 < game.your_score() <= 21 and game.opp_score() <= 21 and game.your_score() < game.opp_score() and game.total_card_you() != 5:
                    win = draw_text('Hahaha, loser!',run_text.font("medium"), run_text.color(3),300,270)
                    new_button.draw(screen)
                    if update_record :
                        record[1] += 1
                        update_record = False
            you_score_text =draw_text(f'Your score: {game.your_score()}',run_text.font("mini"), run_text.color(3),400,660)
            score_text = draw_text(f'WINS: {record[0]}    LOSSES: {record[1]}    DRAWS: {record[2]}',run_text.font("mini"), run_text.color(3),650,660)
            opp = draw_text('Opponent',run_text.font("medium"), run_text.color(3),150,100)
            you = draw_text('You',run_text.font("medium"), run_text.color(3),270,500)
            screen.blit(deck, (20,250))
            if not something1:
                set = game.show_first()
            if something1 :
                set = game.show_card()
            if back_button.draw(screen) :
                menu_state = "main"
            if deal_button.draw(screen):
                menu_state = "start"
            if stand_button.draw(screen):
                menu_state = "start"
            game.add_card_opp()
            game.draw_cards()     
        elif menu_state == "history" :
            scaled_image = pygame.transform.scale(run_image.image(2), run_image.size(3))
            screen.blit(scaled_image, (0, 0))
            history = pygame.image.load(draw.raw())
            scaled_history = pygame.transform.scale(history, run_image.size(6))
            screen.blit(scaled_history, (-90, 50))
            if back_button.draw(screen) :
                menu_state = "main"
            pass
    elif game_pause == False: 
        screen.fill((0,0,0))
        draw_text("GAMBLING IS NOT A VICE",run_text.font("small"), run_text.color(3),340,130)
        draw_text("IT IS AN EXPRESSION OF OUR HUMANNESS.",run_text.font("small"), run_text.color(3),240,230)
        draw_text("(Press space to continue)",run_text.font("small"), run_text.color(3),350,260)
        scaled_logo3 = pygame.transform.scale(run_image.icon(3), run_image.size(2))
        screen.blit(scaled_logo3, (150, 330)) 
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_pause = True
        if event.type == pygame.QUIT:
            NoteDAO.addNote(record[0],record[1],record[2])
            NoteDAO.write_csv()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_pause:
                if menu_state == "start" and back_button.draw(screen):
                    menu_state = "main"
                    NoteDAO.addNote(record[0],record[1],record[2])
                    NoteDAO.write_csv()
                    record = [0,0,0]
                    game.update_cards()
                elif menu_state == "start" and deal_button.draw(screen) and click_count < max_clicks and not result and game.your_score() < 21:
                    menu_state = "start"
                    result = False
                    game.add_card()
                    game.draw_cards()
                    click_count += 1
                elif menu_state == "start" and stand_button.draw(screen) and click_stand < 1 :
                    menu_state = "start"
                    something1 = True
                    opp_score = True 
                    update_record = True
                    result = True
                    click_stand += 1
                elif menu_state == "start" and result :
                        something1 = False
                        opp_score = False 
                        result = False
                        click_stand = 0
                        click_count = 0
                        game.update_cards()
                        pygame.display.update() 
                        menu_state = "start"
    pygame.display.update()
pygame.quit()
