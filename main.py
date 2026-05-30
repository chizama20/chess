import chess
import random
# get uci (start pos + end pos) using move.uci()
# check 
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
                    value = pieceVal[piece]
                    evalScore -= value 
        return evalScore
    
    def minimax(self, board, depth, maximizingPlayer, alpha=float('-inf'), beta=float('inf')):
        if depth == 0 or board.is_game_over():
            return self.evaluate(board)
        
        if maximizingPlayer:
            maxEval = float('-inf')
            for move in board.legal_moves:
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
            for move in board.legal_moves:
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
        for move in board.legal_moves:
            board.push(move)
            score = self.minimax(board, depth - 1, False, alpha, beta)
            board.pop()
            if score > bestScore:
                bestScore = score
                bestMove = move
            alpha = max(alpha, bestScore)
        return bestMove
        
def main():
    
    board = chess.Board()
    engine = Engine()
    
    while not board.is_game_over():
        print(board)
        legal = [board.legal_moves]    
        if board.turn == chess.WHITE:
            """
            print(legal)
            move = input("Enter a move: ")
            board.push_san(move)
            """
            move = random.choice(list(board.legal_moves))
            board.push(move)
        else:
            move = engine.best_move(board)
            board.push(move)
    print("Game Over")
    

if __name__=="__main__":
    main()