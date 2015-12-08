# 2048
This is a simpler version of 2048 in python.

## Rules
There will be 16 empty slots on a 4x4 board. 

The player will start with two numbers that are either two or four, on two random slots on the board.

Empty slots on the board will be shown as "-". 

During each turn, the player will have the option to move the numbers up, down, left, or right. 

The player inputs <kbd>u</kbd>, <kbd>d</kbd>, <kbd>l</kbd>, and <kbd>r</kbd>, for up, down, left, or right respectively.

When moving the numbers to the right, all numbers will be pushed to the right of the board. 

For instance:

4 - 2 -

will become:

- - 4 2

If two numbers are of the same value, they will be added together. 

For instance:

- - 4 4

will become:

- - - 8

The games prints out the board every time the player makes a move. 

If the player gets the number "2048" on the board, he/she wins.

And the player looses if he/she cannot make any move at all. 


