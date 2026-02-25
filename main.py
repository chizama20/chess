import chess
import random

class Engine:
    def evaluate(self, board):
        pass
    def best_move(self, board):
        moveList = list(board.legal_moves)
        move = random.choice(moveList)
        return move

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