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
    """Generates a 2 or 4, and set the number at a random location on board \
    that is originally a 0 """
    
    newNum = str(random.choice([2,4]))
    randomx = random.randrange(4)
    randomy = random.randrange(4)
    while board[randomy][randomx] != "0":
        randomx = random.randrange(4)
        randomy = random.randrange(4)
    board[randomy][randomx] = newNum 
        
def checklose(board):
    """Takes in a list (board), return True the player does not lose (if there is still 0 in the list or \
    if any move can still be made) otherwise False"""
    totalNum = 0
    for line in board:
        for num in line:
            if num != "0":
                totalNum += 1
    if totalNum == 16:
        return pushDirection("u") + pushDirection("d") + pushDirection("l") + pushDirection("r") != 0
    return True            
               
    
def checkwin(board):
    """ Checks if the player has the number 2048 on the board. 
    If so, return True and print a "you win" statement. Otherwise, return False."""
    
    flag = False
    for line in board:
        for num in line:
            if num == "2048":
                print "Congratulations! You win!!!!" 
                flag = True
    return flag
                
def add(i_list, j_list, i_direction, j_direction):
    
    """Iterates through the board, and adds a number with its adjacent neighbor if the two numbers are the same. 
    ex. 2248 becomes 0448.
    i_list, j_list - lists, indicate how add interate through the list.
    i_direction, j_direction - an int, either 1, -1 or 0. Defines the direction of the add. 
    ex. +1, 2248 becomes 0448. -1, 2248 becomes 4480, 0, does not add. 
    
    move is a counter that's later used to determine whether a move can still be made by the player.
    """
    move = 0
    for i in i_list:
        for j in j_list:
                
        #check if 2 numbers are the same, if yes, add them together
            if board[i][j] == board[i + i_direction][j + j_direction]:
                board[i+ i_direction][j + j_direction] = str(int(board[i][j])+int(board[i+ i_direction][j+j_direction]))
                if board[i][j] != "0":
                    move += 1
                board[i][j] = "0"

    return move
    
def push(i_list, j_list, i_direction, j_direction):
    
    """push a number to its adjacent slot if the slot is 0. 
    i_list, j_list - lists, indicate how push interate through the list.
    i_direction, j_direction - an int, either 1, -1 or 0. Defines the direction of the push. 
    move is a counter that's later used to determine whether a move can still be made by the player.
    """
   
    move = 0
    for i in i_list:
        for j in j_list:
            if board[i + i_direction][j + j_direction] == "0":
                board[i + i_direction][j + j_direction] = board[i][j]
                if board[i][j] != "0":
                    move += 1
                board[i][j] = "0"
    return move                

def pushDirection(UserInput):
    """
    Takes in a UserInput and calls add and push function with the proper i_list,\
    j_list, i_direction and j_direction. 
    UserInput - a str
    """
    
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
    move += add(i_list, j_list, i_direction, j_direction)
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
    showboard(board)   
                                            
    while checklose(board):
        
        if checkwin(board):
            break
                                                     
        UserInput = raw_input("Enter u, d, l or r:")
        print "\n"
        try:
            if UserInput in "udlr":
                move = pushDirection(UserInput) 
                if move != 0:
                    addNewNum()                   
            else:
                print "Invalid input, please try again."  
        except:
            print "Invalid input, please try again."
            continue
        
        showboard(board) 
        
    if not checklose(board):
        print "Sorry, Game over"

#debugging code

"""
board[0][1] = "4"
board[0][2] = "2"
board[0][3] = "16" 
board[1][0] = "4"
board[1][1] = "8"
board[1][2] = "4"
board[1][3] = "32"     
board[2][0] = "2"        
board[2][1] = "4"
board[2][2] = "16"
board[2][3] = "128"
board[3][0] = "4"
board[3][1] = "2"
board[3][2] = "1024"
board[3][3] = "1024"   
"""

if __name__=='__main__':
    main()
