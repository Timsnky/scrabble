
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():

    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def getWordScore(word, n):

    score=0
    word1=list(word)
    for e in word1:
        score = score+SCRABBLE_LETTER_VALUES[e]
    score=score*len(word1)
    if len(word)==n:
        score=score+50
    return score

def displayHand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              
    return('              ')            

def dealHand(n):

    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    
    word1=list(word)
    hand2=hand.copy()
    for e in word1:
        if e in hand2:
            hand2[e]=hand2.get(e)-1
    return hand2
    print(hand2)

def isValidWord(word, hand, wordList):

    word1=list(word)
    hand1=[]
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand1.append(letter)
    word2=word1[:]
    if word in wordList:
        for e in word2:
            if e in hand1:
                word1.remove(e)
                hand1.remove(e)
        if len(word1)==0:
            return True
    else:
        return False

def calculateHandlen(hand):
    
    length=0
    for e in hand:
        length=length+hand[e]
    return length



def playHand(hand, wordList, n):                

    Total=0
    hand1=hand.copy()
    for letter in hand1:
        hand2=[]
        for letter in hand.keys():
            for j in range(hand[letter]):
                hand2.append(letter)
    for i in range(len(hand2)):
        if len(hand2)!=0:
            print('Current Hand: '),displayHand(hand1)
            word=str(raw_input('Enter a word, or a "." to indicate that you are finished: ')) 
            dot='.'
            if word==dot:
                print('                               ')
                break
            else:
                Bin=isValidWord(word,hand,wordList)
                if Bin==True:
                    Total=Total+(getWordScore(word,n))
                    print('"'+word+'" earned '+str(getWordScore(word,n))+' points. Total: '+str(Total)+' points')
                    hand1=updateHand(hand1,word)
                    hand2=[]
                    for letter in hand1.keys():
                        for j in range(hand1[letter]):
                            hand2.append(letter)
                    print('                               ')
            if Bin==False:
                print('Invalid word,please try again.')
                print('                               ')
        else:
            print('Run out of letters. Total score: '+str(Total)+' points')
            break

def playGame(wordList):

        for i in range(100):
            i=1
            prompt=str(raw_input('Enter n to deal a new hand, r to replay last hand, or e to end game: '))
            if prompt=='n':
                hand=dealHand(HAND_SIZE)
                freq = {}
                for x in hand:
                    freq[x] = freq.get(x,0) + 1
                hand=freq
                n=HAND_SIZE
                playHand(hand, wordList, n)
                i=i+1
            elif prompt=='r':
                if i!=1:
                    hand=hand
                    n=HAND_SIZE
                    playHand(hand, wordList, n)
                else:
                    print('You have not played a hand yet. Please play a new hand first!')
                    print('                               ')
            elif prompt=='e':
                break
            else:
                print('You have entered an invalid input: ')
        
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
