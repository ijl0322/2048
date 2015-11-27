import random
#initialize board

random.seed(2)
board = [["0"]*4,["0"]*4,["0"]*4,["0"]*4]

    
def showboard(board):
    """ Takes in a list (board), and prints out the board """
    for line in board:
        print "   ".join(line)
        print " "

def addNewNum():
    """Generates a 2 or 4, and set at a random location on board\
    that is originally a 0 """
    
    newNum = str(random.choice([2,4]))
    randomx = random.randrange(4)
    randomy = random.randrange(4)
    while board[randomy][randomx] != "0":
        randomx = random.randrange(4)
        randomy = random.randrange(4)
    board[randomy][randomx] = newNum 
        
def checklose(board):
    """Takes in a list (board), return True if there is still 0 in the list, otherwise False"""
    totalNum = 0
    for line in board:
        for num in line:
            if num != "0":
                totalNum += 1
    return totalNum < 16 

#def pushUP(UserInput):
#    if UserInput.lower() == "u":
#        for i in range(4):
#            if board[0][i] == "0""
#                board[0][i] =  

def pushUP():
    UserInput = raw_input("Enter:")
    if UserInput == "u":
                
        for i in range(3,0,-1):
            for j in range(4):
                #check if 2 numbers are the same, if yes, add them together
                if board[i][j] == board[i-1][j]:
                    board[i-1][j] = str(int(board[i][j])+int(board[i-1][j]))
                    board[i][j] = "0"
                #check if the slot above is empty, if so, push up the number below
                if board[i-1][j] == "0":
                    board[i-1][j] = board[i][j]
                    board[i][j] = "0"
                
        #make sure every number is correctly pushed up
        #showboard(board)
        for i in range(3):
            for j in range(4):             
                if board[i][j] == "0":
                    board[i][j] = board[i+1][j]
                    board[i+1][j] = "0"
                    if board[i-1][j] == "0":
                        board[i-1][j] = board[i][j]
                        board[i][j] = "0"
                
                
    showboard(board)

    
    
  
#board[3][0] = "5"
#board[2][0] = "5"    
#board[3][1] = "3"
#board[2][1] = "3" 

for i in range(10):
    addNewNum()
showboard(board)  
pushUP()
#showboard(board)  
print checklose(board)