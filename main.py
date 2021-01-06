import random

a = 'Stone'
b = 'Paper'
c = 'Scissor'

score = 0
comscore = 0
x=True

while x:
    if score == 3:
        print('You win!!!')
        break
    if comscore == 3:
        print("I win!! , You lost !!!")
        break
    x = input('Press x to exit else any other key to continue : ')
    x = x.lower()
    if x == "x" :
        x = False
    else :
        d = random.choice((a, b, c))
        player = input('Please choose stone, paper , scissor : ')
        player = player.lower()
        if (d==a):
            print(d)
            if (player == 'stone'):
                print("Its an draw!!")
            if (player == 'paper'):
                print('You win!!')
                score+=1
            if (player == 'scissor'):
                print('I win!!!')
                comscore+=1

        if(d == b):
            print(d)
            if (player == 'stone'):
                print("I win !!!")
                comscore += 1
            if (player == 'paper'):
                print('Its a draw !!')
            if (player == 'scissor'):
                print('You win!!!')
                score += 1

        if(d == c):
            print(d)
            if (player == 'stone'):
                print("You win!!!!!")
                score += 1
            if (player == 'paper'):
                print('I win!!')
                comscore += 1
            if(player == "scissor"):
                print('Its a draw!!')
        print('Your score is :', str(score))
        print('My score is :', str(comscore))

