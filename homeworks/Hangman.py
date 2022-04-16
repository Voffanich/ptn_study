class Hangman():
    
    def __init__(self, err_number):
        
        self.__err_number = err_number
        self.guessed_letters = []
        
    def generate_word(self) -> str:
        
        import random
        
        self.__vocab_list = []
        self.__vocab_file = open('WordsStockRus.txt', 'r', encoding='utf-8')
        
        while True:
            
            line = self.__vocab_file.readline()
            
            if not line:
                break
            
            self.__vocab_list.append(line.replace('\n', ''))
        
        self.__vocab_file.close()
        
        self.word = list(self.__vocab_list[random.randint(0, len(self.__vocab_list))])
        self.current_state = list("*" * (len(self.word)))
        
        self.word_s = ''
        
        for letter in self.word:
            self.word_s += str(letter)
        
        return self.word_s

    def show_current_state(self):
        
        self.current_state_s = ''
        
        for letter in self.current_state:
            self.current_state_s += str(letter)
        
        return self.current_state_s
    
    def guess(self, guess_letter):
        
        self.guessed_letters.append(guess_letter)                 # список названных пользователем букв
        
        if len(guess_letter) > 1 or guess_letter not in "абвгдеёжзиклмнопрстуфхцчшщъыьэюя":
            
            return "Please, provide one Russian letter!"
        
        if guess_letter in self.word:
            
            for i in range(len(self.word)):
                
                if self.word[i] == guess_letter:
                    
                    self.current_state[i] = guess_letter
                    
            self.show_current_state
                
            return True
        
        else:
            
            self.__err_number -= 1
            
            return False
        
    def show_error_left(self):
            
        return self.__err_number
    
    def check_win(self):
        
        if '*' in self.show_current_state() and len(self.show_current_state()) > 0:
            return False
        else:
            return True
        
    def show_used_letters(self):
        
        return self.guessed_letters
    
    
g = Hangman(3)

g.generate_word()
print(f'Let\'s begin! You have to guess the word of {len(g.show_current_state())} letters.')
print(g.show_current_state())
guess = input('Please, provide the first letter you think is in the word: ')

while not g.check_win():
    gue = g.guess(guess)
    if  gue == True:
        print(f'Good job! Your guess is right! Have a look at it\'s place in the word:')
        print(g.show_current_state())
        if g.check_win():
            print(f'Congratulations, you won! The word is "{g.word_s}"')
            break
    elif gue != True and gue != False:
        print(gue)
        guess = input('')
        continue
    else:
        print(f'Not this time) No "{guess}" in this word. The number of wrong guesses left is {g.show_error_left()}')
        print(g.show_current_state())
    
    if g.show_error_left() < 1:        
        print(f'You have no more tries. You lost! The word is "{g.word_s}"')
        break
    
    print(f'You\'ve already used letters {g.show_used_letters()}')
    guess = input('Please, provide next letter you think is in the word: ')
        