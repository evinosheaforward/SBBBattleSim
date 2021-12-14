from sbbbattlesim.action import Buff
from sbbbattlesim.events import OnAttackAndKill
from sbbbattlesim.heros import Hero
from sbbbattlesim.utils import StatChangeCause


class SadDraculaOnAttackAndKill(OnAttackAndKill):
    slay = True

    def handle(self, killed_character, stack, *args, **kwargs):
       Buff(reason=StatChangeCause.SAD_DRACULA_SLAY, source=self.sad_dracula, targets=[self.manager],
            attack=3, stack=stack).resolve()


class HeroType(Hero):
    display_name = 'Sad Dracula'
    aura = True

    def buff(self, target_character, *args, **kwargs):
        if target_character.position == 1:
            target_character.register(SadDraculaOnAttackAndKill, temp=True, sad_dracula=self)
