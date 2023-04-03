import random
from dataclasses import dataclass


@dataclass
class Game:
    """Class for overall game."""

    # intializing objects for class
    characters_playing: list[dict[str, str]]
    spells: list[dict[str, str]]

    def bracket_maker(self) -> list[dict[str, str]]:
        """Creates bracket uses selected players"""
        character_pairs = list(
            zip(self.characters_playing[::2], self.characters_playing[1::2])
        )
        return character_pairs

    def print_duel_pairs(self, character_pairs_list: list[dict[str, str]]) -> None:
        """Prints duel games before being played."""
        for duel_pairs in character_pairs_list:
            print("Duel: ", duel_pairs[0]["Name"], "vs.", duel_pairs[1]["Name"])
            print("   ")


# intitializing character list
def read_data(file_name: str) -> list[dict[str, str]]:
    """Reads data into a list of dictionaries."""
    db_list = []
    with open(file_name, "r") as file:
        headers = file.readline().strip().split(",")
        # looping through each row in patient file
        for row in file:
            value = row.strip().split(",")
            # creating a dictionary for each row
            full_row = dict(zip(headers, value))
            db_list.append(full_row)
    return db_list


# reading in data for characters and spells
hp_characters = "../data/Harry_Potter_Characters.tsv"
characters_dict = read_data(hp_characters)

# reading in data for characters and spells
hp_spells = "../data/Harry_Potter_Spells.tsv"
spells_dict = read_data(hp_spells)

# User inputs how many rounds they want played (MAX OF 5 ROUNDS and MIN OF 2)
rounds_character_num = {5: 32, 4: 16, 3: 8, 2: 4}
total_rounds = 5
# generating random list of players for bracket
selected_chars = random.sample(characters_dict, rounds_character_num[total_rounds])

if __name__ == "__main__":
    # running an example game
    game1 = Game(selected_chars, spells_dict)
    bracket = game1.bracket_maker()
    game1.print_duel_pairs(bracket)

