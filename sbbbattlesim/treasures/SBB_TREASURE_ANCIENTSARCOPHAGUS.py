import random

from sbbbattlesim.action import Damage
from sbbbattlesim.events import OnDeath
from sbbbattlesim.treasures import Treasure
from sbbbattlesim.utils import StatChangeCause, Tribe


class AncientSarcophagusOnDeath(OnDeath):
    last_breath = False

    def handle(self, *args, **kwargs):
        for _ in range(self.ancient_sarcophagus.mimic + 1):
            valid_targets = self.manager.owner.opponent.valid_characters()
            if valid_targets:
                Damage(damage=3, reason=StatChangeCause.ANCIENT_SARCOPHAGUS, source=self.ancient_sarcophagus,
                       targets=[random.choice(valid_targets)]).resolve()


class TreasureType(Treasure):
    display_name = 'Ancient Sarcophagus'
    aura = True

    _level = 3

    def buff(self, target_character, *args, **kwargs):
        if Tribe.EVIL in target_character.tribes:
            target_character.register(AncientSarcophagusOnDeath, temp=True, ancient_sarcophagus=self)
