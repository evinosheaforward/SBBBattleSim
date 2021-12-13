from sbbbattlesim.action import Buff, SupportBuff
from sbbbattlesim.characters import Character
from sbbbattlesim.utils import StatChangeCause, Tribe


class CharacterType(Character):
    display_name = 'Wicked Witch of the West'
    support = True

    _attack = 3
    _health = 2
    _level = 3
    _tribes = {Tribe.EVIL, Tribe.MAGE}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        golden_multiplyer = 2 if self.golden else 1
        self.support_buff = SupportBuff(source=self, _lambda=lambda char: Tribe.EVIL in char.tribes,
                                        attack=3 * golden_multiplyer, health=2 * golden_multiplyer)

    def buff(self, target_character, *args, **kwargs):
        self.support_buff.execute(target_character, *args, **kwargs)