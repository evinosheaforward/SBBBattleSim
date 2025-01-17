import pytest

from sbbbattlesim import Board
from tests import make_character, make_player
from sbbbattlesim.action import ActionReason


@pytest.mark.parametrize('golden', (True, False))
def test_yaga_slay(golden):
    player = make_player(
        raw=True,
        characters=[
            make_character(id='SBB_CHARACTER_BABAYAGA', position=6, attack=3, health=6, golden=golden),
            make_character(id='SBB_CHARACTER_CATBURGLAR', attack=4, health=1, position=2),
            make_character(id="SBB_CHARACTER_SHADOWASSASSIN", position=7, attack=1, health=1)
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

    char = board.p1.characters[2]
    buffs = [
        r for r in char._action_history if r.reason == ActionReason.SUPPORT_BUFF
    ]

    assert sum([d.attack for d in buffs]) == (6 if golden else 3)
    assert sum([d.health for d in buffs]) == 0

    final_stats = (4, 1) if golden else (3, 1)
    assert (board.p1.characters[7].attack, board.p1.characters[7].health) == final_stats


def test_yaga_ranged():
    player = make_player(
        characters=[
            make_character(id='SBB_CHARACTER_BABAYAGA', position=6, attack=3, health=6),
        ],
        treasures=[
            '''SBB_TREASURE_HERMES'BOOTS'''
        ]
    )
    enemy = make_player(
        characters=[make_character(attack=1, health=1)],
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=2)


    assert (board.p1.characters[6].attack, board.p1.characters[6].health) == (3, 6)
