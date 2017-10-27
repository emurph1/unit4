#Emily Murphy
#2017-10-23
#warmUp11.py - determine if number is prime


def isPrime(num):
	for i in range(2,num):
		if num%i==0:
			return	False
		return	True
												
print(isPrime(10))	#test1
print(isPrime(11))	#test2
print(isPrime(12))	#test3
