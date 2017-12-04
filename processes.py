from multiprocessing import Pool 

def sum_range(t):
	k, l = t
	s = 0
	for i in range(k, l + 1):
		s = s + i
	return s 

if __name__ == '__main__':
	pool = Pool(processes=4)
	n = 1000000000
	l = pool.map(sum_range, [(0, n//4), ((n//4) +1, n//2),(n//2+1, n//4*3),(n//4*3 + 1, n)])
	print(l)
	s = 0 
	for i in l:
		s = s + i
	print(s)