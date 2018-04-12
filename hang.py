import random
import string

WORDLIST_FILENAME = "palavras.txt"



class Hangman:

    _guesses = 8
    _lettersGuessed = []
    _secretWord = ''


    def _getLetter(self):
        letter = raw_input('Please guess a letter: ')
        return letter

    def _checkLetterInLettesGuessed(self, letter):

        if letter in self._lettersGuessed:
            guessed = self._getGuessedWord()
            for letter in self._secretWord:
                if letter in self._lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        else:
            pass

            
    def _checkLetterInSecretWord(self, letter):
        
        self._lettersGuessed.append(letter)
        guessed = self._getGuessedWord()
        for letter in self._secretWord:
            if letter in self._lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        print 'Good Guess: ', guessed  

    def _letterNotInSecretWord(self, letter):
        
        self._guesses -=1
        self._lettersGuessed.append(letter)

        guessed = self._getGuessedWord()
        for letter in self._secretWord:
            if letter in self._lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        print 'Oops! That letter is not in my word: ',  guessed
    def _menuStart(self):
        
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self._secretWord), ' letters long.'
        print '-------------'   

    def game(self):
        self._loadWords()
        self._menuStart()

        while  self._isWordGuessed(self._secretWord, self._lettersGuessed) == False and self._guesses >0:
            print 'You have ', self._guesses, 'guesses left.'

            available = self._getAvailableLetters()

            for letter in available:
                if letter in self._lettersGuessed:
                    available = available.replace(letter, '')

            print 'Available letters', available
            
            letter = self._getLetter()

            self._checkLetterInLettesGuessed(letter)
                

            if letter in self._secretWord:
                self._checkLetterInSecretWord(letter)
                
            else:
                self._letterNotInSecretWord(letter)
            print '------------'

        
        if self._isWordGuessed(self._secretWord, self._lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', self._secretWord, '.'

    def _loadWords(self):
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
        self._secretWord = random.choice(wordlist)


    def _isWordGuessed(self, secretWord, lettersGuessed):
        secretLetters = []

        for letter in secretWord:
            if letter not in lettersGuessed:
                return False
            else:
                pass

        return True

    def _getGuessedWord(self):

        guessed = ''


        return guessed

    def _getAvailableLetters(self):

        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available        



hangman = Hangman()
hangman.game()
