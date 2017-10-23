#Emily Murphy
#2017-10-23
#warmUp11.py - determine if number is prime

def prime(num):
    if num%num == 0 and num%1 == num:
        return 'True'
    else:
        return 'False'

print(prime(10))