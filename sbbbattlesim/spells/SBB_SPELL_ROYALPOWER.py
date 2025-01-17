from sbbbattlesim.action import Buff, ActionReason
from sbbbattlesim.spells import Spell
from sbbbattlesim.utils import Tribe


class SpellType(Spell):
    display_name = '''Queen's Grace'''
    _level = 4

    def cast(self, target: 'Character' = None, *args, **kwargs):
        Buff(targets=[target], health=7, attack=7, temp=False, reason=ActionReason.QUEENS_GRACE, source=self, *args,
             **kwargs)

    @classmethod
    def filter(cls, char):
        return Tribe.PRINCESS in char.tribes or Tribe.PRINCE in char.tribes
