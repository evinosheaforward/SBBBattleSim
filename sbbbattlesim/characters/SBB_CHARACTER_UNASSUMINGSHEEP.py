import sbbbattlesim
from sbbbattlesim.characters import Character
from sbbbattlesim.characters import registry as character_registry
from sbbbattlesim.events import OnDeath


class CharacterType(Character):
    display_name = 'Sheep in Wolf\'s Clothing'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register(self.SheepWolfLastBreath)

    class SheepWolfLastBreath(OnDeath):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.priority = sbbbattlesim.SUMMONING_PRIORITY

        def handle(self, *args, **kwargs):
            stat = 10 if self.manager.golden else 5
            sheep = [character_registry['Sheep'](self.manager.owner, self.manager.position, stat, stat, golden=False, keywords=[], tribes=['evil', 'animal'], cost=1)]
            self.manager.owner.summon(self.manager.position, *sheep)
            return 'OnLastBreath', [sheep], {}
