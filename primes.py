from multiprocessing import Pool 

primes = set()

def check_prime(x):
	global primes
	if x in primes:
		return True
	for item in primes:
	 	if x % item == 0:
	 		return False
	 	primes.add(x)	
	 	return True

if __name__ == '__main__':
	pool = Pool(processes=4)
	n = 1000
	l = pool.map(check_prime, range(2, n))
	i = 2
	for item in l:
		if item == True:
			i = i+1
		print(i)