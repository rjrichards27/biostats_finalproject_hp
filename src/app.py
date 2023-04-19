import random
from flask import Flask, render_template, url_for, request, session, redirect
from game import read_data, Game
import os
import sys

app = Flask(__name__)
app.config["SECRET_KEY"] = "rachel27"

# reading in data for characters and spells
hp_characters = "../data/Harry_Potter_Characters.tsv"
characters_dict = read_data(hp_characters)

# reading in data for characters and spells
hp_spells = "../data/Harry_Potter_Spells.tsv"
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


# code for rebdering all html templates
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/rounds")
def rounds():
    round_options = ["2", "3", "4", "5"]
    return render_template("rounds.html", round_options=round_options)


@app.route("/bracket1", methods=["POST"])
def bracket1():
    round_num_selected = int(request.form["round_num_selected"])
    if round_num_selected == 5:
        return render_template("bracket1.html", bracket1_5round=bracket1_5round)
    if round_num_selected == 4:
        return render_template("bracket1_4rounds.html", bracket1_4round=bracket1_4round)
    if round_num_selected == 3:
        return render_template("bracket1_3rounds.html", bracket1_3round=bracket1_3round)
    if round_num_selected == 2:
        return render_template("bracket1_2rounds.html", bracket1_2round=bracket1_2round)


@app.route("/bracket1_results")
def bracket1_results():
    return render_template(
        "bracket1_results.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket1_results_4rounds")
def bracket1_results_4rounds():
    return render_template(
        "bracket1_results_4rounds.html",
        print_results_4round=print_results_4round,
        bracket1_4round=bracket1_4round,
    )


@app.route("/bracket1_results_3rounds")
def bracket1_results_3rounds():
    return render_template(
        "bracket1_results_3rounds.html",
        print_results_3round=print_results_3round,
        bracket1_3round=bracket1_3round,
    )


@app.route("/bracket1_results_2rounds")
def bracket1_results_2rounds():
    return render_template(
        "bracket1_results_2rounds.html",
        print_results_2round=print_results_2round,
        bracket1_2round=bracket1_2round,
    )


@app.route("/bracket2")
def bracket2():
    return render_template(
        "bracket2.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket2_3rounds")
def bracket2_3rounds():
    return render_template(
        "bracket2_3rounds.html",
        print_results_3round=print_results_3round,
        bracket1_3round=bracket1_3round,
    )


@app.route("/bracket2_2rounds")
def bracket2_2rounds():
    return render_template(
        "bracket2_2rounds.html",
        print_results_2round=print_results_2round,
        bracket1_2round=bracket1_2round,
    )


@app.route("/bracket2_4rounds")
def bracket2_4rounds():
    return render_template(
        "bracket2_4rounds.html",
        print_results_4round=print_results_4round,
        bracket1_4round=bracket1_4round,
    )


@app.route("/bracket2_results")
def bracket2_results():
    return render_template(
        "bracket2_results.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket2_results_4rounds")
def bracket2_results_4rounds():
    return render_template(
        "bracket2_results_4rounds.html",
        print_results_4round=print_results_4round,
        bracket1_4round=bracket1_4round,
    )


@app.route("/bracket2_results_3rounds")
def bracket2_results_3rounds():
    return render_template(
        "bracket2_results_3rounds.html",
        print_results_3round=print_results_3round,
        bracket1_3round=bracket1_3round,
    )


@app.route("/bracket2_results_2rounds")
def bracket2_results_2rounds():
    return render_template(
        "bracket2_results_2rounds.html",
        print_results_2round=print_results_2round,
        bracket1_2round=bracket1_2round, tournament_winner_2round= tournament_winner_2round
    )


@app.route("/bracket3")
def bracket3():
    return render_template(
        "bracket3.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket3_4rounds")
def bracket3_4rounds():
    return render_template(
        "bracket3_4rounds.html",
        print_results_4round=print_results_4round,
        bracket1_4round=bracket1_4round,
    )


@app.route("/bracket3_3rounds")
def bracket3_3rounds():
    return render_template(
        "bracket3_3rounds.html",
        print_results_3round=print_results_3round,
        bracket1_3round=bracket1_3round,
    )


@app.route("/bracket3_results")
def bracket3_results():
    return render_template(
        "bracket3_results.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket3_results_4rounds")
def bracket3_results_4rounds():
    return render_template(
        "bracket3_results_4rounds.html",
        print_results_4round=print_results_4round,
        bracket1_4round=bracket1_4round,
    )


@app.route("/bracket3_results_3rounds")
def bracket3_results_3rounds():
    return render_template(
        "bracket3_results_3rounds.html",
        print_results_3round=print_results_3round,
        bracket1_3round=bracket1_3round, tournament_winner_3round = tournament_winner_3round
    )


@app.route("/bracket4")
def bracket4():
    return render_template(
        "bracket4.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket4_4rounds")
def bracket4_4rounds():
    return render_template(
        "bracket4_4rounds.html",
        print_results_4round=print_results_4round,
        bracket1_4round=bracket1_4round,
    )


@app.route("/bracket4_results")
def bracket4_results():
    return render_template(
        "bracket4_results.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket4_results_4rounds")
def bracket4_results_4rounds():
    return render_template(
        "bracket4_results_4rounds.html",
        print_results_4round=print_results_4round,
        bracket1_4round=bracket1_4round, tournament_winner_4round= tournament_winner_4round
    )


@app.route("/bracket5")
def bracket5():
    return render_template(
        "bracket5.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
    )


@app.route("/bracket5_results")
def bracket5_results():
    return render_template(
        "bracket5_results.html",
        print_results_5round=print_results_5round,
        bracket1_5round=bracket1_5round,
        tournament_winner=tournament_winner_5round,
    )


@app.route("/saved-pred-winner", methods=["POST"])
def saved_pred_winner():
    pred_winner_input = request.get_json()["pred_winner_input"]
    session["pred_winner_input"] = pred_winner_input
    return "Prediction saved successfully"


@app.route("/restart_simulator")
def restart_simulator():
    session.clear()
    return redirect(url_for("home"))


"""@app.route("/restart_simulator", methods=["POST"])
def restart_simulator():
    os.execl(sys.executable, *sys.argv)
    return redirect(url_for("home"))

    <form method="POST" action="{{ url_for('restart_simulator') }}">
                    <button type="submit" style="background-color: maroon; border-color: maroon;"
                        class="btn btn-primary">Play
                        again!</button></a></p>
                </form>
                
        <p><a href=rounds>
                    <button style="background-color: maroon; border-color: maroon;"
                        class="btn btn-primary">Start</button>
                </a></p>"""


if __name__ == "__main__":
    # running app
    app.run(debug=True)

