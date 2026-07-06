from typing import Tuple
from piece import Color
from move import Move

Square = Tuple[int, int]

DIAGONALS = ((1, 1), (1, -1), (-1, 1), (-1, -1))
ORTHOGONALS = ((1, 0), (-1, 0), (0, 1), (0, -1))
KNIGHT_OFFSETS = ((2, 1), (2, -1), (-2, 1), (-2, -1),
                  (1, 2), (1, -2), (-1, 2), (-1, -2))

class MoveGen:
    
    def get_pawn_move(board, square: Square, color: Color):
        move_list = []
        direction = 1 if color == Color.WHITE else -1
        row, col = square

        # single move forward
        one_step = (direction + row, col)
        if (board.isEmpty(one_step)):
            move_list.append(Move(square, one_step))
        
        # double move forward
        two_step = (row + 2 * direction, col)
        if board.IsAtStartingRank(square) and board.isEmpty(one_step) and board.isEmpty(two_step):
            move_list.append(Move(square, two_step))

        # diagonal move forward
        left_diagonal = (row + direction, col - 1)
        right_diagonal = (row + direction, col + 1)

        if board.hasOpponentPiece(left_diagonal, color):
            move_list.append(Move(square, left_diagonal))

        if board.hasOpponentPiece(right_diagonal, color):
            move_list.append(Move(square, right_diagonal))
        
        return move_list

        # En Passant
        # Promotion

    def get_knight_move(board, square: Square, color: Color):
        move_list = []      
        row, col = square

        for d_row, d_col in KNIGHT_OFFSETS:
            r, c = row + d_row, col + d_col
            if board.inBounds((r, c)):
                if board.isEmpty((r, c)) or board.hasOpponentPiece((r, c), color):
                    move_list.append(Move(square, (r, c)))
        return move_list


    def get_king_move(board, square: Square, color: Color):
        move_list = []      
        directions = DIAGONALS + ORTHOGONALS  
        row, col = square

        for d_row, d_col in directions:
            r, c = row + d_row, d_col + col
            if board.inBounds((r, c)):
                if board.is_empty((r, c)) or board.hasOpponentPiece((r, c), color):
                    move_list.append(Move(square, (r, c)))
        return move_list
    
    def get_bishop_move(board, square: Square, color: Color):
        return MoveGen.slide(board, square, color, DIAGONALS)

    def get_rook_move(board, square: Square, color: Color):
        return MoveGen.slide(board, square, color, ORTHOGONALS)
    
    def get_queen_move(board, square: Square, color: Color):
        return MoveGen.slide(board, square, color, DIAGONALS + ORTHOGONALS)


    def slide(board, square, color, directions):
        move_list = []
        row, col = square
        for d_row, d_col in directions:
            r, c = row + d_row, d_col + col
            while board.inBounds((r, c)):
                if board.isEmpty():
                    move_list.append(Move(square, (r, c)))
                elif board.hasOpponentPiece():
                    move_list.append(Move(square, (r, c)))
                    break
                else:
                    break
                r, c = r + d_row, c + d_col
        return move_list

