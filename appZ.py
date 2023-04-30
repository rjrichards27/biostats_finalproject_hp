"""Playing the game via html pages."""
import random
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    session,
    redirect,
)
from werkzeug.wrappers import Response as WerkzeugResponse
from src.gameAWS import read_data, Game
from typing import Any

# mypy: ignore-errors

app = Flask(__name__)
app.config["SECRET_KEY"] = "rachel27"


# reading in data for characters and spells
hp_characters = "./data/Harry_Potter_Characters.tsv"
characters_dict = read_data(hp_characters)

# reading in data for characters and spells
hp_spells = "./data/Harry_Potter_Spells.tsv"
spells_dict = read_data(hp_spells)

# User inputs how many rounds they want played
# (MAX OF 5 ROUNDS and MIN OF 2)
rounds_character_num = {5: 32, 4: 16, 3: 8, 2: 4}


# code for rendering all html templates
@app.route("/")
def home() -> Any:
    """Render the home page."""
    return render_template("home.html")


@app.route("/rounds")
def rounds() -> Any:
    """Render the rounds page."""
    # clears previous session variables
    session.clear()
    # initializing the number of rounds
    # that are options for the dropdown
    round_options = ["2", "3", "4", "5"]
    return render_template("rounds.html", round_options=round_options)


@app.route("/bracket1_5rounds", methods=["POST"])
def bracket1() -> Any:
    """Render the bracket1 page based on the number of rounds picked."""
    # getting the number of rounds selected
    # from the dropdown list
    round_num_selected = int(request.form["round_num_selected"])
    # rendering the correct first bracket based on
    # the number of rounds selected
    if round_num_selected == 5:
        # creating game instance if not
        # already saved in session
        if "results_5round" not in session:
            # selecting characters
            selected_chars_5round = random.sample(
                characters_dict, rounds_character_num[5]
            )
            # initializing a class for a
            # game with 5 rounds
            game_5rounds = Game(selected_chars_5round, spells_dict, 5)
            # getting game's brackets and results
            bracket_5rounds = game_5rounds.bracket_maker()
            bracket1_5rounds = game_5rounds.print_duel_pairs(bracket_5rounds)
            session["results_5round"] = game_5rounds.play_game()
            # rendering the template with needed variables
            return render_template(
                "bracket1_5rounds.html",
                bracket1_5rounds=bracket1_5rounds,
                results_5round=session["results_5round"],
            )
        # if there are already session variables
        # saved the website redirects to the home page
        else:
            return redirect(url_for("home"))
    if round_num_selected == 4:
        # creating game instance if not
        # already saved in session
        if "results_4round" not in session:
            # selecting characters
            selected_chars_4round = random.sample(
                characters_dict, rounds_character_num[4]
            )
            # initializing a class for a
            # game with 4 rounds
            game_4rounds = Game(selected_chars_4round, spells_dict, 4)
            # getting game's brackets and results
            bracket_4rounds = game_4rounds.bracket_maker()
            bracket1_4rounds = game_4rounds.print_duel_pairs(bracket_4rounds)
            session["results_4round"] = game_4rounds.play_game()
            # rendering the template with needed variables
            return render_template(
                "bracket1_4rounds.html",
                bracket1_4rounds=bracket1_4rounds,
                results_4round=session["results_4round"],
            )
        # if there are already session variables
        # saved the website redirects to the home page
        else:
            return redirect(url_for("home"))
    if round_num_selected == 3:
        if "results_3round" not in session:
            # selecting characters
            selected_chars_3round = random.sample(
                characters_dict, rounds_character_num[3]
            )
            # initializing a class for a
            # game with 3 rounds
            game_3rounds = Game(selected_chars_3round, spells_dict, 3)
            # getting game's brackets and results
            bracket_3rounds = game_3rounds.bracket_maker()
            bracket1_3rounds = game_3rounds.print_duel_pairs(bracket_3rounds)
            session["results_3round"] = game_3rounds.play_game()
            # rendering the template with needed variables
            return render_template(
                "bracket1_3rounds.html",
                bracket1_3rounds=bracket1_3rounds,
                results_3round=session["results_3round"],
            )
        # if there are already session variables
        # saved the website redirects to the home page
        else:
            return redirect(url_for("home"))
    if round_num_selected == 2:
        if "results_2round" not in session:
            # selecting characters
            selected_chars_2round = random.sample(
                characters_dict, rounds_character_num[2]
            )
            # initializing a class for a game with 2 rounds
            game_2rounds = Game(selected_chars_2round, spells_dict, 2)
            # getting game's brackets and results
            bracket_2rounds = game_2rounds.bracket_maker()
            bracket1_2rounds = game_2rounds.print_duel_pairs(bracket_2rounds)
            session["results_2round"] = game_2rounds.play_game()
            # rendering the template with needed variables
            return render_template(
                "bracket1_2rounds.html",
                bracket1_2rounds=bracket1_2rounds,
                results_2round=session["results_2round"],
            )
        # if there are already session variables
        # saved the website redirects to the home page
        else:
            return redirect(url_for("home"))
    return render_template("rounds.html")


# code to render templates showing the
# brackets and results for each game
@app.route("/bracket1_results_5rounds")
def bracket1_results_5rounds() -> Any:
    """Render the bracket1_results page."""
    return render_template("bracket1_results_5rounds.html")


@app.route("/bracket1_results_4rounds")
def bracket1_results_4rounds() -> Any:
    """Render the bracket1_results_4rounds page."""
    return render_template("bracket1_results_4rounds.html")


@app.route("/bracket1_results_3rounds")
def bracket1_results_3rounds() -> Any:
    """Render the bracket1_results_3rounds page."""
    return render_template("bracket1_results_3rounds.html")


@app.route("/bracket1_results_2rounds")
def bracket1_results_2rounds() -> Any:
    """Render the bracket1_results_2rounds page."""
    # initializing a class for game
    return render_template("bracket1_results_2rounds.html")


@app.route("/bracket2_5rounds")
def bracket2_5rounds() -> Any:
    """Render the bracket2 page."""
    return render_template("bracket2_5rounds.html")


@app.route("/bracket2_4rounds")
def bracket2_4rounds() -> Any:
    """Render the bracket2_4rounds page."""
    return render_template("bracket2_4rounds.html")


@app.route("/bracket2_3rounds")
def bracket2_3rounds() -> Any:
    """Render the bracket2_3rounds page."""
    return render_template("bracket2_3rounds.html")


@app.route("/bracket2_2rounds")
def bracket2_2rounds() -> Any:
    """Render the bracket2_2rounds page."""
    return render_template("bracket2_2rounds.html")


@app.route("/bracket2_results_5rounds")
def bracket2_results_5rounds() -> Any:
    """Render the bracket2_results page."""
    return render_template("bracket2_results_5rounds.html")


@app.route("/bracket2_results_4rounds")
def bracket2_results_4rounds() -> Any:
    """Render the bracket2_results_4rounds page."""
    return render_template("bracket2_results_4rounds.html")


@app.route("/bracket2_results_3rounds")
def bracket2_results_3rounds() -> Any:
    """Render the bracket2_results_3rounds page."""
    return render_template("bracket2_results_3rounds.html")


@app.route("/bracket2_results_2rounds")
def bracket2_results_2rounds() -> Any:
    """Render the bracket2_results_2rounds page."""
    return render_template("bracket2_results_2rounds.html")


@app.route("/bracket3_5rounds")
def bracket3_5rounds() -> Any:
    """Render the bracket3 page."""
    return render_template("bracket3_5rounds.html")


@app.route("/bracket3_4rounds")
def bracket3_4rounds() -> Any:
    """Render the bracket3_4rounds page."""
    return render_template("bracket3_4rounds.html")


@app.route("/bracket3_3rounds")
def bracket3_3rounds() -> Any:
    """Render the bracket3_3rounds page."""
    return render_template("bracket3_3rounds.html")


@app.route("/bracket3_results_5rounds")
def bracket3_results_5rounds() -> Any:
    """Render the bracket3_results page."""
    return render_template("bracket3_results_5rounds.html")


@app.route("/bracket3_results_4rounds")
def bracket3_results_4rounds() -> Any:
    """Render the bracket3_results_4rounds page."""
    return render_template("bracket3_results_4rounds.html")


@app.route("/bracket3_results_3rounds")
def bracket3_results_3rounds() -> Any:
    """Render the bracket3_results_3rounds page."""
    return render_template("bracket3_results_3rounds.html")


@app.route("/bracket4_5rounds")
def bracket4_5rounds() -> Any:
    """Render the bracket4 page."""
    return render_template("bracket4_5rounds.html")


@app.route("/bracket4_4rounds")
def bracket4_4rounds() -> Any:
    """Render the bracket4_4rounds page."""
    return render_template("bracket4_4rounds.html")


@app.route("/bracket4_results_5rounds")
def bracket4_results_5rounds() -> Any:
    """Render the bracket4_results page."""
    return render_template("bracket4_results_5rounds.html")


@app.route("/bracket4_results_4rounds")
def bracket4_results_4rounds() -> Any:
    """Render the bracket4_results_4rounds page."""
    return render_template("bracket4_results_4rounds.html")


@app.route("/bracket5_5rounds")
def bracket5_5rounds() -> Any:
    """Render the bracket5 page."""
    return render_template("bracket5_5rounds.html")


@app.route("/bracket5_results_5rounds")
def bracket5_results_5rounds() -> Any:
    """Render the bracket5_results page."""
    return render_template("bracket5_results_5rounds.html")


# code to save user input as their predicted winner
@app.route("/saved-pred-winner", methods=["POST"])
def saved_pred_winner() -> Any:
    """Save the prediction of the winner of the tournament."""
    # gets user input and saves it as a session variable
    pred_winner_input = request.get_json()["pred_winner_input"]
    session["pred_winner_input"] = pred_winner_input
    return "Prediction saved successfully"


@app.route("/restart_simulator")
def restart_simulator() -> WerkzeugResponse:
    """Restart the simulator."""
    # clears previous session variables
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    # running app
    # app.run(debug=True, port=8080, host="0.0.0.0")
    app.run(debug=True, port=8080)
