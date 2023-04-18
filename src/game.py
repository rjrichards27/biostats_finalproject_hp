"""Provide user with a game of The Wizarding World of Harry Potter duels."""
import random
from dataclasses import dataclass


@dataclass
class Game:
    """Class for overall game."""

    # intializing objects for class
    characters_playing: list[dict[str, str]]
    spells: list[dict[str, str]]
    total_rounds: int

    def bracket_maker(self) -> list[tuple[dict[str, str], dict[str, str]]]:
        """Create bracket uses selected players."""
        character_pairs = list(
            zip(self.characters_playing[::2], self.characters_playing[1::2])
        )
        return character_pairs

    def print_duel_pairs(
        self, character_pairs_list: list[tuple[dict[str, str], dict[str, str]]]
    ) -> list[str]:
        """Print duel games before being played."""
        duels_list = []
        for duel_pairs in character_pairs_list:
            duel_title = f"{duel_pairs[0]['Name']} vs. {duel_pairs[1]['Name']}"
            duels_list.append(duel_title)

        return duels_list

    def duel(
        self,
        character_group: tuple[dict[str, str], dict[str, str]],
        spells: list[dict[str, str]],
    ) -> tuple[int, list[str]]:
        """Simulate a duel between two characters.

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
        duel_prints = []

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
                chosen_spell = {
                    "Name": "no spell",
                    "Power": "0",
                    "Description": "too scared to use a spell",
                }
                pass

            else:
                # this means the character used a spell
                chosen_spell = spells_copy.pop(spell_num)
                spell_stats = int(chosen_spell["Power"])

            battle_stats[i] = character_stats + spell_stats
            spells_used[i] = chosen_spell

            duel_prints.append(
                (
                    f"{character['Name']} used {chosen_spell['Name']} "
                    + f"({chosen_spell['Description']})!"
                )
            )
            duel_prints.append(
                (
                    f"{character['Name']} has a total power"
                    f" rating of {battle_stats[i]}!"
                )
            )

        # determining the winner
        # added scenario when the output of battle is a tie
        if battle_stats[0] > battle_stats[1]:
            winner_key = 0
            duel_prints.append(
                (
                    f"{character_group[winner_key]['Name']} defeated "
                    + f"{character_group[abs(winner_key-1)]['Name']}!"
                )
            )
        elif battle_stats[0] == battle_stats[1]:
            winner_key = 0
            duel_prints.append(
                (
                    f"{character_group[winner_key]['Name']} cast the spell "
                    + f"first and defeated "
                    + f"{character_group[abs(winner_key-1)]['Name']}!"
                )
            )
        else:
            winner_key = 1
            duel_prints.append(
                (
                    f"{character_group[winner_key]['Name']} defeated "
                    + f"{character_group[abs(winner_key-1)]['Name']}!"
                )
            )

        # To make the bracket update process simpler
        # the objective is to return the key (index)
        # of the winning character
        return winner_key, duel_prints

    def print_winner(self, winner: dict[str, str]) -> str:
        """Print the winner of the game."""
        return (
            f"The winner of the tournament is {winner['Name']}! " + f"{winner['Bio']}"
        )

    def play_game(self) -> tuple[list[str], str]:
        """Play the game."""
        # creating the bracket
        character_pairs_list = self.bracket_maker()
        # playing the bracket
        round = 1
        temp_winners = []
        print_statements = []
        while round <= self.total_rounds:
            print_statements.append(
                "Prepare your wands! May the best Wizard/Witch win!"
            )
            # print("==================================================")
            for i, duel_pairs in enumerate(character_pairs_list):
                if round == self.total_rounds:
                    pass
                else:
                    print_statements.append(f"Round {round}, Duel {i+1}")
                    print_statements.append(
                        "=================================================="
                    )
                winner_key = self.duel(duel_pairs, self.spells)
                winner_index = winner_key[0]
                print_statements.append(winner_key[-1])
                if i + 1 == len(character_pairs_list) and round != self.total_rounds:
                    print_statements.append(
                        "=================================================="
                    )
                    print_statements.append(f"Round {round} is over!")
                else:
                    pass
                temp_winners.append(duel_pairs[winner_index])
            if len(temp_winners) == 1:
                winner_name = temp_winners[0]["Name"]
                print_statements.append(self.print_winner(temp_winners[0]))
                """if temp_winners[0]["Name"] == self.champion:
                    print_statements.append(f"Your champion is victorious!")
                else:
                    print_statements.append(
                        f"Your champion {self.champion} did not make it "
                        f"to the end..."
                    )"""
                break
            else:
                self.characters_playing = temp_winners
                character_pairs_list = self.bracket_maker()
                temp_winners = []
                round += 1
                if len(character_pairs_list) == 1:
                    print_statements.append(
                        "=================================================="
                    )
                    print_statements.append("Final Duel!")
                    print_statements.append(
                        f"{duel_pairs[0]['Name']} vs. {duel_pairs[1]['Name']}"
                    )
                    print_statements.append("   ")
                else:
                    print_statements.append(
                        "=================================================="
                    )
                    print_statements.append(
                        f"Break is over! "
                        f" While our survivors enjoy their butterbeer in the "
                        f"break room, let's see the next set of duels: "
                    )
                    for duel_pairs in character_pairs_list:
                        print_statements.append(
                            f"{duel_pairs[0]['Name']} vs. {duel_pairs[1]['Name']}"
                        )
        return print_statements, winner_name


# intitializing character list
def read_data(file_name: str) -> list[dict[str, str]]:
    """Read data into a list of dictionaries."""
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


def give_character_choice(characters: list[dict[str, str]]) -> dict[str, str]:
    """Give the user a choice of characters to play with."""
    # printing out the characters
    print("==================================================")
    print("Here are the characters you can choose to be your champion: \n")
    for i, character in enumerate(characters):
        print(f"{i+1}. {character['Name']}")

    # getting user input for character choice
    while True:
        try:
            character_choice = int(
                input("\nPlease enter the number of your champion: ")
            )
            if character_choice > len(characters) or character_choice < 1:
                print("Please enter a valid number!")
            else:
                print("May your champion make it to the end!\n")
                print("==================================================")
                break
        except ValueError:
            print("Please enter a valid number!")

    # returning the character choice
    return characters[character_choice - 1]


# reading in data for characters and spells
hp_characters = "../data/Harry_Potter_Characters.tsv"
characters_dict = read_data(hp_characters)

# reading in data for characters and spells
hp_spells = "../data/Harry_Potter_Spells.tsv"
spells_dict = read_data(hp_spells)


# generating random list of players for bracket
# random.seed(1)


if __name__ == "__main__":
    # running an example game
    rounds_character_num = {5: 32, 4: 16, 3: 8, 2: 4}
    # User inputs how many rounds they want played (MAX OF 5 and MIN OF 2)
    total_rounds = int(
        input(
            f"Welcome to the Harry Potter Wizarding "
            f"Tournament!\nHow many rounds do you want "
            f"to play? (2-5) "
        )
    )
    selected_chars = random.sample(characters_dict, rounds_character_num[total_rounds])
    champion = give_character_choice(selected_chars)
    game1 = Game(selected_chars, spells_dict, total_rounds)
    bracket = game1.bracket_maker()
    duels = game1.print_duel_pairs(bracket)
    print(duels)
    prints = game1.play_game()
    print(prints[0])