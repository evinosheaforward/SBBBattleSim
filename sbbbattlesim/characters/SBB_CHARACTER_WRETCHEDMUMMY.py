import random

from sbbbattlesim.characters import Character
from sbbbattlesim.action import Damage
from sbbbattlesim.events import OnDeath
from sbbbattlesim.utils import StatChangeCause, Tribe


class WretchedMummyDeath(OnDeath):
    last_breath = True

    def handle(self, *args, **kwargs):
        valid_targets = self.manager.owner.opponent.valid_characters()
        if valid_targets:
            Damage(
                damage=self.manager.attack * (1 + bool(self.manager.golden)),
                reason=StatChangeCause.WRETCHED_MUMMY_EXPLOSION,
                source=self.manager,
                targets=[random.choice(valid_targets)]
            ).resolve()


class CharacterType(Character):
    display_name = 'Wretched Mummy'
    last_breath = True

    _attack = 2
    _health = 1
    _level = 3
    _tribes = {Tribe.EVIL, Tribe.MONSTER}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(WretchedMummyDeath)
