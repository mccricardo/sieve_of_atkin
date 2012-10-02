from math import sqrt, ceil, pow

class SieveOfAtkin:
	def __init__(self, limit):
		self.limit = limit
		# Implementation assumes only big limit values will be intoduced
		self.primes = {2:1, 3:1}

	
	def flip(self, prime):
		try:
			self.primes[prime] = 1 if self.primes[prime] == 0 else 0
		except KeyError:
			pass


	def invalidate(self, prime):
		try:
			if self.primes[prime] == 1: self.primes[prime] = 0
		except KeyError:
			pass


	def isPrime(self, prime):
		try:
			if self.primes[prime] == 1: return True
			else: return False
		except KeyError:
			pass		


	def getPrimes(self):	
		otherPrimes	= dict([(x,0) for x in range (5,self.limit) if x%2!=0])
		self.primes = dict(self.primes.items() + otherPrimes.items())

		testingLimit = int(ceil(sqrt(self.limit)))

		for i in range(testingLimit):
			for j in range(testingLimit):
				# n = 4*i^2 + j^2
				n = 4*int(pow(i, 2)) + int(pow(j,2))
				if n <= self.limit and (n % 12 == 1 or n % 12 == 5):				
					self.flip(n)

				# n = 3*i^2 + j^2
				n = 3*int(pow(i, 2)) + int(pow(j,2))
				if n <= self.limit and n % 12 == 7:				
					self.flip(n)				

				# n = 3*i^2 - j^2
				n = 3*int(pow(i, 2)) - int(pow(j,2))
				if n <= self.limit and i > j and n % 12 == 11:					
					self.flip(n)				


		for i in self.primes.keys():
			if self.isPrime(i):
				k = int(pow(i, 2))
				i=2
				while k <= self.limit:
					self.invalidate(k)
					k*=i
					i+=1
					

		return [x for x in self.primes.keys() if self.primes[x] == 1]

