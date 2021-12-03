# -----------------------
#   Advent of Code 2021
#      GiantWaffle
#   Challenge 5 of 50
# -----------------------

diags = []

with open('G:\Repo\AoC2021\Day3\Challenge5Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      diags.append(line.strip())

finalValue = ''
finalValueInverse = ''

for i in range(0,12):
   checkValue = 0
   for diag in diags:
      if diag[i] == '1':
         checkValue += 1
      else:
         checkValue -= 1
   if checkValue > 0:
      finalValue += '1'
      finalValueInverse += '0'
   else:
      finalValue += '0'
      finalValueInverse += '1'

print(finalValue)
print(int(finalValue, 2) * int(finalValueInverse, 2))
