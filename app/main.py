from fastapi import FastAPI
from game import GameBoard

app = FastAPI()
board = GameBoard()



@app.get("/board")
def get_board():
    board_state = [{"position": position, "piece": piece} for position, piece in board.squares.items()]
    return board_state


@app.put("/move/{fx}/{fy}/{tx}/{ty}")
def move_piece(fx:int,fy:int, tx:int, ty:int):
    board.make_move((fx, fy), (tx, ty))
    board.print_board()
    return {"message": "Piece moved successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)