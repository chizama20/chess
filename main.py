# #import chess
# import random
# # Importing Modules
# import pygame
# import requests
# import rembg
# from io import BytesIO

from enum import Enum
from collections import namedtuple


class Engine:
    
    def evaluate(self, board): # evaluate the moves of each piece by score
        pieceVal = { 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 20}
        piecePositions = board.fen().split()[0] # get the piece positions from the FEN string
        evalScore = 0
        for piece in piecePositions:
            if not piece.isalpha(): # if it's not a piece, skip it
                continue
            else:
                if piece.isupper(): # if it's a white piece, get its value
                    value = pieceVal[piece.lower()]
                    evalScore += value
                else: # if it's a black piece, get its value
                    evalScore -= value 
        return evalScore
    
    def minimax(self, board, depth, maximizingPlayer, alpha=float('-inf'), beta=float('inf')):
        if depth == 0 or board.is_game_over():
            return self.evaluate(board)
        
        sorted_moves = sorted(board.legal_moves, key=lambda move: self.move_score(board, move), reverse=True)
        if maximizingPlayer:
            maxEval = float('-inf')
        
            for move in sorted_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, False, alpha, beta)
                board.pop()
                maxEval = max(maxEval, eval)
                alpha = max(maxEval, alpha)
                if beta <= alpha:
                    break
            return maxEval
        else:
            minEval = float('inf')
            for move in sorted_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, True, alpha, beta)
                board.pop()
                minEval = min(minEval, eval)
                beta = min(minEval, beta)
                if beta <= alpha:   
                    break
            return minEval

    def best_move(self, board, depth=3, alpha=float('-inf'), beta=float('inf')):
        bestMove = None
        bestScore = float('-inf')
        sorted_moves = sorted(board.legal_moves, key=lambda move: self.move_score(board, move), reverse=True)
        for move in sorted_moves:
            board.push(move)            
            score = self.minimax(board, depth - 1, False, alpha, beta)
            board.pop()
            if score > bestScore:
                bestScore = score
                bestMove = move
            alpha = max(alpha, bestScore)
        return bestMove
    
    def move_score(self, board, move):
        board.push(move)
        score = self.evaluate(board)
        board.pop()
        return score

    def bestDepth(self, board, depth):  
        for d in range(1, depth + 1):
            bestMove = self.best_move(board, d)
        return bestMove



class Color(Enum):
    WHITE = 0
    BLACK = 1


class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Move:
    pass

Piece = namedtuple('PieceType', 'Color, Move')

RANKS, FILES = 8, 8
class Board:

    def __init__(self):
        self.board = [['*' for _ in range(RANKS)]for _ in range(FILES)]
        self.board[0] = ['wR','wN','wB','wQ','wK','wB','wN','wR']    
        self.board[1] = ['wP'] * 8    
        self.board[6] = ['bR','bN','bB','bQ','bK','bB','bN','bR']    
        self.board[7] = ['bP'] * 8

    def __str__(self):
        rows = []
        for row in self.board:
            rows.append(' '.join(f'{p:2}' for p in row))
        return '\n'.join(rows)


def main():
    board = Board()
    # engine = Engine()
    gameOver = False
    print(board)
    
    # while not gameOver:
        


    #     gameOver = True

if __name__ == "__main__":
    main()