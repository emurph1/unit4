#Emily Murphy
#2017-10-27
#gcf.py - Greatest common factor between two numbers

def gcf(num1,num2):
    x = min(num1,num2)
    for i in range(x,0,-1):
        if num1%x == 0 and num2%x == 0:
            return x
            
print(gcf(10,15))
        
        