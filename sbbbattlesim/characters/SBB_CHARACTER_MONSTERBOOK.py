from sbbbattlesim.characters import Character
from sbbbattlesim.events import OnDeath
from sbbbattlesim.utils import Tribe, random_combat_spell


class CharacterType(Character):
    display_name = 'Monster Book'
    last_breath = True

    _attack = 10
    _health = 5
    _level = 5
    _tribes = {Tribe.EVIL, Tribe.MONSTER}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        class MonsterBookOnDeath(OnDeath):
            last_breath = True
            monster_book = self

            def handle(self, *args, **kwargs):
                spell = random_combat_spell(self.monster_book.owner.level)
                if spell:
                    self.manager.owner.cast(spell)

        self.register(MonsterBookOnDeath)