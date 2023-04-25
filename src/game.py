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

    def print_winner(self, winner: dict[str, list[str]]) -> str:
        """Print the winner of the game."""
        return (
            f"The winner of the tournament is {winner['Name']}! "
            + f"{winner['Bio']}"
        )

    def play_game(self) -> dict[str, list[str]]:
        """Play the game."""
        # creating the bracket
        character_pairs_list = self.bracket_maker()
        # playing the bracket
        round = 1
        temp_winners = []
        results_dict = {}
        while round <= self.total_rounds:
            print_statements = []
            for i, duel_pairs in enumerate(character_pairs_list):
                if round == self.total_rounds:
                    pass
                else:
                    print_statements.append(
                        "-------------------------------------------------"
                    )
                    print_statements.append(f"Round {round}, Duel {i+1}")
                    print_statements.append(
                        "-------------------------------------------------"
                    )
                winner_key = self.duel(duel_pairs, self.spells)
                winner_index = winner_key[0]
                print_statements.extend(winner_key[-1])
                if (
                    i + 1 == len(character_pairs_list)
                    and round != self.total_rounds
                ):
                    print_statements.append(
                        "-------------------------------------------------"
                    )
                    print_statements.append(f"Round {round} is over!")
                else:
                    pass
                temp_winners.append(duel_pairs[winner_index])
            results_dict["Round" + str(round) + "Results"] = print_statements
            if len(temp_winners) == 1:
                results_dict["tournament_winner"] = [
                    temp_winners[0]["Name"],
                    (
                        f"{temp_winners[0]['Name']}. "
                        f"{temp_winners[0]['Bio']}"
                    ),
                ]
                break
            else:
                self.characters_playing = temp_winners
                character_pairs_list = self.bracket_maker()
                temp_winners = []
                round += 1
                if len(character_pairs_list) == 1:
                    results_dict["final_duel"] = [
                        (
                            f"{self.characters_playing[0]['Name']} vs. "
                            f"{self.characters_playing[1]['Name']}"
                        )
                    ]
                else:
                    round_duels_list = []
                    for duel_pairs in character_pairs_list:
                        round_duels_list.append(
                            f"{duel_pairs[0]['Name']} vs. "
                            f"{duel_pairs[1]['Name']}"
                        )
                    results_dict[
                        "Round" + str(round) + "Duels"
                    ] = round_duels_list

        return results_dict


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
