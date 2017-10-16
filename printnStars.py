#Emily Murphy
#2017-10-16
#printnStars.py - stars

def stars(rows):
    for i in range(rows):
    print(' '*(rows-i-1) + '*'*(2*i+1))
    
stars(6)