import logging
import pkgutil
from collections import OrderedDict
from sbbbattlesim.sbbbsobj import SBBBSObject

logger = logging.getLogger(__name__)

logic_path = __path__


class Character(SBBBSObject):
    support = False

    def __init__(self, owner, position, attack, health, golden, keywords, tribes, cost):
        super().__init__()
        self.owner = owner

        self.position = position
        self._base_attack = attack
        self._base_health = health
        self.golden = golden
        self.keywords = keywords
        self.tribes = tribes
        self.cost = cost

        self._temp_attack = 0
        self._temp_health = 0
        self._damage = 0
        self.slay_counter = 0
        self.dead = False

        self.stat_history = []

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'''{self.display_name} pos:{self.position} gold:{self.golden} ({self.attack}/{self.health})'''

    @property
    def attack(self):
        return self._base_attack + self._temp_attack

    @property
    def health(self):
        return self._base_health + self._temp_health - self._damage

    @property
    def max_health(self):
        return self._base_health + self._temp_health

    def change_stats(self, reason, attack=0, health=0, damage=0, temp=True):
        starting_repr = self.__repr__()
        logger.debug(f'{self} stat change b/c {reason} (attack={attack}, health={health}, damage={damage}, temp={temp})')

        if temp:
            self._temp_attack += attack
            self._temp_health += health
        else:
            self._base_attack += attack
            self._base_health += health

        if damage > 0:
            self._damage += damage
            if self.health <= 0:
                self.dead = True
                logger.debug(f'{self} marked for death')
            else:
                # On Damage and Survived Trigger
                # TODO Maybe add more args if needed
                self('OnDamagedAndSurvived', damage=damage)

        if attack > 0 or health > 0:
            self('OnBuff', attack_buff=attack, health_buff=health, damage=damage, reason=reason, temp=temp)

        logger.debug(f'{self} finishsed stat change')

        self.stat_history.append((reason, attack, health, damage, temp, self.__repr__()))

    def clear_temp(self):
        super().clear_temp()

        self._temp_attack = 0
        self._temp_health = 0



class Registry(object):
    characters = OrderedDict()

    def __getitem__(self, item):
        character = self.characters.get(item)
        if not character:
            character = {char.display_name: char for char in self.characters.values()}.get(item)

        if not character:
            class NewCharacter(Character):
                display_name = item

            character = NewCharacter
            # print(f'Creating Generic Character for {item}')

        # Set the id for reference
        character.id = item

        return character

    def __getattr__(self, item):
        return getattr(self.characters, item)

    def __contains__(self, item):
        return item in self.characters

    def register(self, name, character):
        assert name not in self.characters, 'Character is already registered.'
        self.characters[name] = character
        logger.debug(f'Registered {name} - {character}')

    def unregister(self, name):
        self.characters.pop(name, None)

    def autoregister(self):
        for _, name, _ in pkgutil.iter_modules(logic_path):
            try:
                character = __import__(name, globals(), locals(), ['CharacterType'], 1)
                self.register(name, character.CharacterType)
            except ImportError as e:
                pass
            except Exception as exc:
                logger.exception('Error loading characters: {}'.format(name))

    def items(self):
        return {i.display_name: i for i in self.characters.values()}.items()


registry = Registry()
registry.autoregister()
