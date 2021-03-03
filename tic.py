sq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def board():
    print('\n\tTic Tac Toe')
    print('Player 1 (X) - Player 2 (0)')
    print('\t   |   |   ')
    print('\t',sq[1],'|',sq[2],'|',sq[3])
    print('\t___|___|___')
    print('\t   |   |   ')
    print('\t',sq[4],'|',sq[5],'|',sq[6])
    print('\t___|___|___')
    print('\t   |   |   ')
    print('\t',sq[7],'|',sq[8],'|',sq[9])
    print('\t   |   |   ')

def game_status():
    if sq[1] == sq[2] and sq[2] == sq[3]:
        return 1
    elif sq[4] == sq[5] and sq[5] == sq[6]:
        return 1
    elif sq[7] == sq[8] and sq[8] == sq[9]:
        return 1
    elif sq[1] == sq[4] and sq[4] == sq[7]:
        return 1
    elif sq[2] == sq[5] and sq[5] == sq[8]:
        return 1
    elif sq[3] == sq[6] and sq[6] == sq[9]:
        return 1
    elif sq[1] == sq[5] and sq[5] == sq[9]:
        return 1
    elif sq[3] == sq[5] and sq[5] == sq[7]:
        return 1
    elif sq[1] != 1 and sq[2] != 2 and sq[3] != 3 and sq[4] != 4 and sq[5] != 5 and sq[6] != 6 and sq[7] != 7 and sq[8] != 8 and sq[9] != 9:
        return 0
    else:
        return -1
    
player = 1
status = -1
    
while status == -1:
    board()
    if player % 2 == 1:
        player = 1
    else:
        player = 2
    print('\nPlayer', player)
    choice = int(input('Enter a number: '))
    if player == 1:
        mark = 'X'
    else:
        mark = '0'
    
    if choice == 1 and sq[1] == 1:
        sq[1] = mark
    elif choice == 2 and sq[2] == 2:
        sq[2] = mark
    elif choice == 3 and sq[3] == 3:
        sq[3] = mark
    elif choice == 4 and sq[4] == 4:
        sq[4] = mark
    elif choice == 5 and sq[5] == 5:
        sq[5] = mark
    elif choice == 6 and sq[6] == 6:
        sq[6] = mark
    elif choice == 7 and sq[7] == 7:
        sq[7] = mark
    elif choice == 8 and sq[8] == 8:
        sq[8] = mark
    elif choice == 9 and sq[9] == 9:
        sq[9] = mark
    else:
        print('Invalid move')
        player -= 1
    status = game_status()
    player += 1
    
print("RESULT")
if status == 1:
    board()
    print('Player', player-1, 'win')
else:
    print('Game draw')
