from chess import Piece


class Pawn(Piece.Piece):

    # constructor
    def __init__(self, identificator, color, x, y):
        super().__init__(identificator, color, x, y)
        self.__name = "Pawn"

    # returns the name of the piece
    def getname(self):
        return self.__name

    def __str__(self):
        return "P"

    def __repr__(self):
        return "P"
