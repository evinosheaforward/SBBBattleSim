from sbbbattlesim.treasures import Treasure
from sbbbattlesim.utils import StatChangeCause


class TreasureType(Treasure):
    display_name = 'Needle Nose Daggers'

    def buff(self, target_character):
        target_character.change_stats(attack=2, reason=StatChangeCause.NEEDLE_NOSE_DAGGERS, source=self, temp=True)
