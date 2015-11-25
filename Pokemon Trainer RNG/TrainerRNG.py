class TrainerRNG(object):
    """description of class"""

# Written by Stephen (Jack) Henry 25th November 2015
# 1-150 RNG Program with Pokemon - Designed as part of a bigger 'Pokemon Revisited Project.'

import random
import time

n1 = 1
n2 = 150
TrainerPokemon = 7
RNG = 1

while RNG < TrainerPokemon :
    print('Pokemon:', RNG, 'is...', random.randint(int(n1), int(n2)))
    time.sleep(.9)
    RNG += 1 # This is the same thing as RNG = RNG + 1




