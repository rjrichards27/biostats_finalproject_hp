import random
from flask import Flask, render_template, url_for, request, session, redirect
from game import read_data, Game
import app
import os

# reading in data for characters and spells
hp_characters = (
    "D:/Duke/Lectures/07_BIO_821_PYTHON_TOOLS/"
    "biostats_finalproject_hp/data/Harry_Potter_Characters.tsv"
)
characters_dict = read_data(hp_characters)

# reading in data for characters and spells
hp_spells = (
    "D:/Duke/Lectures/07_BIO_821_PYTHON_TOOLS/"
    "biostats_finalproject_hp/data/Harry_Potter_Spells.tsv"
)
spells_dict = read_data(hp_spells)

# User inputs how many rounds they want played (MAX OF 5 ROUNDS and MIN OF 2)
rounds_character_num = {5: 32, 4: 16, 3: 8, 2: 4}

# game with 5 rounds
selected_chars_5round = random.sample(characters_dict, rounds_character_num[5])
game_5round = Game(selected_chars_5round, spells_dict, 5)
bracket_5round = game_5round.bracket_maker()
bracket1_5round = game_5round.print_duel_pairs(bracket_5round)
results_5round = game_5round.play_game()
print_results_5round = results_5round[0]
tournament_winner_5round = results_5round[-1]

# game with 4 rounds
selected_chars_4round = random.sample(characters_dict, rounds_character_num[4])
game_4round = Game(selected_chars_4round, spells_dict, 4)
bracket_4round = game_4round.bracket_maker()
bracket1_4round = game_4round.print_duel_pairs(bracket_4round)
results_4round = game_4round.play_game()
print_results_4round = results_4round[0]
tournament_winner_4round = results_4round[-1]

# game with 3 rounds
selected_chars_3round = random.sample(characters_dict, rounds_character_num[3])
game_3round = Game(selected_chars_3round, spells_dict, 3)
bracket_3round = game_3round.bracket_maker()
bracket1_3round = game_3round.print_duel_pairs(bracket_3round)
results_3round = game_3round.play_game()
print_results_3round = results_3round[0]
tournament_winner_3round = results_3round[-1]

# game with 2 rounds
selected_chars_2round = random.sample(characters_dict, rounds_character_num[2])
game_2round = Game(selected_chars_2round, spells_dict, 2)
bracket_2round = game_2round.bracket_maker()
bracket1_2round = game_2round.print_duel_pairs(bracket_2round)
results_2round = game_2round.play_game()
print_results_2round = results_2round[0]
tournament_winner_2round = results_2round[-1]


def test_app() -> None:
    app.app.testing = True
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
