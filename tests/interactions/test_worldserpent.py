from sbbbattlesim import Board
from tests import make_character, make_player
import pytest

@pytest.mark.parametrize('golden', (True, False))
def test_jormangundr(golden):

    player = make_player(
        characters=[
            make_character(id='SBB_CHARACTER_WORLDSERPENT', position=6, attack=1, health=1, golden=golden),
        ],
        treasures=[
            '''SBB_TREASURE_HERMES'BOOTS'''
        ]
    )
    enemy = make_player(
        characters=[make_character(attack=0, health=1)],
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=1)
    board.p1.resolve_board()
    board.p2.resolve_board()

    final_stats = (41, 41) if golden else (21, 21)
    assert (board.p1.characters[6].attack, board.p1.characters[6].health) == final_stats
