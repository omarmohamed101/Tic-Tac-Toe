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
    if terminal(board):
        return X

    x_count = 0
    for row in board:
        x_count += row.count(X)
        x_count -= row.count(O)
    return X if x_count == 0 else O


def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    res = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.add((i, j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action is None:
        print(action)
        raise Exception('invalid action')

    fake_board = copy.deepcopy(board)

    # unpack the coordinates to perform the action
    i = action[0]
    j = action[1]

    if player(fake_board) == X:
        fake_board[i][j] = X
    else:
        fake_board[i][j] = O

    return fake_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):
        if utility(board) == 1:
            return X
        elif utility(board) == -1:
            return O

    # if the game in progress or it ended a tie
    if not is_full(board) or utility(board) == 0:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    transpose = [[row[i] for row in board] for i in range(3)]

    for row in board:
        if row.count(X) == 3:
            return True
        elif row.count(O) == 3:
            return True

    # check the cols in the board
    for row in transpose:
        if row.count(X) == 3:
            return True
        elif row.count(O) == 3:
            return True

    # check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == X:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return True

    if board[0][2] == board[1][1] == board[2][0] == X:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return True

    if is_full(board) and utility(board) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    transpose = [[row[i] for row in board] for i in range(3)]

    for row in board:
        if row.count(X) == 3:
            return 1
        elif row.count(O) == 3:
            return -1

    # check the cols in the board
    for row in transpose:
        if row.count(X) == 3:
            return 1
        elif row.count(O) == 3:
            return -1

    # check the diagonals
    if board[0][0] == board[1][1] == board[2][2] == X:
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return -1

    if board[0][2] == board[1][1] == board[2][0] == X:
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == "X":

        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value == 1:
                return action

            # keep track the zero if there is no ones to return it in the loop end
            if move_value > -1:
                return action

    if player(board) == "O":

        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value == -1:
                return action

            if move_value < 1:
                return action


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
