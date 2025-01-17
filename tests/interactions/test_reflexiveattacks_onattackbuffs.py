from sbbbattlesim import Board
from sbbbattlesim.utils import Tribe
from tests import make_character, make_player


def test_courtwizard_spearofachilles():
    player = make_player(
        characters=[
            make_character(position=1),
            make_character(position=2)
        ],
        treasures=['''SBB_TREASURE_HERMES'BOOTS''']
    )
    enemy = make_player(
        characters=[
            make_character(position=1, tribes=[Tribe.PRINCE]),
            make_character(id="SBB_CHARACTER_COURTWIZARD", position=5)
        ],
        treasures=['''SBB_TREASURE_SPEAROFACHILLES''']
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=1)


    assert (board.p2.characters[5].attack, board.p2.characters[5].health) == (8, 8)
