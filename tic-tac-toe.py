from colorama import Fore
import time
import random
start = time.time()
game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_'],]
def pri():
    for i in range(3):
        for j in range(3):
            if game[i][j] == '_':
                print(Fore.WHITE+game[i][j],end='  ')
            elif game[i][j] == 'x':
                print(Fore.MAGENTA + game[i][j], end='  ')
            elif game[i][j] == 'O':
                print(Fore.CYAN + game[i][j], end='  ')
        print()
def p1():
    while True:
        print('player 1')
        row=int(input('which row : '))
        col=int(input('which col : '))
        if 0<=row<=2 and 0<=col<=2:
            if game[row][col]=='_':
                game[row][col]='x'
                break
            else:
                print('cell is not impty _ , try again')
        else:
            print('index out of range , try again')
def p2():
    while True:
        print('player 2')
        row=int(input('which row : '))
        col=int(input('which col : '))
        if 0<=row<=2 and 0<=col<=2:
            if game[row][col]=='_':
                game[row][col]='O'
                break
            else:
                print('cell is not impty _ , try again')
        else:
            print('index out of range , try again')
def auto():
    while True:
        a=random.randint(0,2)
        b=random.randint(0,2)
        if game[a][b]=='_':
            game[a][b]='O'
            break
def win():
# radifi
    if game[0][0]=='x' and game[0][1]=='x' and game[0][2]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[1][0]=='x' and game[1][1]=='x' and game[1][2]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[2][0]=='x' and game[2][1]=='x' and game[2][2]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][0]=='O' and game[0][1]=='O' and game[0][2]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[1][0]=='O' and game[1][1]=='O' and game[1][2]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[2][0]=='O' and game[2][1]=='O' and game[2][2]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
# sotooni
    if game[0][0]=='x' and game[1][0]=='x' and game[2][0]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][1]=='x' and game[1][1]=='x' and game[2][1]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][2]=='x' and game[1][2]=='x' and game[2][2]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][0]=='O' and game[1][0]=='O' and game[2][0]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][1]=='O' and game[1][1]=='O' and game[2][1]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][2]=='O' and game[1][2]=='O' and game[2][2]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
# zabdari
    if game[0][0]=='x' and game[1][1]=='x' and game[2][2]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][2]=='x' and game[1][1]=='x' and game[2][0]=='x':
        print('player 1 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][0]=='O' and game[1][1]=='O' and game[2][2]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
    if game[0][2]=='O' and game[1][1]=='O' and game[2][0]=='O':
        print('player 2 is wins. ',"Run Time: " + str( time.time() - start ))
        exit()
# mosavi
    if game[0][0]!='_' and game[0][1]!='_' and game[0][2]!='_' and game[1][0]!='_' and game[1][1]!='_' and game[1][2]!='_'and game[2][0]!='_' and game[2][1]!='_' and game[2][2]!='_':
        print('no winer.',"Run Time: " + str( time.time() - start ))
        exit()
q=int(input("Enter 1 for single player, 2 for multiplayer: "))
if q==2:
    while True:
        pri()
        p1()
        pri()
        win()
        p2()
        win()
else:
    while True:
        pri()
        p1()
        pri()
        win()
        print('player 2')
        auto()
        win()