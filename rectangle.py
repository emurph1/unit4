#Emily Murphy
#2017-10-16
#rectangle.py - plug in length and width and it prints out perimeter and area

l = int(input('Enter length:'))
w = int(input('Enter area:'))

def area(l, w):
    print(l*w)
    
def per(l,w):
    print((l*2) + (w**2))
    
print('Area is', area(l,w))
print('Perimeter is', per(l,w))