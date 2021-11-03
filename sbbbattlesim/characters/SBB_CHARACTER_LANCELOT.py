from sbbbattlesim.characters import Character
from sbbbattlesim.events import OnAttackAndKill


class CharacterType(Character):
    display_name = 'Lancelot'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(self.LancelotSlay)

    class LancelotSlay(OnAttackAndKill):
        def handle(self, killed_character, *args, **kwargs):
            modifier = 4 if self.golden else 2
            self.manager.change_stats(attack=modifier, health=modifier, temp=False, reason=f'{self} slayed an enemy and is growing')