class SieveOfAtkin:
	def __init__(self, limit):
		self.limit = limit

	def getPrimes(self):
		primes = [(2,1), (3,1), (5,1)]
		primes += [(x,0) for x in range (6,limit) if x%2!=0]
		return primes
