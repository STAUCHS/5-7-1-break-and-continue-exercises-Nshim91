#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------



start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))

total = 0
for num in range(start, end + 1):
    if num == 13 or num == 31:
        break
    total += num
print("Sum of numbers:", total)
