#Emily Murphy
#2017-10-20
#stringUnion.py -two strings and returns a string of each letter


def stringUnion(word1, word2):
    answer = ' '
    for ch in word1:
        if ch not in answer:
            answer += ch
    for ch in word2:
        if ch not in answer:
            answer += ch
    return answer
        
print(stringUnion('Mississippi', 'Pennslyvania'))