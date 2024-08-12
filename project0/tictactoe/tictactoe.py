"""
Tic Tac Toe Player
"""
import copy
import math


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
    flag = 0
    for i in {0,1,2}:
        for j in {0,1,2}:
            if board[i][j] != EMPTY:
                flag = 1

    if flag:
        countX = 0
        countO = 0
        for i in {0,1,2}:
            for j in {0,1,2}:
                if board[i][j] == X:
                    countX = countX + 1
                elif board[i][j] == O:
                    countO = countO + 1

        if countX == countO:
            return X
        else:
            return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    for i in {0,1,2}:
        for j in {0,1,2}:
            if board[i][j] == EMPTY:
                res.add((i,j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY or i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception

    newBoard = copy.deepcopy(board)
    i,j = action
    if player(board) == X:
        newBoard[i][j] = X
    else:
        newBoard[i][j] = O
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == X) or \
                (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == X) or \
                (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == X) or \
                (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == X) or \
                (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == X) or \
                (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == X) or \
                (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == X) or \
                (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == X):
            return X
        if(board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == O) or \
                (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == O) or \
                (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == O) or \
                (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == O) or \
                (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == O) or \
                (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == O) or \
                (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == O) or \
                (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == O):
            return O
        return None
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != EMPTY) or \
        (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != EMPTY) or \
        (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != EMPTY) or \
        (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != EMPTY) or \
        (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != EMPTY) or \
        (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != EMPTY) or \
        (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY) or \
        (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY):
        return True
    flag = 0
    for i in {0,1,2}:
        for j in {0,1,2}:
            if board[i][j]==EMPTY:
                return False
    return True





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0



# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     if terminal(board):
#         return None
#     if player(board) == X:
#         action, _ = MaxValue(board)
#     else:
#         action, _ = MinValue(board)
#     return action
#
#
#
# def MaxValue(board):
#     v = float('-inf')
#     actionChosen = None
#
#     if terminal(board):
#         return None, utility(board)
#
#     for action in actions(board):
#         _, minValue = MinValue(result(board,action))
#         if minValue > v:
#             v = minValue
#             actionChosen = action
#     return actionChosen,v
#
# def MinValue(board):
#     v = float('inf')
#     actionChosen = None
#
#     if terminal(board):
#         return None, utility(board)
#
#     for action in actions(board):
#         _, maxValue = MaxValue(result(board,action))
#         if maxValue < v:
#             v = maxValue
#             actionChosen = action
#     return actionChosen,v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        action, _ = MaxValue(board, float('-inf'), float('inf'))
    else:
        action, _ = MinValue(board, float('-inf'), float('inf'))
    return action



def MaxValue(board, alpha, beta):
    v = float('-inf')
    actionChosen = None

    if terminal(board):
        return None, utility(board)

    for action in actions(board):
        _, minValue = MinValue(result(board,action),alpha, beta)
        if minValue > v:
            v = minValue
            actionChosen = action
        alpha = max(alpha,v)
        if alpha >= beta:
            break
    return actionChosen,v

def MinValue(board, alpha, beta):
    v = float('inf')
    actionChosen = None

    if terminal(board):
        return None, utility(board)

    for action in actions(board):
        _, maxValue = MaxValue(result(board,action),alpha, beta)
        if maxValue < v:
            v = maxValue
            actionChosen = action
        beta = min(beta,v)
        if alpha > beta:
            break
    return actionChosen,v