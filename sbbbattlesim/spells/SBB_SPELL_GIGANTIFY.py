from sbbbattlesim.spells import TargetedSpell
from sbbbattlesim.utils import StatChangeCause


class SpellType(TargetedSpell):
    display_name = 'Gigantify'

    def cast(self, target, *args, **kwargs):
        target.change_stats(health=10, temp=False, reason=StatChangeCause.GIGANTIFY, source=self)