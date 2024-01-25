from models.__init__ import (CONN, CURSOR)
from models.game import Game
from models.level import Level

class Player:

    all_players = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    # Property name:
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with more than 3 characters.")

    def __repr__(self) -> str:
        return f"<Player {self.name}>"
    
    # Class method to CREATE table:
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Player instances """
        sql = """
            CREATE TABLE players (
                id INTEGER PRIMARY KEY,
                name TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    # Class method to DROP table:
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Player instances """
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    # Instance method to SAVE a new row into the db:
    def save(self):
        """ Insert a new row with the name value of the current Player instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO players (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        # Assign the id of the instance to be the table's last row id:
        self.id = CURSOR.lastrowid

        # Saves the instance to the "all_players" dictionary:
        type(self).all_players[self.id] = self

    # Class method to create a new Player instance:
    @classmethod
    def create(cls, name):
        """ Initialize a new Player instance and save the object to the database """
        player = cls(name)

        # Save to the db:
        player.save()
        return player
    
    # Class method to update a new Player instance:
    def update(self):
        """Update the table row corresponding to the current Player instance."""
        sql = """
            UPDATE players
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    # Class method to delete a new Player instance:
    def delete(self):
        """Delete the table row corresponding to the current Player instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all_players[self.id]

        # Set the id to None
        self.id = None

    # Class method to instantiate a new Player from the db, taking in "row" as arg:
    @classmethod
    def instance_from_db(cls, row):
        """Return a Player object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        player = cls.all_players.get(row[0])
        if player:
            # ensure attributes match row values in case local instance was modified
            player.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            player = cls(row[1])
            player.id = row[0]
            cls.all_players[player.id] = player
        return player

    # Class method to get all players:
    @classmethod
    def get_all(cls):
        """Return a list containing a Player object per row in the table"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    # Class method to find a player by id:
    @classmethod
    def find_by_id(cls, id):
        """Return a Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # Class method to find a player by name:
    @classmethod
    def find_by_name(cls, name):
        """Return a Player object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM players
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    # Instance method to list all games the player has played:
    def games(self):
        """Return a list of Games played by the current instance"""
        from models.game import Game
        sql = """
            SELECT *
            FROM games
            WHERE player_id is ?
        """

        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [Game.instance_from_db(row) for row in rows]
    
    # Instance method to list the highest level a player has played:
    def highest_level_played(self):
        highest_level_id = max([game.level_id for game in self.games()])
        return Level.find_by_id(highest_level_id).name
    
    # Instance method to list the average accuracy of a player's games:
    def get_avg_accuracy(self):
        games_accuracy = [game.accuracy for game in self.games()]
        return sum(games_accuracy) / len(games_accuracy)
    
    # Instance method to list the average time of a player's games:
    def get_avg_time(self):
        games_times = [float(game.time) for game in self.games()]
        return sum(games_times) / len(games_times)
