#Emily Murphy
#2017-10-30
#quiz4.py -

def csia(word):
    i = 0
    while i <= 5:
        print(word)
        i += 1
csia('Computer Science is Awesome')

def average(num1, num2, num3):
    return (num1+num2+num3)/3

print(average(1,2,3))

def lastLetter(letter):
    for ch in letter:
        letter -= ch
        print(ch)
lastLetter('good')

def same(x,y):
    if x == y:
        return True
    else:
        return False
print(same('hi','hi'))