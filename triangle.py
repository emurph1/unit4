#Emily Murphy
#2017-10-25
#triangle.py - input vertices finds area

from math import sqrt

x1 = int(input('x1:'))
x2 = int(input('x2:'))
x3 = int(input('x3:'))
y1 = int(input('y1:'))
y2 = int(input('y2:'))
y3 = int(input('y3:'))

def distance(x1,y1,x2,y2):
    return (sqrt(((x2-x1)**2) +((y2-y1)**2)))
    

a = distance(x1,y1,x2,y2)
b = distance(x1, y1,x3,y3)
c = distance(x2,y2,x3,y3)
s = .5*(a + b + c)
area = sqrt(s(s-a)(s-b)(s-c))
print(area)


    

