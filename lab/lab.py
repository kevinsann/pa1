import board

grid = []

for i in range(0,8):
	new = []
	for j in range(0,8):
		new.append(' ')

	grid.append(new)

newboard = Board(grid)

newboard.mapBoard()
