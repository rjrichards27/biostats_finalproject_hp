"""Test duel mechanic method."""
from fake_files import fake_files
from game import read_data, Game

character_fake = [
    ["Name", "Bio", "Strength", "Power", "Intelligence", "Emotional Strength"],
    ["Harry Potter", "Main Character.", "7", "9", "6", "8"],
    ["Hermione Granger", "One of Harry's best friends.", "5", "8", "9", "7"],
]

spell_fake = [
    ["Name", "Power", "Description"],
    ["Lumos", "2", "Creates light."],
    ["Accios", "5", "Bring an object to caster."],
]

# initializing fake data for tests
with fake_files(character_fake, spell_fake) as filenames:
    # testing total length of tuple
    test_characters = read_data(filenames[0])
    test_spells = read_data(filenames[1])

game1 = Game(test_characters, test_spells, "Harry Potter", 1)
battle_pair = game1.bracket_maker()


def test_duel() -> None:
    """Test duel mechanic.

    This method tests the duel mechanic of the game.
    It is designed to work with the pairs of characters
    that are fated to battle each other."""

    assert type(game1.duel(battle_pair[0], test_spells)) is int
    assert game1.duel(battle_pair[0], test_spells) in range(0, 3)
    assert game1.duel(battle_pair[0], test_spells) != 2
