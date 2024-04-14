class ChessPiece:
    def __init__(self, color, x_line, y_line, symbol, can_jump=False):
        self.color = color
        self.y_line = y_line
        self.x_line = x_line
        self.symbol = symbol
        self.can_jump = can_jump

    def __repr__(self) -> str:
        return self.symbol

    def get_position(self):
        return f"{self.x_line}{self.y_line}"

    def is_valid_move(self, target_x_line, target_y_line):
        return 1 <= target_y_line <= 8 and 1 <= target_x_line <= 8

    def can_move_to(self, target_x_line, target_y_line):
        raise NotImplementedError("Subclass must implement can_move_to")


class Pawn(ChessPiece):
    def __init__(self, color, x_line, y_line, symbol=None):
        super().__init__(color, x_line, y_line, symbol, can_jump=False)
        self.moved = False

    def can_move_to(self):
        if self.color == 'w':
            available_moves = [(0, 1), (0, 2)]
            if self.moved:
                available_moves = [(0, 1)]

        if self.color == 'b':
            available_moves = [(0, -1), (0, -2)]
            if self.moved:
                available_moves = [(0, -1)]
        moves = []
        for x, y in available_moves:
            moves.append((self.x_line + x, self.y_line + y))
        return moves


class Rook(ChessPiece):
    def __init__(self, color, x_line, y_line, symbol=None):
        super().__init__(color, x_line, y_line, symbol, can_jump=False)

    def can_move_to(self):
        moves = []
        for x in range(1, 9):
            moves.append((x, self.y_line))

        for y in range(1, 9):
            moves.append((self.x_line, y))

        possible_moves = []
        for x, y in moves:
            if self.is_valid_move(x, y):
                possible_moves.append((x, y))

        return possible_moves


class Bishop(ChessPiece):
    def __init__(self, color, x_line, y_line, symbol=None):
        super().__init__(color, x_line, y_line, symbol, can_jump=False)

    def can_move_to(self):
        x = self.x_line
        y = self.y_line
        moves = []

        x_offsets = [1, 1, -1, -1]
        y_offsets = [1, -1, 1, -1]

        for i in range(4):
            x_offset = x_offsets[i]
            y_offset = y_offsets[i]

            new_x = x + x_offset
            new_y = y + y_offset

            while 1 <= new_x <= 8 and 1 <= new_y <= 8:
                moves.append((new_x, new_y))
                new_x += x_offset
                new_y = new_y + y_offset

        return moves


class Queen(ChessPiece):
    def __init__(self, color, x_line, y_line, symbol=None):
        super().__init__(color, x_line, y_line, symbol, can_jump=False)

    def can_move_to(self):
        moves = []
        moves.append(Bishop(self.color, self.y_line, self.x_line).can_move_to())
        moves.append(Rook(self.color, self.y_line, self.x_line).can_move_to())

        return moves


class Knight(ChessPiece):
    def __init__(self, color, x_line, y_line, symbol=None):
        super().__init__(color, x_line, y_line, symbol, can_jump=False)

    def can_move_to(self):
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        possible_moves = []
        for x, y in moves:
            new_x = x + self.x_line
            new_y = y + self.y_line
            if self.is_valid_move(new_x, new_y):
                possible_moves.append((new_x, new_y))

        return possible_moves


class King(ChessPiece):
    def __init__(self, color, x_line, y_line, symbol=None):
        super().__init__(color, x_line, y_line, symbol, can_jump=False)

    def can_move_to(self):
        moves = []

        for y in range(-1, 2):
            for x in range(-1, 2):
                new_y = y + self.y_line
                new_x = x + self.x_line
                if self.is_valid_move(new_x, new_y):
                    moves.append((new_y, new_x))

        return moves


