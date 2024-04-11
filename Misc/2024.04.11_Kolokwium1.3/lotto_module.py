from random import randint

class Lotto:
    def __init__(self, n_of_rolls):
        if n_of_rolls not in [5,6]:
            raise Exception('Has to be 5 or 6')
        rolls = []
        deleted_nums = []
        for i in range(0,n_of_rolls):
            number = randint(0,48)
            while number not in deleted_nums:
                deleted_nums.append(number)
                rolls.append(number)
                i -= 1
        self.rolls = rolls

    # for testing SPRAWDZ
    def override(self, new_values):
        self.rolls = new_values
        return self

    def SPRAWDZ(self, lotto_obj2):
        return sorted(self.rolls) == sorted(lotto_obj2.rolls)