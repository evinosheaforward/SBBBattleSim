from sbbbattlesim import Board
from tests import make_character, make_player
from sbbbattlesim.utils import Tribe
import pytest


def test_temp_damage():
    player = make_player(
        characters=[
            make_character(id="SBB_CHARACTER_BABYROOT", position=5, attack=3, health=3),
            make_character(position=1, attack=5, health=8),
        ],
        treasures=['''SBB_TREASURE_HERMES'BOOTS''']
    )
    enemy = make_player(
        characters=[
            make_character(position=1, attack=5, health=5),
            make_character(id='SBB_CHARACTER_BABYDRAGON', position=6, attack=3, health=3),
            make_character(position=7, attack=0, health=1),
        ]
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=3)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (5, 3)


def test_temp_damage2():
    player = make_player(
        characters=[
            make_character(id="SBB_CHARACTER_BABYROOT", position=5, attack=1, health=1),
            make_character(position=1, attack=5, health=8),
        ],
        treasures=['''SBB_TREASURE_HERMES'BOOTS''']
    )
    enemy = make_player(
        characters=[
            make_character(position=1, attack=3, health=3),
            make_character(id='SBB_CHARACTER_BABYDRAGON', position=6, attack=3, health=3),
        ]
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=2)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (5, 5)


def test_temp_damage3():
    player = make_player(
        characters=[
            make_character(id="SBB_CHARACTER_BABYROOT", position=5, attack=1, health=1),
            make_character(position=1, attack=5, health=8),
        ],
        treasures=['''SBB_TREASURE_HERMES'BOOTS''']
    )
    enemy = make_player(
        characters=[
            make_character(position=1, attack=1, health=1),
            make_character(id='SBB_CHARACTER_BABYDRAGON', position=6, attack=3, health=3),
        ]
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=2)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (5, 5)



def test_temp_damage4():
    player = make_player(
        characters=[
            make_character(id="SBB_CHARACTER_BABYROOT", position=5, attack=3, health=3),
            make_character(position=1, attack=1, health=7),
        ],
        treasures=[
            'SBB_TREASURE_HELMOFCOMMAND',
            'SBB_TREASURE_SPEAROFACHILLES'
        ]
    )
    enemy = make_player(
        characters=[
            make_character(position=1, attack=6, health=1),
            make_character(position=7, attack=1, health=1),
        ],
        treasures = [
            '''SBB_TREASURE_HERMES'BOOTS'''
        ]
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=3)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (8, 7)
