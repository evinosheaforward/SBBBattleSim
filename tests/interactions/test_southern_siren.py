from sbbbattlesim import Board
from tests import make_character, make_player
import pytest
from sbbbattlesim.utils import Tribe

@pytest.mark.parametrize('attacker_golden', (True, False))
@pytest.mark.parametrize('defender_golden', (True, False))
def test_southern_siren(attacker_golden, defender_golden):

    player = make_player(
        characters=[
            make_character(id='SBB_CHARACTER_LOBO', position=1, attack=1, health=1, golden=attacker_golden),
        ],
        treasures=[
            '''SBB_TREASURE_HERMES'BOOTS'''
        ]
    )
    enemy = make_player(
        characters=[make_character(attack=0, health=1, golden=defender_golden, tribes=[Tribe.DWARF])],
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=1)
    board.p1.resolve_board()
    board.p2.resolve_board()

    units_to_check = []
    units_to_check.append(board.p1.characters[2])
    if attacker_golden:
        units_to_check.append(board.p1.characters[3])

    for utc in units_to_check:
        assert utc is not None
        assert utc.golden is defender_golden
        assert utc.tribes == type(utc.tribes)([Tribe.DWARF])