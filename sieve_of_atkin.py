from math import sqrt, ceil, pow

class SieveOfAtkin:
	def __init__(self, limit):
		self.limit = limit
		# Implementation assumes only big limit values will be intoduced
		self.primes = {2:1, 3:1}

	
	def flip(self, prime):
		self.primes[prime] = 1 if self.primes[prime] == 0 else 0

	def getPrimes(self):	
		otherPrimes	= dict([(x,0) for x in range (5,self.limit) if x%2!=0])
		self.primes = dict(self.primes.items() + otherPrimes.items())

		testingLimit = int(ceil(sqrt(self.limit)))

		for i in range(1, testingLimit):
			for j in range(1, testingLimit):
				# n = 4*i^2 + j
				n = 4*int(pow(i, 2)) + j
				if n <= self.limit and (n % 12 == 1 or n % 12 == 5):				
					self.flip(n)

				# n = 3*i^2 + j
				n = 3*int(pow(i, 2)) + j
				if n <= self.limit and n % 12 == 7:				
					self.flip(n)				

				# n = 3*i^2 - j
				n = 3*int(pow(i, 2)) - j
				if n <= self.limit and i > j and n % 12 == 11:					
					self.flip(n)				

		return [x for x in self.primes.keys() if self.primes[x] == 1]

soa = SieveOfAtkin(100)
print soa.getPrimes()