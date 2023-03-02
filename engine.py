class Engine:
    def generateBoard(self):
        board = []
        for i in range(8):
            board.append(["-"] * 8)
        
        _ = ["r", "n", "b", "q", "k", "b", "n", "r"]
        for i in range(8):
            board[0][i] = _[i]
            board[7][i] = _[i].upper()
            board[1][i] = "p"
            board[6][i] = "P"
        return board

    def __init__(self) -> None:
        self.board = self.generateBoard()
        self.moveList = []

    def printBoard(self, board):
        for row in board:
            print(" ".join(row))

engine = Engine()
engine.printBoard(engine.board)