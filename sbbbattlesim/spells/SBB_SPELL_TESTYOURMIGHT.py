from sbbbattlesim.action import Buff, ActionReason
from sbbbattlesim.spells import Spell


class SpellType(Spell):
    display_name = 'Magic Research'
    _level = 2

    def cast(self, target: 'Character' = None, *args, **kwargs):
        Buff(targets=[target], health=1, attack=1, temp=False, reason=ActionReason.MAGIC_RESEARCH, source=self, *args,
             **kwargs)
