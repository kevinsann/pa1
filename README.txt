A game of checkers against an AI.

Game Object: Be the last player standing, conquer all pieces of the AI which will result in a WIN.
		Failure to do this results in a LOSS.
	
	This game is implemented in three stages: initialization, play, and ending. 

INITIALIZATION:

Overall, a board is generated on the screen of the console in concert with the Vassal checkers of the opposing 
factions: the computer and the player. The player is always given the first move in any game. 

Vassal checkers are denoted by lowercase letters, while King checkers are denoted by uppercase letters.
The two factions' pieces are denoted with the computer having checkers 'c', and the user having checkers 'u'.

PLAY:

The player can move by means of console input, using the following commands in order to move the selected piece:
	left, forward = lf
	right, forward = rf

Note: Should a piece from either faction make it to the opposite end of the board, the piece will be deemed a King.
As a King, the piece may now move both forwards and backwards, in the left and right directions. The two additional
commands that can be used by the player because of this are:

	left, backward = lb
	right, backward = rb

Should the player not enter one of these commands as a move, they will be prompted to reenter a move based on 
the commands allotted to the selected piece.

There will be a 3-second timer in place for the computer to make its move, as seemingly simultaneous moves by
both the player and the computer can be very anxiety-inducing to keep track of.

Pieces are allowed to make jumps. Specifically, Vassals (according to the rules for checkers) cannot jump
backwards--only forwards left and right. However, Kings are allotted this ability and allowed to combine jumps in 
different directions.

ENDING:

The game will end once all of the Computer's/User's pieces have been eliminated. Dependent on which outcome takes
place, a message of Win/Loss will display.
