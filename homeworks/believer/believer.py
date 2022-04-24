from enum import Enum
from xmlrpc.client import Boolean, boolean

class GameStatus(Enum):
    IN_PROGRESS = 0
    LOST = 1
    WIN = 2
    NOT_STARTED = 3
    
class Believer:
    
    def __init__(self, err_number: int = 2, file_path: str = ''):
        self.__err_number = err_number
        self.__game_status = GameStatus.NOT_STARTED
        self.__current_question = -1
        self.__file = open(file_path, 'r', encoding='utf-8')
        self.__questions = []
        
        while True:
            line = self.__file.readline()
            if not line:
                break
            self.__questions.append(line.replace('\n', '').split(';'))
            
        print(self.__questions)
             
    def next_question(self) -> str:
        if self.__game_status == GameStatus.NOT_STARTED:
            self.__game_status = GameStatus.IN_PROGRESS
        if self.__game_status == GameStatus.WIN:
            return "You've already won! No more questions" 
        
        self.__current_question += 1
        
        if self.__current_question <= len(self.__questions) - 1:
            next_question = self.__questions[self.__current_question][0]
        else:
            return 'There is no more questions in the game'
        
        return next_question
    
    def check_answer(self, answer: str = '') -> Boolean:
        #print(f'The answer for the {self.__current_question} question is {self.__questions[self.__current_question][1]} and the anwser by the client is {answer}')
        if answer == self.__questions[self.__current_question][1]:
            if self.__current_question == len(self.__questions) - 1:
                self.__game_status = GameStatus.WIN
                return True
            return True
        else:
            self.__err_number -= 1
            if self.__err_number < 1:
                self.__game_status = GameStatus.LOST
            return False
        
    @property
    def game_status(self):
        return self.__game_status
    
    @property
    def correct_answer(self) -> str:
        return self.__questions[self.__current_question][1]
    
    @property
    def err_left(self) -> int:
        return self.__err_number
    
    @property     
    def question_comment(self) -> str:
        return self.__questions[self.__current_question][2]
            
     
    

    
    
    
        
    