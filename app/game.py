from piece import Pawn, King, Knight, Rook, Bishop, Queen, ChessPiece


class GameBoard:

    def __init__(self):
        self.squares = {(x, y): None for x in range(1, 9) for y in range(1, 9)}
        self.setup_board()

    def setup_board(self):

        for i in range(1, 9):
            self.squares[(i, 2)] = Pawn('w', i, 2, 'p')
            self.squares[(i, 7)] = Pawn('b', i, 7, 'p')

        # Setting up other pieces
        self.squares[(1, 1)] = Rook('w', 1, 1, 'r')
        self.squares[(8, 1)] = Rook('w', 8, 1, 'r')
        self.squares[(1, 8)] = Rook('b', 1, 8, 'r')
        self.squares[(8, 8)] = Rook('b', 8, 8, 'r')

        self.squares[(2, 1)] = Knight('w', 2, 1, 'k')
        self.squares[(7, 1)] = Knight('w', 7, 1, 'k')
        self.squares[(2, 8)] = Knight('b', 2, 8, 'k')
        self.squares[(7, 8)] = Knight('b', 7, 8, 'k')

        self.squares[(3, 1)] = Bishop('w', 3, 1, 'b')
        self.squares[(6, 1)] = Bishop('w', 6, 1, 'b')
        self.squares[(3, 8)] = Bishop('b', 3, 8, 'b')
        self.squares[(6, 8)] = Bishop('b', 6, 8, 'b')

        self.squares[(4, 1)] = Queen('w', 4, 1, 'q')
        self.squares[(4, 8)] = Queen('b', 4, 8, 'q')

        self.squares[(5, 1)] = King('w', 5, 1, 'k')
        self.squares[(5, 8)] = King('b', 5, 8, 'k')

    def validate_move(self, from_, to_):
        piece = self.squares[from_]
        enemy = self.squares[to_]

        if not piece:
            return False

        moves = piece.can_move_to()

        if isinstance(piece, (Rook, Pawn, Bishop, Queen)):
            way = self.check_way(from_, to_, moves)
        else:
            way = False
        return (not way and to_ in moves and isinstance(piece, ChessPiece)
                and (enemy is None or piece.color != enemy.color)
        )

    def check_way(self, from_, to_, moves):
        dx = 1 if to_[0] > from_[0] else -1 if to_[0] < from_[0] else 0
        dy = 1 if to_[1] > from_[1] else -1 if to_[1] < from_[1] else 0

        x, y = from_
        while (x, y) != to_:
            x += dx
            y += dy
            if (x, y) in moves:
                return False  
            elif self.squares.get((x, y)):
                return True  
        return False

    def print_board(self):
        for y in range(1, 9):
            for x in range(1, 9):
                if self.squares[(x, y)]:
                    print(self.squares[(x, y)], end=" ")
                else:
                    print('_', end=" ")
            print()

    def make_move(self, from_, to_):
        piece = self.squares.get(from_)
        if piece is None:
            return False

        if to_ not in piece.can_move_to():
            return False

        if not self.validate_move(from_, to_):
            return False
        self.squares[to_] = self.squares[from_]
        self.squares[from_] = None
        return True
    

