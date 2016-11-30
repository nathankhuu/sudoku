class Board():

    index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    dictionary = dict(zip(index, range(len(index))))

    def __init__(self):
        self.curr = [['*' for x in range(9)] for y in range(9)]
        self.top = "  "
        self.starter = set()
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

    def change_board(self, r, c, v):
        if (r, c) not in self.starter:
            row = Board.dictionary[r]
            column = Board.dictionary[c]
            self.curr[row][column] = str(v)
        else:
            print("Cannot change initial values")

    def make_board(self, r, c, v):
        row = Board.dictionary[r]
        column = Board.dictionary[c]
        self.curr[row][column] = str(v)
        self.starter.add((r, c))

    def validate_row(self):
        r = input("row? ")
        while r not in Board.index:
            print("row must be a letter between A and I")
            r = input("row? ")
        return r

    def validate_column(self):
        c = input("column? ")
        while c not in Board.index:
            print("column must be a letter between A and I")
            c = input("column ")
        return c

    def validate_value(self):
        v = input("value? ")
        while not (v.isdigit() and (1 <= int(v) <= 9)):
            print("column must be an integer between 1 and 9")
            v = input("value? ")
        return v

def main():
    b = Board()
    b.print_board()
    make = True
    while make:
        answer = input("make or start? ")
        if answer == "make":
            r = b.validate_row()
            c = b.validate_column()
            v = b.validate_value()
            b.make_board(r, c, v)
            b.print_board()
        elif answer == "start":
            make = False
        else:
            print("choose make or start")
    b.print_board()

if __name__ == "__main__":
    main()

