import hashlib
import Queue
import threading

sha1Queue = Queue.Queue()

def calculateSH1(value):
	m = hashlib.sha1()
	m.update(value)
	return m.hexdigest()


class Sha1Calculator(threading.Thread):

	def __init__(self, distanceCalculatorQueue):
		threading.Thread.__init__(self)
		self.__distanceCalculatorQueue = distanceCalculatorQueue
		
	def run(self):
		print 'Sha1Calculator Thread has started!'
		try:
			while True:
				string = sha1Queue.get(True, 5400)
				sha1= calculateSH1(string)
				self.__distanceCalculatorQueue.put((string, sha1))
		except Queue.Empty:
			print 'end Sha1Calculator'


def main():
	string='RuBy one eight six rspec mongrel MRI jruby jruby memcached exception reflection utf8E'
	print calculateSH1(string)


if __name__=='__main__':
	main()
