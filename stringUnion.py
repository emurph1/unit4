#Emily Murphy
#2017-10-20
#stringUnion.py -two strings and returns a string of each letter


def stringUnion(word1, word2):
    for ch in word1:
        if ch in word1 == word2:
            return str(ch)
        
stringUnion('Mississippi', 'Pennslyvania')
