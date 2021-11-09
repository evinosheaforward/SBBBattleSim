import random

from sbbbattlesim import utils
from sbbbattlesim.spells import NonTargetedSpell, TargetedSpell
from sbbbattlesim.utils import StatChangeCause


class SpellType(TargetedSpell):
    display_name = 'Shrivel'
    level = 0

    def cast(self, target, *args, **kwargs):
        target.change_stats(attack=-12, health=-12, temp=False, reason=StatChangeCause.SHRIVEL, source=self)