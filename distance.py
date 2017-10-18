#Emily Murphy
#2017-10-18
#distance.py - find distance between two points

from math import sqrt

def distance(x1,y1,x2,y2):
    print(sqrt(((x2-x1)**2) +((y2-y1)**2)))

distance(3,4,-5,2)
