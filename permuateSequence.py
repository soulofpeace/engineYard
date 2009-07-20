import random
import Queue
import threading
import time

listGiven=[]
usedWordList=[]
permutatorQueue = Queue.Queue()
randPadChoice = range(33, 127)

def permuate(number=12):
	#print 'hei hei' +str(listGiven)
	permuateList=[]
	while(len(permuateList)<number):
		wordSeed = listGiven[random.randint(0, (len(listGiven)-1))]
		word =''
		for ch in wordSeed:
			upperFlag = random.randint(0, 1)
			if upperFlag:
				ch = ch.upper()
			else:
				ch = ch.lower()
			word +=ch
		
		permuateList.append(word)
	permuateList.append(randPadding())				
	return permuateList

def generate():
	permuateList = permuate()
	key = ' '.join(permuateList)
	while key in usedWordList:
		permuateList = permuate()
		key = ' '.join(permuateList)
	usedWordList.append(key)
	print '##TIMEPERMUATE %s generated at %s' %(key, str(time.time()))
	print '##DEBUG usedWordList Length is %i' %len(usedWordList)
	return key.strip()
	

def randPadding():
	randPad=''
	randPadFlag = random.randint(0,1)
	if randPadFlag:		
		length = random.randint(1,5)
		while(len(randPad)<length):
			randPad+= chr(random.choice(randPadChoice))
	return randPad

class Permutator(threading.Thread):

	def __init__(self, sha1Queue):
		threading.Thread.__init__(self)
		self.__sha1Queue =sha1Queue
		
	def run(self):
		print 'Permutator Thread has started!'
		while True:
			string = generate()
			self.__sha1Queue.put(string)
			
					
		
		
		
def main():
	global listGiven
	listGiven=['eight', 'six', 'memcached', 'mongrel', 'ruby', 'rails', 'tokyo', 'active', 'record', 'controller']
	print generate()
	
	
if __name__=='__main__':
	main()
