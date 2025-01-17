import logging

from sbbbattlesim.action import Buff, Aura, ActionReason
from sbbbattlesim.events import OnDeath
from sbbbattlesim.treasures import Treasure

logger = logging.getLogger(__name__)


class OtherHandOfVekna(OnDeath):
    last_breath = False

    def handle(self, stack, reason, *args, **kwargs):
        positions = (1, 2, 3, 4) if self.manager.position in (1, 2, 3, 4) else (5, 6, 7)
        targets = self.manager.player.valid_characters(_lambda=lambda char: char.position in positions)
        for _ in range(self.source.mimic + 1):
            Buff(reason=ActionReason.OTHER_HAND_OF_VEKNA, source=self.source, targets=targets,
                 health=1, attack=1, stack=stack).resolve()


class TreasureType(Treasure):
    display_name = 'Other Hand of Vekna'
    aura = True

    _level = 4

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aura = Aura(event=OtherHandOfVekna, source=self, priority=-10)
