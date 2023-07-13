class Square:
    """
    Klasa reprezentująca pojedyncze pole na szachownicy.

    Atrybuty:
        position (str): Pozycja pola na szachownicy. Przyjmuje wartości od A1 do H8.
        on (Piece): Obiekt klasy Piece reprezentujący figurę znajdującą się na polu. Domyślnie None.
    
    Metody:
        getPiece(): Zwraca obiekt klasy Piece reprezentujący figurę znajdującą się na polu.
        is_empty(): Zwraca True jeśli pole jest puste, False w przeciwnym wypadku.
        setPiece(new_on): Ustawia figurę na polu na nową figurę new_on.

    """

    def __init__(self, position, on = None):
        self.position = position
        self.on = on
    
    def getPiece(self):
        return self.on

    def is_empty(self):
        if self.on == None:
            return True
        return False

    def setPiece(self, new_on):
        self.on = new_on