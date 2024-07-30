from random import randint

t = ['r', 'p', 's']

comp = t[randint(0, 2)]
player = False

name = input("enter your name: ")
print("type 'reset' to reset score")
playerScore = 0
compScore = 0


message = ""

def win():
    global playerScore
    playerScore += 1
    print(message)
    print('Computer = ', compScore, '\n', name, '=', playerScore)

def lose():
    global compScore
    compScore += 1
    print(message)
    print('Computer = ', compScore, '\n', name, '=', playerScore)

while player == False:
    player = input('Rock, Paper, Scissors?(r, p, s)')
    if player == comp:
        print('Tie!')
        print('Computer =', compScore)
        print(name, '=', playerScore)
    elif player == 'r':
        if comp == 'p':
            message = 'You lose!', 'Paper covers Rock'
            lose()
        else:
            message = 'You win!', 'Rock breaks Scissors'
            win()
    elif player == 'p':
        if comp == 'r':
            message = 'You win!', 'Paper covers Rock'
            win()
        else:
            message = 'You lose!', 'Scissors cut Paper'
            lose()
    elif player == 's':
        if comp == 'r':
            message = 'You lose!', 'Rock breaks Scissors'
            lose()
        else:
            message = 'You win!', 'Scissors cut Paper'
            win()
    elif player == 'reset':
        playerScore = 0
        compScore = 0
        print('The score has been reset!')
    else:
        print('Not a valid option. try again.')
    
    player = False
    comp = t[randint(0, 2)]
