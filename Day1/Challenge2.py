# -----------------------
#   Advent of Code 2021
#      GiantWaffle
#   Challenge 2 of 50
# -----------------------

depths = []
trioSums = []

with open('G:\Repo\AoC2021\Day1\Challenge1Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      depths.append(int(line.strip()))

for i in range(len(depths) - 2):
   trioSum = depths[i] + depths[i+1] + depths[i+2]
   trioSums.append(trioSum)

firstTrio = True
lastTrio = 0
trioCounter = 0

for trio in trioSums:
   if firstTrio:
      lastTrio = trio
      firstTrio = False

   trioDiff = trio - lastTrio
   lastTrio = trio

   if trioDiff > 0:
      trioCounter+=1

print(trioCounter)

   