import random
from os import system, name


def clean_window():
    #Windows
    if name == 'nt':
        _ = system('cls')  
    #Mac or Linux
    else:
        _ = system('clear')

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:
    def __init__(self, word):
        self.word = word
        self.wrong_letters = []
        self.chosen_letters = []
    
    def guess(self, letter):
        if letter in self.word and letter not in self.chosen_letters:
            self.chosen_letters.append(letter)
        
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
        
        else:
            return False
        return True
    

    def hangman_over(self):
        return self.hangman_won() or (len(self.wrong_letters) == 6)
    
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False
    
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.chosen_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn
    
    def game_status(self):
        print (board[len(self.wrong_letters)])
        print ('\nWord: ' + self.hide_word())
        print ('\nWrong Letters: ',) 
        
        for letter in self.wrong_letters:
            print (letter,) 
		
        print ()
        print ('Correct letter: ',)

        for letter in self.chosen_letters:
            print (letter,)
    
        print ()

def rand_word():
    words = ['fish', 'elephant', 'zebra', 'panther', 'ostrich']
    word = random.choice(words)  
    return word

def main():
	clean_window()

	game = Hangman(rand_word())

	while not game.hangman_over():
		game.game_status()
		user_input = input('\nDigit a letter: ')
		game.guess(user_input)

	game.game_status()	

	if game.hangman_won():
		print ('\nYou win!!')
	else:
		print ('\nGame over! You lost')
		print ('The word was ' + game.word)
		
if __name__ == "__main__":
	main()
