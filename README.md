# Project Plan

This repository is for Duke University's "Software Tools for Data Science" course's final project. 
Authors: Rachel Richards, Eric Rios Soderman, and Wafiakmal Mitah

## Description
This repo is for a Harry Potter dueling tournament application. The application takes in Harry Potter characters and generates a dueling tournament based on the user's inputs (how many rounds do they want to have, how many speacial spells can an individual character use, etc.) Once the tournament has been created the first round duels will be shown to the user, where the user can then select what character they think will win the tournament. The first round will then be played where one character wins each duel based on their power, intelligence, skills, etc. as well as if they used any bonus spells. The winning characters will then move on to the next round and duel again, each round will be prompted by the user. This will continue until there is only one character left, the winner. The game will then end with stating if the user won or not, by choosing the correct character to win the tournament.

## Format
The application will be split up into many different functions and classes in order to complete the repetetive aspects of the game. For example, there will be a class for each Harry Potter character and a function that determines the winner of each battle. While there will be one main file where all the functions and classes are compiled to generate the actual gameplay. These code files will all be in the "code" folder, while they will all have their corresponding tests in the "test" folder.

## Steps (detailed as issues)
1. Create Harry Potter character and spells dictionaries
2. Generate a tournament bracket
3. Write code for determining a duel's winner
  * Determine how bonus spells are used
4. Write Code for completing the remaining tournament round and identifying the winner
5. Convert code to an application that utilizes the user's input
