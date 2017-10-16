#Emily Murphy
#2017-10-16
#functionDemo.py - learn how to write functions

def hw():
    print('Hello, World!')

def bigger(num1, num2): #prints which number is bigger --> anything in parantheses are called arguements
    if num1 > num2:
        print(num1)
    else:
        print(num2)
        
def slope(x1, y1, x2, y2): #calculate slope
    print((y2-y1)/(x2-x1))
       
#hw()--actually runs the function 
#bigger(13,27) #test1
#bigger(-10,-15)
#bigger('B', 'C') #prints which is alphabetically first (num2) would have to be after num1 for it to print num2
slope(1,2,2,4)