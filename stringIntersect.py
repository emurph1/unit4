#Emily Murphy
#2017-10-20
#stringIntersect.py -two strings and returns a string of each letter


def stringUnion(word1, word2):
    answer = ''
    answer2 = ''
    answer3 = ''
    for ch in word1:
        if ch not in answer:
            answer += ch
    for ch in word2:
        if ch not in answer2:
            answer2 += ch
    for ch in word1 and word2:
        if answer not in answer2:
            answer3 += ch
    return answer3
        
print(stringUnion('mississippi', 'pennslyvania'))
