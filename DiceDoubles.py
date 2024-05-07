#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

import random

print("HERE COMES THE DICE!")

while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print("Roll #1:", roll1)
    print("Roll #2:", roll2)
    total = roll1 + roll2
    print("The total is", total)
    if roll1 == roll2:
        break
