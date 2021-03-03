import board
import players

def main():
    end = False

    user = players.Player('u',[])
    computer = players.Player('c',[])

    newboard = board.Board([])
    newboard.initBoard(user.pieces, computer.pieces)
    newboard.showBoard()

    print("User Checker # 5")
    print("Before: ", user.pieces[0].getrow())

    user.pieces[0].move_fr()
    newboard.mapBoard(user.pieces[0])

    print("After: ", user.pieces[0].getrow())

    #FIXME GOAL: USE A LOOP HERE THAT KEEPS THE GAME GOING UNTIL WIN.

    newboard.showBoard()

    #while not(end):
    #
    #promptuser
main()