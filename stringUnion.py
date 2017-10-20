#Emily Murphy
#2017-10-20
#stringUnion.py -two strings and returns a string of each letter


def stringUnion(word1, word2):
    answer = ' '
    for ch in word1:
        answer += ch
    for ch in word2:
        if ch in word2 == answer:
            print(answer)
        
stringUnion('Mississippi', 'Pennslyvania')
