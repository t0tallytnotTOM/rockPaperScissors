import random
opt = {1:'rock', 2:'paper', 3:'scissors'}

usIn = input('Please select your option: 1 for rock, 2 for paper, 3 for scissors or select q to quit')
while usIn != 'q':
    usIn = int(usIn)
    winner = False
    usOp = opt[usIn]
    pcOp = opt[random.randint(1, 3)]
    if usOp == pcOp:
        print('You both chose ' + usOp + ', try again')
        usIn = input('Please select your option: 1 for rock, 2 for paper, 3 for scissors or select q to quit')
        continue
    elif usOp == 'rock' and pcOp == 'scissors':
        winner = True
    elif usOp == 'paper' and pcOp == 'rock':
        winner = True
    elif usOp == 'scissors' and pcOp == 'paper':
        winner = True

    if winner:
        again = input('WINNER (' + usOp + ' trumps ' + pcOp + '), do you want to play again? y/n')
        if again == 'y':
            usIn = input('Please select your option: 1 for rock, 2 for paper, 3 for scissors or select q to quit')
            continue
        else:
            break
    else:
        again = input('LOSER (' + pcOp + ' trumps ' + usOp + '), do you want to play again? y/n')
        if again == 'y':
            usIn = input('Please select your option: 1 for rock, 2 for paper, 3 for scissors or select q to quit')
            continue
        else:
            break

print('\n---Thanks for playing---')