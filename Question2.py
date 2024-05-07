#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

# Create a loop that will add the numbers from 5 to 20, inclusive, but not any multiples of 3.
total = 0
for i in range(5, 21):
    if i % 3 == 0:
        continue
    total += i
print(total)
