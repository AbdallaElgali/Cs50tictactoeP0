"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcounter = 0
    ocounter = 0  # Counts the number of X's and O's seen respectively



    for row in board:
        for cell in row:
            if cell == X:
                xcounter += 1
            elif cell == O:
                ocounter += 1

    if xcounter > ocounter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # loop through the board
    action_set = set()


    for row in range(len(board)):
        for cell in range(len(board[0])):
            if board[row][cell] == EMPTY:
                action_set.add((row, cell))

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid move!!")

    new_board = copy.deepcopy(board)

    row, cell = action

    play = player(board)
    new_board[row][cell] = play


    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Winning Conditions, 1. X or O in each of the rows, 2. 3 Xs or Os in one row




    # row condition
    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O

    # For column win
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O

    # diagonal condition
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    else:
        return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    Empty_counter = 0


    for row in board:
        if EMPTY in row:
            Empty_counter += 1
    if Empty_counter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    who_won = winner(board)
    if who_won == X:
        return 1
    elif who_won == O:
        return -1
    elif who_won is None and terminal(board) is True:
        return 0

def max_value(board):

    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):

    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    playerr = player(board)

    if terminal(board):
        return None
    elif playerr == X:
        action_list = []
        # Considering X to be in the Max Player
        for action in actions(board):
            result_board = result(board, action)
            action_list.append([min_value(result_board), action])
        action_list.sort(key=lambda x: x[0], reverse=True)

        return action_list[0][1]

    elif playerr == O:
        action_list = []
        # Considering O to be in the Max Player
        for action in actions(board):
            result_board = result(board, action)
            action_list.append([max_value(result_board), action])
        action_list.sort(key=lambda x: x[0])

        return action_list[0][1]




