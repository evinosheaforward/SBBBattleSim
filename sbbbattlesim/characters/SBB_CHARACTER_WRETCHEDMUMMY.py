from sbbbattlesim.characters import Character
from sbbbattlesim.characters import registry as character_registry
from sbbbattlesim.events import OnDeath


class CharacterType(Character):
    display_name = 'Wretched Mummy'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(self.WretchedMummyDeath)

    class WretchedMummyDeath(OnDeath):
        def handle(self, *args, **kwargs):
            damage = 8 if self.manager.golden else 4
            for char in self.manager.owner.opponent.valid_characters():
                char.damage += damage

            return 'OnLastBreath', [], {'damage_done': damage}