# lib/cli.py

from helpers import (
    exit_program,
    create_new_player,
    list_all_players,
    update_player,
    delete_player,
    list_all_levels,
    # player_avg_accuracy,
    # player_avg_time
)

from models.player import Player
from models.level import Level
from models.game import Game
from termcolor import colored, cprint
from difflib import Differ, SequenceMatcher
import time

def main():
    while True:
        cprint("---Python Type-On---", "white", "on_yellow")
        print("Welcome to Python Type-On! For each level, type in the provided sentence. The game will calculate your typing accuracy and speed.")
        
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            
            playing = True
            player = None
            level = 1

            while playing == True:
                if player == None:
                    player = create_new_player()
                else:
                    #get the string from level:
                    current_level = Level.find_by_id(level)

                    if current_level == None:
                        cprint(f"Congrats, you've reached the end of the game! Your average accuracy is {player.get_avg_accuracy()}", "black", "on_green")
                        exit()

                    print(f"Level {current_level.name} - {current_level.difficulty}")
                    print("When prompted, type the provided sentence")

                    print("Ready?")
                    time.sleep(1)
                    print("Set...")
                    time.sleep(1)
                    print("Type the following:")
                    time.sleep(0.5)
                    cprint(current_level.string, "cyan")

                    #start timer
                    start_timer = time.time()

                    # prompt user for input:
                    player_input = input()
                    print(f"You entered: {player_input}")

                    # stop timer
                    stop_timer = time.time()

                    # compute diff between string and input:
                    d = Differ()
                    s = SequenceMatcher(None, current_level.string, player_input)
                    result = list(d.compare(current_level.string, player_input))

                    formatted_result = [colored(letter, "red") if letter[0] == "-" or letter[0] == "+" else colored(letter, "green") for letter in result]

                    # calculate accuracy and speed
                    accuracy = s.quick_ratio() * 100
                    speed = stop_timer - start_timer
                    
                    # instantiate a new game to store data
                    new_game = Game.create(player.id, current_level.id, player_input, speed, accuracy)

                    #print game results (player input, time and accuracy)
                    print(''.join(formatted_result))
                    cprint(f"Accuracy: {accuracy:.2f}%", "yellow")
                    cprint(f"Speed: {speed:.2f} seconds", "yellow")

                    if accuracy < 80:
                        try_again = input("Your accuracy was less than 80%. Would you like to try again? Y/N > ")
                        if try_again == "Y" or try_again == "":
                            level
                        elif try_again == "N":
                            time.sleep(1)
                            player = None
                            cprint("Now returning to main menu.", "magenta")
                            time.sleep(1)
                            playing = False
                            pass
                        else:
                            print("Please answer Y or N")
                    else:
                        keep_playing = input("Would you like to keep playing? Y/N > ")
                        
                        if keep_playing == "Y":
                            level += 1
                        elif keep_playing == "N" or keep_playing == "":
                            player = None
                            cprint("Now returning to main menu.", "magenta")
                            time.sleep(1)
                            playing = False
                            pass
                        else:
                            print("Please answer Y or N")
                   
        elif choice == "2":
            cprint(".................LEADERBOARD.................", "black", "on_light_cyan")
            list_all_players()
            return_button = input("Press enter to return to main menu ")

            if return_button == "":
                pass
        elif choice == "3":
            list_all_levels()
        elif choice == "4":
            delete_player()
        # elif choice == "5":
            # player_avg_accuracy()
            # player_avg_time()
        else:
            cprint("Invalid choice", "red")

def menu():
    
    print("Main menu:")
    print("0. Exit the game")
    print("1. New game")
    print("2. Stats")
    print("3. List all levels")
    print("4. Delete player")
    # print("5. Player average accuracy and time")
    # print("6. Player average accuracy")

if __name__ == "__main__":
    main()
