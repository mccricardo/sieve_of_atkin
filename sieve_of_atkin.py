class SieveOfAtkin:
	def __init__(self, limit):
		self.limit = limit
		# Implementation assumes only big limit values will be intoduced
		self.primes = {2:1, 3:1, 5:1}

	
	def flip(self, prime):
		self.primes[prime] = 0 if self.primes[prime] == 1 else 1

	def getPrimes(self):	
		otherPrimes	= dict([(x,0) for x in range (6,self.limit) if x%2!=0])
		self.primes = dict(self.primes.items() + otherPrimes.items())
		return self.primes
