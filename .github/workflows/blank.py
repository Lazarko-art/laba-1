import random


class Sudoku:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else "." for num in row))

    def fill_board(self):
        for _ in range(20):  # Add 20 random clues
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
            while not self.is_valid(row, col, num) or self.board[row][col] != 0:
                row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
            self.board[row][col] = num

# Example usage
sudoku = Sudoku()
sudoku.fill_board()
print("Generated Sudoku Puzzle:")
sudoku.print_board()

if sudoku.solve():
    print("\nSolved Sudoku Puzzle:")
    sudoku.print_board()
else:
    print("No solution exists.")
