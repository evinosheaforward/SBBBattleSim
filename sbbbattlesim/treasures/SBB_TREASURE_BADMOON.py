from sbbbattlesim.action import Buff
from sbbbattlesim.events import OnSlay
from sbbbattlesim.treasures import Treasure
from sbbbattlesim.utils import StatChangeCause


class BadMoonSlayBuff(OnSlay):
    def handle(self, source, stack, *args, **kwargs):
        for _ in range(self.bad_moon.mimic + 1):
            Buff(reason=StatChangeCause.BAD_MOON, source=self.bad_moon, targets=[self.manager],
                 attack=1, health=2,  temp=False, stack=stack).resolve()


class TreasureType(Treasure):
    display_name = 'Bad Moon'
    aura = True

    _level = 3

    def buff(self, target_character, *args, **kwargs):
        target_character.register(BadMoonSlayBuff, temp=True, bad_moon=self)
