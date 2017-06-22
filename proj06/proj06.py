# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
#def word1():




def hangman():
    print "Let's play hangman!"
    guesses=6
    userword = raw_input("Do you want to choose a word for your opponent to guess?")
    if userword == "Yes" or userword == "yes" or userword == "yup" or userword == "Yup" or userword == "YUP" or userword == "Hai" or userword == "definetly" or userword == "of course!" or userword == "TOTALLY" or userword == "Yes" or userword == "YES" or userword == "yeah" or userword == "Yeah" or userword == "YEAH" or userword == "Yep" or userword == "yep" or userword == "YEP" or userword == "totally" or userword == "sure" or userword == "Totally" or userword == "sure" or userword == "Sure" or userword == "maybe" or userword == "Maybe" or userword == " yes" or userword == " yeah" or userword == " Yes" or userword == " y" or userword == "y" or userword == "Y" or userword == " yeah" or userword == " Y":
        word = raw_input("Enter a word: ")
        x = raw_input("Enter * to show you're ready")

        theList = []
        for letter in word:
            theList.append(letter)
        #     x = 0
        #
        #     for LETTER in theList:
        #         theList[x] = "*"
        #         x = x + 1


    else:
        word = choose_word(wordlist)
        theList = []
        for letter in word:
            theList.append(letter)
    print "You will recieve 6 wrong guesses before I name you a failure."
    length = len(word)
    #print word
    print "The word you are trying to guess happens to be", length, "letters long."

    blanklist = []
    for letter in word:
        blanklist.append('_')
        guesslist = []
    while guesses>0:
        print " ".join(blanklist)
        g = raw_input ("Guess a letter ")
        a = -1
        b = -1
        c = True
        if g == word:
            print "You got it correct."
            break
            newgame = raw_input("Do you want to play again? *evil face*")
            while newgame == "Yes" or newgame == "yes" or newgame == "yup" or newgame == "Yup" or newgame == "YUP" or newgame == "Hai" or newgame == "definetly" or newgame == "of course!" or newgame == "TOTALLY" or newgame == "Yes" or newgame == "YES" or newgame == "yeah" or newgame == "Yeah" or newgame == "YEAH" or newgame == "Yep" or newgame == "yep" or newgame == "YEP" or newgame == "totally" or newgame == "sure" or newgame == "Totally" or newgame == "sure" or newgame == "Sure" or newgame == "maybe" or newgame == "Maybe" or newgame == " yes" or newgame == " yeah" or newgame == " Yes" or newgame == " y" or newgame == "y" or newgame == "Y" or newgame == " yeah" or newgame == " Y":
                hangman()
        for letters in theList:
                b=b+1
                a=a+1
                #print "a=",a,"and b=",b
                for letter in g:
                    if theList[a]== g:
                        #print "list",a,"=",g
                        print "You got a letter right."
                        blanklist[b]=g
                        c = False
                        #b=b+1
                        #a=a+1
                    elif b >= length-1 and c==True:
                        #print "b=",b,"and length=",length
                        guesses = guesses - 1
                        #print "guesses=",guesses
                        print "You got the letter wrong. You failed, but I'll give you",guesses,"guesses more before I truly name you a failure."
                        guesslist.append(g)
                        print "These are your incorrect guesses:"," ".join(guesslist)
                        if guesses == 0:
                            print "GAME OVER. I NAME YOU A FAILURE."


                    #else:
                        #a=a+1
                        #b=b+1


hangman()


newgame = raw_input("Do you want to play again? *evil face*")
while newgame == "Yes" or newgame=="yes" or newgame == "yup" or newgame == "Yup" or newgame == "YUP" or newgame == "Hai" or newgame == "definetly" or newgame == "of course!" or newgame == "TOTALLY" or newgame=="Yes" or newgame=="YES" or newgame=="yeah" or newgame=="Yeah" or newgame=="YEAH" or newgame=="Yep" or newgame=="yep" or newgame=="YEP" or newgame=="totally" or newgame=="sure" or newgame=="Totally" or newgame=="sure" or newgame=="Sure" or newgame=="maybe" or newgame=="Maybe" or newgame==" yes" or newgame==" yeah" or newgame==" Yes" or newgame==" y" or newgame=="y" or newgame=="Y" or newgame==" yeah" or newgame==" Y":

    hangman()



