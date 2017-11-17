'''given an array of words u have to tell all the anagrams of the word'''
class Word(object):
    def __init__(self,string,index):
        self.string = string
        self.index = index

def createDupArray(string,size):
    dupArray = []
    #one by one copy words from the given wordArray
    for i in range(size):
        dupArray.append(Word(string[i],i))

    return dupArray

#Given a list of words in wordArr[]
def printAnagramsTogether(wordArr, size):
    #create a copy of all words present in wordArr
    dupArray = createDupArray(wordArr,size)
    #iterate through all the words in dupArray and sort individual words
    for i in range(size):
        dupArray[i].string = ''.join(sorted(dupArray[i].string))

    dupArray = sorted(dupArray, key=lambda k: k.string)

    for word in dupArray:
        print wordArr[word.index],

wordArr = ["cat","dog", "tac", "god", "act"]
size = len(wordArr)
printAnagramsTogether(wordArr, size)
