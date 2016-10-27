BOARD GAME EXPLAINED:
The aim of the game, is to predict the best possible move of the given player.
Input is read from an input_#.txt file -
3		- Max Size of board (3x3)(can be upto 26x26)	
ALPHABETA	- Search technique to be used
X		- "CP"-Player who will play at this current board
1		- No of plays to be considered/ or depth of tree to which the program should search
30 58 25	-Values of each cell in the 3x3 board
19 76 93
52 73 24
.O.		-Pawns of the two players X and O on the same 3x3 board
..X
OXX

The aim of the game is to give the best move for CP(Player who has to play at the given board). The program has to search till the depth given. For instance, if depth = 1. The program would keep the pawn of "X" at all "." positions on the board. All the possible values are considered as 1 depth.

. | O | .  
_________
. | . | X
_________
O | X | X
This is the current board state.
At depth 1, if CP = X, Board State can be
X | O | .  |  | .| O | X 
_________  |  | _________
. | . | X  |OR| .| . | X	
_________  |  | __________
O | X | X  |  | O| X | X
____________OR______________
 | O | .   |  |   .| O | .
_________  |  |  _________
X | . | X  |OR|   .| X | X	
_________  |  |  __________
O | X | X  |  |   O| X | X

A player can play 2 ways in one move - 	1) Stake - just keep its pawn at any empty place.
					2) Raid - The pawn can be kept only adjacent to your own player, and any touching enemy pawn(adjacent cell 						  	horizontally or vertically), will be converted to the current player's pawn. If no enemy pawn is present, 						  	this raid would be similar to a stake.


for example:
In this if X is about to play, then a stake is possible at all positions. Raid is possible in the first row-third cell

. | O | . <-Here and also in second row-second col. cell 
_________
. | . | X
_________
O | X | X

If X decides to Raid from these positions then, the end state of board would be:

. | X | X  |	| .| X | . 
_________  |	| _________
. | . | X  | OR	| .| X | X	
_________  |	| __________
O | X | X  |	| O| X | X

hence a total of 6 different states are possible for 1 possible move of X.

if depth was 2,after playing the turn of X, the program would change player to O and play all possible moves of O for each possible move of X generated previous depth. 
For depth = 3, after O has played the program would change player to X and play all possible moves for each move of O generated at previous depth.

This is how a tree would be made and then the Minimax and Alpha-Beta pruning algorithms can be used on the tree.
The program continues till the required depth or till the point where the board is full,(whichever comes first).

When program reaches at the depth or last level, it calculates the score based on the board values and where is each player's pawn. Score is calculated always as the original CP- other player. As given in this example, the score is total values of X- total values of O (CP-OtherPlayer). After obtaining these values Minimum or Maximum is calculated among the nodes as per their cutoff. For depths where CP played, would be Maximum of all child nodes from the same parent and where Other player played, it would be minimum of each child node from same parent. Values are backed up till we obtain the maximum value at the root node. This maximum value is backed up to the root from the depth = 1. Hence, board orientation giving the maximum value if the answer. The output just has a single move judged on the basis of the backed up values by these two algorithms on the game tree.

For ex-
B3 Raid - (colums are alphabetical and rows are numeric) - means second col and third row would be the best move for the CP, with a raid.
C5 Stake - Third Col and 5th row would be the best move.
And underneath in the output is given how the board will look when this move is achieved.







