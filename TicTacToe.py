#for number 3 of the assignment
import math
import copy

class TicTacToe:
    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def display_board(self):
        for row in self.state:
            print(" | ".join(["X" if cell == 1 else "O" if cell == -1 else " " for cell in row]))
            print("-" * 9)

    def make_move(self, row, col, val):
        if 0 <= row < 3 and 0 <= col < 3 and self.state[row][col] == 0:
            self.state[row][col] = val
            return True
        return False

    def is_full(self):
        for row in self.state:
            if 0 in row:
                return False
        return True

    def terminal_node(self):
        for i in range(3):
            if self.state[i][0] == self.state[i][1] == self.state[i][2] != 0:
                return True, self.state[i][0]

            if self.state[0][i] == self.state[1][i] == self.state[2][i] != 0:
                return True, self.state[0][i]

        if self.state[0][0] == self.state[1][1] == self.state[2][2] != 0:
            return True, self.state[0][0]

        if self.state[0][2] == self.state[1][1] == self.state[2][0] != 0:
            return True, self.state[0][2]

        if self.is_full():
            return True, 0

        return False, 0

    def expand_state(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    children.append((i, j))
        return children

    def minimax(self, depth, is_max_player):
        terminal, result = self.terminal_node()

        if terminal:
            if result == 1:
                return 10 - depth
            elif result == -1:
                return depth - 10
            else:
                return 0

        if is_max_player:
            max_eval = -math.inf
            for pos in self.expand_state():
                i, j = pos
                self.state[i][j] = 1
                eval = self.minimax(depth + 1, False)
                self.state[i][j] = 0
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for pos in self.expand_state():
                i, j = pos
                self.state[i][j] = -1
                eval = self.minimax(depth + 1, True)
                self.state[i][j] = 0
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        best_move = None
        best_eval = -math.inf
        for pos in self.expand_state():
            i, j = pos
            self.state[i][j] = 1
            eval = self.minimax(0, False)
            self.state[i][j] = 0
            if eval > best_eval:
                best_eval = eval
                best_move = pos
        return best_move


def main():
    game = TicTacToe()
    while True:
        game.display_board()

        # Human player's move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game.make_move(row, col, -1):
                    break
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Row and column must be between 0 and 2.")

        terminal, result = game.terminal_node()
        if terminal:
            game.display_board()
            if result == 0:
                print("It's a tie!")
            elif result == -1:
                print("You win!")
            else:
                print("AI wins!")
            break

        # AI's move
        ai_move = game.get_best_move()
        game.make_move(ai_move[0], ai_move[1], 1)

        terminal, result = game.terminal_node()
        if terminal:
            game.display_board()
            if result == 0:
                print("It's a tie!")
            elif result == -1:
                print("You win!")
            else:
                print("AI wins!")
            break


if __name__ == "__main__":
    main()