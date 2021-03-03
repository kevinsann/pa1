import checkers
import orderedpair
import moves

class Player:
	def __init__(self, faction, pieces):
		self.faction = faction
		self.pieces = pieces
		self.hasturn = False

	def toggleturn(self):
		self.hasturn = not(self.hasturn)

	def getfaction(self):
		return self.faction

	def getpiecestatus(self, index):
		selected = self.pieces[index]

		print("Piecestatus of piece ", index + 1, ': ')
		print('isAlive:', selected.isliving)
		print('row: ', selected.getrow())
		print('column: ', selected.getcolumn())


	def selectPiece(self, row, column):
		for piece in self.pieces:
			if piece.r == row and piece.c == column:
				piece.selected = True

	def promptPiece(self):
		if (self.faction == 'u'):

			#checkers are selected by means of the input 'mxn', with m denoting the row and n denoting the column
			#of the desired piece.
			selection = input("Select your piece (mxn): ")

			ms = ord(selection[0])
			xs = selection[1]
			ns = ord(selection[2])

			#FIXME trying to get: while not a user piece....
			while not(0 < ms and 8 > ms) or not(0 < ns and 8 > ns) or not(xs=='x'):
				selection = input("Try again: ")
				ms = ord(selection[0])
				xs = selection[1]
				ns = ord(selection[2])

			self.selectPiece(ms,ns)
			starting_coord = orderedpair.OrderedPair(ms,ns)

			return starting_coord

	def promptDestination(self):
		if self.faction == 'u':
			destination = input("Destination (mxn): ")

			md = ord(destination[0])
			xd = destination[1]
			nd = ord(destination[2])

			while not(0 < md and 8 > md) or not(0 < nd and 8 > nd) or not(xd=='x'):
				selection = input("Try again: ")
				md = ord(selection[0])
				xd = destination[1]
				nd = ord(selection[2])

			destination_coord = orderedpair.OrderedPair(md,nd)

			return destination_coord

		elif self.faction == 'c':
			print("Moving..")

	#FIXME def move(self):
		#FIXME if


#del
player = Player('u', 12)
player.toggleturn()


#print(player.hasturn)
#player.promptPiece()
#player.promptDestination()
