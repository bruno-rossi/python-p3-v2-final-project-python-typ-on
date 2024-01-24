# lib/helpers.py
from models.player import Player
from models.level import Level
from models.game import Game
from termcolor import colored, cprint

def exit_program():
    cprint("Goodbye!", "magenta")
    exit()

def create_new_player():
    name = input("What's your name? ")
    player = Player.create(name)
    cprint(f"Welcome, {name}!", "magenta")
    return player

def new_game():
    cprint("New game starts now!", "magenta")

def list_all_players():
    for player in Player.get_all():
        cprint(f"{player.name} - Avg accuracy: {player.get_avg_accuracy()}", "blue")

def update_player():
    _id = input("Enter player id: ")

    if player := Player.find_by_id(_id):
        try:
            name = input("Enter player name: ")
            player.name = name
            player.update()
            cprint(f'Success: {player} updated', "green")
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
       cprint(f'Player {_id} not found', "red")

def delete_player():
    _id = input("Enter player id: ")

    if player := Player.find_by_id(_id):
        try:
            player.delete()
            cprint(f'Success: {player} deleted', "green")
        except Exception as exc:
            print("Error deleting employee: ", exc)
    else:
        cprint(f'Player {_id} not found', "red")

def list_all_levels():
    for level in Level.get_all():
        print(level)

def player_avg_accuracy():
    _id = input("Enter player id: ")

    if player := Player.find_by_id(_id):
        print(player.get_avg_accuracy())
    else:
        print("Player could not be found")
