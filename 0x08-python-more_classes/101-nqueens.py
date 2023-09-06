#!/usr/bin/python3
import sys

"""This module implements the nQueens algorithm"""


def main():
    """
    main - Entry point to the program
    """
    N = handle_errors()
    chessboard = initialize(N)
    solutions = generate_solutions(chessboard, 0, 0, [])
    for solution in solutions:
        print(solution)


def initialize(n):
    """Initializes the chessboard."""
    board = list()
    [board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in board]
    return board


def copy_board(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return board


def get_solution(board):
    """Returns the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def non_attacking_queens(board, row, col):
    """
    non_attacking_queens - is designed to mark the spots on a chessboard where non-attacking queens can no longer be placed, given the position of a queen that has just been placed on the board. This function essentially marks all the rows, columns, and diagonals that are under threat by the newly placed queen.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def generate_solutions(board, row, queens, solutions):
    """
    generate_solutions - generate all possible solutions
                        to the chessboard
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for i in range(len(board)):
        if board[row][i] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][i] = "Q"
            non_attacking_queens(tmp_board, row, i)
            solutions = generate_solutions(tmp_board, row + 1, queens + 1, solutions)

    return solutions


def handle_errors():
    """Handle errors from the command-line arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    return N


if __name__ == "__main__":
    """Entry point"""
    main()
