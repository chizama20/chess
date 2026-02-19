import chess

class Engine:
    def evaluate():
        pass
    def cycle():
        pass
    def best_move():
        pass

def main():
    board = chess.Board()
    start = True

    while not board.is_game_over():
        print(board)
        
        if board.turn == chess.WHITE:
            move = input("Enter a move: ")
            board.push_san(move)
        else:
            engine = Engine()
            move = engine.best_move(board)
            board.parse_san(move)
    print("Game Over")


if __name__=="__main__":
    main()