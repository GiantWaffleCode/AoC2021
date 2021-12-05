# -----------------------
#   Advent of Code 2021
#      GiantWaffle
#   Challenge 7&8 of 50
# -----------------------

# DONT LOOK AT THIS GARBAGE. THIS IS MY GARBAGE

bingoInput = []

with open('Challenge7Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      bingoInput.append(line.strip())

bingoBalls = [int(x) for x in bingoInput[0].split(',')]
bingoCards = []

for i in range((len(bingoInput)//6)):
   tempCard = []
   for j in range(5):
      tempCard.append([int(x) for x in bingoInput[((i*6)+2+j)].split()])
      
   bingoCards.append(tempCard)


#print(bingoBalls)
#print(f'Cards: {bingoCards[0]}')

def checkForNumber(card, number):
   for line in card:
      for j, box in enumerate(line):
         if box == number:
            line[j] = -1
   return card


def checkIfWin(card):
   for row in card:
      if sum(row) == -5:
         return True
   for i in range(5):
      colSum = 0
      for j in range(5):
         colSum += card[j][i]
      if colSum == -5:
         return True
   else:
      return False

def sumWinner(card):
   totalSum = 0
   for line in card:
      for box in line:
         if box != -1:
            totalSum += box
   return totalSum


def playGame(bingoCards, bingoBalls):
   checkedBingoCards = bingoCards
   winnerList = []

   for j, bingoDraw in enumerate(bingoBalls):
      if len(checkedBingoCards) > 0:
         newCheckedBingoCards = []
         for card in checkedBingoCards:
            checkForNumber(card, bingoDraw)
            if checkIfWin(card):
               print('WINNER')
               winnerList.append(card)
            else:
               print('NOT WINNER')
               newCheckedBingoCards.append(card)
         checkedBingoCards = newCheckedBingoCards
      else:
         print('EXITING')
         print(checkedBingoCards)
         return winnerList, bingoBalls[j-1]
      

winningList = playGame(bingoCards, bingoBalls)
winningCard = winningList[0][-1]
print(f'Card: {winningCard}')
winningDraw = winningList[1]
print(f'Draw: {winningDraw}')
winningScore = sumWinner(winningCard) * winningDraw
print(f'FUCK: {winningScore}')
