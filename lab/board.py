import checkers;

class Board:
	def __init__(self, grid):
		self.grid = []

		for i in range(0,8):
			new = []
			for j in range(0,8):
				new.append(' ')

			self.grid.append(new)

	def initBoard( self , u_checkers, c_checkers ):
		#map x and y for the computer's checkers.

		for i in range(0,3):
			for j in range(0,8):
				if ((j%2==1 and i%2==0) or (j%2==0 and i%2==1)):
					newchecker = checkers.Vassal('c',i,j)
					c_checkers.append(newchecker)
					self.grid[i][j] = newchecker.getfaction()
				else:
					self.grid[i][j] = ' '

		#no man's land, init.

		for i in range(3,5):
			for j in range(0,8):
				self.grid[i][j] = ' '

		#map x and y for the user's checkers.

		for i in range(5,8):
			for j in range(0,8):
				if ((j%2==1 and i%2==0) or (j%2==0 and i%2==1)):
					newchecker = checkers.Vassal('u', i, j)
					u_checkers.append(newchecker)
					self.grid[i][j] = newchecker.getfaction()
				else:
					self.grid[i][j] = ' '
	def mapBoard(self, movedchecker):
		for i in range(8):
			for j in range(8):
				if i == movedchecker.getrow() and j == movedchecker.getcolumn():
					self.grid[i][j] = movedchecker.getfaction()

	def showBoard( self ):
		for i in self.grid:
			for j in i:
				print(j, end=' ')
			print()
#FIXME
	#def updateBoard( self, movedchecker ):
		#

#for i in newboard.grid:
#	for j in i:
#		print(j, end=' ')

#	print()
