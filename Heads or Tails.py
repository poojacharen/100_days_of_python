# Heads or Tails
# Create a coin flip program using what you have learnt about randomisation in Python.
# It should randomly print "Heads" or "Tails" everytime it is run

import random

random_coin_flip = random.randint(0, 1)
if random_coin_flip == 0:
    print("Heads")
else:
    print("Tails")
