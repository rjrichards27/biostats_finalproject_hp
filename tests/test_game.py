from fake_files import fake_files
import random
from game import read_data, Game

character_fake = [
    ["Name", "Bio", "Strength", "Power", "Intelligence", "Emotional Strength"],
    ["Harry Potter", "Main Character.", "7", "9", "6", "8"],
    ["Hermione Granger", "One of Harry's best friends.", "5", "8", "9", "7"],
    ["Ron Weasley", "One of Harry's best friends.", "4", "7", "7", "8"],
    ["Fred Weasley", "One of Ron's brothers.", "6", "8", "6", "7"],
]

spell_fake = [
    ["Name", "Power", "Description"],
    ["Lumos", "2", "Creates light."],
    ["Accios", "5", "Bring an object to caster."],
]


def test_reading_data() -> None:
    """Testing the lengths of data after parsing."""
    # initializing variables
    with fake_files(character_fake, spell_fake) as filenames:
        # testing total length of tuple
        assert len(read_data(filenames[0])) == 4
        assert len(read_data(filenames[1])) == 2


# initializing fake data for tests
with fake_files(character_fake, spell_fake) as filenames:
    # testing total length of tuple
    test_characters = read_data(filenames[0])
    test_spells = read_data(filenames[1])

random.seed(1)
rounds_character_num = {5: 32, 4: 16, 3: 8, 2: 4}
total_rounds = 2
selected_chars = random.sample(
    test_characters, rounds_character_num[total_rounds]
)
game1 = Game(selected_chars, test_spells, total_rounds)
battle_pair = game1.bracket_maker()


def test_bracket_maker() -> None:
    """Testing the bracket maker function."""
    assert len(battle_pair) == 2
    assert len(game1.print_duel_pairs(battle_pair)) == 2


def test_duel() -> None:
    """Test duel mechanic.

    This method tests the duel mechanic of the game.
    It is designed to work with the pairs of characters
    that are fated to battle each other."""

    assert type(game1.duel(battle_pair[0], test_spells)) is tuple
    assert len(game1.duel(battle_pair[0], test_spells)) == 2
    assert len(game1.duel(battle_pair[0], test_spells)[1]) == 5


def test_play_game() -> None:
    """Test the play game method."""
    game_dict = game1.play_game()
    assert len(game1.characters_playing) == 2
    assert len(game_dict) == 4
