#Simply notify each vector diferently as row col right diagonal left diagonal
#All n rows are differently structured via using the queen, row, col, diagonal

def initialize(board,n):
    for key in ['queen','row','col','nwtose','swtone']:
        #firstly for our application we make nested distionary
        #we will initialize row by row to these dictionary
        board[key]={}

    for i in range(n):
        board['queen'][i]=-1
        board['row'][i]=0
        board['col'][i]=0
    for i in range(-(n-1),n):
        board['nwtose'][i]=0
    for i in range(2*n-1):
        board['swtone'][i]=0

# This fxn prints the location of queen row wise:        
def printboard(board):
    for row in sorted(board['queen'].keys()):
        print((row,board['queen'][row]))


# as we have used row col l-dia, r-dia, now we can use them in order to 
# determine the position of board is suitable for placing the queen in that 
# row.        
def free(i,j,board):
    return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][j+i]==0)   


#This fxn is used to add the queen in that row and change the value of
#of our defined variables
def addqueen(i,j,board):
    board['queen'][i]=j
    board['row'][i]=1
    board['col'][j]=1
    board['nwtose'][j-i]=1
    board['swtone'][j+i]=1


# This fxn will undo our addqueen step
def undoqueen(i,j,board):
    board['queen'][i]=-1
    board['row'][i]=0
    board['col'][j]=0
    board['nwtose'][j-i]=0
    board['swtone'][j+i]=0


# This is the main fxn it uses our alogorthim 
# We can more modify print-board fxn and giving all possible outputs
def placequeen(i,board):
    n=len(board['queen'].keys())
    for j in range(n):
        if free(i,j,board):
            addqueen(i,j,board)
            if i==n-1:
                return True
            else:
                extendsoln=placequeen(i+1,board)
            if extendsoln:
                return True
            else:
                undoqueen(i,j,board)
    else:
            return False

board={}
n=int(input("How many Queens? : "))
initialize(board,n)
if placequeen(0,board):
    printboard(board)

#you can modify printboard()
# as
#
l='''def printboard(board):
	l=[[" " for i in range(7)] for j in range(7)]
	for row in sorted(board['queen'].keys()):
		#print((row,board['queen'][row]))
		l[row][board['queen'][row]] = 'Q'
	for i in range(len(board['queen'].keys())):
		print('', end='|')
		for j in range(len(board['queen'].keys())):
			print(l[i][j], end='|')
		print('')'''