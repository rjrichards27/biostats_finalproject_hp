# Project Plan

This repository is for Duke University's "Software Tools for Data Science" course's final project. 
Authors: Rachel Richards, Eric Rios Soderman, and Wafiakmal Mitah

## Description
This repo is for a Harry Potter dueling tournament application. The application takes in Harry Potter characters and generates a dueling tournament based on the user's inputs (how many rounds they tournament should have). Once the tournament has been created the first round duels will be shown to the user, where the user can then select what character they think will win the tournament. The first round will then be played where one character wins each duel based on their power, intelligence, skills, etc. as well as if they used any bonus spells. The winning characters will then move on to the next round and duel again, each round will be prompted by the user. This will continue until there is only one character left, the winner. The game will then end with stating if the user won, by choosing the correct character to win the tournament, or not. Then the user has a choice to play again, by choosing a tournament with a different number of rounds.

To use the application link the following link: 

## Format
The overall game will be a class made up of functions in order to complete the repetetive aspects of the game. For example, there will be a function that determines the winner of each battle. These code files will all be in the "src" folder and will all have their corresponding tests in the "test" folder. The application is created using a Flask App webpage, which is built in the "app.py" file while all of the html template files are in the "templates" folder, contained in the "src" folder. Note there are no tests for the "app.py" file as this was not discussed in class so Patrick said it was okay to not test.

## Workload and Steps (detailed in Issues)
1. Create Harry Potter character and spells dictionaries
2. Generate a tournament bracket
3. Write code for determining a duel's winner
  * Determine how bonus spells are used
4. Write Code for completing the remaining tournament round and identifying the winner
5. Convert code to an application that utilizes the user's input


## Replicating the Repo

If you are interested in accessing the repo, used to build the website, use the below code.

**Step 1: Clone the repo.**

```
git clone https://github.com/rjrichards27/biostats_finalproject_hp.git
```

**Step 2: Navigate your way into the repo.**

```
cd biostats_finalproject_hp
```

**Step 3: Install Requirements.**

```
pip install requirements.txt
```

**Step 4: Navigate your way into the src file.**

```
cd src
```

**Step 5: Run Application file.**

```
python app.py
```