

def genCheckers():
	print("ok")

class Checker:
    def __init__(self, faction, r, c):
        self.faction = faction
        self.r = r
        self.c = c

    #setters

    def setfaction(newFaction):
        self.faction = newFaction
    def setrow(r):
        self.r = r;
    def setcolumn(c):
        self.c = c;

    # getters

    def getfaction(self):
        return self.faction
    def getrow(self):
        return self.r
    def getcolumn():
        return self.c


class King( Checker ):
    def __init__(self,
                faction,
                r,
                c):

        super().__init__(self,faction,r,c)

    def move_bl(self):
        r = r - 1;
        c = c - 1;
        #FIXMEdef genPieces() {
    def move_br(self):
        #FIXME
        r = r + 1;
        c = c - 1;
    def move_fl(self):
        #FIXME

        r = r - 1;
        c = c + 1;
    def move_fr(self):
        #FIXME
        r = r + 1;
        c = c + 1;

class Vassal( Checker ):
    def __init__(self,
                faction,
                r,
                c):

        super().__init__(faction,r,c)

    def move_fl(self):
        self.r = self.r - 1;
        self.c = self.c + 1;

    def move_fr(self):
        r = r + 1;
        c = c + 1;
