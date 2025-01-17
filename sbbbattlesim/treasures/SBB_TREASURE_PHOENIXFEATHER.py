from sbbbattlesim.action import Aura
from sbbbattlesim.events import OnDeath
from sbbbattlesim.treasures import Treasure
import copy


class PhoenixFeatherOnDeath(OnDeath):
    last_breath = False

    def handle(self, stack, reason, *args, **kwargs):
        if not self.source.feather_used and self.manager in self.manager.player.graveyard:

            all_characters = self.manager.player.valid_characters() + [self.manager]
            max_attack = max(all_characters, key=lambda x: x.attack).attack
            if self.manager.attack >= max_attack:
                self.source.feather_used = True
                
                self.manager._damage = 0
                self.manager.dead = False
                self.manager.has_attacked = False
                self.manager.player.graveyard.remove(self.manager)
                self.manager.player.summon(self.manager.position, [self.manager])

                if self.source.mimic:
                    new_char = self.manager.copy()
                    self.manager.player.summon(self.manager.position, [new_char], *args, **kwargs)




class TreasureType(Treasure):
    display_name = 'Phoenix Feather'
    aura = True

    _level = 6

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.feather_used = False
        self.aura = Aura(event=PhoenixFeatherOnDeath, source=self, priority=1000)
