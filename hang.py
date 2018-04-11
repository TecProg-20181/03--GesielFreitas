import random
import string

WORDLIST_FILENAME = "palavras.txt"

def loadWords():
    """
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
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

class Hangman:
#def hangman(secretWord):

    _guesses = 8
    _lettersGuessed = []
    _secretWord = ''

    def getSecretWord(self, secretWord):
        self._secretWord = secretWord

    #def menu():
    def gameOver(self):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self._secretWord), ' letters long.'
        print '-------------'

        while  isWordGuessed(self._secretWord, self._lettersGuessed) == False and self._guesses >0:
            print 'You have ', self._guesses, 'guesses left.'

            available = getAvailableLetters()
            for letter in available:
                if letter in self._lettersGuessed:
                    available = available.replace(letter, '')

            print 'Available letters', available
            letter = raw_input('Please guess a letter: ')
            if letter in self._lettersGuessed:

                guessed = getGuessedWord()
                for letter in self._secretWord:
                    if letter in self._lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Oops! You have already guessed that letter: ', guessed
            elif letter in self._secretWord:
                self._lettersGuessed.append(letter)

                guessed = getGuessedWord()
                for letter in self._secretWord:
                    if letter in self._lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Good Guess: ', guessed
            else:
                self._guesses -=1
                self._lettersGuessed.append(letter)

                guessed = getGuessedWord()
                for letter in self._secretWord:
                    if letter in self._lettersGuessed:
                        guessed += letter
                    else:
                        guessed += '_ '

                print 'Oops! That letter is not in my word: ',  guessed
            print '------------'

        
        if isWordGuessed(self._secretWord, self._lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', _secretWord, '.'




secretWord = loadWords().lower()
hangman = Hangman()
hangman.getSecretWord(secretWord)
hangman.gameOver()
