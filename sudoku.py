class Board():

    index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    dictionary = dict(zip(index, range(len(index))))
    values = set(range(1, 10))

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
        r = input("row? ").upper()
        while r not in Board.index:
            print("row must be a letter between A and I")
            r = input("row? ").upper()
        return r

    def validate_column(self):
        c = input("column? ").upper()
        while c not in Board.index:
            print("column must be a letter between A and I")
            c = input("column ").upper()
        return c

    def validate_value(self):
        v = input("value? ")
        while not (v.isdigit() and (1 <= int(v) <= 9)):
            print("column must be an integer between 1 and 9")
            v = input("value? ")
        return int(v)

    def check_win(self):
        return self.check_rows() and self.check_columns() and self.check_squares()

    def check_rows(self):
        for row in self.curr:
            if set(row) != Board.values:
                return False
        return True

    def check_columns(self):
        for j in range(len(self.curr[0])):
            column = []
            for i in range(len(self.curr)):
                column += [self.curr[i][j]]
            if set(column) != Board.values:
                return False
        return True

    def check_squares(self):
        for i in range(0, 9, 3):
            square = []
            for j in range(0, 9, 3):
                for k in range(j, j + 3):
                    square += [self.curr[i][k]]
            if set(square) != Board.values:
                return False
        return True

def main():
    b = Board()
    b.print_board()
    make = True
    while make:
        answer = input("make or start? ")
        if answer == "make" or answer == "m":
            r = b.validate_row()
            c = b.validate_column()
            v = b.validate_value()
            b.make_board(r, c, v)
            b.print_board()
        elif answer == "start" or answer == "s":
            make = False
        else:
            print("choose make or start")
    win = False
    while not win:
        answer = input("change or submit? ")
        if answer == "change" or answer == "c":
            r = b.validate_row()
            c = b.validate_column()
            v = b.validate_value()
            b.change_board(r, c, v)
            b.print_board()
        elif answer == "submit" or answer == "s":
            if b.check_win():
                win = True
            else:
                print("incorrect")
        else:
            print("choose change or submit")
    print("congrats, you won!")


if __name__ == "__main__":
    main()

