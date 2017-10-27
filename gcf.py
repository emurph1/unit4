#Emily Murphy
#2017-10-27
#gcf.py - Greatest common factor between two numbers

def gcf(num1,num2):
    x = min(num1,num2)
    for i in range(x,0,-1):
        if num1%i == 0 and num2%i == 0:
            return i
            
print(gcf(10,15))
        
        