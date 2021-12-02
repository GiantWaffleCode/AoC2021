# -----------------------
#   Advent of Code 2021
#      GiantWaffle
#   Challenge 3 of 50
# -----------------------

instructions = []

with open('G:\Repo\AoC2021\Day2\Challenge3Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      instructions.append(line.strip())

totalForward = 0;
totalDepth = 0;

for instruction in instructions:
   splitList = instruction.split()
   splitList[1] = int(splitList[1])

   match splitList[0]:
      case 'forward':
         totalForward += splitList[1]
      case 'up':
         totalDepth -= splitList[1]
      case 'down':
         totalDepth += splitList[1]

print(totalForward * totalDepth)