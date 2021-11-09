from sbbbattlesim.treasures import Treasure


class TreasureType(Treasure):
    display_name = 'Needle Nose Daggers'

    def buff(self, target_character):
        target_character.change_stats(attack=2, reason=f'{self} aura', temp=True)