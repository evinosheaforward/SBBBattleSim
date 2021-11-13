import random
import time
import traceback
from copy import deepcopy

from sbbbattlesim.events import EventManager
from sbbbattlesim.player import Player
from sbbbattlesim.combat import fight_initialization
import logging

logger = logging.getLogger(__name__)

class Board(EventManager):
    def __init__(self, data):
        super().__init__()
        assert isinstance(data, dict)
        p1id, p2id = list(data)
        p1data, p2data = data[p1id], data[p2id]

        def get_player(pdat, id):
            return Player(
                characters=pdat.get('characters', ()),
                treasures=pdat.get('treasures', ()),
                hero=pdat.get('hero', ''),
                hand=pdat.get('hand', ()),
                id=id,
                spells=pdat.get('spells', ()),
                level=pdat.get('level', 0),
                board=self
            )

        p1, p2 = get_player(p1data, p1id), get_player(p2data, p2id)

        self.p1 = p1
        self.p2 = p2

        self.p1.opponent = self.p2
        self.p2.opponent = self.p1

    def fight(self, limit=None):
        HERMES_BOOTS = '''SBB_TREASURE_HERMES'BOOTS'''
        # Determine Setup and Turn Order
        if self.p1.treasures.get(HERMES_BOOTS) and not self.p2.treasures.get(HERMES_BOOTS):
            attacking, defending = self.p1, self.p2
        elif self.p2.treasures.get(HERMES_BOOTS) and not self.p1.treasures.get(HERMES_BOOTS):
            attacking, defending = self.p2, self.p1
        else:
            attacking, defending = random.sample((self.p1, self.p2), 2)

        return fight_initialization(attacker=attacking, defender=defending, limit=limit, board=self)
