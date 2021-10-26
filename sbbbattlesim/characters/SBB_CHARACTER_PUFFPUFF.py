from sbbbattlesim.characters import Character
from sbbbattlesim.events import Slay


class CharacterType(Character):
    # You will have to make a commit to change this name
    name = 'PUFF MOTHER FUCKING PUFF'

    class PuffPuffDeath(Slay):
        def __call__(self, **kwargs):
            for char in self.character.owner.characters.values():
                if char is not None:
                    if char.name == self.character.name:
                        char.base_health += 2 if self.character.golden else 1
                        char.base_attack += 2 if self.character.golden else 1

    events = (
        PuffPuffDeath,
    )