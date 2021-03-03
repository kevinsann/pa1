class Checker:
    def __init__(self, faction, r, c):
        self.faction = faction
        self.r = r
        self.c = c
        self.isliving = True
        self.selected = False

    #setters
    def setfaction(self, newFaction):
        self.faction = newFaction
    def setrow(self, r):
        self.r = r;
    def setcolumn(self, c):
        self.c = c;

    # getters
    def getfaction(self):
        return self.faction;
    def getrow(self):
        return self.r;
    def getcolumn(self):
        return self.c;

    # moves allowed for both vassals and kings.
    def move_fl(self):
        if (self.faction == 'u'):
            self.r = self.r - 1;
            self.c = self.c - 1;
        #FIXME:
        #if (self.faction == 'c'):

    def move_fr(self):
        #FIXME: IF THE IF STATEMENT IS NOT NEEDED FOR AI TO MOVE
        if (self.faction == 'u'):
            self.r = self.r - 1;
            self.c = self.c + 1;

        #FIXME:
        #if (self.faction == 'c')):

    def togglelife(self):
        self.isliving = False

class King( Checker ):
    def __init__(self,faction,r,c):
        super().__init__(faction,r,c)


    def move_bl(self):
        self.r = self.r + 1;
        self.c = self.c - 1;
        #FIXMEdef genPieces() {
    def move_br(self):
        #FIXME
        self.r = self.r + 1;
        self.c = self.c + 1;

class Vassal( Checker ):
    def __init__(self, faction, r , c):
        super().__init__(faction,r,c)

#    def move_fl(self):
#        self.r = self.r - 1;
#        self.c = self.c - 1;

#    def move_fr(self):
#        self.r = self.r - 1;
#        self.c = self.c + 1;
