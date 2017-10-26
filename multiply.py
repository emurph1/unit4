#Emily Murphy
#2017-10-26
#multiply.py - teach kids how to multiply

from random import randint

numCorrect = 0
def encourage():
    if numCorrect == 5:
        num= randint(1,4)
        if num == 1:
            print('Great job!')
        elif num == 2:
            print('Keep going!')
        elif num == 3:
            print('You are a math wizard!')
        elif num == 4:
            print('Watch out world, here comes the next great multiplier!')
    
while True:
    num1 = randint(1,12)
    num2 = randint(1,12)
    question = 'What is ' + str(num1) + ' * ' + str(num2) + '?'
    answer = int(input(question + ' '))
    if num1 * num2 == answer:
        numCorrect += 1
        if numCorrect == 5:
            numCorrect = 0
            encourage()
    else: 
        print('Incorrect. Try again.')

