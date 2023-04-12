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

    def duel(
        character_group: tuple[dict[str, str], dict[str, str]],
        spells: list[dict[str, str]],
    ) -> int:
        """Simulates a duel between two characters.

        The character group is the pair (or multiple) of characters)
        The spells refers to the list of spell dictionaries.

        The purpose of the function is to calculate power ratings or
        scores for the characters. The spells act as additional points
        or boosters to those scores.

        The return of the function is the indices of the winning character
        to help with updating the bracket.
        """
        # intializing variables for duel

        spells_copy = spells.copy()
        battle_stats = dict()
        spells_used = dict()
        group_list = list(character_group)
        # highest_stat = 0
        # winner = 0
        # tie = False

        for i, character in enumerate(group_list):

            # calculating character stats
            character_stats = (
                int(character["Strength"])
                + int(character["Power"])
                + int(character["Intelligence"])
                + int(character["Emotional Strength"])
            )

            # the random choice and the popping of that choice
            # will impede duplicate spells from being used
            spell_num = random.randint(0, len(spells_copy))
            if spell_num == len(spells_copy):
                # this means the character used no spells
                spell_stats = 0
                chosen_spell = "no spell"
                pass

            else:
                # this means the character used a spell
                chosen_spell = spells_copy.pop(spell_num)
                spell_stats = int(chosen_spell["Power"])

            battle_stats[i] = character_stats + spell_stats
            spells_used[i] = chosen_spell

            print(
                f"{character['Name']} used {chosen_spell['Name']} "
                + f"({chosen_spell['Description']})!"
            )
            print(
                f"{character['Name']} has a total power rating of {battle_stats[i]}!\n"
            )

            # if battle_stats > highest_stat:
            #     highest_stat = battle_stats
            #     winner = i

            #### I'm leaving this here in case ####

            # We want to add a tie breaker in the future
            # elif battle_stats == highest_stat:
            #     winner = random.choice([0, 1])
            #     tie = True

        # if tie is True:
        # print(
        #     f"{character_group[winner]['Name']} narrowly defeated the " +
        #     f"{character_group[abs(winner-1)]['Name']}!" +
        #     f"by using {spells_used[winner]['Name']}!"
        #     )
        # print(f"Spell Description: {spells_used[winner]['Description']}"")
        # )
        # print(f"Both characters used {spells_used[winner]['Name']}!")

        ### Tie finishes here ###

        winner_key = max(battle_stats, key=battle_stats.get)

        print(
            f"{character_group[winner_key]['Name']} defeated "
            + f"{character_group[abs(winner_key-1)]['Name']}!\n\n"
        )

        # To make the bracket update process simpler
        # the objective is to return the key (index)
        # of the winning character
        return winner_key


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
