from fake_files import fake_files
from game import read_data, Game

character_fake = [
    ["Name", "Bio", "Strength", "Power", "Intelligence", "Emotional Strength"],
    ["Harry Potter", "Main Character.", "7", "9", "6", "8"],
    ["Herminone Granger", "One of Harry's best friends.", "5", "8", "9", "7"],
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


# initializing fake data for tests
with fake_files(character_fake, spell_fake) as filenames:
    # testing total length of tuple
    test_characters = read_data(filenames[0])
    test_spells = read_data(filenames[1])

print(test_characters)


def test_bracket_maker() -> None:
    """Testing the bracket maker function."""
    game1 = Game(test_characters, test_spells)
    assert len(game1.bracket_maker()) == 2
