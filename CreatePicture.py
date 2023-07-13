from ChessBoard import ChessBoard
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

class CreatePicture:

    """
    Klasa odpowiedzialna za generowanie obrazu szachownicy z figurami na podstawie stanu szachownicy.

    Atrybuty:
        chess_board (ChessBoard): Obiekt klasy ChessBoard reprezentujący stan szachownicy.

    Metody:
        chessboard_coordinates(): Zwraca słownik zawierający współrzędne pól szachownicy.
        generate_chessboard_with_figures(): Generuje obraz szachownicy z figurami na podstawie stanu szachownicy i wyświetla go w oknie.

    """
    
    def __init__(self, chess_board):
        self.chess_board = chess_board
    
    def chessboard_coordinates(self):
        square_size = 100
        coordinates = {}

        for row in range(8):
            for col in range(8):
                x = col * square_size
                y = row * square_size
                position = chr(ord('A') + col) + str(8 - row)
                coordinates[position] = (x, y)

        return coordinates

    def generate_chessboard_with_figures(self):
        # Tworzenie szachownicy
        square_size = 100
        board_size = square_size * 8
        board_image = Image.new("RGBA", (board_size, board_size))
        draw = ImageDraw.Draw(board_image)

        for row in range(8):
            for col in range(8):
                x = col * square_size
                y = row * square_size
                if (row + col) % 2 == 0:
                    draw.rectangle(
                        [x, y, x + square_size, y + square_size],
                        fill=(240, 217, 181, 255)  # Kolor jasnych pól z pełną przezroczystością
                    )
                else:
                    draw.rectangle(
                        [x, y, x + square_size, y + square_size],
                        fill=(181, 136, 99, 255)  # Kolor ciemnych pól z pełną przezroczystością
                    )
                             
        # Umieszczanie figur na szachownicy
        piece_images = {"King_white": Image.open("images/white_king.png").convert("RGBA"),
                        "Queen_white": Image.open("images/white_queen.png").convert("RGBA"),
                        "Rook_white": Image.open("images/white_rook.png").convert("RGBA"),
                        "Bishop_white": Image.open("images/white_bishop.png").convert("RGBA"),
                        "Knight_white": Image.open("images/white_knight.png").convert("RGBA"),
                        "Pawn_white": Image.open("images/white_pawn.png").convert("RGBA"),
                        "King_black": Image.open("images/black_king.png").convert("RGBA"),
                        "Queen_black": Image.open("images/black_queen.png").convert("RGBA"),
                        "Rook_black": Image.open("images/black_rook.png").convert("RGBA"),
                        "Bishop_black": Image.open("images/black_bishop.png").convert("RGBA"),
                        "Knight_black": Image.open("images/black_knight.png").convert("RGBA"),
                        "Pawn_black": Image.open("images/black_pawn.png").convert("RGBA")}

        figures_positions = dict()
        for k in self.chess_board.getBoardKeys():
            if not self.chess_board.getSquare(k).is_empty():
                figures_positions[k] = self.chess_board.getPieceName(k) + "_" + self.chess_board.getPieceColor(k)

        chessboard_coordinates = self.chessboard_coordinates()

        for position, piece in figures_positions.items():
            if position in chessboard_coordinates:
                piece_image = piece_images.get(piece)
                if piece_image:
                    x, y = chessboard_coordinates[position]
                    piece_image = piece_image.resize((square_size - 20, square_size - 20))
                    piece_x = x + (square_size - piece_image.width) // 2  # Wyśrodkowanie figury względem pola
                    piece_y = y + (square_size - piece_image.height) // 2  # Wyśrodkowanie figury względem pola
                    board_image.paste(piece_image, (piece_x, piece_y), mask=piece_image)  # Używamy maski przezroczystości


        plt.imshow(board_image)
        plt.axis('off')
        plt.show()