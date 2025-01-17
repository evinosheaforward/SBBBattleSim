import pytest

from sbbbattlesim import Board
from tests import make_character, make_player, SpawnOnStart
from sbbbattlesim.characters import registry as character_registry
from sbbbattlesim.events import OnStart

@pytest.mark.parametrize('golden', (True, False))
def test_riverwish(golden):
    player = make_player(
        characters=[
            make_character(id='SBB_CHARACTER_RIVERWISHMERMAID', position=5, attack=1, health=1, golden=golden),
            make_character(position=1, attack=1, health=1)
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

    final_stats = (3, 3) if golden else (2, 2)
    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == final_stats


def test_riverwish_cloakoftheassassin():
    player = make_player(
        characters=[
            make_character(id='SPAWN_TEST', spawn_char=character_registry['SBB_CHARACTER_RIVERWISHMERMAID'],
                           spawn_pos=5, position=7, attack=1, health=1),
            make_character(position=1, attack=1, health=1)
        ],
        treasures=[
            '''SBB_TREASURE_CLOAKOFTHEASSASSIN'''
        ]
    )
    enemy = make_player()
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=0)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (4, 4)


def test_riverwish_cloakoftheassassin_doubledip():
    player = make_player(
        characters=[
            make_character(id='SPAWN_TEST', spawn_char=character_registry['SBB_CHARACTER_RIVERWISHMERMAID'],
                           spawn_pos=5, position=7, attack=1, health=1),
            make_character(id='SBB_CHARACTER_NIGHTSTALKER', position=1, attack=1, health=1)
        ],
        treasures=[
            '''SBB_TREASURE_CLOAKOFTHEASSASSIN'''
        ]
    )
    enemy = make_player()
    board = Board({'PLAYER': player, 'ENEMY': enemy})

    winner, loser = board.fight(limit=0)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (1, 1)


def test_riverwish_cloakoftheassassin_doubledip2():
    player = make_player(
        characters=[
            make_character(id='SPAWN_TEST', spawn_char=character_registry['SBB_CHARACTER_NIGHTSTALKER'],
                           position=1, attack=1, health=1, spawn_pos=1)
        ],
        treasures=[
            '''SBB_TREASURE_CLOAKOFTHEASSASSIN'''
        ]
    )
    enemy = make_player()
    board = Board({'PLAYER': player, 'ENEMY': enemy})

    class FakeTrojanDonkeySummon(OnStart):

        def handle(self, *args, **kwargs):
            summon = character_registry['SBB_CHARACTER_RIVERWISHMERMAID'].new(
                player=self.manager.p1,
                position=5,
                golden=False,
            )
            self.manager.p1.summon(5, [summon])

    board.register(FakeTrojanDonkeySummon, priority=-999)

    winner, loser = board.fight(limit=0)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (4, 4)


def test_riverwish_cloakoftheassassin_dies():
    player = make_player(
        characters=[
            make_character(id='SPAWN_TEST', spawn_char=character_registry['SBB_CHARACTER_RIVERWISHMERMAID'],
                           spawn_pos=5, position=5, attack=1, health=1),
            make_character(position=1, attack=1, health=1)
        ],
        treasures=[
            '''SBB_TREASURE_CLOAKOFTHEASSASSIN'''
        ]
    )
    enemy = make_player(
        characters=[make_character(id='SBB_CHARACTER_BABYDRAGON', attack=30, health=30)],
        treasures=['''SBB_TREASURE_HERMES'BOOTS''']
    )
    board = Board({'PLAYER': player, 'ENEMY': enemy})
    winner, loser = board.fight(limit=1)

    assert (board.p1.characters[1].attack, board.p1.characters[1].health) == (1, 1), [i.pretty_print() for i in board.p1.valid_characters()]