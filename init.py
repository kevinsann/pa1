import board
import players
import timer

def main():
    end = False

    user = players.Player('u', [])
    computer = players.Player('c', [])

    for i in user.pieces:
        i.set_enemy(computer)

    for i in computer.pieces:
        i.set_enemy(user)

    newboard = board.Board([])
    newboard.initBoard(user.pieces, computer.pieces)
    newboard.showBoard()

    while not end:
        user.prompt_piece(newboard.grid)
        user.prompt_destination(newboard.grid)

        newboard.showBoard()

        print()
        print("Computer moving in:")
        timer.display()
        computer.decision_maker(newboard.grid)

        newboard.showBoard()

        if len(user.pieces) == 0:
            print("Game over. You lose!")
            end = True
        elif len(computer.pieces) == 0:
            print("Game over. You won!")
            end = True

main()
