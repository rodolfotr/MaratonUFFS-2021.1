## Quantity of tests.
qtdTests = int(input())

for test in range(qtdTests):
	## For each test, read amount of stones.
	numberOfStones = int(input())
	
	## Read list of stones.
	listOfStones = [int(i) for i in input().split()]

	## Get lowest number index.
	minNumber = min(listOfStones)
	minIndex = listOfStones.index(minNumber)
	
	## Get highest number index.
	maxNumber = max(listOfStones)
	maxIndex = listOfStones.index(maxNumber)
 
	x1 =  max(maxIndex, minIndex) + 1
	x2 =  numberOfStones - min(maxIndex, minIndex)
	x3 =  min(maxIndex + 1, numberOfStones - maxIndex) + min( minIndex + 1, numberOfStones - minIndex)

	print(min(x1,x2,x3))