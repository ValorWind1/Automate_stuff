"""

tic tac toc game made by dictionary
"""
b = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def The_board(board):
    """
    We are calling the key in dict for bottom ones
    """
    print(board["top-L"] + "|" + board ["top-M"] + "|" + board["top-R"])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = "X"
for i in range(9):
    The_board(b)
    print("Turn for: " + turn + ". move on which space ? ")
    move = input()
    b[move] = turn                  # You named the place mid-L , top-M etc ... to play .
    if turn == "X":
        turn = "O"
    else:
        turn ="X"
The_board(b)