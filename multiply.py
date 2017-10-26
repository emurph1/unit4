#Emily Murphy
#2017-10-26
#multiply.py - teach kids how to multiply

from random import randint

numCorrect = 0
while True:
    num1 = randint(1,12)
    num2 = randint(1,12)
    question = 'What is ' + str(num1) + ' * ' + str(num2) + '?'
    answer = int(input(question))
    if num1 * num2 == answer:
        print('Correct')
        numCorrect += 1
    else: 
        print('Incorrect. Try again')

def encourage():
    if numcorrect == 5:
        numcorrect == 0
        print('You are doing great! Keep going')
