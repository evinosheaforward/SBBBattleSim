import pytest

from sbbbattlesim import Board
from sbbbattlesim.utils import Tribe
from tests import make_character, make_player


@pytest.mark.parametrize('roundtable', (True, False))
def test_onstart_trees(roundtable):
    player = make_player(
        characters=[
            make_character(
                id="SBB_CHARACTER_KINGTREE", position=2,
                attack=1, health=100, tribes=[Tribe.EVIL, Tribe.TREANT]
            ),
            make_character(
                id="SBB_CHARACTER_ELDERTREANT", position=5,
                attack=0, health=7, tribes=[Tribe.GOOD, Tribe.TREANT]
            )

        ],
        treasures=[
            "SBB_TREASURE_IVORYOWL",
            "SBB_TREASURE_HELMOFTHEUGLYGOSLING",
            "SBB_TREASURE_THEROUNDTABLE" if roundtable else ""
        ]
    )
    enemy = make_player()
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=0)


    ashwood = board.p1.characters[2]
    elderwood = board.p1.characters[5]
    shoulders = board.p1.characters[7]

    if roundtable:
        assert (ashwood.attack, ashwood.health) == (109, 109)
        assert (elderwood.attack, elderwood.health) == (121, 121)
    else:
        assert (ashwood.attack, ashwood.health) == (109, 104)
        assert (elderwood.attack, elderwood.health) == (121, 24)


def test_onstart_arthur_and_lordy():
    player = make_player(
        characters=[
            make_character(
                id="SBB_CHARACTER_KINGARTHUR", position=2, golden=True,
                attack=5, health=5, tribes=[Tribe.PRINCE]
            ),
            make_character(
                id="SBB_CHARACTER_FORGEMASTERDWARF", position=3, golden=True,
                attack=5, health=5, tribes=[Tribe.PRINCE]
            ),
            make_character(
                position=5, attack=6, health=6
            )
        ],
        treasures=[
            "SBB_TREASURE_HELMOFTHEUGLYGOSLING"
        ]
    )
    enemy = make_player()
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=0)


    arthur = board.p1.characters[2]
    lordy = board.p1.characters[3]
    generic = board.p1.characters[5]

    assert (arthur.attack, arthur.health) == (9, 9)
    assert (generic.attack, generic.health) == (21, 21)
