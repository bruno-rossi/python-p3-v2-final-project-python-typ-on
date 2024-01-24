# lib/cli.py

from helpers import (
    exit_program,
    create_new_player,
    list_all_players,
    update_player,
    delete_player,
    list_all_levels,
    new_game,
    player_avg_accuracy
)

from models.player import Player
from models.level import Level
from models.game import Game
from termcolor import colored, cprint
from difflib import Differ, SequenceMatcher
import time

# Code pygame setup:
import pygame
import pygame_textinput
from sys import exit

def main():

    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Python TypeOn")
    clock = pygame.time.Clock()
    game_font = pygame.font.Font(None, 50)
    menu_active = True
    game_active = False
    stats_active = False
    name_input_active = False
    mouse_pos = None
    player_name = None

    pygame.display.flip()

    while True:

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and new_game_rect.collidepoint(mouse_pos):
                print("Clicked 'New Game'")
                name_input_active = not name_input_active
                print(name_input_active)
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and stats_rect.collidepoint(mouse_pos):
                print("Clicked 'Stats'")
                menu_active = False

        # Fill background surface
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((204, 255, 255))
        
        if menu_active:
            #Display menu surface
            menu = pygame.Surface((512, 512))
            menu = menu.convert()
            menupos = menu.get_rect()
            menupos.centerx = background.get_rect().centerx
            menupos.centery = background.get_rect().centery
            menu.fill((255, 255, 255))

            # "New game" button:
            new_game_text = game_font.render("New game", 1, (10, 10, 10))
            new_game_rect = new_game_text.get_rect(center = (menupos.centerx, 300))

            # "Stats" button:
            stats_text = game_font.render("Stats", 1, (10, 10, 10))
            stats_rect = stats_text.get_rect(center = (menupos.centerx, 400))

            # Blit everything to the screen in the following order:
            screen.blit(background, (0, 0))
            screen.blit(menu, menupos)
            screen.blit(new_game_text, new_game_rect)
            screen.blit(stats_text, stats_rect)
        
        
        # Create TextInput-object
        nameInput = pygame_textinput.TextInputVisualizer()     
        while name_input_active:
            print("Name input screen")
            screen.blit(background, (0, 0))
            name_input_label = game_font.render("What's your name?", 1, (10, 10, 10))

            start_button_text = game_font.render("Start", 1, (10, 10, 10))
            start_button_text_rect = start_button_text.get_rect()
            
            events = pygame.event.get()
            nameInput.update(events)

            for event in events:
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    print(mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and start_button_text_rect.collidepoint(mouse_pos):
                    player_name = nameInput.value
                    print("Clicked 'Start'")
                    print(player_name)
                    name_input_active = False
                    menu_active = True
                    # game_active = True

            screen.blit(name_input_label, (0, 0))
            screen.blit(nameInput.surface, (0, 100))
            screen.blit(start_button_text, start_button_text_rect)

        if game_active:
            screen.blit(background, (0, 0))

            player_name_label = game_font.render(f"Player name: {player_name}", 1, (10, 10, 10))
            screen.blit(player_name_label)

            # print(nameInput.value)
            pygame.display.update()
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                pygame.quit()
                exit()
       
        # def game():
        # def insert_name():
        # def results():
        # def stats():

        #pygame position / button press

            # draw all elements
            # update everything

        pygame.display.update()
        clock.tick(60)

if __name__=="__main__":
    # call the main function
    main()
    

    # ----------------
    # CLI game functionality:
# def main():
    # while True:
        
    #     print("---Python Type-On---")
    #     print("Welcome to Python Type-On!")
    #     menu()
    #     choice = input("> ")
    #     if choice == "0":
    #         exit_program()
    #     elif choice == "1":
            
    #         playing = True
    #         player = None
    #         level = 1

    #         while playing == True:
    #             if player == None:
    #                 player = create_new_player()
    #             else:
    #                 #get the string from level:
    #                 current_level = Level.find_by_id(level)

    #                 if current_level == None:
    #                     print("Congrats, you've reached the end of the game!")
    #                     exit()

    #                 print(f"{current_level.name} - {current_level.difficulty}")
    #                 cprint(current_level.string, "cyan")

    #                 #start timer
    #                 start_timer = time.time()

    #                 # prompt user for input:
    #                 player_input = input()
    #                 print(f"You entered: {player_input}")

    #                 # stop timer
    #                 stop_timer = time.time()

    #                 # compute diff between string and input:
    #                 d = Differ()
    #                 s = SequenceMatcher(None, current_level.string, player_input)
    #                 result = list(d.compare(current_level.string, player_input))

    #                 formatted_result = [colored(letter, "red") if letter[0] == "-" or letter[0] == "+" else colored(letter, "green") for letter in result]

    #                 # calculate accuracy and speed
    #                 accuracy = s.quick_ratio() * 100
    #                 speed = stop_timer - start_timer
                    
    #                 # instantiate a new game to store data
    #                 new_game = Game.create(player.id, current_level.id, player_input, speed, accuracy)

    #                 #print game results (player input, time and accuracy)
    #                 print(''.join(formatted_result))
    #                 cprint(f"Accuracy: {accuracy}%", "yellow")
    #                 cprint(f"Speed: {speed} seconds", "yellow")

    #                 if accuracy < 80:
    #                     try_again = input("Your accuracy was less than 80%. Would you like to try again? ")
    #                     if try_again == "Y":
    #                         level
    #                     elif try_again == "N":
    #                         exit()
    #                     else:
    #                         cprint("Please answer Y or N", "red")
    #                 else:
    #                     keep_playing = input("Would you like to keep playing? ")
                        
    #                     if keep_playing == "Y":
    #                         level += 1
    #                     elif keep_playing == "N":
    #                         exit()
    #                     else:
    #                         cprint("Please answer Y or N", "red")
                   
    #     elif choice == "2":
    #         list_all_players()
    #     elif choice == "3":
    #         update_player()
    #     elif choice == "4":
    #         delete_player()
    #     elif choice == "5":
    #         list_all_levels()
    #     elif choice == "6":
    #         player_avg_accuracy()
    #     elif choice == "7":
    #         pass
    #     elif choice == "8":
    #         pass
    #     else:
    #         print("Invalid choice")

# def menu():
    
#     print("0. Exit the program")
#     print("1. New game")
#     print("2. List all players")
#     print("3. Update player")
#     print("4. Delete player")
#     print("5. List all levels")
#     print("6. Player average accuracy")
#     print("7. List of players by avg accuracy")
#     print("8. List of players by avg speed")

# if __name__ == "__main__":
#     main()
