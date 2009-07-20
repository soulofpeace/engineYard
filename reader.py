import permuateSequence
import calculateSH1
import calculateHammingDistance
import sys

def readInputFile(inputFile):
	list =[]
	for line in inputFile:
		line = line.strip()
		list.append(line)
	return list


def main():
	print 'here'
	inputFile = open(sys.argv[1], 'r')
	stringGiven = sys.argv[2]
	print stringGiven
	hashToMatch = calculateSH1.calculateSH1(stringGiven)
	calculateHammingDistance.hashToMatch= hashToMatch
	numberOfPermutator=int(sys.argv[3])
	numberOfSha1Calculator= int(sys.argv[4])
	numberOfDistanceCalculator = int(sys.argv[5])
	permuateSequence.listGiven = readInputFile(inputFile)

	for i in range(numberOfDistanceCalculator):
		calculateHammingDistance.DistanceCalculator().start()

	for i in range(numberOfSha1Calculator):
		calculateSH1.Sha1Calculator(calculateHammingDistance.distanceCalculatorQueue).start()
	
	for i in range(numberOfPermutator):
		permuateSequence.Permutator(calculateSH1.sha1Queue).start() 
	
		
	
if __name__=='__main__':
	main()
