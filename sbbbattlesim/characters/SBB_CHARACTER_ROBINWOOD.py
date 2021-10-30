from sbbbattlesim.characters import Character
from sbbbattlesim.events import OnFightStart
from sbbbattlesim.utils import find_strongest_character, find_weakest_character


class CharacterType(Character):
    display_name = 'Robin Wood'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        class RobinWoodOnFightStart(OnFightStart):
            priority = 50
            golden = self.golden

            def handle(self, *_args, **_kwargs):
                strongest_enemy_char = find_strongest_character(self.manager.opponent)
                weakest_allied_char = find_weakest_character(self.manager)

                strongest_enemy_char.base_attack -= 30 if self.golden else 15
                weakest_allied_char.base_attack += 30 if self.golden else 15

        self.owner.register(RobinWoodOnFightStart)


