import orderedpair

class Parser:
    def __init__(self, start, destination):
        self.start = start
        self.destination = destination

class Move:
    def __init__(self):
        self.isValid = False

    def validate(self, starting_coord, destination_coord):
        start_r = starting_coord.orderedpair.row
        start_c = starting_coord.orderedpair.column

        end_r = destination_coord.orderedpair.row
        end_c = destination_coord.orderedpair.column

        if abs(end_r - start_r) > 1 or abs(end_c - start_c) > 1:
            return False
        else:
            return True