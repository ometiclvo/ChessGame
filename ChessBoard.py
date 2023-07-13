from Square import Square
from Piece import Piece, Rook, Knight, Bishop, Queen, King, Pawn

class ChessBoard:
    """
    Klasa reprezentująca szachownicę. Zawiera listę obiektów klasy Square.

    Atrybuty:
        board (list): Lista obiektów klasy Square reprezentujących pola na szachownicy.
        d (dict): Słownik, którego kluczami są pozycje pól na szachownicy, a wartościami pozycje tych pól na tablicy.

    Metody:
        getBoardDict(): Zwraca słownik d.
        getBoardKeys(): Zwraca listę kluczy słownika d.
        getSquare(position): Zwraca obiekt klasy Square reprezentujący pole o pozycji position (position - str reprezentujący pozycję pola na szachownicy).
        getSquareFromNumber(number): Zwraca obiekt klasy Square reprezentujący pole o pozycji number.  (number - krotka (x, y) reprezentująca pozycję pola na tablicy)
        getPiece(position): Zwraca obiekt klasy Piece reprezentujący figurę znajdującą się na polu o pozycji position.
        getPieceColor(position): Zwraca kolor figury znajdującej się na polu o pozycji position.
        getPieceName(position): Zwraca nazwę figury znajdującej się na polu o pozycji position.

    """

    def __init__(self):
        self.board = [[Square("A8",Rook("black", "Rook")), Square("B8",Knight("black", "Knight")), Square("C8",Bishop("black", "Bishop")), Square("D8",Queen("black", "Queen")),    # 8 row
                      Square("E8",King("black", "King")), Square("F8",Bishop("black", "Bishop")), Square("G8",Knight("black", "Knight")), Square("H8",Rook("black", "Rook",))],
                      [Square("A7",Pawn("black", "Pawn")), Square("B7",Pawn("black", "Pawn")), Square("C7",Pawn("black", "Pawn")), Square("D7",Pawn("black", "Pawn")),        # 7 row
                      Square("E7",Pawn("black", "Pawn")), Square("F7",Pawn("black", "Pawn")), Square("G7",Pawn("black", "Pawn")), Square("H7",Pawn("black", "Pawn"))],
                      [Square("A6"), Square("B6"), Square("C6"), Square("D6"), Square("E6"), Square("F6"), Square("G6"), Square("H6")],   # 6 row
                      [Square("A5"), Square("B5"), Square("C5"), Square("D5"), Square("E5"), Square("F5"), Square("G5"), Square("H5")],   # 5 row
                      [Square("A4"), Square("B4"), Square("C4"), Square("D4"), Square("E4"), Square("F4"), Square("G4"), Square("H4")],   # 4 row
                      [Square("A3"), Square("B3"), Square("C3"), Square("D3"), Square("E3"), Square("F3"), Square("G3"), Square("H3")],   # 3 row
                      [Square("A2",Pawn("white", "Pawn")), Square("B2",Pawn("white", "Pawn")), Square("C2",Pawn("white", "Pawn")), Square("D2",Pawn("white", "Pawn")),     # 2 row
                      Square("E2",Pawn("white", "Pawn")), Square("F2",Pawn("white", "Pawn")), Square("G2",Pawn("white", "Pawn")), Square("H2",Pawn("white", "Pawn"))],
                      [Square("A1",Rook("white", "Rook")), Square("B1",Knight("white", "Knight")), Square("C1",Bishop("white", "Bishop")), Square("D1",Queen("white", "Queen")), 
                      Square("E1",King("white", "King")), Square("F1",Bishop("white", "Bishop")), Square("G1",Knight("white", "Knight")), Square("H1",Rook("white", "Rook"))]]   # 1 row

        self.d = dict(  A8 = (0, 0), B8 = (0, 1), C8 = (0, 2), D8 = (0, 3), E8 = (0, 4), F8 = (0, 5), G8 = (0, 6), H8 = (0, 7),
                        A7 = (1, 0), B7 = (1, 1), C7 = (1, 2), D7 = (1, 3), E7 = (1, 4), F7 = (1, 5), G7 = (1, 6), H7 = (1, 7),
                        A6 = (2, 0), B6 = (2, 1), C6 = (2, 2), D6 = (2, 3), E6 = (2, 4), F6 = (2, 5), G6 = (2, 6), H6 = (2, 7),
                        A5 = (3, 0), B5 = (3, 1), C5 = (3, 2), D5 = (3, 3), E5 = (3, 4), F5 = (3, 5), G5 = (3, 6), H5 = (3, 7),
                        A4 = (4, 0), B4 = (4, 1), C4 = (4, 2), D4 = (4, 3), E4 = (4, 4), F4 = (4, 5), G4 = (4, 6), H4 = (4, 7),
                        A3 = (5, 0), B3 = (5, 1), C3 = (5, 2), D3 = (5, 3), E3 = (5, 4), F3 = (5, 5), G3 = (5, 6), H3 = (5, 7),
                        A2 = (6, 0), B2 = (6, 1), C2 = (6, 2), D2 = (6, 3), E2 = (6, 4), F2 = (6, 5), G2 = (6, 6), H2 = (6, 7),
                        A1 = (7, 0), B1 = (7, 1), C1 = (7, 2), D1 = (7, 3), E1 = (7, 4), F1 = (7, 5), G1 = (7, 6), H1 = (7, 7))

    def getBoardDict(self):
        return self.d
    
    def getBoardKeys(self):
        return self.d.keys()
    
    def getSquare(self, position):
        return self.board[self.d[position][0]][self.d[position][1]]

    def getSquareFromNumber(self, number):
        return self.board[number[0]][number[1]]

    def getPiece(self, position):
        return self.getSquare(position).getPiece()
    
    def getPieceColor(self, position):
        return self.getPiece(position).getColor()

    def getPieceName(self, position):
        return self.getPiece(position).getName()