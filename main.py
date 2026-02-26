import chess
import random
# get uci (start pos + end pos) using move.uci()
# check 
class Engine:
    
    def evaluate(self, board): # evaluate the moves of each piece by score
        #piecePriceList = { 'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 20}
        captureMoves = []
        for move in board.legal_moves:
            if board.is_capture(move):
                captureMoves.append(move)    
        return captureMoves
    
    def get_uci(self, board):
        fullMoveList = []
        for move in board.legal_moves:
            fullMoveList.append(move.uci())
        return fullMoveList

    def best_move(self, board):
        moveList =  list(board.legal_moves)
        captureMoveList = self.evaluate(board)
        if captureMoveList:
            return random.choice(captureMoveList)
        else:
            return random.choice(moveList)

def main():
    board = chess.Board()
    engine = Engine()
    
    while not board.is_game_over():
        print(board)
        legal = [board.legal_moves]    
        if board.turn == chess.WHITE:
            print(legal)
            move = input("Enter a move: ")
            board.push_san(move)
        else:
            move = engine.best_move(board)
            board.push(move)
    print("Game Over")

if __name__=="__main__":
    main()