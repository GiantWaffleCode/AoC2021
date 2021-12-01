# -----------------------
#   Advent of Code 2021
#      GiantWaffle
#   Challenge 1 of 50
# -----------------------

depths = []

with open('G:\Repo\AoC2021\Day1\Challenge1Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      depths.append(int(line.strip()))

firstDepth = True
lastDepth = 0
depthCounter = 0

for depth in depths:
   if firstDepth:
      lastDepth = depth
      firstDepth = False

   depthDiff = depth - lastDepth
   lastDepth = depth

   if depthDiff > 0:
      depthCounter+=1

print(depthCounter)


