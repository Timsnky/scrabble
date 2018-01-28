from ps4a import *
import time
HAND_SIZE=10
n=HAND_SIZE

def compChooseWord(hand, wordList):

    value=0
    word=''
    for word1 in wordList:
        word4=''
        Sum=0
        word2=list(word1)
        hand1=[]
        for letter in hand.keys():
            for j in range(hand[letter]):
                hand1.append(letter)
        word3=word2[:]
        for e in word3:
            if e in hand1:
                word2.remove(e)
                hand1.remove(e)
        if len(word2)==0:
            Sum=getWordScore(word1,n)
            word4=word4+word1
            if value<Sum:
                value=Sum
                word=word4
            else:
                value=value
                word=word
    if len(word)!=0:
        return word
    if len(word)==0:
        return None

def compPlayHand(hand, wordList):

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
            word=compChooseWord(hand1,wordList)
            if word==None:
                print('Goodbye! Total score: '+str(Total)+' points')
                print
                break
            else:
                Total=Total+(getWordScore(word,n))
                print('"'+word+'" earned '+str(getWordScore(word,n))+' points')
                hand1=updateHand(hand1,word)
                hand2=[]
                for letter in hand1.keys():
                    for j in range(hand1[letter]):
                        hand2.append(letter)
                print
    else:
        print('Run out of letters. Total score: '+str(Total)+' points')
        print
    return Total
    
def playGame(wordList):
    
    n=HAND_SIZE
    for i in range(1000):
        prompt=str(raw_input('Enter n to deal a new hand, r to replay last hand, or e to end game: '))
        if prompt=='n':
            prompt2=str(raw_input('Who`s turn to play? Enter c for computer and u for player: '))
            print
            if prompt2=='u':
                hand=dealHand(HAND_SIZE)
                hand2=hand.copy()
                playHand(hand, wordList, n) 
                hand=hand2.copy()
            if prompt2=='c':
                hand=dealHand(HAND_SIZE)
                hand2=hand.copy()
                compPlayHand(hand,wordList)
                hand=hand2.copy()
        elif prompt=='r':
            if i==0:
                print('You have not played a hand yet. Please play a new hand first!')
                print
            else:
                hand=hand2.copy()
                if prompt2=='c':
                    print
                    compPlayHand(hand,wordList)                   
                if prompt2=='u':
                    print
                    playHand(hand, wordList, n)
                    
        elif prompt=='e':
            break
        else:
            print('You have entered an invalid input: ')
            print


if __name__ == '__main__':
    wordList = loadWords()
    n=HAND_SIZE
    hand=dealHand(HAND_SIZE)
    playGame(wordList)
    



