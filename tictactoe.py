import os
import random
import time
cls = lambda : os.system('clear')
def box(pos):
    print('\n\n')
    print('\t\t   =============================')
    print('\t\t   ||       ||       ||       ||')
    print(f'\t\t   ||   {pos[0]}   ||   {pos[1]}   ||   {pos[2]}   ||')
    print('\t\t   ||       ||       ||       ||')
    print('\t\t   =============================')
    print('\t\t   ||       ||       ||       ||')
    print(f'\t\t   ||   {pos[3]}   ||   {pos[4]}   ||   {pos[5]}   ||')
    print('\t\t   ||       ||       ||       ||')
    print('\t\t   =============================')
    print('\t\t   ||       ||       ||       ||')
    print(f'\t\t   ||   {pos[6]}   ||   {pos[7]}   ||   {pos[8]}   ||')
    print('\t\t   ||       ||       ||       ||')
    print('\t\t   =============================\n\n')
def verify_locks(opo, v,pos):
    if pos[0] == pos[1] == pos[2] == v or pos[3] == pos[4] == pos[5] == v or pos[6] == pos[7] == pos[8] == v or pos[0] == pos[3] == pos[6] == v or pos[1] == pos[4] == pos[7] == v or pos[2] == pos[5] == pos[8] == v or pos[0] == pos[4] == pos[8] == v or pos[2] == pos[4] == pos[6] == v :
        print(f'\n\t\t   [ {opo} WIN\'S ]')
        return True
    else:
        print(f'\n\t\t   [ Game is Tie ]')

cls()
ppos = ['-' for x in range(9)]
choice = [1,2,3,4,5,6,7,8,9]
chance = 8
turn = 0
while chance >= 0:
    cls()
    print('\n\t\t*****[ Welcome to Tik-Tak-Tow ]*****')
    box(ppos)
    if chance % 2 == 0:
        turn = int(input('\n\n\t\t  Your turn : '))
        if turn not in choice:
            print('\n\t\tAlready selected ,try another.')
            time.sleep(2)
            continue
        ppos[turn-1] = 'X'
        if verify_locks('You', 'X', ppos) == True:
            break
        choice.remove(turn)
    else:
        turn = random.choice(choice)
        print(f'\n\n\t\t  Computer turn : {turn}')
        time.sleep(2)
        ppos[turn-1] = 'O'
        if verify_locks('Computer', 'O', ppos) == True:
            break
        choice.remove(turn)
    box(ppos)
    chance -= 1

print('\n\t\t      [ RESULT ]')
box(ppos)

print('\n\n\t\t*****[ Game Over ]*****')
