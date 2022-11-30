def in_boardboundary(col, row):
    print(type(col))
    print(type(row))
    if col[0] < 0 or col[0] > 7:
        return False
    if row[0] < 0 or row[0] > 7:
        return False
    return True


class Board:
    def __init__(self):
        self.board = {}
        self.empty()

    def empty(self):
        for col in "abcdefgh":
            for row in "12345678":
                self.board[col + row] = " "

    def set(self, pos, piece):
        if pos in self.board.keys():
            self.board[pos] = piece

    def draw(self):
        print("    a   b   c   d   e   f   g   h")
        print("  +---+---+---+---+---+---+---+---+")
        for row in "87654321":
            print(
                " {}| {} | {} | {} | {} | {} | {} | {} | {} |{}".format(
                    row,
                    self.board["a" + row],
                    self.board["b" + row],
                    self.board["c" + row],
                    self.board["d" + row],
                    self.board["e" + row],
                    self.board["f" + row],
                    self.board["g" + row],
                    self.board["h" + row],
                    row,
                )
            )
            print("  +---+---+---+---+---+---+---+---+")
        print("    a   b   c   d   e   f   g   h")


class Chess_Piece:
    def __init__(self, board, pos, color="white"):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())

    def get_index(self, pos):
        return ("abcdefgh".index(pos[0]), "12345678".index(pos[1]))

    def get_name(self):
        pass

    def moves(self, board):
        pass


class King(Chess_Piece):
    def get_name(self):
        return "K"

    def moves(self, board):
        col = "abcdefgh"
        row = "12345678"
        index_col = (self.position[0],)
        index_row = self.position[1]
        if in_boardboundary(index_col, index_row):
            pos = col[index_col[0]] + row[index_row]
            board.set(pos, "x")
        index_col = (self.position[0] + 1,)
        index_row = self.position[1]
        if in_boardboundary(index_col, index_row):
            pos = col[index_col[0]] + row[index_row]
            board.set(pos, "x")

        index_col = (self.position[0] + 1,)
        index_row = self.position[1] + 1
        pos = col[index_col[0]] + row[index_row]
        board.set(pos, "x")

        index_col = (self.position[0],)
        index_row = self.position[1] + 1
        pos = col[index_col[0]] + row[index_row]
        board.set(pos, "x")

        index_col = (self.position[0] - 1,)
        index_row = self.position[1] + 1
        pos = col[index_col[0]] + row[index_row]
        board.set(pos, "x")

        index_col = (self.position[0] - 1,)
        index_row = self.position[1]
        pos = col[index_col[0]] + row[index_row]
        board.set(pos, "x")

        index_col = (self.position[0] - 1,)
        index_row = self.position[1] - 1
        pos = col[index_col[0]] + row[index_row]
        board.set(pos, "x")

        index_col = (self.position[0],)
        index_row = self.position[1] - 1
        pos = col[index_col[0]] + row[index_row]
        board.set(pos, "x")

        index_col = (self.position[0] + 1,)
        index_row = self.position[1] - 1
        pos = col[index_col[0]] + row[index_row]
        board.set(pos, "x")


# class Pawn(Chess_Piece):

# class Rook(Chess_Piece):

# class Bishop(Chess_Piece):

# class Queen(Rook, Bishop):

# class Knight(Chess_Piece):


if __name__ == "__main__":
    print("Welcome to the Chess Game!")
    board = Board()
    board.draw()
    while True:
        move = input(
            "Enter a chess piece and its position or type X to exit:\n"
        ).lower()
        tmp = ""
        tmp += move[0].upper()
        tmp += move[1].lower()
        tmp += move[2]
        move = tmp
        if move[0] == "K":
            if len(move) == 3:
                if move[0] in "KRQBN":
                    if move[1] in "abcdefgh":
                        if move[2] in "12345678":
                            pos = move[1:3]
                            king = King(board, pos)
                board.empty()
                king = King(board, move[1:3])
                king.moves(board)

        elif move[0] == "R":
            pass
        elif move == "Q":
            pass
        elif move == "N":
            pass
        elif move == "X":
            print("Goodbye!")
            break
        else:
            print("Try again!")
            continue
