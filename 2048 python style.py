import random
#initialize board

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

def pushUp():
                
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
    for i in range(3):
        for j in range(4):         

            if board[i][j] == "0" and board[i-1][j] == "0":
                board[i][j] = board[i+1][j]
                board[i+1][j] = "0"
                board[i-1][j] = board[i][j]
                board[i][j] = "0"
            elif board[i][j] == "0":
                board[i][j] = board[i+1][j]
                board[i+1][j] = "0"
            if board[i][j] == board[i+1][j]:
                board[i][j] = str(int(board[i][j])+int(board[i+1][j]))
                board[i+1][j] = "0"

def pushDown(): #Need debugging
                
    #make sure every number is correctly pushed up
    for i in range(3):
        for j in range(4):

            #check if 2 numbers are the same, if yes, add them together
            if board[i][j] == board[i+1][j]:
                board[i+1][j] = str(int(board[i][j])+int(board[i+1][j]))
                board[i][j] = "0"

            #check if the slot above is empty, if so, push up the number below
            if board[i+1][j] == "0":
                board[i+1][j] = board[i][j]
                board[i][j] = "0"
                
    for i in range(2,0,-1):
        for j in range(4):         

            if board[i][j] == "0" and board[i+1][j] == "0":
                board[i][j] = board[i-1][j]
                board[i-1][j] = "0"
                board[i+1][j] = board[i][j]
                board[i][j] = "0"
                #showboard(board)
            elif board[i][j] == "0":
                board[i][j] = board[i-1][j]
                board[i-1][j] = "0"
<<<<<<< HEAD
                #showboard(board)        
            if board[i][j] == board[i+1][j]:
                board[i+1][j] = str(int(board[i][j])+int(board[i+1][j]))
                board[i][j] = "0"
=======
                #showboard(board)

def pushRight():
                
    for i in range(3,0,-1):
        for j in range(4):
            #check if 2 numbers are the same, if yes, add them together
            if board[j][i] == board[j][i-1]:
                board[j][i-1] = str(int(board[j][i])+int(board[j][i-1]))
                board[j][i] = "0"
            #check if the slot above is empty, if so, push up the number below
            if board[j][i-1] == "0":
                board[j][i-1] = board[j][i]
                board[j][i] = "0"
            
    #make sure every number is correctly pushed up
    for i in range(3):
        for j in range(4):             
            if board[j][i] == "0" and board[j][i] == "0":
                board[j][i] = board[j][i+1]
                board[j][i+1] = "0"
                board[j][i-1] = board[j][i]
                board[j][i] = "0"
            elif board[j][i] == "0":
                board[j][i] = board[j][i+1]
                board[j][i+1] = "0"
        



>>>>>>> master
def main():
    
    print "Hi, welcome to 2048 game!"
    print "Enter u to move all numbers upward"
    print "Enter d to move all numbers downward"
    print "Enter l to move all numbers tp the left"
    print "Enter r to move all numbers to the right"
    print " "
    
    showboard(board)
    UserInput = raw_input("Enter u, d, l or r:")
    if UserInput == "u":    
        pushUp()
    elif UserInput == "d":    
        pushDown()
    elif UserInput == "r":
        pushRight()
    showboard(board)
  


for i in range(10):
    addNewNum()
  
main()






