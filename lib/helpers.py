# lib/helpers.py
from models.player import Player
from models.level import Level
from models.game import Game

def exit_program():
    print("Goodbye!")
    exit()

def create_new_player():
    name = input("What's your name? ")
    player = Player.create(name)
    print(f"Welcome, {name}!")
    return player

def list_all_players():
    # Lists all players, their avg accuracy, and speed, order by accuracy:
    
    # players = [player for player in Player.get_all()]
    players = [{"name": player.name, "avg_accuracy": player.get_avg_accuracy(), "avg_time": player.get_avg_time(), "highest_lvl": player.highest_level_played()} for player in Player.get_all()]

    players.sort(key=lambda player: player["avg_accuracy"], reverse=True)
    
    for player in players:
        print(f"{player['name']}\t| Accuracy: {player['avg_accuracy']:.2f}\t| Speed: {player['avg_time']:.2f} seconds\t| Highest level: {player['highest_lvl']}")

def update_player():
    _id = input("Enter player id: ")

    if player := Player.find_by_id(_id):
        try:
            name = input("Enter player name: ")
            player.name = name
            player.update()
            print(f'Success: {player} updated')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {_id} not found')

def delete_player():
    _id = input("Enter player id: ")

    if player := Player.find_by_id(_id):
        try:
            player.delete()
            print(f'Success: {player} deleted')
        except Exception as exc:
            print("Error deleting employee: ", exc)
    else:
        print(f'Employee {_id} not found')

def list_all_levels():
    for level in Level.get_all():
        print(f"{level.name} - {level.difficulty} - {level.string}" )

# def player_avg_accuracy():
#     _id = input("Enter player id: ")

#     if player := Player.find_by_id(_id):
#         print(f"{player.get_avg_accuracy():.2f}")
#     else:
#         print("Player could not be found")

# def player_avg_time():
#     _id = input("Enter player id: ")

#     if player := Player.find_by_id(_id):
#         print(player.get_avg_time())
#     else:
#         print("Player could not be found")