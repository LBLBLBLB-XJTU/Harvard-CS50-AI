import sys

from project0.tictactoe.tictactoe import EMPTY, player, X, O, actions, result, terminal, winner, minimax


def main():
    state1 = [[X, O,O],
            [O, X, X],
            [X, O, O]]
    state2 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    state3 = [[EMPTY, X, O],
              [EMPTY, X, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
    state4 = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, X],
            [X, EMPTY, O]]
    state5  = [[EMPTY, O, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    res = minimax(state1)
    print(res)


if __name__ == "__main__":
    main()