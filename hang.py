import random
import string
import warnings

warnings.simplefilter('error')

WORDLIST_FILENAME = "palavras.txt"



class Hangman:

    __guesses = 8
    __lettersGuessed = []
    __secretWord = ''


    def _getLetter(self):
        
        letter = raw_input('Please guess a letter: ')

        # garanted only letter

        while len(letter) > 1 or letter.isdigit() == True:
            letter = raw_input('Please guess a only letter: ')

        return letter    
          

    def _checkLetterInLettesGuessed(self, letter):

        if letter in self.__lettersGuessed:
            guessed = self._getGuessedWord()
            for letter in self.__secretWord:
                if letter in self.__lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        else:
            pass

            
    def _checkLetterInSecretWord(self, letter):
        
        self.__lettersGuessed.append(letter)
        guessed = self._getGuessedWord()
        for letter in self.__secretWord:
            if letter in self.__lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        print 'Good Guess: ', guessed  

    def _letterNotInSecretWord(self, letter):
        
        self.__guesses -=1

        self.__lettersGuessed.append(letter)

        guessed = self._getGuessedWord()
        for letter in self.__secretWord:
            if letter in self.__lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        print 'Oops! That letter is not in my word: ',  guessed
    def _menuStart(self):
        
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.__secretWord), ' letters long and', self._letterDiferrent(),' different letters'
        print '-------------'   

    def game(self):
        self._loadWords()
        self._menuStart()

        while  self._isWordGuessed(self.__secretWord, self.__lettersGuessed) == False and self.__guesses >0:
            print 'You have ', self.__guesses, 'guesses left'

            available = self._getAvailableLetters()

            for letter in available:
                if letter in self.__lettersGuessed:
                    available = available.replace(letter, '')

            print 'Available letters', available
            
            letter = self._getLetter()

            self._checkLetterInLettesGuessed(letter)
                

            if letter in self.__secretWord:
                self._checkLetterInSecretWord(letter)
                
            else:
                self._letterNotInSecretWord(letter)
            print '------------'

        
        if self._isWordGuessed(self.__secretWord, self.__lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', self.__secretWord, '.'

    def _loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        
        try:
            # inFile: file
            inFile = open(WORDLIST_FILENAME, 'r', 0)

        except FileNotFoud:
            print("This file", self.wordlist_filename, "not exist in currency directory!")
            sys.exit(0)   
        
        # line: string
        line = inFile.readline()
        
        # wordlist: list of strings
        wordlist = string.split(line)
        print "  ", len(wordlist), "words loaded."

        self.__secretWord = random.choice(wordlist)
        


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

    def _letterDiferrent(self):
        letterDiferrent = self.__secretWord
        total = 0
        for letter in letterDiferrent:
            if letter in letterDiferrent:
                letterDiferrent = letterDiferrent.replace(letter, '')    
                total += 1
        return total        

hangman = Hangman()
hangman.game()
