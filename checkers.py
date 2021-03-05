import players


class Checker:
    def __init__(self, faction, enemy_pieces, r, c):
        self.faction = faction

        if self.faction == 'c':
            self.enemy = players.Player('u', enemy_pieces)
        elif self.faction == 'u':
            self.enemy = players.Player('c', enemy_pieces)

        self.r = r
        self.c = c
        self.jumped = False
        self.selected = False

    # setters

    def set_enemy(self, enemy):
        self.enemy = enemy

    # getters
    def getfaction(self):
        return self.faction

    def getrow(self):
        return self.r

    def getcolumn(self):
        return self.c

    # checking if the move is allowed.
    # GOING TO TRY AND MAKE IT SO MOVE_FL AND CAN_MOVE ARE MERGED INTO CAN_MOVE

    # can_move to be renamed move.
    # NEED CAN_MOVE TO CHECK IF THE PIECE IS EVEN OKAY TO MOVE

    def can_move(self, grid):
        if self.faction == 'u':
            if (grid[self.r - 1][self.c - 1] == ' ' or grid[self.r - 1][self.c + 1] == ' '):
                return True
            else:
                return False

    def can_jump(self, grid):
        if self.faction == 'u':
            if (grid[self.r - 1][self.c - 1] == 'c' and grid[self.r - 2][self.c - 2] == ' ') \
                    or (grid[self.r - 1][self.c + 1] == 'c' and grid[self.r - 2][self.c + 2] == ' '):
                return True
            else:
                return False

    # in its current implementation, can_move can be used in player.prompt_destination.

    # in current implementation, move(grid,dest) takes in grid of board and a destination.
    # dest is an OrderedPair().
    def move(self, grid, dest):
        if self.faction == 'u':

            if (dest.r == self.r - 1 and dest.c == self.c - 1 and grid[self.r - 1][self.c - 1] == ' ') \
                    or (dest.r == self.r - 1 and dest.c == self.c + 1 and grid[self.r - 1][self.c + 1] == ' '):

                grid[self.r][self.c] = ' '
                grid[dest.r][dest.c] = self.faction

                self.r = dest.r
                self.c = dest.c

                return True
            else:
                return False
        elif self.faction == 'c':

            if (dest.r == self.r + 1 and dest.c == self.c - 1 and grid[self.r + 1][self.c - 1] == ' ') \
                    or (dest.r == self.r + 1 and dest.c == self.c + 1 and grid[self.r + 1][self.c + 1] == ' '):

                grid[self.r][self.c] = ' '
                grid[dest.r][dest.c] = self.faction

                self.r = dest.r
                self.c = dest.c

                return True
            else:
                return False

    # jumps are different from moves-- they kill pieces.
    # use the killpiece() method--select the enemy piece (selectpiece) return its indice, and kill it.
    def jump(self, grid, dest):

        if self.faction == 'u':
            if dest.r == self.r - 2 and dest.c == self.c - 2 and grid[self.r - 1][self.c - 1] == 'c' and \
                    grid[self.r - 2] \
                            [self.c - 2] == ' ':

                grid[self.r][self.c] = ' '
                grid[dest.r][dest.c] = self.faction

                # killing enemy piece
                selected_indice = self.enemy.selectPiece(self.r - 1, self.c - 1)
                self.enemy.killpiece(self.enemy.pieces[selected_indice])

                return True
            elif dest.r == self.r - 2 and dest.c == self.c + 2 and grid[self.r - 1][self.c + 1] == 'c' and \
                    grid[self.r - 2] \
                            [self.c + 2] == ' ':

                grid[self.r][self.c] = ' '
                grid[dest.r][dest.c] = self.faction

                # killing enemy piece
                selected_indice = self.enemy.selectPiece(self.r - 1, self.c + 1)
                self.enemy.killpiece(self.enemy.pieces[selected_indice])

                return True
            else:
                return False

        elif self.faction == 'c':
            if dest.r == self.r + 2 and dest.c == self.c + 2 and grid[self.r + 1][self.c + 1] == 'u' and \
                    grid[self.r + 2][self.c + 2] == ' ':

                grid[self.r][self.c] = ' '
                grid[dest.r][dest.c] = self.faction

                selected_indice = self.enemy.selectPiece(self.r + 1, self.c + 1)
                self.enemy.killpiece(self.enemy.pieces[selected_indice])

                return True
            elif dest.r == self.r + 2 and dest.c == self.c - 2 and grid[self.r + 1][self.c - 1] == 'u' and \
                    grid[self.r + 1][self.c - 2] == ' ':

                grid[self.r][self.c] = ' '
                grid[dest.r][dest.c] = self.faction

                selected_indice = self.enemy.selectPiece(self.r + 1, self.c - 1)
                self.enemy.killpiece(self.enemy.pieces[selected_indice])

                return True
            else:
                return False
        else:
            print("Jump not working!")
            return False


class King(Checker):
    def __init__(self, faction, r, c):
        super().__init__(faction, r, c)

    def move_bl(self):
        self.r = self.r + 1
        self.c = self.c - 1
        # FIXMEdef genPieces() {

    def move_br(self):
        # FIXME
        self.r = self.r + 1;
        self.c = self.c + 1;


class Vassal(Checker):
    def __init__(self, faction, enemy_pieces, r, c):
        super().__init__(faction, enemy_pieces, r, c)