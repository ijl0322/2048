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
        print "\n\n"


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
    
def checkwin(board):
    flag = False
    for line in board:
        for num in line:
            if num == "2048":
                print "Congratulations! You win!!!!" 
                flag = True
    return flag
                
def push(i_list, j_list, i_direction, j_direction):
    move = 0
    for i in i_list:
        for j in j_list:
                
        #check if 2 numbers are the same, if yes, add them together
            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i+ i_direction][j + j_direction] = str(int(board[i][j])+int(board[i+ i_direction][j+j_direction]))
                if board[i][j] != "0":
                    move += 1
                board[i][j] = "0"
            
                   
            #check if the slot above is empty, if so, push up the number below
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                if board[i][j] != "0":
                    move += 1
                board[i][j] = "0"

    return move

def pushDirection(UserInput):
    move = 0
    if UserInput == "u":
        i_list, j_list = range(1,4), range(4)
        i_direction, j_direction = -1, 0
    elif UserInput == "d":
        i_list, j_list = range(2,-1,-1), range(4)
        i_direction, j_direction = 1, 0
    elif UserInput == "l":
        i_list, j_list = range(4), range(1,4)
        i_direction, j_direction = 0, -1
    elif UserInput == "r":
        i_list, j_list = range(4), range(2,-1,-1)
        i_direction, j_direction = 0, 1
       
    for i in range(4): 
        move += push(i_list, j_list, i_direction, j_direction)
    return move

def main():
    
    print "Hi, welcome to 2048 game!"
    print "Enter u to move all numbers upward"
    print "Enter d to move all numbers downward"
    print "Enter l to move all numbers tp the left"
    print "Enter r to move all numbers to the right"
    print " "
    addNewNum() 
    addNewNum()                          
    while checklose(board):
        
          
        showboard(board) 
        UserInput = raw_input("Enter u, d, l or r:")
        print "\n"
        if UserInput in "udlr":
            move = pushDirection(UserInput) 
            if move != 0:
                addNewNum()                   
        else:
            print "Invalid input, please try again."  
        
        if checkwin(board):
            break
        elif not checklose(board):
            print "Sorry, Game over"
        

if __name__=='__main__':
    main()
