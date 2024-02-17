# collatzLibrary

'''
first 200 primes
'''
primes200=[5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223]

'''
get nextCore,power as the cordinates which is the unique id for this number as a node in the tree :D
'''
def getPoint(odd):
	return nextOdd(odd,True)


def nextOdd(odd,asPoint=False):
	odd=oddFromEven(odd)
	odd=oddFromEven(3*odd+1,asPoint)
	return odd

'''
helper, remove twos 2
'''
def oddFromEven(even,asPoint=False):
	n=0
	while even%2==0:
		n+=1
		even//=2
	if(asPoint):
		return (even,n)
	return even

'''
print full sequence from number till it reach 1
'''
def printCollatzSequence(number):
	odd=oddFromEven(number)
	if odd==1:
		print(1)
		return
	print(odd,end='-> ')
	even =3*odd+1
	printCollatzSequence(even)

'''
opts of 1 which are of type T3
'''
def OPT1T3(n):
	return (4**(3+3*n) -1)//3


def primeFactors(n):
	factors = {}
	divisor = 2

	while n > 1:
		if n % divisor == 0:
			if divisor not in factors:
				factors[divisor] = 1
			else:
				factors[divisor] += 1
			n = n // divisor
		else:
			divisor += 1
	return factors

'''
helper functions to calculate opt and opt prime only :D
'''
def getNStart(odd,startPowerIndex):
	t=odd%6
	if t==3:
		raise ValueError("t3 has no opt")
	if(t==1):
		nstart=2+(startPowerIndex*2)
	else:
		nstart=1+(startPowerIndex*2)
	return nstart

def getNStop(nstart,lengthForN):
	return nstart+ 2*lengthForN

def printNormal(val):
	print(val,end=', ')

def printPrimeOnly(val):
	prime_factors=primeFactors(val)
	if len(prime_factors)==1:
		first_key, first_value = next(iter(prime_factors.items()))
		print("({},{})".format(first_key,first_value))

def calculateValue(odd, n, startPowerIndex):
	return (2**n * odd - 1) // 3
  
def process_numbers(odd, startPowerIndex, lengthForN, printer_function):
	nstart = getNStart(odd, startPowerIndex)
	nstop = getNStop(nstart, lengthForN)
	
	for n in range(nstart, nstop, 2):
		val = calculateValue(odd, n, startPowerIndex)
		printer_function(val)

def prime_OPT_only(odd, startPowerIndex=0, lengthForN=10):
	process_numbers(odd, startPowerIndex, lengthForN, printPrimeOnly)

def opt(odd, startPowerIndex=0, lengthForN=100):
	process_numbers(odd, startPowerIndex, lengthForN, printNormal)
 

'''
print sequnce for each number from-> to range
'''
def forRangePrintSequences(a,b):
	for number in range(a,b):
		printCollatzSequence(number)

'''
print sequnce for each number in array
'''
def foreachPrintSequences(arr):
	for number in arr:
		printCollatzSequence(number)



def getDifferences(numbers):
    return [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

def summationFormat(point):
	odd=point[0]
	t=odd%6
	n=point[1]
	if t==1:
		x1=(odd-1)//6
		print('{}*2^{}+'.format(x1,n+1),'{}'.format((2**n -1)//3))
	else:
		x5=(odd-5)//6
		print('{}*2^{}+'.format(x5,n+1),'2^{}+{}'.format(n,(2**(n+1) -1)//3))
