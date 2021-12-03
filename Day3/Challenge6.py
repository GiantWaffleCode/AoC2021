# -----------------------
#   Advent of Code 2021
#      GiantWaffle
#   Challenge 6 of 50
# -----------------------

from typing import final


diags = []

with open('G:\Repo\AoC2021\Day3\Challenge5Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      diags.append(line.strip())

def determineDom(checkList, checkBit):
   checkValue = 0
   for currentValue in checkList:
      if currentValue[checkBit] == '1':
         checkValue += 1
      else:
         checkValue -= 1
   if checkValue >= 0:
      return 1
   else:
      return 0

def determineDomInv(checkList, checkBit):
   checkValue = 0
   for currentValue in checkList:
      if currentValue[checkBit] == '1':
         checkValue += 1
      else:
         checkValue -= 1
   if checkValue >= 0:
      return 0
   else:
      return 1

def createNewDiags(currentList, determinationBit, determinationValue):
   newList = []
   for line in currentList:
      if line[determinationBit] == str(determinationValue):
         newList.append(line)
   return newList

def createNewDiagsInv(currentList, determinationBit, determinationValue):
   newList = []
   for line in currentList:
      if line[determinationBit] == str(determinationValue):
         newList.append(line)
   return newList

finalValue = ''

newDiags = createNewDiags(diags, 0, determineDom(diags, 0))
newDiagsInv = createNewDiagsInv(diags, 0, determineDomInv(diags, 0))

for i in range(1,len(diags[0])+1):
   if len(newDiags) > 1:
      newDiags = createNewDiags(newDiags, i, determineDom(newDiags, i))
   else:
      oxyRating = int(newDiags[0], 2)
      print(oxyRating)

for i in range(1,len(diags[0])+1):
   if len(newDiagsInv) > 1:
      newDiagsInv = createNewDiagsInv(newDiagsInv, i, determineDomInv(newDiagsInv, i))
   else:
      cooRating = int(newDiagsInv[0], 2)
      print(cooRating)

print(oxyRating * cooRating)


