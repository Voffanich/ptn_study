from telnetlib import GA
from believer import Believer
from believer import GameStatus

file_path = 'Questions.csv'

game = Believer(2, file_path)
win = False

while not win:
    print('Here is the next question: ' + game.next_question())
    print("Do you think it's true or not? Type 'y' or 'n' as answer")
    answer = input().lower()
    
    while True:
        if answer == 'y':
            answer = "Yes"
            break
        elif answer == 'n':
            answer = "No"
            break
        else:
            answer = input("Please, provide answer as 'y' or 'n' only: ").lower()

    if game.check_answer(answer):
        print(f'You\'re absolutely right! {game.question_comment}' + '\n')
    else:
        print(f'Oops, that\'s not correct! The correct answer is {game.correct_answer}. {game.question_comment}')
        print(f'You\'ve got {game.err_left} errors left' + '\n')
    
    if game.game_status == GameStatus.WIN:
        print('Congratulations! You won. Good job!')
        break
    elif game.game_status == GameStatus.LOST:
        print('Unfortunately, you\'re out of tries. You lost! Maybe next time you\'ll be more lucky.')
        break
       
            