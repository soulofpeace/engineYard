import threading
import Queue
import time

lowest=99999
distanceCalculatorQueue = Queue.Queue()
hashToMatch=''

def calculateHaming(hex2):
	a = int(hashToMatch, 16)
	b = int(hex2, 16)
	c = a^b
	cstr = bin(c)[2:]
	diff =0
	for ch in cstr:
		if ch=='1':
			diff+=1
	return diff

class DistanceCalculator(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		
	def run(self):
		print 'distanceCalculator Thread has started!'
		global lowest
		try:
			while True:
				string, hex2 = distanceCalculatorQueue.get(True, 5400)
				distance = calculateHaming(hex2)
				print '##TIMEDISTANCE %s of %s generated at %s' %(distance, string, str(time.time()))
				if distance < lowest:
					lowest = distance
					print '##RESULT: %s, %s' %(string, distance)
		except Queue.Empty:
			print 'end DifferenceCalculator'


def main():
	global hashToMatch
	hashToMatch='7f83e6b422af5ca4e3112486aea3e702e98a894e'
	print calculateHaming('075a32acb1816b570607189475ebbbaccce8b79f')
	

if __name__=='__main__':
	main()
				
			
			
