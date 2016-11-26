class Board():

    index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    dictionary = dict(zip(index, range(len(index))))

    def __init__(self):
        self.curr = [['*' for x in range(9)] for y in range(9)]
        self.top = "  "
        for x in range(len(Board.index)):
            self.top += Board.index[x] + " "
            if (x + 1) % 3 == 0:
                self.top += "  "

    def print_board(self):
        print(self.top)
        for i in range(len(self.curr)):
            line = Board.index[i] + " "
            for j in range(len(self.curr[i])):
                line += self.curr[i][j] + " "
                if (j + 1) % 3 == 0 and j < 8:
                    line += "| "
            print(line)
            if (i + 1) % 3 == 0 and i < 8:
                print("  " + "-" * 21)
        print("\n")

    def change_board(self, x, y, value):
        x = Board.dictionary[x]
        y = Board.dictionary[y]
        self.curr[x][y] = str(value)


def main():
    print("idk")
    b = Board()
    b.print_board()
    b.change_board('A', 'C', 4)
    b.print_board()

if __name__ == "__main__":
    main()

