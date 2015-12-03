import random
#initialize board

board = [["0"]*4,["0"]*4,["0"]*4,["0"]*4]

    
def showboard(board):
    """ Takes in a list (board), and prints out the board """
    for line in board:
        for item in line:
            if item == "0":
                print "     -",
            elif int(item)/1000 > 0:
                print " ", item,
            elif int(item)/100 > 0:
                print "  ", item,
            elif int(item)/10 > 0:
                print "   ", item,
            else:
                print "    ", item,
        print " "
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

def push(i_list, j_list, i_direction, j_direction):
    for i in i_list:
        for j in j_list:
                
        #check if 2 numbers are the same, if yes, add them together
            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i+ i_direction][j + j_direction] = str(int(board[i][j])+int(board[i+ i_direction][j+j_direction]))
                board[i][j] = "0"
                        
            #check if the slot above is empty, if so, push up the number below
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                board[i][j] = "0"

def pushDirection(UserInput):
    if UserInput == "u":
        i_list, j_list = range(3,0,-1), range(4)
        i_direction, j_direction = -1, 0
    elif UserInput == "d":
        i_list, j_list = range(3), range(4)
        i_direction, j_direction = 1, 0
    elif UserInput == "l":
        i_list, j_list = range(4), range(3,0,-1)
        i_direction, j_direction = 0, -1
    elif UserInput == "r":
        i_list, j_list = range(4), range(3)
        i_direction, j_direction = 0, 1
       
    for i in range(4): 
        push(i_list, j_list, i_direction, j_direction)

def main():
    
    print "Hi, welcome to 2048 game!"
    print "Enter u to move all numbers upward"
    print "Enter d to move all numbers downward"
    print "Enter l to move all numbers tp the left"
    print "Enter r to move all numbers to the right"
    print " "
    addNewNum() 
                        
    while checklose(board):

        addNewNum()              
        showboard(board) 
        UserInput = raw_input("Enter u, d, l or r:")
        if UserInput in "udlr":
            pushDirection(UserInput)
        else:
            print "Invalid input, please try again."  
        if not checklose(board):
            print "Sorry, Game over"

if __name__=='__main__':
    main()
