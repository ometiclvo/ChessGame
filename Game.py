from ChessBoard import ChessBoard
from CreatePicture import CreatePicture
from Square import Square

class Game:

    """
    Klasa odpowiedzialna za obsługę gry w szachy i interakcję z użytkownikiem w konsoli.

    Atrybuty:
        turn (str): Zmienna przechowująca informację o tym, czyja jest kolej na ruch. Przyjmuje wartości "white" lub "black".
        chess_board (ChessBoard): Obiekt klasy ChessBoard reprezentujący stan szachownicy.
        
    Metody:
        positionTransform(position): Zwraca krotkę zawierającą współrzędne pola na szachownicy na podstawie pozycji w postaci np. "A1 A2".
        changePiece(position): Zmienia pionek na wybraną przez użytkownika figurę (hetman, wieża, goniec, skoczek).
        availableMoves(position): Zwraca True jeśli ruch jest prawidłowy, False w przeciwnym wypadku (na podstawie pozycji w postaci np. "A1 A2").
        mateSymulation(position): Sprawdza, czy ruch jest prawidłowy, a następnie symuluje ruch i sprawdza, czy po nim król jest szachowany. Zwraca True jeśli tak, False w przeciwnym wypadku.
        checkPosition(position): Sprawdza, czy ruch jest prawidłowy oraz prawidłowo wpisany przez użytkownika. Zwraca True jeśli tak, False w przeciwnym wypadku.
        go(position): Wykonuje ruch na szachownicy (na podstawie pozycji w postaci np. "A1 A2").
        show(): Wyświetla szachownicę w konsoli.
        help(): Wyświetla pomoc.
        next_turn(): Wykonuje przejscie do następnej tury (zmienia zmienną turn) oraz opcję z help().
        play(): Rozpoczyna grę.
    """
    def __init__(self):
        self.turn = "white"
        self.chess_board = ChessBoard()

    def positionTransform(self, position):
        return (self.chess_board.getBoardDict().get(position[0:2]), self.chess_board.getBoardDict().get(position[3:5]))
    
    def changePiece(self, position):
        print("Wybierz na jaką figurę chcesz zamienić pionka: \t 1. Hetman \t 2. Wieża \t 3. Goniec \t 4. Skoczek")
        choice = input()
        if choice == "1": self.chess_board.getSquare(position).setPiece("Queen", self.turn)
        elif choice == "2": self.chess_board.getSquare(position).setPiece("Rook", self.turn)
        elif choice == "3": self.chess_board.getSquare(position).setPiece("Bishop", self.turn)
        elif choice == "4": self.chess_board.getSquare(position).setPiece("Knight", self.turn)
        else: print("Nie ma takiej opcji")
    
    def availableMoves(self, position):
        from_ , to_ = position[0:2], position[3:5]
        from_number , to_number = self.positionTransform(position)

        # Pawn moves
        if self.chess_board.getPieceName(from_) == "Pawn":
            if (self.chess_board.getSquare(to_).is_empty() and self.chess_board.getPiece(from_).availableMoves(from_number, to_number) and
                    abs(from_number[0] - to_number[0]) == 2):
                    if self.turn == "white" and self.chess_board.getSquareFromNumber((from_number[0] - 1, from_number[1])).is_empty():
                        return True
                    elif self.turn == "black" and self.chess_board.getSquareFromNumber((from_number[0] + 1, from_number[1])).is_empty():
                        return True
            elif self.chess_board.getSquare(to_).is_empty() and self.chess_board.getPiece(from_).availableMoves(from_number, to_number):
                return True
            elif not self.chess_board.getSquare(to_).is_empty() and self.chess_board.getPiece(from_).availableHits(from_number, to_number):
                return True
            return False
        
        # Rooke moves
        if self.chess_board.getPieceName(from_) == "Rook":
            if self.chess_board.getPiece(from_).availableMoves(from_number, to_number):
                if from_number[0] == to_number[0]:
                    for i in range(min(from_number[1], to_number[1]) + 1, max(from_number[1], to_number[1])):
                        if not self.chess_board.getSquareFromNumber((from_number[0], i)).is_empty():
                            return False
                elif from_number[1] == to_number[1]:
                    for i in range(min(from_number[0], to_number[0]) + 1, max(from_number[0], to_number[0])):
                        if not self.chess_board.getSquareFromNumber((i, from_number[1])).is_empty():
                            return False
                else: return True

        # Bishop moves
        if self.chess_board.getPieceName(from_) == "Bishop":
            if self.chess_board.getPiece(from_).availableMoves(from_number, to_number):
                if from_number[0] > to_number[0] and from_number[1] < to_number[1]:
                    for i, j in zip(range(from_number[0] - 1, to_number[0], -1), range(from_number[1] + 1, to_number[1])):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                elif from_number[0] < to_number[0] and from_number[1] > to_number[1]:
                    for i, j in zip(range(from_number[0] + 1, to_number[0]), range(from_number[1] - 1, to_number[1], -1)):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                elif from_number[0] > to_number[0] and from_number[1] > to_number[1]:
                    for i, j in zip(range(from_number[0] - 1, to_number[0], -1), range(from_number[1] - 1, to_number[1], -1)):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                elif from_number[0] < to_number[0] and from_number[1] < to_number[1]:
                    for i, j in zip(range(from_number[0] + 1, to_number[0]), range(from_number[1] + 1, to_number[1])):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                else: return True



        # Queen moves
        if self.chess_board.getPieceName(from_) == "Queen":
            if self.chess_board.getPiece(from_).availableMoves(from_number, to_number):
                if from_number[0] == to_number[0]:
                    for i in range(min(from_number[1], to_number[1]) + 1, max(from_number[1], to_number[1])):
                        if not self.chess_board.getSquareFromNumber((from_number[0], i)).is_empty():
                            return False
                elif from_number[1] == to_number[1]:
                    for i in range(min(from_number[0], to_number[0]) + 1, max(from_number[0], to_number[0])):
                        if not self.chess_board.getSquareFromNumber((i, from_number[1])).is_empty():
                            return False

                elif from_number[0] > to_number[0] and from_number[1] < to_number[1]:
                    for i, j in zip(range(from_number[0] - 1, to_number[0], -1), range(from_number[1] + 1, to_number[1])):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                elif from_number[0] < to_number[0] and from_number[1] > to_number[1]:
                    for i, j in zip(range(from_number[0] + 1, to_number[0]), range(from_number[1] - 1, to_number[1], -1)):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                elif from_number[0] > to_number[0] and from_number[1] > to_number[1]:
                    for i, j in zip(range(from_number[0] - 1, to_number[0], -1), range(from_number[1] - 1, to_number[1], -1)):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                elif from_number[0] < to_number[0] and from_number[1] < to_number[1]:
                    for i, j in zip(range(from_number[0] + 1, to_number[0]), range(from_number[1] + 1, to_number[1])):
                        if not self.chess_board.getSquareFromNumber((i, j)).is_empty():
                            return False
                else: return True
                return True
        
        # other pieces
        if self.chess_board.getPiece(from_).availableMoves(from_number, to_number):
            return True
        
        return False

    def mateSymulation(self, position):
        # wywoływane jako ostatnia metoda w funkcji checkPosition, zatem wszystkie warunki zostały już sprawdzone
        # symuluje ruch i sprawdza czy król jest szachowany
        tmp = "normal"
        from_ , to_ = position[0:2], position[3:5]
        from_copy = self.chess_board.getPiece(from_)
        to_copy = self.chess_board.getPiece(to_)
        self.chess_board.getSquare(to_).setPiece(from_copy)
        self.chess_board.getSquare(from_).setPiece(None)
        self.turn = "black" if self.turn == "white" else "white"    # zmiana tury

        for i in self.chess_board.getBoardKeys():
            if not self.chess_board.getSquare(i).is_empty() and self.chess_board.getPieceColor(i) == self.turn:
                for j in self.chess_board.getBoardKeys():
                    if (not self.chess_board.getSquare(j).is_empty() and self.chess_board.getPieceName(j) == "King" and
                        self.chess_board.getPieceColor(j) != self.turn and self.availableMoves(i + " " + j)):
                        tmp = "szach"
                        break
        
        # cofnięcie symulacji
        self.chess_board.getSquare(from_).setPiece(from_copy)
        self.chess_board.getSquare(to_).setPiece(to_copy)
        self.turn = "black" if self.turn == "white" else "white"

        if tmp == "szach": return True
        else: return False

    def checkPosition(self, position):

        from_ , to_ = position[0:2], position[3:5]

        if from_ not in self.chess_board.getBoardKeys() or to_ not in self.chess_board.getBoardKeys():
            print("Nieznane pole. Spróbuj ponownie.")
            return False

        if from_ == to_:
            print("Musisz się ruszyć.")
            return False
        if self.chess_board.getSquare(from_).is_empty():
            print("W tym miejscu nie ma twojego pionka.")
            return False
        if self.chess_board.getPieceColor(from_) != self.turn:
            print("To nie twój pionek!")
            return False
        if not self.chess_board.getSquare(to_).is_empty() and self.chess_board.getPieceColor(to_) == self.turn:
            print("Nie możesz zbić swojego pionka!")
            return False
        if not self.availableMoves(position):
            print("Nie możesz się tak poruszyć!")
            return False
        if self.mateSymulation(position):
            print("Nie możesz wykonać tego ruchu, ponieważ król jest szachowany!")
            return False
        return True

    def go(self, position):
        from_ , to_ = position[0:2], position[3:5]
        from_number , to_number = self.positionTransform(position)

        if not self.chess_board.getSquare(to_).is_empty():
            if self.chess_board.getPieceColor(to_) != self.turn: print("Gratulacje. Zbiłeś pionka przeciwnika!")
            if self.chess_board.getPieceName(to_) == "King": 
                print("Gratulacje. Wygrałeś!")
                self.turn = "quit"
        self.chess_board.getSquare(to_).setPiece(self.chess_board.getPiece(from_))
        self.chess_board.getSquare(from_).setPiece(None)
        if self.chess_board.getPieceName(to_) == "Pawn" and to_number[0] in (0, 7):
            self.changePiece(to_)

    def show(self):
        picture = CreatePicture(self.chess_board)
        picture.generate_chessboard_with_figures()

    def help(self):
        print("Aby wykonać ruch, wpisz pole, na którym znajduje się twój pionek, a następnie pole, na które chcesz go przenieść. \n"
              "Pola wpisuj w formacie: litera cyfra, np. 'C2 C4' \n"
              "Aby zakończyć grę, wpisz 'quit' \n"
              "Aby wyświetlić szachownicę, wpisz 'show' \n"
              "Aby wyświetlić pomoc, wpisz 'help' \n")

    def next_turn(self):

        while True:
            if self.turn == "white":
                position = input("Ruch białych. Gdzie ma się poruszyć?    ")
            else:
                position = input("Ruch czarnych. Gdzie ma się poruszyć?    ")

            if position == "help": 
                self.help()
                continue
            elif position == "quit":
                break
            elif position == "show":
                self.show()
                continue
            elif self.checkPosition(position):
                self.go(position)
                if self.turn == "quit": 
                    self.show()
                    break    # koniec gry
                self.turn = "black" if self.turn == "white" else "white"
                continue

    def play(self):
        print("Witaj w grze w szachy!")
        self.help()
        self.next_turn()
        print("Dziękuję za grę!")

if __name__ == "__main__":

    g = Game()
    g.play()