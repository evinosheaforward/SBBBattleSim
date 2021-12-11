from sbbbattlesim.action import Buff
from sbbbattlesim.spells import TargetedSpell
from sbbbattlesim.utils import StatChangeCause, Tribe


class SpellType(TargetedSpell):
    display_name = '''Beauty's Influence'''
    _level = 3

    def cast(self, target, *args, **kwargs):
        Buff(reason=StatChangeCause.BEAUTYS_INFLUENCE, source=self, targets=[target],
             health=4, attack=0, temp=False, *args, **kwargs).resolve()

        target.tribes.remove(Tribe.EVIL)
        target.tribes.add(Tribe.GOOD)

    def filter(self, char):
        return Tribe.EVIL in char.tribes
