class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x):
        self.x = x

    def unset(self):
        self.x = -1

    def show(self):
        print(self.x, self.y)

    def conflicts(self, queen2):
        x = self.x
        y = self.y
        p = queen2.x
        q = queen2.y

        if x == -1 or p == -1:
            return False
        elif x == p or y == q or (x - y) == (p - q) or (x + y) == (p + q):
            return True
        else:
            return False


class Board:
    count = 0
    queens = []
    boards = []
    board1 = []

    def __init__(self):
        for i in range(8):
            q = Queen(-1, i)
            self.queens.append(q)

    def is_safe(self):
        for i in range(8):
            for j in range(8):
                if i != j:
                    if self.queens[i].conflicts(self.queens[j]):
                        return False

        return True

    def print_board(self):
        queens = []
        for queen in self.queens:
            queens.append(queen.x)

        """for x in range(8):
            for y in range(8):
                if queens[x] == y:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
        print("\n")"""
        # print(self.board1)
        self.boards.append(self.board1)

    def place_queen(self, y):
        if y >= 8:
            self.count += 1
            self.get_board()
            self.print_board()
            return False

        for i in range(8):
            self.queens[y].set(i)
            if self.is_safe() and self.place_queen(y + 1):
                print(0)
                return True
            else:
                self.queens[y].unset()

        return False

    def get_board(self):
        self.board1 = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]
        for queen in self.queens:
            self.board1[queen.x][queen.y] = 1


if __name__ == '__main__':
    board = Board()
    board.place_queen(0)
