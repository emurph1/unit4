#Emily Murphy
#2017-10-26
#recursionDemo.py - recursive version of countdown function

def countdown(n):
    if n == 0:
        print('Boom!')
    else:
        print(n)
        countdown(n-1)
    
countdown(5)
