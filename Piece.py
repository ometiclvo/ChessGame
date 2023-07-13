class Piece:
    """
    Klasa bazowa dla wszystkich figur.

    Argumenty:
        color(str) - kolor figury (white, black)
        name(str) - nazwa figury (Pawn, Rook, Knight, Bishop, Queen, King)

    Metody:
        getName() - zwraca nazwę figury
        getColor() - zwraca kolor figury
        availableMoves(from_, to_) - sprawdza czy ruch jest możliwy (dla podklas figury),
                                    from_ i to_ to krotki (x, y) z pozycją startową i końcową ruchu (np. (0, 0) -> (1, 1))
        availableHits(from_, to_) - sprawdza czy bicie jest możliwe (dla podklas figury)
    """

    def __init__(self,color, name):
        self.name = name
        self.color = color
    
    def getName(self):
        return self.name

    def getColor(self):
        return self.color

class Pawn(Piece):
    
    def availableMoves(self, from_, to_):
        if self.color == "white": sgn = 1
        else: sgn = -1
        if from_[0] == 6 and to_[0] in (4, 5) and from_[1] == to_[1]: return True    # first move for white
        elif from_[0] == 1 and to_[0] in (2, 3) and from_[1] == to_[1]: return True    # first move for black
        elif (sgn * (from_[0] - to_[0])) == 1 and from_[1] == to_[1]: return True    # normal move
        return False

    def availableHits(self, from_, to_):
        if from_[0] == to_[0] - 1 and abs(from_[1] - to_[1]) == 1: return True    # white hit
        elif from_[0] == to_[0] + 1 and abs(from_[1] - to_[1]) == 1: return True    # black hit
        return False

class Rook(Piece):

    def availableMoves(self, from_, to_):
        if from_[0] == to_[0] or from_[1] == to_[1]: return True
        return False

class Knight(Piece):

    def availableMoves(self, from_, to_):
        if from_[0] - to_[0] == 2 and abs(from_[1] - to_[1]) == 1: return True    # 2 up 1 right/left
        elif from_[0] - to_[0] == -2 and abs(from_[1] - to_[1]) == 1: return True    # 2 down 1 right/left
        elif from_[1] - to_[1] == 2 and abs(from_[0] - to_[0]) == 1: return True    # 2 right 1 up/down
        elif from_[1] - to_[1] == -2 and abs(from_[0] - to_[0]) == 1: return True    # 2 left 1 up/down
        return False

class Bishop(Piece):
    
    def availableMoves(self, from_, to_):
        if from_[0] - to_[0] == to_[1] - from_[1]: return True    # diagonal up right
        elif from_[0] - to_[0] == from_[1] - to_[1]: return True    # diagonal up left
        return False

class Queen(Piece):

    def availableMoves(self, from_, to_):
        if Bishop("white", "Bishop").availableMoves(from_, to_) or Rook("white", "Rook").availableMoves(from_, to_): return True
        return False

class King(Piece):
    
    def availableMoves(self, from_, to_):
        if from_[0] == to_[0] and abs(from_[1] - to_[1]) == 1: return True    # 1 right/left
        elif from_[1] == to_[1] and abs(from_[0] - to_[0]) == 1: return True    # 1 up/down
        elif abs(from_[0] - to_[0]) == 1 and abs(from_[1] - to_[1]) == 1: return True    # 1 diagonal
        return False