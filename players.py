import orderedpair
import random

class Player:
    def __init__(self, faction, pieces):
        self.faction = faction

        self.pieces = pieces
        self.selectedpiece = None

    def getfaction(self):
        return self.faction

    def getpiecestatus(self, index):
        selected = self.pieces[index]

        print("Piecestatus of piece ", index + 1, ': ')
        print('isAlive:', selected.isliving)
        print('row: ', selected.getrow())
        print('column: ', selected.getcolumn())

    def killpiece(self, slain_piece):
        self.pieces.remove(slain_piece)

    # Currently, upon valid input, returns row and column in ordered pair of the selected piece.

    def prompt_piece(self, grid):
        if self.faction == 'u':
            valid_piece = False;

            # checkers are selected by means of the input 'rxc', with r denoting the row and c denoting the column
            # of the desired piece. r and c must be separated by space.
            #FIXME: REITERATE IN README THAT THERE MUST BE A SPACE BETWEEN R AND C
            while not valid_piece:
                selection = input("Select your piece (rxc): ")

                coords = selection.split()

                rs = int(coords[0])
                cs = int(coords[1])

                # USE A FOR LOOP TO PARSE THROUGH PIECES AND COMPARE MS AND NS:

                if self.selectPiece(rs, cs) and (self.pieces[self.selectedpiece].can_jump(grid) or self.pieces[self.selectedpiece].can_move(grid)):
                    valid_piece = True

    def prompt_destination(self, grid):
        valid_destination = False

        selectedpiece = self.selectedpiece

        if self.faction == 'u':
            while not valid_destination:
                selection = input("Destination (r,c): ")

                destination = selection.split()

                dest_r = int(destination[0])
                dest_c = int(destination[1])

                dest_coord = orderedpair.OrderedPair(dest_r, dest_c)

                if self.pieces[selectedpiece].move(grid, dest_coord):
                    valid_destination = True
                    self.selectedpiece = None

                elif self.pieces[selectedpiece].jump(grid, dest_coord):
                    valid_destination = True
                    self.selectedpiece = None
                else:
                    continue

        elif self.faction == 'c':
            print("Moving..")

    # README IMPORTANT: CHANGED SELECTEDPIECE TO ONLY BE AN INDICE OF THE PIECES ARRAY FOR PLAYER.
    # ALSO USE SELECTPIECE TO KILL PIECE WHEN IT IS JUMPED.
    def selectPiece(self, r, c):

        for i in range(len(self.pieces)):
            if self.pieces[i].r == r and self.pieces[i].c == c:
                self.pieces[i].selected = True
                self.selectedpiece = i

                return True
            else:
                continue

    def decision_maker(self, grid):
        random.seed(a=None,version=2)

        for i in range(len(self.pieces)):
            current_r = self.pieces[i].r
            current_c = self.pieces[i].c

            reg_moveby = random.randrange(-1,1,2)
            jump_moveby = random.randrange(-2,2,4)

            reg_destination = orderedpair.OrderedPair(current_r + 1, current_c + reg_moveby)
            jump_destination = orderedpair.OrderedPair(current_r + 2, current_c + jump_moveby)

            if self.pieces[i].jump(grid, jump_destination):
                return 0
            elif self.pieces[i].move(grid, reg_destination):
                return 1
            else:
                continue
