#Emily Murphy
#2017-10-23
#warmUp11.py - determine if number is prime

def prime(num):
    i += 1
    while i <= num:
        num = num//i
        if num == 0 or num:
            return 'True'
        else:
            return 'False'

print(prime(17))