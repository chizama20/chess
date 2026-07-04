
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